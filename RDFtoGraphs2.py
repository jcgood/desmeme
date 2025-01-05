#!/usr/bin/python2.7

# See: https://stackoverflow.com/questions/18649512/unicodedecodeerror-ascii-codec-cant-decode-byte-0xe2-in-position-13-ordinal?rq=4
import sys
#reload(sys)
#sys.setdefaultencoding('utf8')

import tdag
from tdag import rdfGraph, Namespace, RDF, tdag, conflate, process_template, prettyName
from tdag import simUI_d, get_distances, to_nex, draw_graphs, full_grid, process_templates, draw_components


rdfTemplates = rdfGraph()

instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.parse("./template-CHx.rdf")

# Get template IDs from RDF
templatesGenerator = rdfTemplates.subjects(RDF.type, instanceNS['desmeme'])

templates = []
for template in templatesGenerator:
	templates.append(template)
			
gTemplates = process_templates(templates, rdfTemplates)


graphfolder = "Graphs/"
draw_graphs(gTemplates, graphfolder)


graphfolder = "ComponentGraphs/"
draw_components(gTemplates, graphfolder)