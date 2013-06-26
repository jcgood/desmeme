from tdag import tdag

class avm ( ):

	def __init__(self, name, type):
		"""
		Initialize an AVM.
		"""
		
		self.name = name

		# These are typed AVMs, after all.
		self.type = type

		#A list for feature-value pairs
		self.featvals = [ ]
	
	
	
	def addFV(self, featval):
		"""
		Add a typed feature-values pair
		"""
				
		feat = featval.feature
		storedFeatvals = self.featvals
		
		print "f", feat
		
		# Avoid duplication due to re-entrancy
		hasFeature = False
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
		print "keys:", tgraph.edges
		
		neighbors = pygraph.neighbors(root)
		
		for neighbor in neighbors:
			
			# TODO: I'M LOSING EDGES WITH REENTRANCY (EG IN CHICH AVM) ONLY ONE EDGE FOUND...NEED TO WORK ON FINDING EDGES, CHECK TO DOT?
			
			edge_props =  pygraph.get_edge_properties((root,neighbor))
			attribute = edge_props['label']
				
			value = neighbor
			node_attrs = pygraph.node_attributes(neighbor)
			for a,v in node_attrs:
				if a == "label":
					value = v

			if self.terminal(neighbor, tgraph):
				FV = featval(attribute,value)
				self.addFV(FV)
			
			else:
				embeddedAVM = avm(neighbor, value)
				embeddedAVM.graph_toAVM(tgraph, neighbor)
				FV = featval(attribute, embeddedAVM)
				self.addFV(FV)

	
	def canonicalize(self):
		self.order()
		#self.normalize()


	# Order the feature-value pairs following order specified in orderings in function.
	# Append leftover pairings if any to end.
	# Recursive
	def order(self):

		orderings = { 'desmeme' 			: ["CONDITIONING", "VIOLABILITY", "STRICTURE", "FOUNDATION" ],
					  'length'  			: ["CONSTITUENT", "COUNT" ],
					  'order'  				: ["CONSTITUENT", "COUNT", "RELATIONS" ],
					  'arch'  				: ["LEFT_SUPPORT", "LEFT_VOUSSOIR", "KEYSTONE", "RIGHT_VOUSSOIR", "RIGHT_SUPPORT"],
					  'span'  				: ["LEFT_SUPPORT", "RIGHT_SUPPORT"],
					  'component'		  	: ["ELASTICITY", "FILLEDNESS", "STABILITY" ],
					  'elastic'  			: ["MAXIMUM", "MINUMUM" ],
					  'partially filled'  	: ["FILLER_POSITION", "FORM", "COHERENCE" ],
					  'unstable'  			: ["SUPPORT", "SUPPORT_POSITION" ],
					  'lexicoconstructionalConditioning': ["FILLER_POSITION", "FILLED_COMPONENT" ],
					}

		# I want to use type() later, so I can't assign type to a string!
		type = self.type
		ufeatvals = self.featvals # "u" stands for "unordered"

		try:
			featorder = orderings[type]
		except:
			featorder = [] # Empty list to block to the for loop below, probably not a "pythonic" way of doing things
		
		
		ofeatvals = []
		for ofeat in featorder: # "o" stands for ordered
			for ufeatval in ufeatvals:
				ufeat = ufeatval.feature
				uval = ufeatval.value
				if ofeat == ufeat:
					# We've found the feature we want in the unordered list; add it to the ordered list and delete from the unordered one.
					if isinstance(uval ,avm):
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

	
	# Removes duplicate component features, adding reference tags
	# Recursive
	def normalize(self, components = {}):

		# TODO: FILL THIS OUT

		components = self.buildcomponentlist()

		id = self.name
		type = self.type
		ufeatvals = self.featvals # "u" stands for "unordered"



	# Removes duplicate component features, adding reference tags
	# Recursive
	def buildcomponentlist(self, components = {}):

		# TODO: THIS HAS ODD BEHAVIOR, OVERCOUNTING COMPONENTS. I DON"T KNOW WHY, GOT distracted by lost edges...

		id = self.name
		type = self.type
		featvals = self.featvals

		if type == "component":
			print type, id
			try:
				components[id] += 1
			except:
				components[id] = 0

		for featval in featvals:
			val = featval.value
			if isinstance(val, basestring):
				pass
			else:
				print val.name
				val.buildcomponentlist(components)
			
		return components

	
	# Let's us know if there's an embedded AVM or not
	def terminal(self, node, tgraph):

		pygraph = tgraph.core
		neighbors = pygraph.neighbors(node)
		if neighbors:
			return False
		else:
			return True


	# Recursive
	def to_latex(self, embedding = 0, seencomponents = { }, componentcount = 1):
		
		id = self.name
		type = self.type
		featvals = self.featvals
				
		
		print "\t"*embedding+"type:", type, "("+id+")"
		
		for featval in featvals:
					
			feat = featval.feature
			val = featval.value
			
			if isinstance(val, basestring):
				print "\t"*embedding, feat, val

			else:
				print "\t"*embedding, feat
				
				embedding += 1
				val.to_latex(embedding, seencomponents, componentcount)
				embedding -= 1
				
		


class featval ( ):

	def __init__(self, feature, value):
		"""
		Initialize a typed feature-value pair.
		"""
		
		self.feature = feature
		self.value = value


	def to_latex(self):
		print self.type, self.feature, self.value