# Functions for comparing graphs, once they've been properly despecified,
# including visualization.

import os

from pygraph.readwrite.dot import write
from pygraph.readwrite import *

import despecification
from despecification import prettyName

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
	
			# If the standard template is already on the distances table, retrieve its hash
			if distances.has_key(gTName):
			
				gTDists = distances[gTName]
	 
				if gTDists.has_key(gTcName):
					pass
				
				# If this distance isn't there yet, add it in, and then reassign the template's hash to the final hash
				else:
					gTDists[gTcName] = distance
					distances[gTName] = gTDists
				
			# Different logic for first time assigning a hash in the hash since we need to create its ash
			else:
				firstgTDists = {}
				firstgTDists[gTcName] = distance
				distances[gTName] = firstgTDists
	
	return distances

	
# Turns a distance hash into a nexus file for SplitsTree
def to_nex(distances, outfile):
	
	outfile = open(outfile, "w")

	distkeys = distances.keys()
	distkeys.sort()
	
	outfile.write("#nexus\n")
	outfile.write("\n")
	outfile.write("BEGIN Taxa;\n")
	outfile.write("DIMENSIONS ntax="+str(len(distkeys))+";\n")
	outfile.write("TAXLABELS\n")
	
	for template in distkeys:	
		templateName = prettyName(template)
		outfile.write(templateName + "\n")
		
	outfile.write(";\n")
	outfile.write("END; [Taxa]\n")
	
	outfile.write("\n")
	
	outfile.write("BEGIN Distances;\n")
	outfile.write("DIMENSIONS ntax="+str(len(distkeys))+";\n")
	outfile.write("FORMAT labels=left diagonal triangle=lower;\n")
	outfile.write("MATRIX\n")
	
	templateCount =  0
	distkeys = distances.keys()
	distkeys.sort()
	
	for template in distkeys:
		
		tempDistances = distances[template]
	
		distanceString = ""
		gridCount = 0
	
		tempdistkeys = tempDistances.keys()
		tempdistkeys.sort()
	
		for comparisonTemplate in tempdistkeys:
			
			# Prints half grid
			if gridCount > templateCount:
				break
				
			else:
				roundedDistance = round(tempDistances[comparisonTemplate],2)
				distanceString += ("\t" + str(roundedDistance))
				
			gridCount  += 1
	
		# Write out the distances string manually
		outfile.write(template + "\t" + distanceString + "\n")
	
		templateCount += 1
	
	outfile.write(";\n")
	outfile.write("END; [Distances]\n")


# Turns a distance hash into a format more suitable for R (for multidimensional scaling)
def full_grid(distances):
	
	distkeys = distances.keys()
	distkeys.sort()
	
	grid = ""
	for template in distkeys:
		
		tempDistances = distances[template]
	
		distanceString = ""
		gridCount = 0
	
		tempdistkeys = tempDistances.keys()
		tempdistkeys.sort()
	
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
		
		pscmd = "pdf2ps " + outpath + str(name) + '.pdf' + " " + outpath + str(name) + '.ps' 
		print pscmd
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

# 		pdfcmd = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape " + outpath + str(name) + '.svg' + " --export-pdf " + outpath + str(name) + '.pdf'
# 		os.system(pdfcmd)
# 
# 		epscmd = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape " + outpath + str(name) + '.svg' + " --export-eps " + outpath + str(name) + '.eps'
# 		os.system(epscmd)
		
		
		
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
		print pscmd
		os.system(pscmd)

		# ps2eps has different syntax from others 
		epscmd = "ps2eps " + outpath + str(name) + '.ps' 
		os.system(epscmd)
		
		# Cleanup
		rmdot = "rm " + outpath + str(name) + '.dot'
		os.system(rmdot)
		rmps = "rm " + outpath + str(name) + '.ps'
		os.system(rmps)


# 		dotcmd = "dot -Tsvg " + outpath + str(name) + '.dot' + " > " + outpath + str(name) + '.svg'
# 		os.system(dotcmd)
# 
# 		imgcmd = "/Applications/Inkscape.app/Contents/Resources/bin/inkscape " + outpath + str(name) + '.svg' + " --export-pdf " + outpath + str(name) + '.pdf'
# 		os.system(imgcmd)
