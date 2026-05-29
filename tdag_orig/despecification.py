from rdflib import URIRef, Literal, BNode, Namespace, RDF, RDFS
from rdflib import BNode as rdfNode

from . tdag_orig import tdag

# This takes in a regular template and outputs a despecified one, removing
# RDF bits not important for the comparative analysis.
# It's recursive and passes back the original nodes and a despecified/generic one.
def process_template(mother,genericMother,rdfGraph,tdag):
		
	for predicate, daughter in rdfGraph.predicate_objects(mother):

		# Conflate (if applicable) the daughters of the mother if possible and create pretty names.
		despecifiedD = conflate(daughter,rdfGraph)
		prettyDName = prettyName(despecifiedD)
		prettyPredName = prettyName(predicate)
		
		if prettyPredName == "CONSTITUENT":
			#print "Skipping CONSTITUENT node to avoid circularity!"
			#continue
			pass

		# Here is a hack to deal with the fact that, at least for Tiene, associates can criss-cross
		# This results in infinite recursion. So, we need special treatment
		if is_associate(predicate):
			
			# If I'm already in the graph, just add my edge if it's not already there.
			if daughter in tdag.components:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
				if tdag.has_edge((genericMother, prettyDName), prettyPredName):
					pass
				else:
					# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
					tdag.add_edge((genericMother, prettyDName), label=prettyPredName)

			# Otherwise, add me per usual	
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
				process_template(daughter, prettyDName, rdfGraph, tdag)
		
		# Need to skip source information, probably better solution out there
		elif is_metadata(predicate):
			# Will decide later if it is worth implementing this. I kind of doubt it. May do it by hand.
			print("UU", prettyDName,daughter,mother,predicate)
			#process_template(daughter, prettyDName, rdfGraph, tdag)
			pass


		# Here we need some special logic to make sure that (components especially)
		# Have their potentially shared nodes "split" up so that each component points
		# to its own nodes rather than shared nodes. This is only a problem for
		# generic and/or conflatable nodes which may not be unique.
		elif is_generic(predicate,tdag) or conflatable(daughter,rdfGraph):

			# I don't understand why but, somehow, the invocation of this boolean
			# detects cases of duplicatable nodes not yet properly handled. This seems
			# to be an accident, but a useful one. So, I am keeping it.
			if tdag.has_node(prettyDName,daughter):
				prettyDName = tdag.has_node(prettyDName,daughter)
				#print "Warning ", daughter, "may be a case of a duplicatable node not yet properly handled. Examine the template using it and the class function in tdag and add a case for this if graph does not properly duplicate nodes. A known raising of this error which is not a problem occurs when a component with an Associate is also a filler for a lexicoconstructional template."
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
			
			# The method used here is from the original pygraph, and does not involve labeled edges
			if tdag.has_edge((genericMother, prettyDName), prettyPredName):
				pass
			else:
				# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
			
			# Now send the rest of the template, after conflation of this layer, back through the function.
			process_template(daughter, prettyDName, rdfGraph, tdag)
			
		# Not a generic/conflatable node. So, we don't add anything but, instead, just cycle through.
		else: process_template(daughter, genericMother, rdfGraph, tdag)
	
	# We've been passing the same tdag around adding nodes and edges.
	# It should be all built up by now. So, we return it.
	return tdag


