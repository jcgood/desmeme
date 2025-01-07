from tdag.validator import schema

desmemeFileName = "ChichewaDesmemes.tsv"

# For later, get the schema
schemaFileName = "DesmemeSchema.tsv"
desmemeSchema = schema(schemaFileName, "desmeme")
[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()

with open(desmemeFileName) as desmemeFile:
	 desmemes = file.read().split('\n\n')
	 
print(desmemes)