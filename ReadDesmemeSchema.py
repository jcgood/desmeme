from tdag.validator import schema

schemaFileName = "DesmemeSchema.tsv"

desmemeSchema = schema(schemaFileName, "desmeme")

[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()

