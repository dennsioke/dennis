Repository
https://github.com/acacode/swagger-typescript-api
Commit: b57c9d20df2cf7a0f2fe2018d5aa223b5f6a9671

Title
OpenAPI 3.1 prefixItems tuple type generation

The code generator doesn't handle OpenAPI 3.1's prefixItems keyword for array schemas. When prefixItems is present, the output should be a TypeScript tuple reflecting each positional entry rather than a uniform array type.

If items accompanies prefixItems as a schema, the tuple needs a rest element for additional entries beyond the fixed positions. If items is false or absent, the tuple should be strict with no rest element.

minItems should control which trailing positional entries become optional. Entries past the minItems boundary are optional; all are required when minItems is absent or meets the prefixItems length.

The usual behaviors still apply — $ref entries resolve to their component names, nullable arrays union with null, nested prefixItems produce nested tuples, and tuples work as object property types.