# A version which keeps the full information (WiP)
def process_template_full(mother,genericMother,rdfGraph,tdag):
		
	for predicate, daughter in rdfGraph.predicate_objects(mother):

		# Conflate (if applicable) the daughters of the mother if possible and create pretty names.
		despecifiedD = conflate(daughter,rdfGraph)
		prettyDName = prettyName(despecifiedD)
		prettyPredName = prettyName(predicate)
		
		#if prettyPredName == "CONSTITUENT":
			#print "Skipping CONSTITUENT node to avoid circularity!"
			#continue
		#	pass

		# Here is a hack to deal with the fact that, at least for Tiene, associates can criss-cross
		# This results in infinite recursion. So, we need special treatment
		if is_associate(predicate):
			
			# If I'm already in the graph, just add my edge if it's not already there.
			if daughter in tdag.components:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
				if tdag.has_edge((genericMother, prettyDName), prettyPredName):
					pass
				else:
					# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
					tdag.add_edge((genericMother, prettyDName), label=prettyPredName)

			# Otherwise, add me per usual	
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
				process_template_full(daughter, prettyDName, rdfGraph, tdag)
		
		# Need to skip source information, probably better solution out there
		elif is_metadata(predicate):
			# Will decide later if it is worth implementing this. I kind of doubt it. May do it by hand.
			#print("MD", prettyDName,daughter,mother,predicate)
			prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate) # to self: the reassignment of prettyDName is because this function tracks repeatable nodes and unique IDs
			prettyPredName = "NT:"+prettyPredName
			tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
			process_template_full(daughter, prettyDName, rdfGraph, tdag)
			pass

			#Need to get data on
			#terms:bibliographicCitation
			#notes:CONDITIONS
			#function:FUNCTION
			#function:CLASS
			#function:FILLER_CLASS
			#function:CLASSES
			#speccomponent:FORM
			#form:canonicalLineate
			#form:LIAISON
			#form:transcription
			#specform:TRANSCRIPTION_STRING

		# Here we need some special logic to make sure that (components especially)
		# Have their potentially shared nodes "split" up so that each component points
		# to its own nodes rather than shared nodes. This is only a problem for
		# generic and/or conflatable nodes which may not be unique.
		elif is_generic(predicate,tdag) or conflatable(daughter,rdfGraph):

			# I don't understand why but, somehow, the invocation of this boolean
			# detects cases of duplicatable nodes not yet properly handled. This seems
			# to be an accident, but a useful one. So, I am keeping it.
			if tdag.has_node(prettyDName,daughter):
				prettyDName = tdag.has_node(prettyDName,daughter)
				#print "Warning ", daughter, "may be a case of a duplicatable node not yet properly handled. Examine the template using it and the class function in tdag and add a case for this if graph does not properly duplicate nodes. A known raising of this error which is not a problem occurs when a component with an Associate is also a filler for a lexicoconstructional template."
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
			
			# The method used here is from the original pygraph, and does not involve labeled edges
			if tdag.has_edge((genericMother, prettyDName), prettyPredName):
				pass
			else:
				# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
			
			# Now send the rest of the template, after conflation of this layer, back through the function.
			process_template_full(daughter, prettyDName, rdfGraph, tdag)
			
		# Not a generic/conflatable node. So, we don't add anything but, instead, just cycle through.
		else: process_template_full(daughter, genericMother, rdfGraph, tdag)
	
	# We've been passing the same tdag around adding nodes and edges.
	# It should be all built up by now. So, we return it.
	return tdag
	


