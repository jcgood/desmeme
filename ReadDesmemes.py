from tdag.tdag import tdag
from tdag.validator import schema
from tdag.avm import avm

from tdag.comparison import draw_graphs

import re
from collections import defaultdict


desmemeFileName = "ChichewaDesmemes.tsv"
componentFileName = "ChichewaComponents.tsv"

graphfolder = "Graphs/"

# For later, get the schema
schemaFileName = "DesmemeSchema.tsv"
desmemeSchema = schema(schemaFileName, "desmeme")
[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()

URIs = defaultdict(int)


# To do: Validation
with open(desmemeFileName) as desmemeFile:
	 desmemes = desmemeFile.read().split('\n\n')

 
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
	#embedding = 0
	
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

			previousCompType = URI
			topURI = URI

			with open(componentFileName) as componentFile:
				components = componentFile.read().split('\n\n')
			
			for component in components:
	
				# repeating a lot of code here, will need to refactor, but I want to try to get a working pass first
	
				# * unpacks the remainder to featvals
				[compidfv, complangfv, *compfeatvals] = component.split('\n')
	
				[compidfeat, compid] = compidfv.split('\t')
				if compidfeat != "IDENTIFIER":
					raise(ValueError('Expected leading IDENTIFIER feature, but found {compidfeat}'.format(compidfeat=repr(compidfeat))))
				
				# could do validation here to verify language match
				[complangfeat, complang] = complangfv.split('\t')
				if complangfeat != "LANGUAGE":
					raise(ValueError('Expected leading LANGUAGE feature, but found {complangfeat}'.format(complangfeat=repr(complangfeat))))
	
				# Maybe don't need this, overriden below?
				adjustedID = "component_" + compid
				if adjustedID == URI:

					#print("Found it:", compid)
					
					if compid in seenComps:
						continue
					else:
						seenComps.append(compid)

					
					compPrevTabCount = 0
					compTabCount = 0
					compURIbase = compid
				
					tabEmbeddings = { }

					# Do I even need this (and the above one?)
					compURIs = defaultdict(int)
					
					for compfeatval in compfeatvals:
					
						tabs = re.match('^\t+', compfeatval)
						if tabs != None:
							compTabCount = tabs[0].count('\t')
						else: compTabCount = 0
						compfeatval = compfeatval.lstrip()
						
						# Deals with a final line break issue, maybe can be handled better
						if compfeatval == "": continue
						else: feature, value = compfeatval.split('\t')
				
						URI = compURIbase + "_" + value				
						
						# special logic for digits since they break python-graph somehow
						if value.isdigit() or value == "∞":
							value = compURIbase + "-" + feature + "_" + value
							URI = value
						
						# Was using URI's to disambiguate repeating features (e.g., in components)
						# Will need to adapt...
						if compTabCount == compPrevTabCount:
							
							# I don't know when this if condition comes up
							# It isn't good for components
							#if (not desdag.has_node(value, URI)):
								# capture the new name to disambiguate repeated features
								
							print("==", previousCompType, value, feature)
							adjustedValue = desdag.add_node(value, URI)
							tabEmbeddings[compTabCount + 1] = adjustedValue
							desdag.add_edge((previousCompType, adjustedValue), feature)
				
						# Should only ever increment by one tab
						elif compTabCount > compPrevTabCount: 		
				
							compPrevTabCount = compTabCount
				
							#if (not desdag.has_node(value, URI)):
								# capture the new name to disambiguate repeated features
							adjustedValue = desdag.add_node(value, URI)
							tabEmbeddings[compTabCount + 1] = adjustedValue
							#print("ADJ", adjustedValue)

							previousCompType = tabEmbeddings[compTabCount]
							#print(">", previousCompType, value, feature)
							desdag.add_edge((previousCompType, adjustedValue), feature)

				
						elif compTabCount < compPrevTabCount: 		
							compPrevTabCount = compTabCount
				
							#if (not desdag.has_node(value, URI)):
								# capture the new name to disambiguate repeated features
							adjustedValue = desdag.add_node(value, URI)
							tabEmbeddings[compTabCount + 1] = adjustedValue
				
							try: previousCompType = tabEmbeddings[compTabCount - 1]
							except: previousCompType = topURI
							#print("<", previousCompType, value, feature)
							desdag.add_edge((previousCompType, adjustedValue), feature)
						
					# No need to go further, we only need the one component
					# I hope I got the embedding right
					break

## Also, some data is in RDF that needs dumped, like source, notes, transcription string, usw.
## May need to open up Protege to verify, or check book dump?
## I accidentally broke RDFtoTabbed. Is it worth fixing? Or, should I verify the desmemes?
	
	# proof of concept is now OK, but a lot of detailed work to be done
	# components are not yet done at all!!
	templateAVM = avm(id_, "desmeme")
	templateAVM.graph_toAVM(desdag)
	
	# to_ASCII prints to STDOUT
	templateAVM.to_ASCII()
	print()
	
	# expects a list of graphs; so construct a list of one element
	# maybe make a draw_graph function at some point?
	draw_graphs([desdag], graphfolder)


"""
with open(componentFileName) as componentFile:
	 components = componentFile.read().split('\n\n')

for component in components:
	
	# * unpacks the remainder to featvals
	[idfv, langfv, *featvals] = component.split('\n')
		
	[idfeat, id_] = idfv.split('\t')
	if idfeat != "IDENTIFIER":
		raise(ValueError('Expected leading IDENTIFIER feature, but found {idfeat}'.format(idfeat=repr(idfeat))))
		
	[langfeat, lang] = langfv.split('\t')
	if langfeat != "LANGUAGE":
		raise(ValueError('Expected leading IDENTIFIER feature, but found {idfeat}'.format(langfeat=repr(langfeat))))

	compdag = tdag(id_)

	topType = "component"
	previousType = topType
	prevtabCount = 0
	URI = "URI" # dummy, need to fix to fully utilize existing code effectively

	# add root
	compdag.add_node(topType, URI)

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

			# somehow component node isn't being added??? I do it on l.134.
			# the issue is that tdag has special logic for components. I need to figure out URIs, I think to make use of that!
			print(previousType, value, feature)
			if (not compdag.has_node(value, URI)): compdag.add_node(value, URI)
			compdag.add_edge((previousType, value), feature)


		# Should only ever increment by one tab
		if tabCount > prevtabCount: 		

			embeddings[tabCount + 1] = value
			prevtabCount = tabCount

			if (not compdag.has_node(value, URI)): compdag.add_node(value, URI)
			previousType = embeddings[tabCount]
			compdag.add_edge((previousType, value), feature)

		if tabCount < prevtabCount: 		
			embeddings[tabCount + 1] = value
			prevtabCount = tabCount

			if (not compdag.has_node(value, URI)): compdag.add_node(value, URI)

			try: previousType = embeddings[tabCount - 1]
			except: previousType = topType
			compdag.add_edge((previousType, value), feature)
			
	# proof of concept is now OK, but a lot of detailed work to be done
	# components are not yet done at all!!
	templateAVM = avm(id_, "component")
	templateAVM.graph_toAVM(compdag)
	
	# to_ASCII prints to STDOUT
	templateAVM.to_ASCII()
	print()
	
	# expects a list of graphs; so construct a list of one element
	# maybe make a draw_graph function at some point?
	#draw_graphs([desdag], graphfolder)
"""
