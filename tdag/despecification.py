from rdflib import URIRef, Literal, BNode, Namespace, RDF, RDFS
from rdflib import BNode as rdfNode

from tdag import tdag

# This takes in a regular template and outputs a despecified one, removing
# RDF bits not important for the comparative analysis.
# It's recursive and passes back the original nodes and a despecified/generic one.
def process_template(mother,genericMother,rdfGraph,tdag):
	
	print "mother", mother, genericMother
	
	for predicate, daughter in rdfGraph.predicate_objects(mother):

		# Conflate (if applicable) the daughters of the mother if possible and create pretty names.
		despecifiedD = conflate(daughter,rdfGraph)
		prettyDName = prettyName(despecifiedD)
		prettyPredName = prettyName(predicate)

		print mother, predicate, daughter

		# Here we need some special logic to make sure that (components especially)
		# Have their potentially shared nodes "split" up so that each component points
		# to its own nodes rather than shared nodes. This is only a problem for
		# generic and/or conflatable nodes which may not be unique.
		if is_generic(predicate,tdag) or conflatable(daughter,rdfGraph):

			# I don't understand why but, somehow, the invocation of this boolean
			# detects cases of duplicatable nodes not yet properly handled. This seems
			# to be an accident, but a useful one. So, I am keeping it.
			if tdag.has_node(prettyDName,daughter):
				prettyDName = tdag.has_node(prettyDName,daughter)
				print "Warning ", prettyDName, daughter, mother, "may be a case of a duplicatable node not yet properly handled. Examine the template using it and the class function in tdag and add a case for this if graph does not properly duplicate nodes."
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
			
			# The method used here is from the original pygraph, and does not involve labeled edges
			
			#print genericMother, prettyDName,prettyPredName
			
			if tdag.has_edge((genericMother, prettyDName), prettyPredName):
				pass
			else:
				# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
				#print "added above!"
			
			# Now send the rest of the template, after conflation of this layer, back through the function.
			process_template(daughter, prettyDName, rdfGraph, tdag)
			print "Recursion:", prettyDName
			
		# Not a generic/conflatable node. So, we don't add anything but, instead, just cycle through.
		else: process_template(daughter, genericMother, rdfGraph, tdag)
	
	# We've been passing the same tdag around adding nodes and edges.
	# It should be all built up by now. So, we return it.
	return tdag


# This function conflates/collapses an RDF node with its type if it is a typed node.
# For instance, a specific FOUNDATION may become a type rather than a foundation ID.
def conflate(rdfNode,rdfGraph):
	type = rdfGraph.value(subject=rdfNode, predicate=RDF.type)
	if type == None:
		return rdfNode
	else: return type
	

# This boolean says if a given node is conflatable with a special cade for transcriptions.
# Transcriptions are conflatable but should not be conflated.
def conflatable(rdfNode,rdfGraph):

	type = rdfGraph.value(subject=rdfNode, predicate=RDF.type)

	# Here be a hack for transcriptions
	if str(type) == "http://purl.org/linguistics/jcgood/form#transcription":
		return False

	elif type:
		return True

	else: return False


def is_generic(rdfPred,tdag):

	for genPfx in tdag.genericPredPfxs:
		if rdfPred.count(genPfx) > 0:
			return True
	return False
	

# Parses a URI of an instance to find a "pretty name", stripping off lots of prefixal material
def prettyName(rdfElement):
	labelPosition = rdfElement.find("#") + 1
	prettyName = rdfElement[labelPosition:]
	return prettyName
	

# Runs through a list of templates, to create a list of despecified templates
def process_templates(templates, rdfTemplates):

	gTemplates = [ ]

	for template in templates:

		tname = prettyName(template)
		templatesDAG = tdag(tname)

		# Beginning of template is special case--then we can process them by tree
		genericT = conflate(template,rdfTemplates)
		prettyT = prettyName(genericT)
		templatesDAG.add_node(prettyT,template)
	
		despecifiedTemplate = process_template(template,prettyT,rdfTemplates,templatesDAG)

		gTemplates.append(despecifiedTemplate)

	return gTemplates