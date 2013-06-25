#!/sw/bin/python2.4


### TODO ####: PRINT OUT FORM FEATURES FOR COMPONENTS

# Changes for 2.6?
#from rdflib.Graph import Graph
#from rdflib.Namespace import Namespace
#from rdflib.Graph import QuotedGraph

from rdflib import Graph
from rdflib import Namespace
#from rdflib import QuotedGraph

from rdflib import URIRef, Literal, BNode, Namespace
from rdflib import RDF

import re

import pprint

store = Graph()

instanceNS = Namespace("http://purl.org/linguistics/jcgood/template#")
componentNS = Namespace("http://purl.org/linguistics/jcgood/component#")
store.load("/Volumes/Obang/MyDocuments/Linearity/template_ontology/template.rdf")


# Readable names of categories
readableTranslation = {
	'lexicoconstructionalConditioning' : 'lexico-constructional',
	'constructionalConditioning' : 'constructional',
	'consonantalConditioning' : 'consonantal',
	'partiallyFilled' : 'partial',

	}

# Get the templates
# RDFLib gives us a generator
templates = store.subjects(RDF.type, instanceNS['desmeme'])

prettyTemplates = {}

indentLevel = 0
for template in templates:
	
	templateName = template.split('#')[1]
	
	prettyTemplate = {}
	
	for type in store.objects(template, RDF.type):
		typeName = type.split('#')[1]
		prettyTemplate['type'] = typeName
	
	
	indentLevel = indentLevel + 1
	for p,o in store.predicate_objects(template):

			
		# Filter out a subset of interesting cases based on their URIs
		if p.count("http://purl.org/linguistics/jcgood/general#") > 0 or \
			p.count("http://purl.org/linguistics/jcgood/template#") > 0 or \
			p.count("http://purl.org/linguistics/jcgood/templates#") > 0:

			attributeName = p.split('#')[1]
			valueName = o.split('#')[1]
	
			prettyTemplate[attributeName] = valueName


		# Filter out a subset of interesting cases based on their URIs
		elif p.count("http://purl.org/linguistics/jcgood/specgeneral#") > 0 or \
			p.count("http://purl.org/linguistics/jcgood/spectemplate#") > 0:

			subtemplateName = p.split('#')[1]

			prettySubtemplate = {}
						
			indentLevel = indentLevel + 1
			for type in  store.objects(o, RDF.type):
				typeName = type.split('#')[1]
				prettySubtemplate['type'] = typeName
			
			for p,o in store.predicate_objects(o):
				
				if p.count("http://purl.org/linguistics/jcgood/general#") > 0 or \
					p.count("http://purl.org/linguistics/jcgood/template#") > 0 or \
					p.count("http://purl.org/linguistics/jcgood/templates#") > 0:
		
					attributeName = p.split('#')[1]
					
					try: valueName = o.split('#')[1]
					except: valueName = o
			
					prettySubtemplate[attributeName] = valueName
		


				# Filter out a subset of interesting cases based on their URIs
				elif p.count("http://purl.org/linguistics/jcgood/specgeneral#") > 0 or \
					p.count("http://purl.org/linguistics/jcgood/spectemplate#") > 0:
		
					attributeName = p.split('#')[1]
			
					indentLevel = indentLevel + 1
					for type in  store.objects(o, RDF.type):
						typeName = type.split('#')[1]
						
						if typeName == "component":
							component = o
							prettySubtemplate[attributeName] = str(component)

					indentLevel = indentLevel - 1
							
				
				
				prettyTemplate[subtemplateName] = prettySubtemplate
				
			indentLevel = indentLevel - 1
			
			
	indentLevel = 0
	
	prettyTemplates[templateName] = prettyTemplate
	
	pp = pprint.PrettyPrinter(indent=4)
	#pp.pprint(prettyTemplate)
	

	
# Get the components
# RDFLib gives us a generator
components = store.subjects(RDF.type, componentNS['component'])

