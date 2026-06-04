"""
Module for processing graphs describing templates.

This module helps process templates described graphs.
It adds a layer on top of pygraph in some cases to deal with cases of re-entrancy.
"""

## To do: https://github.com/Shoobx/python-graph/tree/afd6f1cf0f04350d05ea28ad3ea567b623031ae4
# is the library used here, but no longer maintained
# maybe switch to NetworkX?
# https://networkx.org/documentation/stable/index.html

from pygraph.classes.digraph import digraph
from pygraph.classes.exceptions import AdditionError

# Do I need all these? (Commented out on 1/4/2025 to see if needed)
# from pygraph.classes.exceptions import InvalidGraphType
# from pygraph.classes.graph import graph
# from pygraph.classes.hypergraph import hypergraph
# from pygraph.readwrite.markup import write

import pydot
import re

# A series of functions for abstracting away from some RDF specificities, including documentation fields
import tdag.despecification as despecification


class tdag ( ):
	
	def __init__(self, name):
		"""
		Class for DAGs for templates, these DAGs contain despecified templates because
		process_templates only adds properly despecifed nodes.
		The code here is sensitive to the current working model of a template.
		So, this makes it somewhat brittle.
		"""
		
		self.name = name
		
		# to do: Add metadata fields (language, source, usw.)
		
		# The "core" of a template DAG is a directed graph from pygraph, allowing us to use most of its functionality.
		# But, some extra information needs to be added on top of this core to get repeatable nodes and multiple
		# pointing to/from the same nodes.
		# POSSIBLE CONFUSION: In a few places, we call tdag functions and pygraph functions
		# with the same and/or similar names. This is noted in some places (where remembered).
		self.core = digraph()
		
		# Information from here down is kept track of to deal with special properties of tdags.
		# We store a copy of edges at DAG level so we can add IDs to them.
		# This helps us get foundation re-entrancy.
		# These are just labeled edges with an ID.
		self.edgeCount = 0
		self.edges = { }
		
		
		# To do: Generalize this to work with non-RDF template descriptions? Probably done in another function.
		# The mappings below relate a given component's URI to a more readable
		# label made unique by adding an integer

		# Nodes that can repeat need to be created here and relevant logic needs to be added to add_node().
		# This has been implemented for all attested cases, but not logically possible ones.
		# So, some may need to be added, but there should be warnings when this is a problem.
		self.components = [ ]
		self.componentMapping = { }

		# The next two are for component elasticity
		self.elastics = [ ]
		self.elasticMapping = { }

		self.inelastics = [ ]
		self.inelasticMapping = { }


		# The next two are for types of component stability
		self.stabilities = [ ]
		self.stabilityMapping = { }

		self.unstabilities = [ ]
		self.unstabilityMapping = { }


		# The next four are for types of component filledness
		self.opens = [ ]
		self.openMapping = { }

		self.filleds = [ ]
		self.filledMapping = { }

		self.partialfilleds = [ ]
		self.partialfilledMapping = { }

		# For positioning of partiallyFilled elements.
		# Need to add other positions as coded.
		# In fact, none were needed initially since repetition didn't come up, but "final" was added as a test.
		self.finals = [ ]
		self.finalMapping = { }

		self.nulls = [ ]
		self.nullMapping = { }

		self.coherents = [ ]
		self.coherentMapping = { }

		self.incoherents = [ ]
		self.incoherentMapping = { }


		# For canonical fillers of components (as opposed to templatic fillers)
		self.canonicals = [ ]
		self.canonicalMapping = { }

		# For embedded desmemes
		self.embeddeds = [ ]
		self.embeddedMapping = { }


		# For different integer counts in the graphs
		# This part of the description language should be updated, probably,
		# to fixedSlot, optionalSlot, field (see Template2Notes.txt) 
		
		## Don't think these are needed for new implementation, 1/19/2025
		#self.seenCounts = [ ]
		#self.counts = { }
		#self.countMapping = { }

		
		# Some namespaces are for properties that can be typologically compared and some are not.
		# These are the ones that are good for comparison.
		# This "hardcoding" of the generic prefixes in the template class may not be ideal in the long run.
		# This is for RDF-based processing, which I expect to be a legacy mode of processing at some point
		self.genericPredPfxs = ["http://purl.org/linguistics/jcgood/general#",
				   "http://purl.org/linguistics/jcgood/template#",
				   "http://purl.org/linguistics/jcgood/templates#",
				   "http://purl.org/linguistics/jcgood/component#"]
	
	
	def add_node(self, node, URI, mother="", predicate=""):
		"""
		Adds desired RDF node to internal graph and does some processing for readability.
		Includes special logic for dealing with "repeatable" nodes (in components and fillers).
		This function returns a nodeName with an integer for disambiguation purposes, if needed.
		If the same node is attempted to be added twice, just returns graph nodename as side effect
		"""
				
		nodeName = node
		
		# Originally, node names were italicized, but the dot->pdf rendering messes up
		# the way "f" is rendered (and maybe some other characters) in Times New Roman
		# italics. So, I am turning off italics for now, but using these variables to
		# bring them back if that problem can be addressed.
		it = ""
		nt = ""
		#it = "<<i>" # dot italics prefix
		#nt = "</i>>" # dot italics suffix
		
		
		# Cases may need to be added as new possible "duplicate" possibilities are attested.
		
		# Similar logic applies to all countable nodes. See comments here will help understand others.
		if "component_" in node:				

			self.core.add_node(nodeName, attrs=[("label", it + "component" + nt)])
				
