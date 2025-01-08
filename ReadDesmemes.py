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

	parent = "desmeme"
	prevtabCount = 0
	URI = "URI" # dummy
	for featval in featvals:
	
		tabs = re.match('^\t+', featval)
		if tabs != None:
			tabCount = tabs[0].count('\t')
		else: tabCount = 0
		featval = featval.lstrip()
		
		# final \n caused an extra empty line that broke things. will need to check this
		try: feature, value = featval.split('\t')
		except: print("X", featval)
		
		# Was using URI's to disambiguate repeating features (e.g., in components)
		# Will need to adapt...
		if tabCount == prevtabCount:
		
			if (not desdag.has_node(parent, URI)): desdag.add_node(parent, URI)
			if (not desdag.has_node(value, URI)): desdag.add_node(value, URI)
			desdag.add_edge((parent, value), feature)
	
	
	# proof of concept is now OK, but a lot of detailed work to be done
	templateAVM = avm(id_, "desmeme")
	templateAVM.graph_toAVM(desdag)
	
	print(templateAVM.to_ASCII(templateAVM))