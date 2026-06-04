from tdag.tdag import tdag
from tdag.validator import schema
from tdag.avm import avm
from tdag.tabbed import get_tabbed_desmemes

from tdag.comparison import draw_graphs

import re
from collections import defaultdict


desmemeFileName = "data/nya/ChichewaDesmemes.tsv"
componentFileName = "data/nya/ChichewaComponents.tsv"

graphfolder = "output/Graphs_full/"

desmemeSchemaFileName = "schema/DesmemeSchema.tsv"
componentSchemaFileName = "schema/ComponentSchema.tsv"

## Validation seems done
## Next step: Extract other information (e.g., source, transcription) from RDF, and incorporate somehow...

# Should I make a test suite?
	
## Also, some data is in RDF that needs dumped, like source, notes, transcription string, usw.
## May need to open up Protege to verify, or check book dump?

desdags = get_tabbed_desmemes(desmemeFileName, componentFileName, desmemeSchemaFileName, componentSchemaFileName)

for desdag in desdags:
	
	name = desdag.name
		
	templateAVM = avm(name, "desmeme")
	templateAVM.graph_toAVM(desdag)

	# to_ASCII prints to STDOUT
	print("ID:\t" + name)
	templateAVM.to_ASCII()
	print()

	# expects a list of graphs; so construct a list of one element
	# maybe make a draw_graph function at some point?
	#draw_graphs([desdag], graphfolder)

# This breaks on full templates with metadata, etc.
#draw_graphs(desdags, graphfolder)
