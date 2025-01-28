import re
from collections import defaultdict
from copy import deepcopy
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
						except: type_ = self.topType
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
				
		# level of indirection to start the recursion
		with open(filename) as schemaFile:
			processFile(schemaFile, embedding, type_, feature)

		# listify the sets
		#https://stackoverflow.com/questions/43600688/turn-dictionary-of-sets-into-dictionary-of-lists
		typesToFeaturesList = {key: list(values) for key, values in typesToFeatures.items()}
		featuresToTypesList = {key: list(values) for key, values in featuresToTypes.items()}

		self.typesToFeatures = typesToFeaturesList
		self.typesToFeaturesOriginal = deepcopy(typesToFeaturesList) # We need a version we won't destroy
		self.featuresToTypes = featuresToTypesList

		# To self: return is a syntax construct, not a function; this returns a tuple
		#return typesToFeaturesList, featuresToTypesList


	def validate_value(self, feature, value):
		
		featuresToTypes	= self.featuresToTypes
		
		try: validTypes = featuresToTypes[feature]
		except:
			# For features coded with Kleene + or *
			try: validTypes = featuresToTypes[feature+"+"]
			except:
				try: validTypes = featuresToTypes[feature+"*"]
				except: raise Exception(f"Feature {feature} not found in schema when "
										f"processing feature-value pair {feature} {value}.")

		# Check for ID/count values coded as a list with a dot
		if validTypes == ['.'] and isinstance(value, str):
			valueOK = True
		elif value in validTypes:
			valueOK = True
		# I wonder if I can improve error reporting since it can be hard to work out
		# specific issue from these
		else: raise Exception(f"Feature {feature} not found in schema when "
									f"processing feature-value pair {feature} {value}.")


	# This doesn't really need to be under schema, but I'm putting it here for tracking things better
	def allowed_feature(self, feature, type_):
		
		typesToFeatures = self.typesToFeaturesOriginal
		
		# Cleanup for component types
		cleanedType = type_
		if cleanedType.startswith("component_"):
			cleanedType = "component"
		elif cleanedType.startswith("elastic"):
			cleanedType = "elastic"
		elif cleanedType.startswith("inelastic"):
			cleanedType = "inelastic"
		elif cleanedType.startswith("partiallyFilled"):
			cleanedType = "partiallyFilled"
		elif cleanedType.startswith("stable"):
			cleanedType = "stable"
		elif cleanedType.startswith("unstable"):
			cleanedType = "unstable"
		
		validFeatures = typesToFeatures[cleanedType]
		
		if feature in validFeatures:
			pass
		elif feature+"+" in validFeatures:
			pass
		elif feature+"*" in validFeatures:
			pass
		else:
			raise Exception(f"Feature {feature} not associated with type {type_}.")
			

	# This doesn't really need to be under schema, but I'm putting it here for tracking things better
	def process_feature(self, embedding, feature, featureList):
		
		workingFeatures = featureList[embedding]
		
		try: workingFeatures.remove(feature)
		except:
			try: workingFeatures.remove(feature+"+")
			except:
				try: workingFeatures.remove(feature+"*")
				except: pass
			


	# This doesn't really need to be under schema, but I'm putting it here for tracking things better
	# It works in two different conditions, one with a tabCount and one without
	# If a tabCount is provided, it checks one list at one level above the tabCount
	def missing_features(self, featureLevelDict, level=None):

		if level == None:

			for featureSet in featureLevelDict:

				for feature in featureLevelDict[featureSet]:
					if feature.endswith("*"): featureLevelDict[featureSet].remove(feature)
					
				if featureLevelDict[featureSet] != []:
					raise Exception(f"Some required features were missing: {featureLevelDict[featureSet]} {featureLevelDict}.")
					
		else:
			featureList = featureLevelDict[level + 1]
			if featureList != []:
				raise Exception(f"Some required features were missing: {featureList}, level: {level+1}.")
				

	# This doesn't really need to be under schema, but I'm putting it here for tracking things better
	# Checks is all extant components are used
	# We check if a component referenced by a desmeme is actually found elsewhere in the
	# parser.
	def extra_comps(self, desCompRefs, componentFileName):

		with open(componentFileName) as componentFile:
			components = componentFile.read().split('\n\n')

		allCompRefs = set()
		for component in components:
			[compidfv, *compfeatvals] = component.split('\n')
			[compidfeat, compid] = compidfv.split('\t')
			if compidfeat != "IDENTIFIER":
				raise Exception(f"Expected leading IDENTIFIER feature, but found {compidfeat}.")
			else:
				allCompRefs.add(compid)
		
		unusedComps = allCompRefs - desCompRefs
		if unusedComps:
			raise Exception(f"Found components in component file that are not used: {unusedComps}.")
