from tdag.tdag import tdag
from tdag.validator import schema
from tdag.avm import avm
from tdag.tabbed import get_tabbed_component

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


					


with open(desmemeFileName) as desmemeFile:
	 desmemes = desmemeFile.read().split('\n\n')

URIs = defaultdict(int)
for desmeme in desmemes:
	
	seenComps = [ ]

	# Features with component as a value since these need special treatment
	componentFeatures = [
							"LEFT_SUPPORT",
							"LEFT_VOUSSOIR",
							"KEYSTONE",
							"RIGHT_VOUSSOIR",
							"RIGHT_SUPPORT",
							"RESTKOMPONENTE",
							"FILLED_COMPONENT",
							"ASSOCIATE"
						]
	
	# * unpacks the remainder to featvals
	[idfv, langfv, *featvals] = desmeme.split('\n')
	
	[idfeat, id_] = idfv.split('\t')
	if idfeat != "IDENTIFIER":
		raise(ValueError('Expected leading IDENTIFIER feature, but found {idfeat}'.format(idfeat=repr(idfeat))))
	
	print("ID", id_)
	
	[langfeat, lang] = langfv.split('\t')
	if langfeat != "LANGUAGE":
		raise(ValueError('Expected leading LANGUAGE feature, but found {langfeat}'.format(langfeat=repr(langfeat))))

	desdag = tdag(id_)

	topType = "desmeme"
	previousType = topType
	prevtabCount = 0
	URIbase = id_

	# add root
	desdag.add_node(topType, URIbase)

	embeddings = { }
	
	for featval in featvals:
		
		# Tracks if we need to do do component parsing
		atComponent = False
		
		tabs = re.match('^\t+', featval)
		if tabs != None:
			tabCount = tabs[0].count('\t')
		else: tabCount = 0
		featval = featval.lstrip()
		
		# Deals with a final line break issue, maybe can be handled better
		if featval == "": continue
		else: feature, value = featval.split('\t')

		# Override component ID in node label with generic type
		if feature in componentFeatures:
			value = "component" + "_" + value
			URI = value
			atComponent = True
	
		else:
			URIstem = URIbase +"-" + previousType + "-" + feature
			featcounter = URIs[URIstem]
			URI = URIstem + "-" + str(featcounter + 1)
			URIs[URIstem] += 1

		# special logic for digits since they break python-graph somehow
		if value.isdigit() or value == "∞":
			value = URI + "_" + value
			URI = value

		
		# Was using URI's to disambiguate repeating features (e.g., in components)
		# Will need to adapt...
		if tabCount == prevtabCount:

			embeddings[tabCount + 1] = value

			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)
			desdag.add_edge((previousType, value), feature)


		# Should only ever increment by one tab
		elif tabCount > prevtabCount: 		

			embeddings[tabCount + 1] = value
			prevtabCount = tabCount

			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)
			previousType = embeddings[tabCount]
			desdag.add_edge((previousType, value), feature)

		elif tabCount < prevtabCount: 		
			embeddings[tabCount + 1] = value
			prevtabCount = tabCount

			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)

			try: previousType = embeddings[tabCount - 1]
			except: previousType = topType
			desdag.add_edge((previousType, value), feature)
			
		# If we are adding a component, then get the component features in the component file
		# This is an ugly, redundant process since I don't think the graph library that I am
		# using can merge graphs, which is why it should probably be updated (see above)
		if atComponent == True:
			get_tabbed_component(desdag, URI, componentFileName)



	## Also, some data is in RDF that needs dumped, like source, notes, transcription string, usw.
	## May need to open up Protege to verify, or check book dump?
	## I accidentally broke RDFtoTabbed. Is it worth fixing? Or, should I verify the desmemes?
	
	templateAVM = avm(id_, "desmeme")
	templateAVM.graph_toAVM(desdag)
	
	# to_ASCII prints to STDOUT
	templateAVM.to_ASCII()
	print()
	
	# expects a list of graphs; so construct a list of one element
	# maybe make a draw_graph function at some point?
	draw_graphs([desdag], graphfolder)


