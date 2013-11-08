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

for tgraph in gTemplates:
	g = tgraph.core
	nodes = g.nodes()
	edges = g.edges()
	
	labeledEdges = [ ]
	for edge in edges:
		edge_props =  g.get_edge_properties(edge)
		attribute = edge_props['label']
		n1, n2 = (edge)
		#print n1, n2
		labeledEdges.append([n1, n2, attribute])
		
	print nodes
	print labeledEdges