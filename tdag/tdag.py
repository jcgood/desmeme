"""
tdag — DAG wrapper for templatic constructions.

Wraps a pygraph digraph with two layers of extra machinery:

1. Repeatable node types (elastic, filled, stable, etc.) can appear
   multiple times in one graph. Each instance gets a disambiguating
   integer suffix (elastic1, elastic2, …) while sharing the same
   display label. _repeatable_node() handles this uniformly.

2. Labeled parallel edges. pygraph's digraph allows at most one edge
   between any two nodes. Templates with foundation re-entrancy (e.g.
   a component appearing as both LEFT_SUPPORT and KEYSTONE) need
   multiple labeled arcs between the same pair of nodes. add_edge()
   and add_labeled_edge() implement this by maintaining a separate
   self.edges dict alongside pygraph's internal edge table.

The canonical way to build a tdag from data is via
tdag.tabbed.get_tabbed_desmemes().

Dependencies: pygraph (Shoobx fork), pydot.
Possible future work: migrate from pygraph to NetworkX.
"""

from pygraph.classes.digraph import digraph
from pygraph.classes.exceptions import AdditionError

import pydot
import re


def _dot_id(name):
    """Return a DOT-safe node ID.

    Colons are port separators in DOT syntax, so namespace-prefixed
    values (e.g. local:valency) must have their colons replaced before
    being passed to pydot. The display label is unaffected.
    """
    return name.replace(":", "_")


# Node types that can appear more than once within a single tdag (e.g.
# two components can both be 'elastic'). Each instance is stored under a
# disambiguated name (elastic1, elastic2, …); add_node dispatches on this
# set to route them through _repeatable_node().
_REPEATABLE_TYPES = frozenset({
    "elastic", "inelastic",
    "stable", "unstable",
    "filled", "open", "partiallyFilled", "null",
    "coherent", "incoherent",
    "canonicalLineate", "embeddedDesmeme",
    "final",
})