prettyComponents = {}

indentLevel = 0
for component in components:
	
	#componentName = component.split('#')[1]
	componentName = str(component)
	
	prettyComponent = {}
		
	for type in store.objects(component, RDF.type):
		typeName = type.split('#')[1]
		prettyComponent['type'] = typeName
	
	
	indentLevel = indentLevel + 1
	for p,o in store.predicate_objects(component):

			
		# Filter out a subset of interesting cases based on their URIs
		if p.count("http://purl.org/linguistics/jcgood/general#") > 0 or \
			p.count("http://purl.org/linguistics/jcgood/component#") > 0 or \
			p.count("http://purl.org/linguistics/jcgood/components#") > 0:

			attributeName = p.split('#')[1]
			valueName = o.split('#')[1]
	
			prettyComponent[attributeName] = valueName


		# Filter out a subset of interesting cases based on their URIs
		elif p.count("http://purl.org/linguistics/jcgood/specgeneral#") > 0 or \
			p.count("http://purl.org/linguistics/jcgood/speccomponent#") > 0:

			subcomponentName = p.split('#')[1]

			prettySubcomponent = {}
						
			indentLevel = indentLevel + 1
			for type in  store.objects(o, RDF.type):
				typeName = type.split('#')[1]
				prettySubcomponent['type'] = typeName
			
			for p,o in store.predicate_objects(o):

				if p.count("http://purl.org/linguistics/jcgood/general#") > 0 or \
					p.count("http://purl.org/linguistics/jcgood/component#") > 0 or \
					p.count("http://purl.org/linguistics/jcgood/components#") > 0:
		
					attributeName = p.split('#')[1]
					
					try: valueName = o.split('#')[1]
					except: valueName = o

					prettySubcomponent[attributeName] = valueName
		


				# Filter out a subset of interesting cases based on their URIs
				elif p.count("http://purl.org/linguistics/jcgood/specgeneral#") > 0 or \
					p.count("http://purl.org/linguistics/jcgood/speccomponent#") > 0:

					subsubcomponentName = p.split('#')[1]

					prettySubsubcomponent = {}
		
					attributeName = p.split('#')[1]

					indentLevel = indentLevel + 1

					for type in  store.objects(o, RDF.type):
						typeName = type.split('#')[1]
						prettySubsubcomponent['type'] = str(typeName)						
								
					for p,o in store.predicate_objects(o):


		
						if p.count("http://purl.org/linguistics/jcgood/form#") > 0 or \
							p.count("http://purl.org/linguistics/jcgood/component#") > 0 or \
							p.count("http://purl.org/linguistics/jcgood/components#") > 0:
				
							attributeName = p.split('#')[1]
							
							try: valueName = o.split('#')[1]
							except: valueName = o
					
							prettySubsubcomponent[attributeName] = valueName

					indentLevel = indentLevel - 1
							
					prettySubcomponent[subsubcomponentName] = prettySubsubcomponent
				
				
				prettyComponent[subcomponentName] = prettySubcomponent
				
			indentLevel = indentLevel - 1
				
	indentLevel = 0
	prettyComponents[componentName] = prettyComponent
	pp = pprint.PrettyPrinter(indent=4)

#pp.pprint(prettyTemplates)
#pp.pprint(prettyComponents)



