Repository
https://github.com/acacode/swagger-typescript-api
Commit: b57c9d20df2cf7a0f2fe2018d5aa223b5f6a9671

Title
OpenAPI 3.1 prefixItems tuple type generation

OpenAPI 3.1 introduced `prefixItems` for defining positional element types in array schemas. The generator currently ignores this keyword entirely, so any schema using `prefixItems` just produces a generic array type.

Schemas with `prefixItems` should produce typed tuples where each position corresponds to its declared type. When `items` is also present as a schema, the tuple should allow additional elements of that type beyond the fixed positions. When `items` is `false` or omitted, no additional elements should be allowed.

`minItems` should determine which positional entries are required versus optional — entries past the `minItems` boundary become optional, and all entries are required by default.

Standard behaviors should carry through: `$ref` resolution, nullable unions, nesting, and usage as object property types.