# This takes in a regular template and outputs a despecified one, removing
# RDF bits not important for the comparative analysis.
# It's recursive and passes back the original nodes and a despecified/generic one.
def process_template_noComp(mother,genericMother,rdfGraph,tdag):
		
	for predicate, daughter in rdfGraph.predicate_objects(mother):

		# Conflate (if applicable) the daughters of the mother if possible and create pretty names.
		despecifiedD = conflate(daughter,rdfGraph)
		prettyDName = prettyName(despecifiedD)
		prettyPredName = prettyName(predicate)

		if despecifiedD.encode('utf-8') == "http://purl.org/linguistics/jcgood/component#component":
			pass
			
		else:

			# Need to skip source information, probably better solution out there
			if is_metadata(predicate):
				pass


			# Here we need some special logic to make sure that (components especially)
			# Have their potentially shared nodes "split" up so that each component points
			# to its own nodes rather than shared nodes. This is only a problem for
			# generic and/or conflatable nodes which may not be unique.
			elif is_generic(predicate,tdag) or conflatable(daughter,rdfGraph):

				# I don't understand why but, somehow, the invocation of this boolean
				# detects cases of duplicatable nodes not yet properly handled. This seems
				# to be an accident, but a useful one. So, I am keeping it.
				if tdag.has_node(prettyDName,daughter):
					prettyDName = tdag.has_node(prettyDName,daughter)
					print("Warning ", prettyDName, daughter, mother, "may be a case of a duplicatable node not yet properly handled. Examine the template using it and the class function in tdag and add a case for this if graph does not properly duplicate nodes.")
				else:
					prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
			
				# The method used here is from the original pygraph, and does not involve labeled edges
				if tdag.has_edge((genericMother, prettyDName), prettyPredName):
					pass
				else:
					# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
					tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
			
				# Now send the rest of the template, after conflation of this layer, back through the function.
				process_template_noComp(daughter, prettyDName, rdfGraph, tdag)
			
			# Not a generic/conflatable node. So, we don't add anything but, instead, just cycle through unless it's a component
			else: process_template_noComp(daughter, genericMother, rdfGraph, tdag)
	
		
	# We've been passing the same tdag around adding nodes and edges.
	# It should be all built up by now. So, we return it.
	return tdag


# For new tabbed template structure XXX (will work this out in a script first)
def process_tabbed(mother,genericMother,rdfGraph,tdag):
		
	for predicate, daughter in rdfGraph.predicate_objects(mother):

		# Conflate (if applicable) the daughters of the mother if possible and create pretty names.
		despecifiedD = conflate(daughter,rdfGraph)
		prettyDName = prettyName(despecifiedD)
		prettyPredName = prettyName(predicate)
		
		if prettyPredName == "CONSTITUENT":
			#print "Skipping CONSTITUENT node to avoid circularity!"
			#continue
			pass

		# Here is a hack to deal with the fact that, at least for Tiene, associates can criss-cross
		# This results in infinite recursion. So, we need special treatment
		if is_associate(predicate):
			
			# If I'm already in the graph, just add my edge if it's not already there.
			if daughter in tdag.components:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
				if tdag.has_edge((genericMother, prettyDName), prettyPredName):
					pass
				else:
					# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
					tdag.add_edge((genericMother, prettyDName), label=prettyPredName)

			# Otherwise, add me per usual	
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
				process_template(daughter, prettyDName, rdfGraph, tdag)
		
		# Need to skip source information, probably better solution out there
		elif is_metadata(predicate):
			# Will decide later if it is worth implementing this. I kind of doubt it. May do it by hand.
			#print(prettyDName,daughter,mother,predicate)
			#process_template(daughter, prettyDName, rdfGraph, tdag)
			pass


		# Here we need some special logic to make sure that (components especially)
		# Have their potentially shared nodes "split" up so that each component points
		# to its own nodes rather than shared nodes. This is only a problem for
		# generic and/or conflatable nodes which may not be unique.
		elif is_generic(predicate,tdag) or conflatable(daughter,rdfGraph):

			# I don't understand why but, somehow, the invocation of this boolean
			# detects cases of duplicatable nodes not yet properly handled. This seems
			# to be an accident, but a useful one. So, I am keeping it.
			if tdag.has_node(prettyDName,daughter):
				prettyDName = tdag.has_node(prettyDName,daughter)
				#print "Warning ", daughter, "may be a case of a duplicatable node not yet properly handled. Examine the template using it and the class function in tdag and add a case for this if graph does not properly duplicate nodes. A known raising of this error which is not a problem occurs when a component with an Associate is also a filler for a lexicoconstructional template."
			else:
				prettyDName = tdag.add_node(prettyDName,daughter,mother,predicate)
			
			# The method used here is from the original pygraph, and does not involve labeled edges
			if tdag.has_edge((genericMother, prettyDName), prettyPredName):
				pass
			else:
				# Now we are using the special tdag methods to add an edge with a label for multiple arcs from/to same nodes
				tdag.add_edge((genericMother, prettyDName), label=prettyPredName)
			
			# Now send the rest of the template, after conflation of this layer, back through the function.
			process_template(daughter, prettyDName, rdfGraph, tdag)
			
		# Not a generic/conflatable node. So, we don't add anything but, instead, just cycle through.
		else: process_template(daughter, genericMother, rdfGraph, tdag)
	
	# We've been passing the same tdag around adding nodes and edges.
	# It should be all built up by now. So, we return it.
	return tdag
	

