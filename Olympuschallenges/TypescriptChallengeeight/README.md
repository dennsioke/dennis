Repository
https://github.com/lukeautry/tsoa
Commit: f0f9aa792d25c16c6ad4dd152cbac347c5faa471

Title
Discriminated union oneOf with discriminator across spec generation, route generation, and runtime validation

TypeScript discriminated unions -- where every member of a union is a named object type and they all share a common required property with a unique string literal type -- should be recognized and treated specially throughout the pipeline.
In the generated OpenAPI 3.0 and 3.1 specs, these unions should produce oneOf with a discriminator object instead of the current anyOf. The discriminator needs a propertyName and a mapping from each literal value to its schema ref. Unions that don't qualify (primitives, inline objects, no common literal property) should keep emitting anyOf as they do today. For OAS 3.0 nullable discriminated unions should retain both the discriminator and the nullable flag. For OAS 3.1 nullable discriminated unions should use a null type member in the oneOf array rather than the nullable flag, since nullable was removed in OpenAPI 3.1.
In Swagger 2.0 specs, discriminated unions should use the allOf inheritance pattern: the union type alias becomes a base schema with a discriminator string property, and each member schema wraps its own properties in an allOf that extends the base. Non-discriminated unions should continue to degrade to a plain object type as before.
This detection also needs to flow through route model generation so that runtime request validation can use the discriminant value to jump directly to the right variant rather than trying each sub-schema in sequence. If the discriminant value doesn't match any known variant, validation should report the unrecognized value rather than falling through to a generic union mismatch error.
