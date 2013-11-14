#!/usr/bin/python2.7

import tdag
from tdag import rdfGraph, Namespace, RDF, tdag, conflate, process_template, prettyName
from tdag import simUI_d, get_distances, to_nex, draw_graphs, full_grid, process_templates, draw_components

outfile = open("GraphFlooding.pl", "w")

rdfTemplates = rdfGraph()

instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.load("./template.rdf")

# Get template IDs from RDF
templatesGenerator = rdfTemplates.subjects(RDF.type, instanceNS['desmeme'])

templates = []
for template in templatesGenerator:
	templates.append(template)
			
gTemplates = process_templates(templates, rdfTemplates)


print >> outfile, "#! /usr/bin/perl"
print >> outfile, "use strict;"


print >> outfile, "use FindBin;"
print >> outfile, "use lib \"$FindBin::Bin/.\";"
print >> outfile, "use GraphJG::SimilarityJG;"

print >> outfile, ""
print >> outfile, ""

templateNames = [ ]
print >> outfile, "my %templateGraphs = {};"
print >> outfile, ""

for tgraph in gTemplates:
	g = tgraph.core
	name = tgraph.name
	templateNames.append("\""+name+"\"") # quotes for perl
	nodes = g.nodes()
	edges = g.edges()
	
	print >> outfile, "my $"+name+" = Graph->new(multiedged => 1);"
	print >> outfile, "$"+name+"->set_graph_attribute(\"name\", "+"\""+name+"\""+");"
	labeledEdges = [ ]
	for edge in edges:
		edge_props =  g.get_edge_properties(edge)
		attribute = edge_props['label']
		n1, n2 = (edge)
		print >> outfile, "$"+name+"->add_edge_by_id(\""+n1+"\", "+"\""+n2+"\", "+"\""+attribute+"\");"
	print >> outfile, "$templateGraphs{"+name+"} = $"+name+";"
	print >> outfile, ""

templateNames.sort()
print >> outfile, "my @templates = ("+", ".join(templateNames)+");"
print >> outfile, "my @templatesCopy = @templates;"
print >> outfile, ""

print >> outfile, "open (NULL, '>FloodingSimilarities.txt');  #Erase file"

print >> outfile, "for my $templateName1 (@templates) {"
print >> outfile, ""
print >> outfile, "	for my $templateName2 (@templatesCopy) {"
print >> outfile, ""
print >> outfile, "		my $s = new GraphJG::SimilarityJG(graph => [$templateGraphs{$templateName1}, $templateGraphs{$templateName2}]);"
print >> outfile, "		my $method = $s->use('SimilarityFlooding');"
print >> outfile, "		$method->setNumOfIteration(100);"
print >> outfile, "		$method->calculate();"
print >> outfile, ""
print >> outfile, "		$method->getLargeSimilarities($templateName1,$templateName2);"
print >> outfile, "	"
print >> outfile, "		}"
print >> outfile, "	}"