# This function conflates/collapses an RDF node with its type if it is a typed node.
# For instance, a specific FOUNDATION may become a type rather than a foundation ID.
# Hacking this to get some metadata nodes out as part of the data format conversion to tabbed 1/29/2025
def conflate(rdfNode,rdfGraph):
	type = rdfGraph.value(subject=rdfNode, predicate=RDF.type)
	if type == None:
		return rdfNode
	elif type.endswith("source"): #Todo: Probably delete this condition since I'm handling this differently
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


			#Need to get data on
			#terms:bibliographicCitation : Not parsing easily, do by hand since just a few examples
			#notes:CONDITIONS
			#function:FUNCTION
			#function:CLASS
			#function:FILLER_CLASS
			#function:CLASSES
			#speccomponent:FORM
			#form:canonicalLineate
			#form:LIAISON
			#form:transcription
			#specform:TRANSCRIPTION_STRING

# To do / ToDo: Now have more predicates because I got the process_templates_full recursion working
# So, start from there maybe regenerating untitled output.
# Check Tabbed output and adjust
# Maybe do some last bits by hand? It might be faster.
# We cannot draw the graphs from process_templates_full, compare with process_templates for that

# I want to add prefix like "NT:" (for non typological) to all triples that aren't
# typological comparison. I'm doing that with "MD" for now, but I don't know how to find the
# identifier triple and the language triple yet, and I need to still add in the above URLs

def is_metadata(rdfPred):

	# Not very general yet
	if (
		rdfPred == URIRef("http://purl.org/linguistics/jcgood/notes#HAS_SOURCE") or
		rdfPred == URIRef("http://purl.org/linguistics/jcgood/notes#CONDITIONS") or
	   	rdfPred == URIRef("http://purl.org/dc/terms#bibliographicCitation") or
	    rdfPred == URIRef("http://purl.org/linguistics/jcgood/notes#")
	   	): return True
	return False

def is_associate(rdfPred):

	# Not very general yet
	if rdfPred == URIRef("http://purl.org/linguistics/jcgood/speccomponent#ASSOCIATE"):
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


# Runs through a list of templates, to create a list of despecified templates with more info than regular one
# For RDF export to new data system
def process_templates_full(templates, rdfTemplates):

	gTemplates = [ ]

	for template in templates:

		tname = prettyName(template)
		templatesDAG = tdag(tname)

		# Beginning of template is special case--then we can process them by tree
		genericT = conflate(template,rdfTemplates)
		prettyT = prettyName(genericT)
		templatesDAG.add_node(prettyT,template)
	
		despecifiedTemplate = process_template_full(template,prettyT,rdfTemplates,templatesDAG)

		gTemplates.append(despecifiedTemplate)

	return gTemplates
	

# Runs through a list of templates, to create a list of despecified templates without components
def process_templates_noComp(templates, rdfTemplates):

	gTemplates = [ ]

	for template in templates:

		tname = prettyName(template)
		templatesDAG = tdag(tname)

		# Beginning of template is special case--then we can process them by tree
		genericT = conflate(template,rdfTemplates)
		prettyT = prettyName(genericT)
		templatesDAG.add_node(prettyT,template)
	
		despecifiedTemplate = process_template_noComp(template,prettyT,rdfTemplates,templatesDAG)

		gTemplates.append(despecifiedTemplate)

	return gTemplates