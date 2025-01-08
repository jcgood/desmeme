from tdag.validator import schema

#schemaFileName = "DesmemeSchema.tsv"
schemaFileName = "CmponentSchema.tsv"

#desmemeSchema = schema(schemaFileName, "desmeme")
desmemeSchema = schema(schemaFileName, "component")

[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()

