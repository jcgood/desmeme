#!/usr/bin/python2.7

from rdflib import Graph as rdfGraph
from rdflib import URIRef, Literal, BNode, Namespace, RDF, RDFS
from rdflib import BNode as rdfNode


rdfsTemplates = rdfGraph()
rdfsTemplates.load("./template.rdfs")

# Only classes in my namespaces should be paid attention to.
# BUG: I DON'T ACTUALLY USE THIS NOW...I probably should
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
propfile = open('/Volumes/Obang/MyDocuments/Linearity/TemplatesBook/TemplateProps.tex', 'w')


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


	# Keeps us from printing out the bibliographic class
	if classURI == URIRef("http://purl.org/linguistics/jcgood/notes#source"):
		return()

	print >> outfile, "\t"*embedding+"\item \\emph{"+getClassLabel(classURI)+"}"
	
	# Get documentation, if it exists, and print it
	RDFSdocumentation = rdfsTemplates.value(subject=classURI,predicate=RDFS['comment'])
	if RDFSdocumentation:
		print >> outfile, "\t"*embedding+"\\hspace{1em}\\parbox[t]{\\linegoal}{\\footnotesize "+RDFSdocumentation+"}"
	
	print >> outfile, "\n"
	
	
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
				propertyRangeType = "{integer}"
							
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


# Called recursively, gets subclasses of classes, and their properties, wraps LaTeX code around
def processProp(propURI,embedding=0):

	print >> propfile, "\t"*embedding+"\item \\textsc{"+getPropertyLabel(propURI)+"}"
	
	# Get documentation, if it exists, and print it
	RDFSdocumentation = rdfsTemplates.value(subject=propURI,predicate=RDFS['comment'])
	if RDFSdocumentation:
		print >> propfile, "\t"*embedding+"\\hspace{1em}\\parbox[t]{\\linegoal}{\\footnotesize "+RDFSdocumentation+"}"
	
	print >> propfile, "\n"
		
#=========End Functions============#




# I can't use the singular "class" since it's a reserved word in python

# First do the various types of the typology
classGenerator = rdfsTemplates.subjects(RDFS['subClassOf'], RDFS['Resource'])
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


slotGenerator = rdfsTemplates.subjects(RDF['type'], RDF['Property'])
props = {}
for propURI in slotGenerator:
	label = getPropertyLabel(propURI)
	props[label] = propURI

# The name type is a special case for sorting and other things
print >> propfile,  "\\def\\name{name {\\rm \hspace{1em}\\parbox[t]{\\linegoal}{\\footnotesize A string representation of a the name of a type used for purposes of reference.}}}\n" # Name is a special case since it's a built-in protege property that can't be altered in protege
print >> propfile, "\\begin{proplist}\n"
for propLabel in sorted(props.iterkeys()):
 	if propLabel == "bibliographiccitation": # Hack to not print out a bib feature
 		continue
 	propURI = props[propLabel]
 	processProp(propURI)
print >> propfile,  "\\end{proplist}"


# Now do all the different features of the typology