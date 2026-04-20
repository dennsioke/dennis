Repository
https://github.com/lukeautry/tsoa
Commit: f0f9aa792d25c16c6ad4dd152cbac347c5faa471

Title
Add discriminated union detection with oneOf/discriminator spec output, Swagger 2 allOf inheritance, and discriminator-aware runtime validation

Add automatic detection of TypeScript discriminated unions -- where every member is a named object type sharing a common required property with a unique string literal type -- and introduce new spec output, route model propagation, and runtime validation behavior for them.
For detected discriminated unions, OpenAPI 3.0 and 3.1 spec generators must emit a new oneOf array with a discriminator object containing propertyName and a mapping from each literal value to its schema ref. Non-qualifying unions (primitives, inline objects, no common literal property) must continue to emit anyOf. For OAS 3.0 nullable discriminated unions must include both the discriminator and the nullable flag. For OAS 3.1 nullable discriminated unions must add a null type member in the oneOf array instead of nullable.
For Swagger 2.0, detected discriminated unions must use a new allOf inheritance pattern: the union type alias becomes a base schema with a discriminator string property, and each member schema wraps its own properties in an allOf that extends the base. Member schemas must not duplicate the discriminant property in their own allOf block; only the base schema declares it. Non-discriminated unions must continue to degrade to a plain object type.
Route model propagation must include discriminator metadata on the union schema -- a propertyName and a mapping from each literal value to its model ref -- so that ValidationService can use it at runtime. A new discriminator-aware validation path must be added so that the discriminant value routes directly to the matching variant. If the discriminant value does not match any known variant, a specific error must be reported that includes the offending discriminant value in its message. If the input is not an object, validation must fall back to sequential union matching even when a discriminator is configured.

Hints

Swagger 2.0 allOf member schemas: In buildDefinitions(), pre-scan metadata.referenceTypeMap for refAlias entries whose type is a union with a discriminator to build a member→union membership map. When emitting a refObject that is a member, output an allOf: [{ $ref: '#/definitions/<UnionName>' }, { type: 'object', properties: { ...ownProps } }] where ownProps EXCLUDES the discriminant property (only the base declares it). Also add allOf to the Swagger.Schema2 interface in swagger.ts.

OAS 3.1 nullable discriminated unions: Override getSwaggerTypeForUnionType in specGenerator31.ts. For nullable discriminated unions, add { type: 'null' } as a member of the oneOf array and do NOT set nullable. Non-nullable discriminated unions emit oneOf + discriminator without nullable (same structure as 3.0).
