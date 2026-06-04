# Functions for comparing tdag graphs, including distance metrics, nexus output, and visualization.

import os

from pygraph.readwrite.dot import write
from pygraph.readwrite import *


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
		gridCount = 0

		tempdistkeys = sorted(tempDistances.keys())
	
		for comparisonTemplate in tempdistkeys:
							
			
			roundedDistance = round(tempDistances[comparisonTemplate],2)
			distanceString += ("\t" + str(roundedDistance))
	
		# Write out the distances string manually
		grid = grid + template + distanceString + "\n"
	
	return grid
	

# Turns a template into a .dot file for visualization, requires the special graphs
# created by tdag
def draw_graphs(graphs, outpath, format="png"):

	extension = "." + format
	for graph in graphs:	
		name = graph.name
		dot = graph.to_dot() # my hack for reentrancy from foundation
		
		# To self: I spent a long time working out why .dot files had attributes
		# such as width and pos that I didn't have in my representation.
		# This "write_dot" function is a special pydot feature that doesn't
		# exist as an actual method but is, rather, generated automatically based on the extension (sort of).
		# The internal representation is passed through the dot program and the output adds these extra features.
		# This seems to be the same as the "default" ones if they aren't added.
		# I looked into this to see how I should be customizing node placement.
		# I guess I'd have to delve deep into dot to find out at this point.
		dot.write_dot(outpath + str(name) + '.dot')
		
		# dot's PS driver doesn't work well. Go to pdf and then to .ps
		dotcmd = "dot -Tpdf " + outpath + str(name) + '.dot' + " > " + outpath + str(name) + '.pdf'
		os.system(dotcmd)
		
		# 1/23/2025: I don't know why I take these extra steps, maybe I needed .eps at one point?
		pscmd = "pdf2ps " + outpath + str(name) + '.pdf' + " " + outpath + str(name) + '.ps' 
		#print(pscmd)
		os.system(pscmd)

		# ps2eps has different syntax from others 
		epscmd = "ps2eps " + outpath + str(name) + '.ps' 
		os.system(epscmd)
		
		# Cleanup
		rmdot = "rm " + outpath + str(name) + '.dot'
		#os.system(rmdot)
		rmps = "rm " + outpath + str(name) + '.ps'
		os.system(rmps)
		rmeps = "rm " + outpath + str(name) + '.eps'
		os.system(rmeps)

		
	
# Turns a template into a .dot file but only gives components
def draw_components(graphs, outpath, format="png"):

	extension = "." + format
	for graph in graphs:	
		name = graph.name
		dot = graph.to_dot_components() # my hack for reentrancy from foundation
		dot.write_dot(outpath + str(name) + '.dot')

		# dot's PS driver doesn't work well. Go to pdf and then to .ps
		dotcmd = "dot -Tpdf " + outpath + str(name) + '.dot' + " > " + outpath + str(name) + '.pdf'
		os.system(dotcmd)
		
		pscmd = "pdf2ps " + outpath + str(name) + '.pdf' + " " + outpath + str(name) + '.ps' 
		#print(pscmd)
		os.system(pscmd)

		# ps2eps has different syntax from others 
		epscmd = "ps2eps " + outpath + str(name) + '.ps' 
		os.system(epscmd)
		
		# Cleanup
		rmdot = "rm " + outpath + str(name) + '.dot'
		os.system(rmdot)
		rmps = "rm " + outpath + str(name) + '.ps'
		os.system(rmps)
		rmeps = "rm " + outpath + str(name) + '.eps'
		os.system(rmeps)

