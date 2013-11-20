#!/sw/bin/python2.7

import tdag
from tdag import rdfGraph, Namespace, RDF, process_templates
from tdag.avm import avm


# Load templates, turn them into despecified graphs
rdfTemplates = rdfGraph()
instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.load("./template.rdf") ## relative paths broken on laptop; see above fix with import OS, extend to other scripts
templatesGenerator = rdfTemplates.subjects(RDF['type'], instanceNS['desmeme'])
templates = []
for template in templatesGenerator:
	templates.append(template)
gTemplates = process_templates(templates, rdfTemplates)

avmfolder = "/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/AVMs/"
#avmfolder = "/Users/jcgood/Desktop/AVMs/"


for gTemplate in gTemplates:
	
	templateAVM = avm(gTemplate.name,"desmeme")
	templateAVM.graph_toAVM(gTemplate)
	templateAVM.canonicalize()
	
	outfile = open(avmfolder+templateAVM.name+".tex", "w")

	templateAVM.to_latex(templateAVM, outfile)
	
	#templateAVM.to_ASCII(templateAVM)
		
	#print "\n"