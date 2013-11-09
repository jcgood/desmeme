#!/usr/bin/python2.7

import re

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

procTemps = { }
for tgraph in gTemplates:

	name = tgraph.name
	g = tgraph.core
	edges = g.edges()

	predToEdge = { }
	for edge in edges:
		edge_props =  g.get_edge_properties(edge)
		pred = edge_props['label']
		n1, n2 = (edge)
		
		if n1 == 'order' or n1 == 'length':
			
			countMatch = re.compile('COUNT(\d)-(\d)')
			matches = countMatch.match(n2)

			if matches: predToEdge[str(pred)] = (matches.group(1))
			else: predToEdge[str(pred)] = (n2)
		
		elif pred != 'COUNT' :
			predToEdge[str(pred)] = (n2)
		
		else: pass # Ignore component counts
		
	procTemps[name] = predToEdge


print "name,violability,conditioning,exceptionality,reparability,foundation,stricture,relations,constituent,count"
for tempName in procTemps.keys():
	
	temp = procTemps[tempName]
	
	viol = temp['VIOLABILITY']
	cond = temp['CONDITIONING']
	found = temp['FOUNDATION']
	stric = temp['STRICTURE']
	count = temp['COUNT']
	const = temp['CONSTITUENT']

	try: rel = temp['RELATIONS']
	except: rel = "NA"
	
	try: exc = temp['EXCEPTIONALITY']
	except: exc = "NA"
	
	try: rep = temp['REPARABILITY']
	except: rep = "NA"
		
	print tempName+","+viol+","+cond+","+exc+","+rep+","+found+","+stric+","+rel+","+const+","+count
	