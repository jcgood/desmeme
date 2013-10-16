from tdag import tdag

# Possible improvement: Make subclass of "topAVM" adding features (e.g., totaltags, tags) just for that class.
class avm ( ):

	def __init__(self, name, type):
		"""
		Initialize an AVM.
		"""
		
		self.name = name

		# These are typed AVMs, after all.
		
		# Hackish fix: I added HTML <i> tags to values to help with the graph-based output.
		# It was easiest to do this at the graph-construction stage. For AVMs, I need to remove them.
		type = type.replace("<<i>", "")
		type = type.replace("</i>>", "")
		self.type = type

		#A list for feature-value pairs
		self.featvals = [ ]
	
		# For re-entrancy, a tag say this is a re-entered AVM and one saying
		# If it is the "primary" one--i.e., to be expressed in the LaTeX form.
		# These get re-set as appropriate. We also store a counter for the numeric tag for re-entrancy.
		self.reentered = False
		self.primary = False
		self.tag = 0
		
		# top-level AVMs will also keep track of how many tags they have inside of them and what the tags are for a given AVM.
		self.totaltags = 0
		self.tags = { }
	
	
	def addFV(self, featval):
		"""
		Add a typed feature-values pair
		"""
				
		feat = featval.feature
		storedFeatvals = self.featvals
		
		
		# Avoid duplication due to re-entrancy except for restkomponenten and filledcomponents (code a bit hackish and non-general here)
		hasFeature = False

		if feat == 'RESTKOMPONENT':
				self.featvals.append(featval)
				
		elif feat == 'FILLED_COMPONENT':
				self.featvals.append(featval)
		
		else:
			for storedFeatval in storedFeatvals:
				storedFeat = storedFeatval.feature			
				if feat == storedFeat:
					hasFeature = True
		
			if hasFeature == True:
				pass
			else:
				self.featvals.append(featval)


	# Will need recursive
	def graph_toAVM(self, tgraph, root="desmeme"):
	
		pygraph = tgraph.core
		nodes = pygraph.nodes()
		edges = pygraph.edges()
				
		neighbors = pygraph.neighbors(root)
		
		for neighbor in neighbors:

			# We need to do something special for the case where a pair of nodes is
			# associated with two distinct edges. It would be nice to find a general
			# solution, but since, for now, this only happens for foundations, I'm going with
			# a specific one
			# TO CONSIDER: Can I just replace the old "else" code with this code? Is there a reason to believe it won't generalize?
			# If I did above, I'd have to alter getfoundation() too...
			if root == 'arch' or root == 'span':
				
				alledges = tgraph.edges
				foundationedges = self.getfoundation(alledges)
				
				for foundationedge in foundationedges.keys():
					
					((n1, n2), attribute) = foundationedges[foundationedge]
					
					node_attrs = pygraph.node_attributes(n2)
					value = n2
					for a,v in node_attrs:
						if a == "label":
							value = v
							
					# Should only point to components
					embeddedAVM = avm(n2, value)
					embeddedAVM.graph_toAVM(tgraph, n2)
					FV = featval(attribute, embeddedAVM)
					self.addFV(FV)
			
			
			else:
				edge_props =  pygraph.get_edge_properties((root,neighbor))
				attribute = edge_props['label']
				
				value = neighbor
				node_attrs = pygraph.node_attributes(neighbor)
				for a,v in node_attrs:
					if a == "label":
						value = v

				if self.terminal(neighbor, tgraph):
					# Hackish fix: I added HTML <i> tags to values to help with the graph-based output.
					# It was easiest to do this at the graph-construction stage. For AVMs, I need to remove them.
					value = value.replace("<<i>", "")
					value = value.replace("</i>>", "")
					FV = featval(attribute,value)
					self.addFV(FV)
			
				# We need a special condition to deal with criss-crossing Associates, as with Tiene.
				# This is a semi-hack.
				elif attribute == "ASSOCIATE":
					embeddedAVM = avm(neighbor, value)
					FV = featval(attribute, embeddedAVM)
					self.addFV(FV)
					pass
				
				else:
					embeddedAVM = avm(neighbor, value)
					embeddedAVM.graph_toAVM(tgraph, neighbor)
					FV = featval(attribute, embeddedAVM)
					self.addFV(FV)

	
	def getfoundation(self, edges):
		
		keys = edges.keys()

		foundationedges = { }
		for key in keys:
			
			# The values of edges are a pair of nodes, followed by a label
			((n1, n2), label) = edges[key]
			
			# Check if we are dealing with foundation nodes
			if n1 == 'arch' or n1 == 'span':
				foundationedges[label] = ((n1, n2), label)
				
		return foundationedges
			
			
	
	def canonicalize(self):
		self.order()
		self.normalize()


	# Order the feature-value pairs following order specified in orderings in function.
	# Append leftover pairings if any to end.
	# Recursive
	def order(self):

		# These lists need to be exhaustive or the output won't come out right, that is, you can't, for instance, leave out the last element
		orderings = { 'desmeme' 			: ["CONDITIONING", "VIOLABILITY", "STRICTURE", "FOUNDATION" ],
					  'length'  			: ["CONSTITUENT", "COUNT" ],
					  'order'  				: ["CONSTITUENT", "COUNT", "RELATIONS" ],
					  'arch'  				: ["LEFT_SUPPORT", "LEFT_VOUSSOIR", "KEYSTONE", "RIGHT_VOUSSOIR", "RIGHT_SUPPORT", "RESTKOMPONENTEN"], # Need full ordering or RKs are ignored (which is bad)
					  'span'  				: ["LEFT_SUPPORT", "RIGHT_SUPPORT", "RESTKOMPONENTEN"],
					  'component'		  	: ["ELASTICITY", "FILLEDNESS", "STABILITY" ],
					  'elastic'  			: ["MINIMUM", "MAXIMUM" ],
					  'partiallyFilled'  	: ["FILLER_PLACEMENT", "FORM", "COHERENCE" ],
					  'unstable'  			: ["SUPPORT", "SUPPORT_POSITION" ],
					  'lexicoconstructionalConditioning': ["FILLER_POSITION", "FILLED_COMPONENT", "FILLED_COMPONENTS" ],
					  'restkomponentenSet'	: ["RESTKOMPONENT"], # Need this list of one to allow components in side RK to be procssed; unfortunate hack
					  'filledComponentSet'	: ["FILLED_COMPONENTS"], # Need this list of one to allow components in side set to be procssed; unfortunate hack
					  'potentiallyViolable'	: ["EXCEPTIONALITY", "REPARABILITY"], 
					  'unstable'			: ["ASSOCIATE_POSITION", "ASSOCIATE"],
					}

		# Beware that this could screw up usage of Python's type() function
		type = self.type

		ufeatvals = self.featvals # "u" stands for "unordered"



		try:
			featorder = orderings[type]
		except:
			featorder = [] # Empty list to block to the for loop below, probably not a "pythonic" way of doing things
		
		
		# RKs are a special case, generalization no doubt possible, but I don't want to deal with it now.
		if type == 'restkomponentenSet':
			# RKsets only contain RKs which are themselves components. So, we just order all of them.
			for ufeatval in ufeatvals:
				uval = ufeatval.value
				uval.order()
					
		else:
			ofeatvals = []
			for ofeat in featorder: # "o" stands for ordered
				for ufeatval in ufeatvals:
					ufeat = ufeatval.feature
					uval = ufeatval.value
					if ofeat == ufeat:
						# We've found the feature we want in the unordered list; add it to the ordered list and delete from the unordered one.
						if isinstance(uval, avm):
							uval.order()
							ofeatvals.append(ufeatval)
							ufeatvals.remove(ufeatval)
						else:
							ofeatvals.append(ufeatval)
							ufeatvals.remove(ufeatval)
					
			# If anything remains in unordered list, just append it to the ordered list as leftovers
			for ufeatval in ufeatvals:
				ofeatvals.append(ufeatval)
			
			# set original featvals to ordered list
			self.featvals = ofeatvals

	
	# Removes duplicate component features, adding reference tag
	def normalize(self, components = None):

		# A list for prioritizing which features get the full AVM and (implicitly) which just get tags.
		# All possible features for components need to be listed here for the function to work.
		prioritylist = [ "KEYSTONE", "LEFT_SUPPORT", "RIGHT_SUPPORT", "LEFT_VOUSSOIR", "RIGHT_VOUSSOIR", "RESTKOMPONENT", "FILLED_COMPONENT", "FILLED_COMPONENTS", "SUPPORT", "ASSOCIATE"]
		
		if components == None: components = {}

		#Get a list of components and associated attributes that point to them
		components = self.buildcomponentlist()

		for component in components.keys():
			
			attributes = components[component]
			
			if len(attributes) > 1:
								
				priorityset = False
				for foundationfeature in prioritylist:
				
					if foundationfeature in attributes and priorityset == False and foundationfeature is "RESTKOMPONENT":
						self.RKre = component
						self.makepriorityfeature(foundationfeature, self, component)
						priorityset = True
						# Hack for Nimboran RK reentrancy; does not scale

					elif foundationfeature in attributes and priorityset == False:
						self.makepriorityfeature(foundationfeature, self)
						priorityset = True

					elif foundationfeature in attributes:
						self.makereenteredfeature(foundationfeature)
						
				if priorityset == False:
					print "Error: No prioritized feature found for", component
					

	# Removes duplicate component features, adding reference tags
	# Recursive
	def buildcomponentlist(self, feature = None, components = None):
		
		# Mutable defaults fix!
		if components == None: components = {}

		id = self.name
		type = self.type
		featvals = self.featvals

		if type == "component":
			
			try:
				attributes = components[id]
				attributes.append(feature)
				components[id] = attributes
			except:
				components[id] = [feature]

		for featval in featvals:
			val = featval.value
			feat = featval.feature
			if isinstance(val, basestring):
				pass
			else:
				val.buildcomponentlist(feat,components)
			
		return components


	# For a given feature, set it it as being the priority feature of a re-entrant AVM
	# We need to keep track of the highest AVM so we can set the tag numbers as appropriate
	# Recursive
	def makepriorityfeature(self, priorityfeature, topavm, componentID = False):

		featvals = self.featvals
		tagcount = topavm.totaltags

		for featval in featvals:
			feat = featval.feature
			val = featval.value
			
			# Hack for RK reentrancy
			try: RKre = topavm.RKre
			except: RKre = False
			
			#print "ci", componentID, feat

			# Hack to handle re-entrancy in RKset for Nimboran; breaks if reentrancy more than one
			if feat == priorityfeature and feat == "RESTKOMPONENT" and RKre == val.name:
				
				id = val.name
				val.reentered = True
				val.primary = True
				tagcount += 1
				val.tag = tagcount
				topavm.totaltags = tagcount
				topavm.tags[id] = tagcount

			# Only allow one re-entered RK per AVM--hack! not good assumption
			elif feat == priorityfeature and feat != "RESTKOMPONENT":
		
				id = val.name
				val.reentered = True
				val.primary = True
				tagcount += 1
				val.tag = tagcount
				topavm.totaltags = tagcount
				topavm.tags[id] = tagcount
			
			else:
				if isinstance(val, basestring):
					pass
				# Otherwise, we must have an embedded AVM to process to find what we need
				else:
					val.makepriorityfeature(priorityfeature, topavm, componentID)

	# For a given feature, set it it as being a non=priority re-entered feature
	# Recursive
	def makereenteredfeature(self, priorityfeature):

		featvals = self.featvals

		for featval in featvals:
			feat = featval.feature
			val = featval.value

			if feat == priorityfeature:
				val.reentered = True
			
			else:
				if isinstance(val, basestring):
					pass
				# Otherwise, we must have an embedded AVM to process to find what we need
				else:
					val.makereenteredfeature(priorityfeature)
		
		
	
	# Let's us know if there's an embedded AVM or not
	def terminal(self, node, tgraph):

		pygraph = tgraph.core
		neighbors = pygraph.neighbors(node)
		if neighbors:
			return False
		else:
			return True


	# Recursive
	# Pass around topavm to keep track of tags for re-entered components
	def to_ASCII(self, topavm, embedding = 0, seencomponents = { }, componentcount = 1):
		
		id = self.name
		type = self.type
		reentered = self.reentered
		primary = self.primary
		featvals = self.featvals
		
		# Check for re-entrancy conditions

		# If re-entered and not primary, just print a tag			
		if self.reentered and not(self.primary):
			tag = topavm.tags[id]
			print "\t"*embedding+"type:", "@"+str(tag), "("+id+")"

		else:
			if self.primary:
				tag = self.tag
				print "\t"*embedding+"type:", "@"+str(tag), type, "("+id+")"

			else:
				print "\t"*embedding+"type:", type, "("+id+")"
		
			for featval in featvals:
					
				feat = featval.feature
				val = featval.value
			
				if isinstance(val, basestring):
					print "\t"*embedding, feat, val

				else:
					print "\t"*embedding, feat
					embedding += 1
					val.to_ASCII(topavm, embedding, seencomponents, componentcount)
					embedding -= 1
				
	
	# Recursive
	# Pass around topavm to keep track of tags for re-entered components
	def to_latex(self, topavm, outfile, embedding = 0, seencomponents = { }, componentcount = 1):
		
		id = self.name
		type = self.type
		reentered = self.reentered
		primary = self.primary
		featvals = self.featvals
		
		# Check for re-entrancy conditions
		if embedding == 0:
			
			latexLabel = id.replace("_", "")
			id = id.replace("_", " ")
			#print >> outfile, "\\textbf{"+id+"}\n"
			#print >> outfile, "\\begin{figure}[ht]"
			print >> outfile, "{\\singlespacing\\avmshrink"
			print >> outfile, "\\begin{center}"
			print >> outfile, "\\begin{avm}"

		# If re-entered and not primary, just print a tag			
		if self.reentered and not(self.primary):
			tag = topavm.tags[id]
			print >> outfile, "\t"*embedding+"\\phantom{\\@{\\text{"+str(0)+"}}}"+"\\@{\\text{"+str(tag)+"}}"+"\\raisebox{-.5em}{\\rule{0pt}{1.5em}}"

		else:
			if self.primary:
				tag = self.tag
				print >> outfile, "\t"*embedding+"\\@{\\text{"+str(tag)+"}}", "\\[\t\\emph{"+type+"} \\cr"

			else:
				print >> outfile, "\t"*embedding+"\\phantom{\\@{\\text{"+str(0)+"}}}", "\\[\t\\emph{"+type+"} \\cr"
		
			for featval in featvals:
					
				feat = featval.feature
				val = featval.value
			
				prettyfeat = feat.lower()
				prettyfeat = prettyfeat.replace("_", " ")
			
				if isinstance(val, basestring):
					# Don't italicize numbers and change the "100" placeholder to infinity
					try:
						float(val)
						
						if val == '100':
							print >> outfile, "\t"*embedding, "\\textsc{"+prettyfeat+"}\t&\t", "\\phantom{\\@{\\text{"+str(0)+"}}}"+"$\infty$", "\\raisebox{-.5em}{\\rule{0pt}{1.5em}}\\cr"
						
						else:
							print >> outfile, "\t"*embedding, "\\textsc{"+prettyfeat+"}\t&\t", "\\phantom{\\@{\\text{"+str(0)+"}}}"+val, "\\raisebox{-.5em}{\\rule{0pt}{1.5em}}\\cr"
					
					except:
						print >> outfile, "\t"*embedding, "\\textsc{"+prettyfeat+"}\t&\t", "\\phantom{\\@{\\text{"+str(0)+"}}}"+"\\emph{"+val+"}", "\\raisebox{-.5em}{\\rule{0pt}{1.5em}}\\cr"

				else:					
					print >> outfile, "\t"*embedding, "\\textsc{"+prettyfeat+"}"+"\t&\t",
					embedding += 1
					val.to_latex(topavm, outfile, embedding, seencomponents, componentcount)
					print >> outfile, "\t"*embedding, " \\cr"
					embedding -= 1
					
			print >> outfile, "\t"*embedding, "\\]"

			if embedding == 0:
				print >> outfile, "\\end{avm}"
				print >> outfile, "\\end{center}}"
				#print >> outfile, "\\caption{Attribute-value representation of", id, "template", "\\label{"+latexLabel+"}}"
				#print >> outfile, "\\end{figure}"




class featval ( ):

	def __init__(self, feature, value):
		"""
		Initialize a typed feature-value pair.
		"""
		
		self.feature = feature
		self.value = value


	def to_latex(self):
		print self.type, self.feature, self.value