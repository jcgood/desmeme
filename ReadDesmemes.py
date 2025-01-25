from tdag.tdag import tdag
from tdag.validator import schema
from tdag.avm import avm
from tdag.tabbed import get_tabbed_desmemes

from tdag.comparison import draw_graphs

import re
from collections import defaultdict


desmemeFileName = "ChichewaDesmemes.tsv"
componentFileName = "ChichewaComponents.tsv"

graphfolder = "Graphs/"

# For later, get the schema
schemaFileName = "DesmemeSchema.tsv"
desmemeSchema = schema(schemaFileName, "desmeme")

# To do: Validation
[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()


# Should I make a test suite?

# To do, can I refactor the add node/add edge logic for the desmeme loop like I did for component?

	
## Also, some data is in RDF that needs dumped, like source, notes, transcription string, usw.
## May need to open up Protege to verify, or check book dump?

desdags = get_tabbed_desmemes(desmemeFileName, componentFileName)

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

#draw_graphs(desdags, graphfolder)
