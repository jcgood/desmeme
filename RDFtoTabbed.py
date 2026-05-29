# I have a weird mix of the older and newer functions now
import tdag_orig
from tdag_orig import rdfGraph, Namespace, RDF, process_templates, process_templates_full
from tdag_orig.tabbed import tabbed
from tdag.comparison import draw_graphs
import os

# Load templates, turn them into despecified graphs
rdfTemplates = rdfGraph()
instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
rdfTemplates.parse("./template-CHx.rdf")
templatesGenerator = rdfTemplates.subjects(RDF['type'], instanceNS['desmeme'])
templates = []
for template in templatesGenerator:
	templates.append(template)
gTemplates = process_templates_full(templates, rdfTemplates)


desfilename = "ChichewaDesmemes_full"
compfilename = "ChichewaComponents_full"

# Erase existing files
# Needed temp files due to annoying problem where I couldn't avoid a blank
# first line. Deleting it was very hard. Really weird issues when I tried to write back to
# the original file.
open(desfilename + "_temp.tsv", "w").close()
open(compfilename + "_temp.tsv", "w").close()
open(desfilename + ".tsv", "w").close()
open(compfilename + ".tsv", "w").close()

graphfolder = "Graphs_full/"


# Need to keep track of components appear in more than one place
seenComponents = [ ]
for gTemplate in gTemplates:

	templateTabbed = tabbed(gTemplate.name,"desmeme")
	templateTabbed.graph_toAVM(gTemplate)
	templateTabbed.canonicalize()
	
	desfile = open(desfilename + "_temp.tsv", "a")
	templateTabbed.to_tabbed_desmeme(desfile)
	desfile.close()

	with open(desfilename + "_temp.tsv", 'r') as fin:
		data = fin.read().splitlines(True)
	with open(desfilename + ".tsv", 'w') as fout:
		fout.writelines(data[1:])	

	compfile = open(compfilename + "_temp.tsv", "a")
	# This function returns an updated seenComponents list
	seenComponents = templateTabbed.to_tabbed_components(compfile, seenComponents)
	compfile.close()

	with open(compfilename + "_temp.tsv", 'r') as fin:
		data = fin.read().splitlines(True)
	with open(compfilename + ".tsv", 'w') as fout:
		fout.writelines(data[1:])

os.remove(desfilename + "_temp.tsv") 		
os.remove(compfilename + "_temp.tsv")

# This breaks on full templates with metadata, etc.
#draw_graphs(gTemplates, graphfolder)