def prettyprintComponent(componentName, indentLevel, reference):

	# A hack to get numbers to print before AVMs
	# Sees if a component is referred to by a unique predicate more than once
	# Filters on some inconsequential predicates for this
	preds = {}
	pred_count = 0
	for s,p in store.subject_predicates(URIRef(componentName)):
		if preds.has_key(p):
			pass
		else:
			if p.rfind('FILLED') > -1:
				pass
			else:
				preds[p] = 1
				pred_count = pred_count + 1
	
	label = ""
	if pred_count > 1:
		label = "\\leavevmode\\llap{\\@" + str(reference) + "}"
	else: pass

	prettyComponent = label + "\\[\t" + "\\avmspan{\\emph{component}}" + "\\cr\n"
	
	indentLevel = indentLevel + 4
	
	component = prettyComponents[componentName]
	
	elasticity = component['ELASTICITY']
	elasticityType = elasticity['type']
	prettyComponent = prettyComponent + "\t"*indentLevel + "ELASTICITY\t&\t\\[\t" + "\\avmspan{\\emph{" + elasticityType + "}}" + "\\cr\n"
	
	if elasticityType == "inelastic":
		indentLevel = indentLevel + 4
		count = elasticity['COUNT']		
		prettyComponent = prettyComponent + "\t"*indentLevel + "COUNT\t&\t" + count + "\\cr\n"

	if elasticityType == "elastic":
		indentLevel = indentLevel + 4
		minimum = elasticity['MINIMUM']		
		maximum = elasticity['MAXIMUM']		
		prettyComponent = prettyComponent + "\t"*indentLevel + "MINIMUM\t&\t" + minimum + "\\cr\n"
		prettyComponent = prettyComponent + "\t"*indentLevel + "MAXIMUM\t&\t" + maximum + "\\cr\n"

	prettyComponent = prettyComponent + "\t"*indentLevel + "\\]\\cr\n"
	indentLevel = indentLevel - 4


	filledness = component['FILLEDNESS']
	fillednessType = filledness['type']

	if fillednessType == "filled":
		prettyComponent = prettyComponent + "\t"*indentLevel + "FILLEDNESS\t&\t" + "{\\emph{" + fillednessType + "}}" + "\\cr\n"

	if fillednessType == "null":
		prettyComponent = prettyComponent + "\t"*indentLevel + "FILLEDNESS\t&\t" + "{\\emph{" + fillednessType + "}}" + "\\cr\n"


	if fillednessType == "empty":
		
		prettyComponent = prettyComponent + "\t"*indentLevel + "FILLEDNESS\t&\t\\[\t" + "\\avmspan{\\emph{" + fillednessType + "}}" + "\\cr\n"
		
		indentLevel = indentLevel + 4
		coherence = filledness['COHERENCE']		
		# Coherence can be complex, but we only store the type for now
		coherenceType = coherence['type']		
		prettyComponent = prettyComponent + "\t"*indentLevel + "COHERENCE\t&\t" + "{\\emph{" + coherenceType + "}}" + "\\cr\n"

		indentLevel = indentLevel - 2
		prettyComponent = prettyComponent + "\t"*indentLevel + "\\]\\cr\n"


	if fillednessType == "partiallyFilled":
		
		fillednessPrettyName = readableTranslation[fillednessType]
		prettyComponent = prettyComponent + "\t"*indentLevel + "FILLEDNESS\t&\t\\[\t" + "\\avmspan{\\emph{" + fillednessPrettyName + "}}" + "\\cr\n"

		indentLevel = indentLevel + 4

		coherence = filledness['COHERENCE']		
		coherenceType = coherence['type']		
		prettyComponent = prettyComponent + "\t"*indentLevel + "UNFILLED COHERENCE\t&\t" + "{\\emph{" + coherenceType + "}}" + "\\cr\n"
		
		position = filledness['FILLER_POSITION']
		prettyComponent = prettyComponent + "\t"*indentLevel + "FILLER POSITION\t&\t" + position + "\n"

		prettyComponent = prettyComponent + "\t"*indentLevel + "\\]\\cr\n"



	stability = component['STABILITY']
	stabilityType = stability['type']
	
	if stabilityType == "stable":
		prettyComponent = prettyComponent + "\t"*indentLevel + "STABILITY\t&\t" + "{\\emph{" + stabilityType + "}}" + "\\cr\n"

	if stabilityType == "unstable":

		prettyComponent = prettyComponent + "\t"*indentLevel + "STABILITY\t&\t\\[\t" + "\\avmspan{\\emph{" + stabilityType + "}}" + "\\cr\n"
		
		indentLevel = indentLevel + 4
		position = stability['SUPPORT_POSITION']		
		prettyComponent = prettyComponent + "\t"*indentLevel + "SUPPORT POSITION\t&\t" + position + "\\cr\n"

		indentLevel = indentLevel - 2
		prettyComponent = prettyComponent + "\t"*indentLevel + "\\]\\cr\n"



	prettyComponent = prettyComponent + "\t"*indentLevel + "\\]\\cr\n"
	indentLevel = indentLevel - 4


	return prettyComponent


