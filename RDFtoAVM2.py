import tdag
from tdag import rdfGraph, Namespace, RDF, process_templates
from tdag.avm import avm


# Load templates, turn them into despecified graphs
rdfTemplates = rdfGraph()
instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.parse("./template-CHx.rdf")
templatesGenerator = rdfTemplates.subjects(RDF['type'], instanceNS['desmeme'])
templates = []
for template in templatesGenerator:
	templates.append(template)
	print(template)
gTemplates = process_templates(templates, rdfTemplates)

#avmfolder = "/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/AVMs/"
avmfolder = "./AVMs/"


for gTemplate in gTemplates:

	#print(gTemplate)
	
	templateAVM = avm(gTemplate.name,"desmeme")
	templateAVM.graph_toAVM(gTemplate)
	templateAVM.canonicalize()
	
	outfile = open(avmfolder+templateAVM.name+".tex", "w")

	templateAVM.to_latex(templateAVM, outfile)
	
	templateAVM.to_ASCII(templateAVM)
		
