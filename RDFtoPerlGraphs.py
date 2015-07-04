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
	edges = tgraph.edges.values() # Important: Grab the edges of the tdag, not the embedded dag to deal with re-entrancy!
	
	#print name
	#print edges
	
	print >> outfile, "my $"+name+" = Graph->new(multiedged => 1);"
	print >> outfile, "$"+name+"->set_graph_attribute(\"name\", "+"\""+name+"\""+");"
	labeledEdges = [ ]
	
	for edge in edges:
		#edge_props =  g.get_edge_properties(edge)
		#attribute = edge_props['label']
		#print edge, edge_props
		(n1, n2), attribute = (edge)
		#print n1, n2, attribute
		print >> outfile, "$"+name+"->add_edge_by_id(\""+n1+"\", "+"\""+n2+"\", "+"\""+attribute+"\");"
	
	print >> outfile, "$templateGraphs{"+name+"} = $"+name+";"
	print >> outfile, ""

templateNames.sort()

# Ugly, I know.

print >> outfile, "my @templates = ("+", ".join(templateNames)+");"
print >> outfile, "my @templatesCopy = @templates;"
print >> outfile, ""

print >> outfile, "open (NULL, '>FloodingSimilarities.txt');  #Erase file"
print >> outfile, "my %seenPairs = { };"
print >> outfile, "for my $templateName1 (@templates) {"
print >> outfile, ""
print >> outfile, "	for my $templateName2 (@templatesCopy) {"
print >> outfile, ""
print >> outfile, "		if ($seenPairs{$templateName2.\"/\".$templateName1}) { print next; }"
print >> outfile, ""
print >> outfile, "		# Initialize simList for calculating Euclidean distances."
print >> outfile, "		my $initialS = new GraphJG::SimilarityJG(graph => [$templateGraphs{$templateName1}, $templateGraphs{$templateName2}]);"
print >> outfile, "		my $initialMethod = $initialS->use('SimilarityFlooding');"
print >> outfile, "		$initialMethod->setNumOfIteration(1);"
print >> outfile, "		$initialMethod->calculate();"
print >> outfile, "		my %simList = $initialMethod->getAllSimilarities;"
print >> outfile, "	"
print >> outfile, "		print \"$templateName1/$templateName2\\n\";"
print >> outfile, ""
print >> outfile, "		# Keep incrementing the iteration until we reach Euclidean distance of less than or equal to .05. Start at 2 to get difference from initial condition."
print >> outfile, "		for (my $count = 2; $count <=100; $count++) {"
print >> outfile, ""
print >> outfile, "			my $s = new GraphJG::SimilarityJG(graph => [$templateGraphs{$templateName1}, $templateGraphs{$templateName2}]);"
print >> outfile, "			my $method = $s->use('SimilarityFlooding');"
print >> outfile, "			$method->setNumOfIteration($count);"
print >> outfile, "			$method->calculate();"
print >> outfile, ""
print >> outfile, "			my %newSimList = $method->getAllSimilarities;"
print >> outfile, ""
print >> outfile, "			my @dists;"
print >> outfile, "			for my $v (keys(%simList)) {"
print >> outfile, "				# This is messy: We run through the paired graph to see if this paired node is in any subgraph."
print >> outfile, "				# \"Free-floating\" nodes get ignored for the purposes of calculating the Euclidean distance."
print >> outfile, "				# Appears to not actually make a difference if epsilon is set to .05 since the residuals converge pretty quickly to nearly the same. This is because free-floating nodes rapidly get a score close to zero."
print >> outfile, "				my $pcg = $method->pcg;"
print >> outfile, "				my @pairedvs = $pcg->vertices();"
print >> outfile, "				for my $pairedv (@pairedvs) {"
print >> outfile, "					if($v eq $pairedv) {"
print >> outfile, "						my $oldSim = $simList{$v};"
print >> outfile, "						my $newSim = $newSimList{$v};"
print >> outfile, "						my $diff = $oldSim - $newSim;"
print >> outfile, "						push(@dists,$diff);"
print >> outfile, "						last;"
print >> outfile, "						}"
print >> outfile, "					}"
print >> outfile, "				}"
print >> outfile, "	"
print >> outfile, "			my $eucSum;"
print >> outfile, "			for my $dist (@dists) {	"
print >> outfile, "				$eucSum += $dist*$dist;"
print >> outfile, "				}"
print >> outfile, "	"
print >> outfile, "			my $eucDist = sqrt($eucSum);"
print >> outfile, "			print \"$count: $eucDist\\n\";"
print >> outfile, "	"
print >> outfile, "			if ($eucDist < .05) {"
print >> outfile, "	 			$method->getLargeSimilarities($templateName1,$templateName2);"
print >> outfile, " 				$seenPairs{$templateName1.\"/\".$templateName2} = 1;"
print >> outfile, "				last;"
print >> outfile, "				}"
print >> outfile, "	"
print >> outfile, "			%simList = %newSimList;"
print >> outfile, "	"
print >> outfile, "			}"
print >> outfile, "		}"
print >> outfile, "	}"