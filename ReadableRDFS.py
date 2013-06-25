#!/usr/bin/python2.7

from rdflib import Graph as rdfGraph
from rdflib import URIRef, Literal, BNode, Namespace, RDF, RDFS
from rdflib import BNode as rdfNode


rdfsTemplates = rdfGraph()
rdfsTemplates.load("/Volumes/Obang/MyDocuments/Linearity/template_ontology/template.rdfs")

# Only classes in my namespaces should be paid attention to.
myPfxs = ["http://purl.org/linguistics/jcgood/template#",
	"http://purl.org/linguistics/gold#",
	"http://purl.org/linguistics/jcgood/component#",
	"http://purl.org/linguistics/jcgood/form#",
	"http://purl.org/linguistics/jcgood/general#",
	"http://purl.org/linguistics/jcgood/function#",
	]


# For some cases with properties, the Protege properties are more informative,
# specifying when a range is, for instance, a class or an integer.
protege = Namespace("http://protege.stanford.edu/system#")

outfile = open('/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/TemplateOntology.tex', 'w')

#=========Begin Functions============#

# Get readable labels from URIs; different conditions for Classes and Properties
def getClassLabel(URI):
	labelPosition = URI.find("#") + 1
	prettyName = URI[labelPosition:]
	# Add a gold prefix to GOLD URIs
	if URI.find("http://purl.org/linguistics/gold#") > -1:
		prettyName = "gold:"+prettyName	
	return prettyName

def getPropertyLabel(URI):
	labelPosition = URI.find("#") + 1
	prettyName = URI[labelPosition:]
	prettyName = prettyName.lower()
	prettyName = prettyName.replace("_", " ")
	prettyName = prettyName.replace(" name", "\\name")
	return prettyName


# Called recursively, gets subclasses of classes, and their properties, wraps LaTeX code around
def processClass(classURI,embedding=0):

	print >> outfile, "\t"*embedding+"\item \\emph{"+getClassLabel(classURI)+"}\n"
	
	# Get properties
	RDFSpropertiesURIs = rdfsTemplates.subjects(RDFS['domain'], classURI)
	
	# Need to know if there are any properties in the first place
	RDFSpropertiesURIsForCounting = rdfsTemplates.subjects(RDFS['domain'], classURI)
	propertyCount = sum(1 for _ in RDFSpropertiesURIsForCounting)	

	# Build up property list and print it out if there are any; for properties we also want to find out their range
	if propertyCount > 0:

		properties = {}
		for propertyURI in RDFSpropertiesURIs:
			label = getPropertyLabel(propertyURI)
			properties[label] = propertyURI
		
		print >> outfile,  "\t"+"\t"*embedding+"\\begin{proplist}\n"		
		
		for RDFSpropertyLabel in sorted(properties.iterkeys()):

			RDFSpropertyURI = properties[RDFSpropertyLabel]
			propertyRangeClass = rdfsTemplates.value(RDFSpropertyURI, RDFS['range'], None)
			propertyRangeType = rdfsTemplates.value(RDFSpropertyURI, protege['range'], None)
				
			# There is some hacky mapping here for readability
			
			# The default range is an instance
			if propertyRangeType == None:
				propertyRangeType = "instance of"
			
			# The protege _name property is a special case here
			if RDFSpropertyURI == URIRef('http://protege.stanford.edu/system#_name'):
				propertyRangeClass = "name"
				propertyRangeType = "string representation of"
				
			# If the value is an integer, then don't give class specification
			if propertyRangeType == Literal('integer'):
				propertyRangeClass = ""
				propertyRangeType = "\\emph{integer}"
							
			# If the range is a class, not an instance, get the allowed classes using the protege property
			if propertyRangeType == Literal('cls'):
				propertyRangeType = "" # Just don't print anything in this case
				propertyRangeClass = rdfsTemplates.value(RDFSpropertyURI, protege['allowedParents'], None)

			# If the range is a string literal for transcription change to string
			if propertyRangeClass == URIRef('http://www.w3.org/2000/01/rdf-schema#Literal'):
				propertyRangeClass = "transcription"
				propertyRangeType = "string representation of"

				
			print >> outfile,  "\t"+"\t"*embedding+"\item \\textsc{"+getPropertyLabel(RDFSpropertyURI)+"} $\\rightarrow$", propertyRangeType, "\\emph{"+getClassLabel(propertyRangeClass)+"}"+"\n"

		print >> outfile,  "\t"+"\t"*embedding+"\\end{proplist}\n"

	embedding += 1	

	
	# Get subclasses
	subClassURIs = rdfsTemplates.subjects(RDFS['subClassOf'], classURI)

	# Need to know if there are any properties in the first place
	subClassURIsForCounting = rdfsTemplates.subjects(RDFS['subClassOf'], classURI) # Make another copy to determine generator size to set list formatting conditions
	subClassCount = sum(1 for _ in subClassURIsForCounting)

	# Build up subclass list and print it out if there are any
	subClasses = {}
	for subClassURI in subClassURIs:
		label = getClassLabel(subClassURI)
		subClasses[label] = subClassURI		
	if subClassCount > 0:
		print >> outfile,  "\t"*embedding+"\\begin{classlist}\n"
		for subClassLabel in sorted(subClasses.iterkeys()):
			subClassURI = subClasses[subClassLabel]
			# Here be recursion
			processClass(subClassURI,embedding)
		print >> outfile,  "\t"*embedding+"\\end{classlist}\n"
		
#=========End Functions============#



# Get template IDs from RDF
classGenerator = rdfsTemplates.subjects(RDFS['subClassOf'], RDFS['Resource'])

# I can't use the singular "class" since it's a reserved word in python
classes = {}
for classURI in classGenerator:
	label = getClassLabel(classURI)
	classes[label] = classURI

# The name type is a special case for sorting and other things
print >> outfile,  "\\def\\name{name}\n"
print >> outfile,  "\\begin{ontologytop}\n"
for classLabel in sorted(classes.iterkeys()):
	classURI = classes[classLabel]
	processClass(classURI)
print >> outfile,  "\\end{ontologytop}"


