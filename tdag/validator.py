import re
from collections import defaultdict
import warnings

# Sets as a lazy way of dealing with duplicates, too bad order is not maintained
typesToFeatures = defaultdict(set)
featuresToTypes = defaultdict(set)
embeddings = { }

class schema ( ):

	def __init__(self, filename, topType):
		"""
		Load a tabbed schema...
		"""
		
		self.filename = filename
		self.topType = topType
		
		self.typesToFeatures = defaultdict(set)
		self.featuresToTypes = defaultdict(set)
		self.embeddings = { }
		

	def processSchema(self):
	
		filename = self.filename
		type_ = self.topType
		embedding = 0
		feature = ""
			
		def processFile(schemaFile, embedding, type_, feature):
				
			for line in schemaFile:
		
				line = line.rstrip()
			
				tabs = re.match('^\t+', line)
				if tabs != None:
					tabCount = tabs[0].count("\t")
				else: tabCount = 0
				line = line.lstrip()
			
				# Different embedding levels have different parameters for tracing features and values
				if tabCount == embedding:
		
					# Condition 1: We have an attribute-value pair on one line
					if(re.match('^.+\t.+$', line)):
						(newFeature, newType) = line.split("\t")
						typesToFeatures[type_].add(newFeature)
						featuresToTypes[newFeature].add(newType)
						# Keep track of feature/value at current embedding level
						embeddings[embedding] = newFeature
						embeddings[tabCount + 1] = newType
						processFile(schemaFile, tabCount, type_, newFeature)
					
					# Condition 2: We only have a type on a line
					else:
						newType = line
						embeddings[tabCount] = newType
						featuresToTypes[feature].add(newType)
				
		
				elif tabCount > embedding:
		
					if(re.match('^.+\t.+$', line)):
						(newFeature, newType) = line.split("\t")
						try: type_ = embeddings[tabCount - 1] # previous level of list gets us last type
						except: type_ = topType
						typesToFeatures[type_].add(newFeature)
						featuresToTypes[newFeature].add(newType)
						embeddings[tabCount] = newFeature
						embeddings[tabCount + 1] = newType
						# Add 1 to tab count since we are dealing with a feature-value pair that takes up two tab positions
						processFile(schemaFile, tabCount + 1, newType, newFeature)
						
					else:
						newType = line
						featuresToTypes[feature].add(newType)
						embeddings[tabCount] = newType
						embedding = tabCount
		
		
				elif tabCount < embedding:
							
					if(re.match('^.+\t.+$', line)):
						(newFeature, newType) = line.split("\t")
						# Because the top type is at position "-1" in the system, we need a special logic
						try: type_ = embeddings[tabCount - 1]
						except: type_ = "desmeme"
						typesToFeatures[type_].add(newFeature)
						featuresToTypes[newFeature].add(newType)
						embeddings[tabCount] = newFeature
						embeddings[tabCount + 1] = newType
						# Add 1 to tab count since we are dealing with a feature-value pair that takes up two tab positions
						processFile(schemaFile, tabCount + 1, newType, newFeature)
						
					else:
						feature = embeddings[tabCount - 1]
						newType = line.lstrip()
						featuresToTypes[feature].add(newType)
						embeddings[tabCount] = newType
						embedding = tabCount
				

		with open(filename) as schemaFile:
			processFile(schemaFile, embedding, type_, feature)

		return([typesToFeatures, featuresToTypes])
