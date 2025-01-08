from tdag.tdag import tdag
from tdag.validator import schema
from tdag.avm import avm

import re

desmemeFileName = "ChichewaDesmemes.tsv"

# For later, get the schema
schemaFileName = "DesmemeSchema.tsv"
desmemeSchema = schema(schemaFileName, "desmeme")
[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()

with open(desmemeFileName) as desmemeFile:
	 desmemes = desmemeFile.read().split('\n\n')
	 
for desmeme in desmemes:
	
	# * unpacks the remainder to featvals
	[idfv, langfv, *featvals] = desmeme.split('\n')
	
	[idfeat, id_] = idfv.split('\t')
	if idfeat != "IDENTIFIER":
		raise(ValueError('Expected leading IDENTIFIER feature, but found {idfeat}'.format(idfeat=repr(idfeat))))
		
	[langfeat, lang] = langfv.split('\t')
	if langfeat != "LANGUAGE":
		raise(ValueError('Expected leading IDENTIFIER feature, but found {idfeat}'.format(langfeat=repr(langfeat))))

	desdag = tdag(id_)

	topType = "desmeme"
	previousType = topType
	prevtabCount = 0
	URI = "URI" # dummy, need to fix to fully utilize existing code effectively

	# add root
	desdag.add_node(topType, URI)

	embeddings = { }
	#embedding = 0
	for featval in featvals:
		
		tabs = re.match('^\t+', featval)
		if tabs != None:
			tabCount = tabs[0].count('\t')
		else: tabCount = 0
		featval = featval.lstrip()
		
		# Deals with a final line break issue, maybe can be handled better
		if featval == "": pass
		else: feature, value = featval.split('\t')
		
		# special logic for digits since they break python-graph somehow
		if value.isdigit():
			value = "no" + value
		
		# Was using URI's to disambiguate repeating features (e.g., in components)
		# Will need to adapt...
		if tabCount == prevtabCount:

			embeddings[tabCount + 1] = value

			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)
			desdag.add_edge((previousType, value), feature)


		# Should only ever increment by one tab
		if tabCount > prevtabCount: 		

			embeddings[tabCount + 1] = value
			prevtabCount = tabCount

			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)
			previousType = embeddings[tabCount]
			desdag.add_edge((previousType, value), feature)

		if tabCount < prevtabCount: 		
			embeddings[tabCount + 1] = value
			prevtabCount = tabCount

			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)

			try: previousType = embeddings[tabCount - 1]
			except: previousType = topType
			desdag.add_edge((previousType, value), feature)
	
	
	# proof of concept is now OK, but a lot of detailed work to be done
	templateAVM = avm(id_, "desmeme")
	templateAVM.graph_toAVM(desdag)
	
	templateAVM.to_ASCII()
	print()