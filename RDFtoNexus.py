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