print "{"

templates = prettyTemplates.keys()

indentLevel = 1
for template in templates:

	componentCount = 1
	components = {}

	templateDescription = prettyTemplates[template]
	
	mainType = templateDescription['type']
	
	templateName = template.replace("_", " ")
	
	print "\\item {\\bf "+templateName + "}\n"
	
	print "\\begin{avm}"
	
	print "\\[\t" + "\\avmspan{\\emph{" + mainType + "}}" + "\\cr\n"
	
	stricture = templateDescription['STRICTURE']	
	strictureType = stricture['type']
	print "\t"*indentLevel + "STRICTURE\t&\t\\[\t"+ "\\avmspan{\\emph{" + strictureType + "}}\\cr"	
	if stricture: # Dummy to allow indentation

		indentLevel = indentLevel + 1
		count = stricture['COUNT']
		print "\t"*indentLevel + "COUNT\t&\t" + count + "\\cr"
	
		try:
			unit = stricture['CONSTITUENT']
			print "\t"*indentLevel + "CONSTITUENT\t&\t" + unit + "\\cr"
		
		except:
			relations = stricture['RELATIONS']
			print "\t"*indentLevel + "RELATIONS\t&\t" + "\\emph{" + relations + "}" + "\\cr"
	
		print "\t"*indentLevel + "\\]\\cr\n"
		
		indentLevel = indentLevel - 1
	
	foundation = templateDescription['FOUNDATION']	
	foundationType = foundation['type']
	print "\t"*indentLevel + "FOUNDATION\t&\t\\[\t"+ "\\avmspan{\\emph{" + foundationType + "}}" + "\\cr\n"
	if foundation: # Dummy to allow indentation

		indentLevel = indentLevel + 1
	
		hasKeystone = 0
		try:
			keystone = foundation['KEYSTONE']
			hasKeystone = 1
		except:
			pass
				
		if hasKeystone == 1:
		
			if components.has_key(keystone):
				componentReference = components[keystone]
				print "\t"*indentLevel + "KEYSTONE\t&\t" + "\\@" + str(componentReference) + "\\cr"
			
			else:
				components[keystone] = componentCount
				componentReference = components[keystone]
				print "\t"*indentLevel + "KEYSTONE\t&\t" + prettyprintComponent(keystone, indentLevel, componentCount)
				componentCount = componentCount + 1
					
	
		hasLV = 0
		try:
			leftVoussoir = foundation['LEFT_VOUSSOIR']
			hasLV = 1
		except:
			pass

		if hasLV == 1:
			leftVoussoir = foundation['LEFT_VOUSSOIR']
		
			if components.has_key(leftVoussoir):
				componentReference = components[leftVoussoir]
				print "\t"*indentLevel + "LEFT VOUSSOIR\t&\t" +  "\\@" + str(componentReference) + "\\cr\n"
		
			else:
				components[leftVoussoir] = componentCount
				print "\t"*indentLevel + "LEFT VOUSSOIR\t&\t" + prettyprintComponent(leftVoussoir, indentLevel, componentCount)
				componentCount = componentCount + 1
			

		hasLS = 0
		try:
			leftSupport = foundation['LEFT_SUPPORT']
			hasLS = 1
		except:
			pass

		if hasLS == 1:
			leftSupport = foundation['LEFT_SUPPORT']
		
			if components.has_key(leftSupport):
				componentReference = components[leftSupport]
				print "\t"*indentLevel + "LEFT SUPPORT\t&\t" +  "\\@" + str(componentReference) + "\\cr\n"
		
			else:
				components[leftSupport] = componentCount
				componentReference = components[leftSupport]
				print "\t"*indentLevel + "LEFT SUPPORT\t&\t" + prettyprintComponent(leftSupport, indentLevel, componentCount)
				componentCount = componentCount + 1



		hasRV = 0
		try:
			rightVoussoir = foundation['RIGHT_VOUSSOIR']
			hasRV = 1
		except:
			pass

		if hasRV == 1:
			rightVoussoir = foundation['RIGHT_VOUSSOIR']
		
			if components.has_key(rightVoussoir):
				componentReference = components[rightVoussoir]
				print "\t"*indentLevel + "RIGHT VOUSSOIR\t&\t" +  "\\@" + str(componentReference, ) + "\\cr\n"
		
			else:
				components[rightVoussoir] = componentCount
				componentReference = components[rightVoussoir]
				print "\t"*indentLevel + "RIGHT VOUSSOIR\t&\t" + prettyprintComponent(rightVoussoir, indentLevel, componentCount)
				componentCount = componentCount + 1		
			
		# Odd... why am I not using has_key (and above as well) think about this in refactor
		hasRS = 0
		try:
			rightSupport = foundation['RIGHT_SUPPORT']
			hasRS = 1
		except:
			pass

		if hasRS == 1:
			rightSupport = foundation['RIGHT_SUPPORT']
		
			if components.has_key(rightSupport):
				componentReference = components[rightSupport]
				print "\t"*indentLevel + "RIGHT SUPPORT\t&\t" +  "\\@" + str(componentReference) + "\\cr\n"
		
			else:
				components[rightSupport] = componentCount
				componentReference = components[rightSupport]
				print "\t"*indentLevel + "RIGHT SUPPORT\t&\t" + prettyprintComponent(rightSupport, indentLevel, componentCount)
				componentCount = componentCount + 1	




		# ONLY WORKS IF RK < 2. FOR NOW THIS IS THE CASE
		hasRK = 0
		try:
			restKomp = foundation['RESTKOMPONENTEN']
			hasRK = 1
		except:
			pass

		if hasRK == 1:
			restKomp = foundation['RESTKOMPONENTEN']
		
			if components.has_key(restKomp):
				componentReference = components[restKomp]
				print "\t"*indentLevel + "RESTKOMPONENTEN\t&\t" +  "\\@" + str(componentReference) + "\\cr\n"
		
			else:
				components[restKomp] = componentCount
				componentReference = components[restKomp]
				print "\t"*indentLevel + "RESTKOMPONENTEN\t&\t" + prettyprintComponent(restKomp, indentLevel, componentCount)
				componentCount = componentCount + 1	



		print "\t"*indentLevel + "\\]\\cr\n"
		indentLevel = indentLevel - 1



	conditioning = templateDescription['CONDITIONING']	
	conditioningType = conditioning['type']
	conditioningLabel = readableTranslation[conditioningType]
	print "\t"*indentLevel + "CONDITIONING\t&\t"+ "\\emph{" + conditioningLabel + "}" + "\\cr\n"

	violability = templateDescription['VIOLABILITY']	
	print "\t"*indentLevel + "VIOLABILITY\t&\t"+ "\\emph{" + violability + "}" + "\\cr\n"

	#stratification = templateDescription['STRATIFICATION']	
	#print "\t"*indentLevel + "STRATIFICATION\t&\t"+ "\\emph{" + stratification + "}" + "\\cr\n"


	
	print "\\]\n\n"
	
	print "\\end{avm}\n\n\n"

	
	indentLevel = 1
	
print "}"