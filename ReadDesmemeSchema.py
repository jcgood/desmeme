from tdag.validator import schema

#schemaFileName = "DesmemeSchema.tsv"
schemaFileName = "ComponentSchema.tsv"

#desmemeSchema = schema(schemaFileName, "desmeme")
desmemeSchema = schema(schemaFileName, "component")

[typesToFeatures, featuresToTypes] = desmemeSchema.processSchema()

print(typesToFeatures,"\n\n",featuresToTypes)