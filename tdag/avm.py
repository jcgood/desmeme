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

	
	
	# Let's us know if there's an embedded AVM or not
	def terminal(self, node, tgraph):

		pygraph = tgraph.core
		neighbors = pygraph.neighbors(node)
		if neighbors:
			return False
		else:
			return True


	## TODO: HAVE NOT HANDLED COMPONENT REFERENCES SINCE I DISCOVERED ERROR IN RESTKOMPONENT WRTING THAT I WANTED FIXED
	## STILL MAY BE WEIRD DUPLICATION OF FOUNDATIONS CHECK AFTER RK LISTS DONE
	def to_latex(self, embedding = 0, seencomponents = { }, componentcount = 1):
		
		id = self.name
		type = self.type
		featvals = self.featvals
				
		# We need to keep track of components that have been written to deal
		# with re-entrancy
		
		print "\t"*embedding+"type:", type, "("+id+")"
		
		for featval in featvals:
					
			feat = featval.feature
			val = featval.value
			
			if isinstance(val, basestring):
				print "\t"*embedding, feat, val
			else:

				if type == "component":
					try: seencomponents['id']
					except: print "xxxxxx"
				
				print "\t"*embedding, feat
				
				embedding += 1
				val.to_latex(embedding, seencomponents, componentcount)
				embedding -= 1
				
				if type == "component":
					seencomponents['id'] = componentcount
					componentcount += 1
		


class featval ( ):

	def __init__(self, feature, value):
		"""
		Initialize a typed feature-value pair.
		"""
		
		self.feature = feature
		self.value = value


	def to_latex(self):
		print self.type, self.feature, self.value