# 			if URI in self.components:
# 				nodeName = self.componentMapping[URI]
# 				pass
# 			else:
# 				componentNumber = len(self.components) + 1 # These increments ensure each repeatable node gets its own identifier.
# 				nodeName = URI # Use actual component IDs now
# 				self.components.append(URI)
# 				self.componentMapping[URI] = nodeName # This is the nodename with the number on it to make sure it can be identified properly for pydot.
# 				self.core.add_node(nodeName, attrs=[("label", it + URI + nt)]) # Now we add the node to the internal graph, giving it a label without the extra digit.


		elif node == "elastic":
			if URI in self.elastics:
				nodeName = self.elasticMapping[URI]
			else:
				elasticNumber = len(self.elastics) + 1
				nodeName = node + str(elasticNumber)
				self.elastics.append(URI)
				self.elasticMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "elastic" + nt)])
		
		elif node == "inelastic":		
			
			if URI in self.inelastics:
				nodeName = self.inelasticMapping[URI]
			else:
				inelasticNumber = len(self.inelastics) + 1
				nodeName = node + str(inelasticNumber)
				self.inelastics.append(URI)
				self.inelasticMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "inelastic" + nt)])

		elif node == "stable":
			if URI in self.stabilities:
				nodeName = self.stabilityMapping[URI]
			else:
				stabilityNumber = len(self.stabilities) + 1
				nodeName = node + str(stabilityNumber)
				self.stabilities.append(URI)
				self.stabilityMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "stable" + nt)])

		elif node == "unstable":
			if URI in self.unstabilities:
				nodeName = self.unstabilityMapping[URI]
			else:
				unstabilityNumber = len(self.unstabilities) + 1
				nodeName = node + str(unstabilityNumber)
				self.unstabilities.append(URI)
				self.unstabilityMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "unstable" + nt)])

		elif node == "filled":
			if URI in self.filleds:
				nodeName = self.filledMapping[URI]
			else:
				filledNumber = len(self.filleds) + 1
				nodeName = node + str(filledNumber)
				self.filleds.append(URI)
				self.filledMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "filled" + nt)])

		elif node == "open":
			if URI in self.opens:
				nodeName = self.openMapping[URI]
			else:
				openNumber = len(self.opens) + 1
				nodeName = node + str(openNumber)
				self.opens.append(URI)
				self.openMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "open" + nt)])

		elif node == "partiallyFilled":
			if URI in self.partialfilleds:
				nodeName = self.partialfilledMapping[URI]
			else:
				partialfilledNumber = len(self.partialfilleds) + 1
				nodeName = node + str(partialfilledNumber)
				self.partialfilleds.append(URI)
				self.partialfilledMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "partiallyFilled" + nt)])

		elif node == "final":
			if URI in self.finals:
				nodeName = self.finalMapping[URI]
			else:
				finalNumber = len(self.finals) + 1
				nodeName = node + str(finalNumber)
				self.finals.append(URI)
				self.finalMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "final" + nt)])

		elif node == "null":
			if URI in self.nulls:
				nodeName = self.nullMapping[URI]
			else:
				nullNumber = len(self.nulls) + 1
				nodeName = node + str(nullNumber)
				self.nulls.append(URI)
				self.nullMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "null" + nt)])

		elif node == "coherent":
			if URI in self.coherents:
				nodeName = self.coherentMapping[URI]
			else:
				coherentNumber = len(self.coherents) + 1
				nodeName = node + str(coherentNumber)
				self.coherents.append(URI)
				self.coherentMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "coherent" + nt)])

		elif node == "incoherent":
			if URI in self.incoherents:
				nodeName = self.incoherentMapping[URI]
			else:
				incoherentNumber = len(self.incoherents) + 1
				nodeName = node + str(incoherentNumber)
				self.incoherents.append(URI)
				self.incoherentMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "incoherent" + nt)])

		elif node == "canonicalLineate":
			if URI in self.canonicals:
				nodeName = self.canonicalMapping[URI]
			else:
				canonicalNumber = len(self.canonicals) + 1
				nodeName = node + str(canonicalNumber)
				self.canonicals.append(URI)
				self.canonicalMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "canonicalLineate" + nt)])

		elif node == "embeddedDesmeme":
			if URI in self.canonicals:
				nodeName = self.embeddedMapping[URI]
			else:
				embeddedNumber = len(self.embeddeds) + 1
				nodeName = node + str(embeddedNumber)
				self.embeddeds.append(URI)
				self.embeddedMapping[URI] = nodeName
				self.core.add_node(nodeName, attrs=[("label", it + "embeddedDesmeme" + nt)])

		# components code nodes slightly differently from desmemes
		elif "-MAXIMUM_" in node or "-MINIMUM_" in node or "-COUNT" in node:

			# The URI is designed to contain the count value after an underscore at the end of the string
			countno = re.search(r'(?<=_)([0-9]+)$', node).group(0)
			
			# Use URI as nodename for digits since digits are not unique
			if countno == '100':
				self.core.add_node(URI,  attrs=[("label", '∞')])			
			else:
				self.core.add_node(URI,  attrs=[("label", countno)])


		elif node == "source":
			print(node, nodeName)
			pass
		
		# If we've made it this far, it's a non-repeatable, generic node.		
		else:
			# make first letter of type name lowercase (needed for names borrowed from GOLD)
			node = node[0].lower() + node[1:]
			self.core.add_node(nodeName, attrs=[("label", it + node + nt)])

		# This allows us to capture the generated name to build the edges
		return nodeName


			
	def has_node(self, node, URI):
		"""
		This function doesn't seem to be strictly needed, and I don't really
		understand what it was doing. But, I found that it can be useful for
		error checking since it somehow finds repeatable nodes that are not
		being properly handled. So, I'm keeping it. It seems to work by telling
		us if a node with that name has already been added, which normally
		shouldn't happen.
		"""
		if self.core.has_node(node) == True:
			return node


	#This allows for multiple edges between the same node with different labels.
	#It's not intended to be pretty.
	def add_edge(self, edge, label, wt=1, attrs=[]):
		
		# Begin hack
		# An edge consists of a pair of nodes to be connected.
		u, v = edge
		
		# Do some error checking--make sure the nodes are already there.
		for n in [u,v]:
			if not n in self.core.node_neighbors:
				raise AdditionError( "%s is missing from the node_neighbors table" % n )
			if not n in self.core.node_incidence:
				raise AdditionError( "%s is missing from the node_incidence table" % n )
		
		# Check to see if edge exists already; if so we need to make sure we create a new one with a new label
		if v in self.core.node_neighbors[u] and u in self.core.node_incidence[v]:
			for storedEdge in self.core.edges():
				if edge == storedEdge:
					storedLabel = self.core.edge_label(storedEdge)
					if label == storedLabel:
						# This shouldn't happen. So, if it does, we raise an error.
						raise AdditionError("Edge (%s, %s, %s) already in digraph" % (u, v, label))
						print("Edge (%s, %s, %s, %s) already in digraph" % (u, v, label, self.name))
						pass
					else:
						# Looks good, add the edge with the new label.
						self.add_labeled_edge(edge, label, wt=1, attrs=[])
				else:
					pass

		# This is the usual case: One pair of nodes, one edge. Just add it.
		else:
			self.add_labeled_edge(edge, label, wt=1, attrs=[])
	

	# Checks to see if a labeled edge is already there.
	def has_edge(self, edge, label):
	
		# For re-entrancy in foundations from same parent
		if self.core.has_edge(edge):
			for storedEdge in self.core.edges():
				if edge == storedEdge:
					storedLabel = self.core.edge_label(storedEdge)
					if label == storedLabel:
						return True
					else: pass
				else: pass
			return False
			
		#Standard
		else: return False

	# This uses pygraphs built-in graph capabilities but adds labeled edges for
	# re-entrancy.
	def add_labeled_edge(self, edge, label, wt=1, attrs=[]):
		u, v = edge
		self.core.node_neighbors[u].append(v)
		self.core.node_incidence[v].append(u)
		self.core.set_edge_weight((u, v), wt)
		self.core.add_edge_attributes( (u, v), attrs )
		self.core.set_edge_properties( (u, v), label=label, weight=wt )
		self.edges[self.edgeCount] = ((u,v), label)
		self.edgeCount = self.edgeCount + 1



	# Stub--used edge system for to_dot
	def to_R(self):
		nodes = self.core.nodes()
		edges = self.core.edges()
		
		for node in nodes:
			print(node)
			
		for edge in edges:
			print(edge)
			
			
	# Stub--used edge system for to_dot
	def to_XML(self):
		graph = self.core
		write(graph)

	
	# Adds a layer on top of normal .dot file creation for multiple edges to across same nodes
	def to_dot(dag, weighted=False):

		# Get the core graph we've made
		dagGraph = dag.core
		
		# Create a pydot object
		dotDag = pydot.Dot()
		
		# For now, we don't set the name because "_" seems to cause an error
		# So we use the existing name. I no longer follow all the logic.
		if not 'name' in dir(dagGraph):
			dotDag.set_name('graphname')
		else:
			dotDag.set_name(dag.name)
		
		# Go through all the nodes in the graph
		for node in dagGraph.nodes():
			attr_list = {}
			for attr in dagGraph.node_attributes(node):
				attr_list[str(attr[0])] = str(attr[1])
			
			newNode = pydot.Node(str(node), **attr_list)
			
			dotDag.add_node(newNode)
			
		# Hacking for my specific drawing needs--no weights, just labels
		# Add all the edges with labels.
		dagEdgeKeys = dag.edges.keys()
		for dagEdgeKey in dagEdgeKeys:
			
			(edge, label) = dag.edges[dagEdgeKey]
			(edge_from, edge_to) = edge
			
			# Clean up label for printing
			label = str(label)
			label = label.replace("_", " ")

			attr_list = {}
			attr_list['label'] = label
			
			newEdge = pydot.Edge(str(edge_from), str(edge_to), **attr_list)
			
			dotDag.add_edge(newEdge)
			
		#return dotDag.to_string()
		return dotDag
		
		

	# Makes dot files just for the components of a graph
	# BUG: prints out floating digit nodes for digity things that aren't part of components also floats lexico-constructional conditioning position
	def to_dot_components(dag, weighted=False):

		# These are the nodes that can be in components
		componentcats = ['component','elastic','inelastic','null','filled','open','partiallyFilled','canonicalLineate','coherent','incoherent','stable','unstable','final','initial','medial', 'MAXIMUM', 'MINIMUM', 'COUNT']

		# Get the core graph we've made
		dagGraph = dag.core
		
		# Create a pydot object
		dotDag = pydot.Dot()
		
		# For now, we don't set the name because "_" seems to cause an error
		# So we use the existing name. I no longer follow all the logic.
		if not 'name' in dir(dagGraph):
			dotDag.set_name('graphname')
		else:
			dotDag.set_name(dag.name)
		
		# Go through all the nodes in the graph for components
		for node in dagGraph.nodes():
			attr_list = {}
			for attr in dagGraph.node_attributes(node):
				attr_list[str(attr[0])] = str(attr[1])
			
			for cat in componentcats:
				catmatch = re.compile(cat)
				if catmatch.match(node): # Need numeric nodes, too
					newNode = pydot.Node(str(node), **attr_list)			
					dotDag.add_node(newNode)
		
		
		# Hacking for my specific drawing needs--no weights, just labels
		# Add all the edges with labels.
		dagEdgeKeys = dag.edges.keys()
		for dagEdgeKey in dagEdgeKeys:
			
			(edge, label) = dag.edges[dagEdgeKey]
			(edge_from, edge_to) = edge
			
			# Clean up label for printing
			label = str(label)
			label = label.replace("_", " ")

			attr_list = {}
			attr_list['label'] = label
			
						
			for cat in componentcats:
				catmatch = re.compile(cat)
				if catmatch.match(edge_from):
					newEdge = pydot.Edge(str(edge_from), str(edge_to), **attr_list)
					dotDag.add_edge(newEdge)
				
		#return dotDag.to_string()
		return dotDag