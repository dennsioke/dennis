Repository
https://github.com/lukeautry/tsoa
Commit: f0f9aa792d25c16c6ad4dd152cbac347c5faa471

Title
Add discriminated union detection with oneOf/discriminator spec output, Swagger 2 allOf inheritance, and discriminator-aware runtime validation

Add automatic detection of TypeScript discriminated unions -- where every member is a named object type sharing a common required property with a unique string literal type -- and introduce new spec output, route model propagation, and runtime validation behavior for them.
For detected discriminated unions, OpenAPI 3.0 and 3.1 spec generators must emit a new oneOf array with a discriminator object containing propertyName and a mapping from each literal value to its schema ref. Non-qualifying unions (primitives, inline objects, no common literal property) must continue to emit anyOf. For OAS 3.0 nullable discriminated unions must include both the discriminator and the nullable flag. For OAS 3.1 nullable discriminated unions must add a null type member in the oneOf array instead of nullable.
For Swagger 2.0, detected discriminated unions must use a new allOf inheritance pattern: the union type alias becomes a base schema with a discriminator string property, and each member schema wraps its own properties in an allOf that extends the base. Non-discriminated unions must continue to degrade to a plain object type.
A new discriminator-aware validation path must be added to route model generation and runtime request validation so that the discriminant value routes directly to the matching variant. If the discriminant value does not match any known variant, a new specific error must be reported instead of falling through to generic union mismatch.
