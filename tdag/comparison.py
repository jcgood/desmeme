# Functions for comparing tdag graphs, including distance metrics, nexus output, and visualization.

import os
import re
import subprocess


# ---------------------------------------------------------------------------
# Label normalisation for similarity flooding
# ---------------------------------------------------------------------------

_SUFFIX_RE = re.compile(r'\d+$')


def _strip_suffix(name):
	"""Strip trailing disambiguation integers from a node name.

	tdag.add_node() appends integers to repeatable types (e.g. stable1,
	stable2). This strips those suffixes so that stable1 and stable2 are
	treated as instances of the same type 'stable' during flooding
	initialisation.
	"""
	return _SUFFIX_RE.sub('', name)


# ---------------------------------------------------------------------------
# Similarity flooding
# ---------------------------------------------------------------------------

def similarity_flooding(g1, g2, iterations=100, convergence_threshold=1e-6,
                        mismatch_init=0.5):
	"""Compute pairwise node similarity between two tdags via similarity flooding.

	Adapts the algorithm of Melnik, Garcia-Molina & Rahm (2002) "Similarity
	Flooding: A Versatile Graph Matching Algorithm and its Application to
	Schema Matching" (ICDE 2002), following the variant developed in:

	    Good, J. (forthcoming). *The Linguistic Typology of Templates*.
	    Cambridge University Press.

	and first implemented in the Perl GraphJG library archived in
	scripts/earlier/GraphJG/.

	**Differences from canonical Melnik et al.**

	Melnik et al. weight each propagation arc by 1 / (number of PCG arcs
	with the *same label* incident on the source node). In the template
	graphs used here there is generally at most one arc per label from any
	node, so that weighting would always equal 1 and have no effect. Instead,
	following Melnik et al. (2001) §9, which notes that the weighting can be
	computed in different ways, each arc is weighted by 1 / (total outgoing
	arcs from that PCG node regardless of label). This transforms the PCG
	into a network in which the similarity transmitted from a node is
	inversely proportional to its number of neighbours — preventing scores
	from inflating in ways that make cross-node comparison difficult, and
	producing behaviour analogous to simple recurrent networks (Jordan 1986;
	Elman 1990).

	Algorithm outline:
	  1. Initialise: sim(v1, v2) = 1.0 if stripped labels match, else
	     mismatch_init (default 0.5).
	  2. Build the Pairwise Connectivity Graph (PCG): for each label L
	     shared by both graphs, for each edge src1→dst1 (L) in g1 and
	     src2→dst2 (L) in g2, add bidirectional PCG edge
	     (src1,src2) ↔ (dst1,dst2) and record outgoing counts.
	  3. Iterate: next_sim(v1,v2) = sim(v1,v2) +
	              Σ sim(n1,n2)/outgoing(n1,n2) over PCG neighbours (n1,n2).
	     Normalise by the current maximum after each round.
	     Stop early if max change < convergence_threshold.

	Args:
	    g1, g2:                tdag objects to compare.
	    iterations:            Maximum number of propagation rounds (default 100).
	    convergence_threshold: Stop early when max score change falls below
	                           this value (default 1e-6).
	    mismatch_init:         Initial similarity for node pairs whose stripped
	                           labels differ (default 0.5; quasi-arbitrary per
	                           Melnik et al.).

	Returns:
	    dict mapping (v1, v2) -> float similarity in [0, 1] for all node pairs.
	    If iterations=0, returns the initial similarity matrix before any
	    propagation or normalisation.
	"""
	nodes1 = list(g1.core.nodes())
	nodes2 = list(g2.core.nodes())

	# Step 1: Initialise
	sim = {
		(v1, v2): (1.0 if _strip_suffix(v1) == _strip_suffix(v2) else mismatch_init)
		for v1 in nodes1
		for v2 in nodes2
	}

	if iterations == 0:
		return sim

	# Step 2: Build PCG
	edges1 = {}  # {label: [(src, dst), ...]}
	for _, ((src, dst), label) in g1.edges.items():
		edges1.setdefault(label, []).append((src, dst))

	edges2 = {}
	for _, ((src, dst), label) in g2.edges.items():
		edges2.setdefault(label, []).append((src, dst))

	pcg = {}       # {(v1,v2): [(n1,n2), ...]}  — PCG adjacency
	outgoing = {}  # {(v1,v2): int}              — total outgoing count per PCG node

	for label in set(edges1) & set(edges2):
		for (src1, dst1) in edges1[label]:
			for (src2, dst2) in edges2[label]:
				a, b = (src1, src2), (dst1, dst2)
				pcg.setdefault(a, []).append(b)
				pcg.setdefault(b, []).append(a)
				outgoing[a] = outgoing.get(a, 0) + 1
				outgoing[b] = outgoing.get(b, 0) + 1

	# Step 3: Iterate
	for _ in range(iterations):
		next_sim = {}
		max_val = 0.0

		for v1 in nodes1:
			for v2 in nodes2:
				propagated = sum(
					sim[(n1, n2)] / outgoing[(n1, n2)]
					for (n1, n2) in pcg.get((v1, v2), [])
				)
				val = sim[(v1, v2)] + propagated
				next_sim[(v1, v2)] = val
				if val > max_val:
					max_val = val

		if max_val > 0.0:
			for key in next_sim:
				next_sim[key] /= max_val

		max_change = max(abs(next_sim[k] - sim[k]) for k in sim)
		sim = next_sim
		if max_change < convergence_threshold:
			break

	return sim


