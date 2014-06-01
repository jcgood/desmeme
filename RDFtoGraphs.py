#!/usr/bin/python2.7

import tdag
from tdag import rdfGraph, Namespace, RDF, tdag, conflate, process_template, prettyName
from tdag import simUI_d, get_distances, to_nex, draw_graphs, full_grid, process_templates, draw_components


rdfTemplates = rdfGraph()

instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.load("./template.rdf")

# Get template IDs from RDF
templatesGenerator = rdfTemplates.subjects(RDF.type, instanceNS['desmeme'])

templates = []
for template in templatesGenerator:
	templates.append(template)
			
gTemplates = process_templates(templates, rdfTemplates)

# NOTE: CAN NO LONGER GO DIRECTLY TO PNG or PDF; MUST MANUALLY PROCESS .dot FOR NOW
#graphfolder = "/Volumes/Obang/MyDocuments/Linearity/template_ontology/Graphs/"
#graphfolder = "/Users/jcgood/Desktop/Graphs/"
#graphfolder = "/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/Graphs/"

graphfolder = "/Users/jcgood/Dropbox/TemplatesBook/Graphs/"

draw_graphs(gTemplates, graphfolder)


graphfolder = "/Users/jcgood/Dropbox/TemplatesBook/ComponentGraphs/"
draw_components(gTemplates, graphfolder)