import re
import os
from collections import defaultdict
from copy import deepcopy
import warnings

def _load_grammatical_categories():
    schema_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(schema_dir, "schema", "GrammaticalCategories.tsv")
    with open(path) as f:
        return {line.strip() for line in f if line.strip()}

GRAMMATICAL_CATEGORIES = _load_grammatical_categories()

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

		# NT: is the legacy prefix used before the MD:/AN:/EX: scheme was
		# introduced. Accept any string value; the migration script will
		# rename these to the correct prefix.
		if feature.startswith("NT:") and isinstance(value, str):
			return

		featuresToTypes	= self.featuresToTypes

		try: validTypes = featuresToTypes[feature]
		except:
			# For features coded with Kleene + or *
			try: validTypes = featuresToTypes[feature+"+"]
			except:
				try: validTypes = featuresToTypes[feature+"*"]
				except: raise Exception(f"Feature {feature} not found in schema when "
										f"processing feature-value pair {feature} {value}.")

		# @-sigil type checking
		if validTypes == ['@id'] and isinstance(value, str):
			valueOK = True
		elif validTypes == ['@lang'] and isinstance(value, str):
			valueOK = True
		elif validTypes == ['@int']:
			valueOK = (isinstance(value, str) and (value.isdigit() or value == '∞'))
			if not valueOK:
				raise Exception(f"Feature {feature} expects an integer, got {value!r}.")
		elif validTypes == ['@ref'] and isinstance(value, str):
			valueOK = True
		elif validTypes == ['@str'] and isinstance(value, str):
			valueOK = True
		elif validTypes == ['@grammaticalCategory']:
			valueOK = value in GRAMMATICAL_CATEGORIES
			if not valueOK:
				raise Exception(f"Value {value!r} for feature {feature} is not a known "
								f"grammatical category.")
		# Legacy dot placeholder (kept for backward compatibility during migration)
		elif validTypes == ['.'] and isinstance(value, str):
			valueOK = True
		elif value in validTypes:
			valueOK = True
		else:
			raise Exception(f"Value {value!r} not valid for feature {feature} "
							f"(expected one of {validTypes}).")


	# This doesn't really need to be under schema, but I'm putting it here for tracking things better
	def allowed_feature(self, feature, type_):
		
		typesToFeatures = self.typesToFeaturesOriginal
		
		# Strip numeric suffixes added by tdag.add_node for repeatable node types
		# (e.g. filled1 -> filled, canonicalLineate2 -> canonicalLineate).
		# Must be exact base name + digits only, to avoid false matches like
		# filledComponentSet or HymanMchombo-2002.
		_REPEATABLE = ("elastic", "inelastic", "partiallyFilled", "filled",
		               "open", "null", "coherent", "incoherent",
		               "stable", "unstable", "canonicalLineate",
		               "embeddedDesmeme", "final")
		cleanedType = type_
		if cleanedType.startswith("component_"):
			cleanedType = "component"
		else:
			for _base in _REPEATABLE:
				if cleanedType == _base or (cleanedType.startswith(_base) and cleanedType[len(_base):].isdigit()):
					cleanedType = _base
					break
		
		validFeatures = typesToFeatures.get(cleanedType, [])

		if feature in validFeatures:
			pass
		elif feature+"+" in validFeatures:
			pass
		elif feature+"*" in validFeatures:
			pass
		elif feature.startswith(("MD:", "AN:", "EX:", "NT:")):
			# Prefixed features are validated against the schema by their full name.
			# If not found under the current type, check if any type in the schema
			# allows them (they may be optional and the parser may not have
			# descended into their parent yet). Raise only if completely unknown.
			allFeatures = set()
			for feats in typesToFeatures.values():
				allFeatures.update(feats)
			if feature not in allFeatures and feature+"*" not in allFeatures and feature+"+" not in allFeatures:
				raise Exception(f"Prefixed feature {feature} not found anywhere in schema.")
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
				featureLevelDict[featureSet] = [f for f in featureLevelDict[featureSet] if not f.endswith("*")]
				if featureLevelDict[featureSet] != []:
					raise Exception(f"Some required features were missing: {featureLevelDict[featureSet]} {featureLevelDict}.")
					
		else:
			featureList = [f for f in featureLevelDict[level + 1] if not f.endswith("*")]
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
