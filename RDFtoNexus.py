#!/usr/bin/python2.7

import tdag
from tdag import rdfGraph, Namespace, RDF, tdag, conflate, process_template, prettyName
from tdag import simUI_d, get_distances, to_nex, draw_graphs, full_grid, process_templates, process_templates_noComp


rdfTemplates = rdfGraph()

instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.load("./template.rdf")

# Get template IDs from RDF
templatesGenerator = rdfTemplates.subjects(RDF.type, instanceNS['desmeme'])

templates = []
for template in templatesGenerator:
	templates.append(template)
			
gTemplates = process_templates(templates, rdfTemplates)
gTemplatesNoComp = process_templates_noComp(templates, rdfTemplates) # Get rid of components for another comparison

distances = get_distances(gTemplates)
outfile = "/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/template.nex"
to_nex(distances,outfile)

noCompDistances = get_distances(gTemplatesNoComp)
noCompOutfile = "/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/templateNoComp.nex"
to_nex(noCompDistances,noCompOutfile)

print full_grid(distances)

print "NoComp"

distancesNoComp = get_distances(gTemplatesNoComp)
print full_grid(distancesNoComp)


# As long as here, let's generate some LaTeX--probably should put this in the module, but I'm too lazy right now
pairwiseComps = open("/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/pairwiseComps.tex", "w")
print >> pairwiseComps, "\\begin{sidewaystable}[ht!]"
print >> pairwiseComps, "{\\footnotesize"
print >> pairwiseComps, "\\setlength{\\tabcolsep}{.45em}"
print >> pairwiseComps, "\\begin{tabular}{@{}lrrrrrrrrrrrrrrrrrrrr}"

distkeys = distances.keys()
distkeys.sort()
templateCount =  0
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
			roundedDistance = '{0:.2f}'.format(round(tempDistances[comparisonTemplate],2))
			distanceString += ("\t&\t" + str(roundedDistance))
			
		gridCount  += 1

	# Write out the distances string
	print >> pairwiseComps, template + distanceString + "\t\\\\"
	templateCount += 1
		
print >> pairwiseComps, "\\end{tabular}}"
print >> pairwiseComps, "\\caption{Pairwise distances among examined templates including component nodes \\label{Distances}}"
print >> pairwiseComps, "\\end{sidewaystable}"

pairwiseComps = open("/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/pairwiseComps.tex", "w")
print >> pairwiseComps, "\\begin{sidewaystable}[ht!]"
print >> pairwiseComps, "{\\footnotesize"
print >> pairwiseComps, "\\setlength{\\tabcolsep}{.45em}"
print >> pairwiseComps, "\\begin{tabular}{@{}lrrrrrrrrrrrrrrrrrrrr}"


# Now no comps distances
pairwiseNoComps = open("/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/pairwiseNoComps.tex", "w")
print >> pairwiseNoComps, "\\begin{sidewaystable}[ht!]"
print >> pairwiseNoComps, "{\\footnotesize"
print >> pairwiseNoComps, "\\setlength{\\tabcolsep}{.45em}"
print >> pairwiseNoComps, "\\begin{tabular}{@{}lrrrrrrrrrrrrrrrrrrrr}"

distkeys = distancesNoComp.keys()
distkeys.sort()
templateCount =  0
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
			roundedDistance = '{0:.2f}'.format(round(tempDistances[comparisonTemplate],2))
			distanceString += ("\t&\t" + str(roundedDistance))
			
		gridCount  += 1

	# Write out the distances string
	print >> pairwiseNoComps, template + distanceString + "\t\\\\"
	templateCount += 1
		
print >> pairwiseNoComps, "\\end{tabular}}"
print >> pairwiseNoComps, "\\caption{Pairwise distances among examined templates excluding component nodes \\label{Distances}}"
print >> pairwiseNoComps, "\\end{sidewaystable}"

