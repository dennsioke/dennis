Repository
https://github.com/acacode/swagger-typescript-api
Commit: b57c9d20df2cf7a0f2fe2018d5aa223b5f6a9671

Title
OpenAPI 3.1 prefixItems tuple type generation

Array schemas with a prefixItems array must generate TypeScript tuple types instead of uniform array types, e.g. [string, number, boolean] rather than (string | number | boolean)[]. When items is set to a schema object alongside prefixItems, additional elements beyond the positional entries must appear as a rest element in the tuple, e.g. [string, ...number[]]. When items is false or absent, no rest element is produced.
When minItems is less than the length of prefixItems, positional entries beyond the minItems boundary must be marked optional in the tuple, e.g. [string, number?, boolean?] for minItems of 1 with three prefixItems entries. All prefixItems entries are required by default when minItems is absent or greater than or equal to the prefixItems length.
prefixItems entries that use $ref must resolve to the referenced component type name. Nullable array schemas with prefixItems must produce a tuple unioned with null. prefixItems schemas that themselves contain a nested prefixItems must produce a nested tuple. A prefixItems array used as an object property must appear as a tuple type for that field.
