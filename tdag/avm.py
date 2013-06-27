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
				
		neighbors = pygraph.neighbors(root)
		
		for neighbor in neighbors:

			# We need to do something special for the case where a pair of nodes is
			# associated with two distinct edges. It would be nice to find a general
			# solution, but since, for now, this only happens for foundations, I'm going with
			# a specific one
			# TO CONSIDER: Can I just replace the old "else" code with this code? Is there a reason to believe it won't generalize?
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
					#print attribute, embeddedAVM			
			
			else:
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

	def getfoundation(self, edges):
		
		keys = edges.keys()

		foundationedges = { }
		for key in keys:
			
			# The values of edges are a pair of nodes, followed by a label
			((n1, n2), label) = edges[key]
			
			# Check if we are dealing with foundation nodes
			if n1 == 'arch' or n1 == 'span':
				#print n1, n2, label
				foundationedges[label] = ((n1, n2), label)
				
		return foundationedges
			
			
	
	def canonicalize(self):
		self.order()
		self.normalize()


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
	def normalize(self, components = None):

		
		if components == None: components = {}

		# TODO: FILL THIS OUT
		# I now have a nice components list for finding re-entrancy.
		# I just need to use it...

		components = self.buildcomponentlist()

		print components


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