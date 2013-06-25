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
		
			print attribute, value
			
			# Todo: This will make only a flat list, we need to add structure to this somehow
			FV = featval(attribute,value)
			self.addFV(FV)
			
			self.graph_toAVM(tgraph, neighbor)
			
	#	for edge in edges:
	#		print pygraph.get_edge_properties(edge)

	#	for node in nodes:
	#		print node, pygraph.neighbors(node)
	#		#print node, pygraph.incidents(node) # incidence is reverse of neighbors
	#		print node, pygraph.node_attributes(node)
	
		
	
			
	# to self: we'll need logic that says, if node has a label attribute, use it, otherwise use node name.

class featval ( ):

	def __init__(self, feature, value):
		"""
		Initialize a typed feature-value pair.
		"""
		
		self.feature = feature
		self.value = value


	def to_latex(self):
		print self.type, self.feature, self.value