#!/sw/bin/python2.7

import tdag
from tdag import rdfGraph, Namespace, RDF, process_templates
from tdag.avm import avm
import inspect

# Load templates, turn them into despecified graphs
rdfTemplates = rdfGraph()
instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.load("./template.rdf")
templatesGenerator = rdfTemplates.subjects(RDF['type'], instanceNS['desmeme'])
templates = []
for template in templatesGenerator:
	templates.append(template)
gTemplates = process_templates(templates, rdfTemplates)

for gTemplate in gTemplates:
	
	templateAVM = avm(gTemplate.name,"desmeme")
	templateAVM.graph_toAVM(gTemplate)
	
	templateAVM.canonicalize()
	#templateAVM.to_latex(templateAVM)
	templateAVM.to_ASCII(templateAVM)
		
	print "\n"