def sf_distance(g1, g2, iterations=100, convergence_threshold=1e-6,
                mismatch_init=0.5):
	"""Template-level distance derived from similarity flooding.

	Runs similarity_flooding(g1, g2) and aggregates the node-level scores
	to a single distance value using the mean. The result is in [0, 1] and
	reflects structural dissimilarity: lower means more similar.

	Note on interpretation: because the flooding algorithm normalises scores
	by the per-iteration maximum, absolute values are not directly comparable
	across different graph pairs. sf_distance should be used for *ranking*
	templates by similarity, not for comparing absolute distance values.
	Self-distance (g vs g) will be low but not necessarily exactly 0.

	Args:
	    g1, g2: tdag objects.
	    See similarity_flooding() for remaining arguments.

	Returns:
	    float in [0, 1].
	"""
	scores = similarity_flooding(g1, g2, iterations, convergence_threshold,
	                             mismatch_init)
	if not scores:
		return 1.0
	return 1.0 - sum(scores.values()) / len(scores)


# Implements simUI distance measure for templates
def simUI_d(t1,t2):

	nodes1 = t1.nodes()
	nodes2 = t2.nodes()

	union = list(set(nodes1) | set(nodes2))
	intersection = list(set(nodes1) & set(nodes2))

	distance =  1 - (len(intersection) / float(len(union)))

	return distance


# Implements simUI distance measure for templates but returns similarity measure rather than distance
def simUI_s(t1,t2):

	nodes1 = t1.nodes()
	nodes2 = t2.nodes()

	union = list(set(nodes1) | set(nodes2))
	intersection = list(set(nodes1) & set(nodes2))

	distance = (len(intersection) / float(len(union)))

	return distance


# For all pairs of templates, calculates distances
def get_distances(gTemplates):

	gTemplatesCda = gTemplates
	distances = { }

	for gT in gTemplates:

		gTName = gT.name

		for gTc in gTemplatesCda:

			gTcName = gTc.name

			distance = simUI_d(gT.core, gTc.core)

			if gTName in distances:
				if gTcName not in distances[gTName]:
					distances[gTName][gTcName] = distance
			else:
				distances[gTName] = {gTcName: distance}

	return distances


# Turns a distance hash into a nexus file for SplitsTree
def to_nex(distances, outpath):

	distkeys = sorted(distances.keys())

	with open(outpath, "w") as outfile:

		outfile.write("#nexus\n")
		outfile.write("\n")
		outfile.write("BEGIN Taxa;\n")
		outfile.write("DIMENSIONS ntax="+str(len(distkeys))+";\n")
		outfile.write("TAXLABELS\n")

		for template in distkeys:
			outfile.write(template + "\n")

		outfile.write(";\n")
		outfile.write("END; [Taxa]\n")

		outfile.write("\n")

		outfile.write("BEGIN Distances;\n")
		outfile.write("DIMENSIONS ntax="+str(len(distkeys))+";\n")
		outfile.write("FORMAT labels=left diagonal triangle=lower;\n")
		outfile.write("MATRIX\n")

		templateCount = 0
		for template in distkeys:

			tempDistances = distances[template]
			distanceString = ""
			gridCount = 0

			for comparisonTemplate in sorted(tempDistances.keys()):
				if gridCount > templateCount:
					break
				roundedDistance = round(tempDistances[comparisonTemplate], 2)
				distanceString += ("\t" + str(roundedDistance))
				gridCount += 1

			outfile.write(template + "\t" + distanceString + "\n")
			templateCount += 1

		outfile.write(";\n")
		outfile.write("END; [Distances]\n")


# Turns a distance hash into a format more suitable for R (for multidimensional scaling)
def full_grid(distances):

	distkeys = sorted(distances.keys())

	grid = ""
	for template in distkeys:

		tempDistances = distances[template]
		distanceString = ""

		for comparisonTemplate in sorted(tempDistances.keys()):
			roundedDistance = round(tempDistances[comparisonTemplate],2)
			distanceString += ("\t" + str(roundedDistance))

		grid = grid + template + distanceString + "\n"

	return grid


# Renders each tdag to a .dot and rendered output file in outpath.
# Keeps .dot files for inspection; raises CalledProcessError if graphviz fails.
def draw_graphs(graphs, outpath, format="pdf"):

	os.makedirs(outpath, exist_ok=True)
	for graph in graphs:
		name = graph.name
		dot_file = os.path.join(outpath, str(name) + '.dot')
		out_file = os.path.join(outpath, str(name) + '.' + format)
		graph.to_dot().write_dot(dot_file)
		subprocess.run(["dot", f"-T{format}", dot_file, "-o", out_file], check=True)


# Renders only the component subgraph of each tdag.
def draw_components(graphs, outpath, format="pdf"):

	os.makedirs(outpath, exist_ok=True)
	for graph in graphs:
		name = graph.name
		dot_file = os.path.join(outpath, str(name) + '.dot')
		out_file = os.path.join(outpath, str(name) + '.' + format)
		graph.to_dot_components().write_dot(dot_file)
		subprocess.run(["dot", f"-T{format}", dot_file, "-o", out_file], check=True)
