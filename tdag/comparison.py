# Functions for comparing tdag graphs, including distance metrics, nexus output, and visualization.

import os
import subprocess


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