class tdag:
	"""DAG representing a single templatic construction.

	Attributes:
	    name (str): The desmeme identifier (e.g. 'ChichewaAR-MOR').
	    lang (str|None): ISO 639-3 language code (e.g. 'nya', 'cao').
	    core (digraph): The underlying pygraph directed graph. Nodes are
	        stored here; use tdag methods rather than accessing core
	        directly where possible.
	    edges (dict): Maps integer edge IDs to ((from, to), label) tuples.
	        Maintained alongside pygraph's internal edge table to support
	        labeled parallel edges for foundation re-entrancy.
	    edgeCount (int): Monotonically increasing ID for the next edge.
	"""

	def __init__(self, name, lang=None):
		self.name = name
		self.lang = lang

		self.core = digraph()

		# Labeled edge tracking for re-entrancy (see module docstring).
		self.edgeCount = 0
		self.edges = {}

		# Maps each repeatable type name to a dict of {URI -> node_name}.
		# Populated lazily by _repeatable_node().
		self._repeatable = {}


	def _repeatable_node(self, type_name, URI):
		"""Return the disambiguated node name for a repeatable-type node.

		If URI has been seen before for this type, returns the existing
		node name. Otherwise creates a new numbered node (e.g. elastic3)
		in the core graph and records the mapping.
		"""
		mapping = self._repeatable.setdefault(type_name, {})
		if URI not in mapping:
			n = len(mapping) + 1
			node_name = type_name + str(n)
			mapping[URI] = node_name
			self.core.add_node(node_name, attrs=[("label", type_name)])
		return mapping[URI]


	def add_node(self, node, URI, mother="", predicate=""):
		"""Add a node to the graph and return the name it was stored under.

		Handles four cases:
		- component_ nodes: each has a unique ID; label is always 'component'.
		- Repeatable structural types (elastic, filled, etc.): delegated to
		  _repeatable_node() which appends a disambiguating integer.
		- Count-value nodes for component elasticity (MINIMUM/MAXIMUM/COUNT):
		  stored under their full URI with the bare digit as display label.
		- Everything else: stored under the (lowercased) node name directly.
		  A has_node guard allows shared nodes such as grammatical category
		  values (e.g. local:valency) that may appear in multiple components.
		"""
		if "component_" in node:
			self.core.add_node(node, attrs=[("label", "component")])
			return node

		if node in _REPEATABLE_TYPES:
			return self._repeatable_node(node, URI)

		# Component elasticity counts: URI encodes the value after a final
		# underscore (e.g. ChichewaApplicative-inelastic1-MINIMUM_1). Value
		# 100 is a sentinel for ∞.
		if "-MAXIMUM_" in node or "-MINIMUM_" in node or "-COUNT" in node:
			countno = re.search(r'(?<=_)([0-9]+)$', node).group(0)
			label = '∞' if countno == '100' else countno
			self.core.add_node(URI, attrs=[("label", label)])
			return node

		# Generic non-repeatable node. The node is stored under its original
		# name (so edges built by tabbed.py can find it), but the display
		# label lowercases the first letter for visual consistency —
		# GOLD-derived names (e.g. Syllable) are capitalised in the ontology.
		label = node[0].lower() + node[1:]
		if not self.core.has_node(node):
			self.core.add_node(node, attrs=[("label", label)])
		return node


	def has_node(self, node, URI):
		"""Return node if it already exists in the core graph, else None.

		Used by tabbed.py as a guard before calling add_node(), to avoid
		re-adding shared nodes (e.g. a grammatical category value that
		appears in multiple components of the same template).
		"""
		if self.core.has_node(node):
			return node


	def add_edge(self, edge, label, wt=1, attrs=None):
		"""Add a labeled edge, supporting parallel edges between the same nodes.

		pygraph allows at most one edge between any two nodes. Foundation
		re-entrancy (e.g. a component that is both LEFT_SUPPORT and KEYSTONE)
		requires two differently-labeled arcs between the same pair. This
		method checks for an existing edge and, if found, adds a new
		labeled parallel edge rather than raising a duplicate error.
		"""
		if attrs is None:
			attrs = []
		u, v = edge

		for n in [u, v]:
			if n not in self.core.node_neighbors:
				raise AdditionError("%s is missing from the node_neighbors table" % n)
			if n not in self.core.node_incidence:
				raise AdditionError("%s is missing from the node_incidence table" % n)

		if v in self.core.node_neighbors[u] and u in self.core.node_incidence[v]:
			for storedEdge in self.core.edges():
				if edge == storedEdge:
					storedLabel = self.core.edge_label(storedEdge)
					if label == storedLabel:
						raise AdditionError("Edge (%s, %s, %s) already in digraph" % (u, v, label))
					else:
						self.add_labeled_edge(edge, label)
		else:
			self.add_labeled_edge(edge, label)


	def has_edge(self, edge, label):
		"""Return True if a labeled edge already exists between these nodes."""
		if self.core.has_edge(edge):
			for storedEdge in self.core.edges():
				if edge == storedEdge:
					if self.core.edge_label(storedEdge) == label:
						return True
		return False


	def add_labeled_edge(self, edge, label, wt=1, attrs=None):
		"""Low-level: add a labeled edge directly, bypassing duplicate checks.

		Maintains both pygraph's internal neighbor/incidence tables and the
		tdag-level self.edges dict. The self.edges dict is what to_dot()
		iterates over when rendering, since it preserves labels for parallel
		edges that pygraph's edge list would otherwise collapse.
		"""
		if attrs is None:
			attrs = []
		u, v = edge
		self.core.node_neighbors[u].append(v)
		self.core.node_incidence[v].append(u)
		self.core.set_edge_weight((u, v), wt)
		self.core.add_edge_attributes((u, v), attrs)
		self.core.set_edge_properties((u, v), label=label, weight=wt)
		self.edges[self.edgeCount] = ((u, v), label)
		self.edgeCount += 1


	def to_dot(self, weighted=False):
		"""Render the full tdag as a pydot graph.

		Iterates over self.edges (not pygraph's edge list) so that labeled
		parallel edges for re-entrancy are preserved. Node names are passed
		through _dot_id() to sanitise namespace-prefixed values (e.g.
		local:valency → local_valency) that DOT would otherwise misparse
		as node:port pairs.
		"""
		dotDag = pydot.Dot()
		dotDag.set_name(self.name)

		for node in self.core.nodes():
			attr_list = {str(k): str(v) for k, v in self.core.node_attributes(node)}
			dotDag.add_node(pydot.Node(_dot_id(str(node)), **attr_list))

		for (edge, label) in self.edges.values():
			edge_from, edge_to = edge
			attr_list = {'label': str(label).replace("_", " ")}
			dotDag.add_edge(pydot.Edge(_dot_id(str(edge_from)), _dot_id(str(edge_to)), **attr_list))

		return dotDag


	def to_dot_components(self, weighted=False):
		"""Render only the component subgraph of this tdag as a pydot graph.

		Filters to nodes and edges whose names match the set of component-
		internal type names. Used by draw_components() to produce component-
		only visualisations.

		Known issue: floating digit nodes (COUNT/MINIMUM/MAXIMUM values not
		attached to a component) and lexicoconstructional conditioning
		positions may appear in the output.
		"""
		component_types = {
			'component', 'elastic', 'inelastic', 'null', 'filled', 'open',
			'partiallyFilled', 'canonicalLineate', 'coherent', 'incoherent',
			'stable', 'unstable', 'final', 'initial', 'medial',
			'MAXIMUM', 'MINIMUM', 'COUNT',
		}

		def _is_component_node(name):
			return any(re.compile(cat).match(name) for cat in component_types)

		dotDag = pydot.Dot()
		dotDag.set_name(self.name)

		for node in self.core.nodes():
			if _is_component_node(node):
				attr_list = {str(k): str(v) for k, v in self.core.node_attributes(node)}
				dotDag.add_node(pydot.Node(_dot_id(str(node)), **attr_list))

		for (edge, label) in self.edges.values():
			edge_from, edge_to = edge
			if _is_component_node(edge_from):
				attr_list = {'label': str(label).replace("_", " ")}
				dotDag.add_edge(pydot.Edge(_dot_id(str(edge_from)), _dot_id(str(edge_to)), **attr_list))

		return dotDag
