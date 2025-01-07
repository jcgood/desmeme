from tdag.validator import schema

schemaFileName = "DesmemeSchema.tsv"

desmemeSchema = schema(schemaFileName, "desmeme")

[a, b] = desmemeSchema.processSchema()

print(a)
print(b)