Repository
https://github.com/lukeautry/tsoa
Commit: f0f9aa792d25c16c6ad4dd152cbac347c5faa471

Title
Add discriminated union detection with oneOf/discriminator spec output, Swagger 2 allOf inheritance, and discriminator-aware runtime validation

Add automatic detection of TypeScript discriminated unions -- where every member is a named object type sharing a common required property with a unique string literal type -- and introduce new spec output, route model propagation, and runtime validation behavior for them.
For detected discriminated unions, OpenAPI 3.0 and 3.1 spec generators must emit a new oneOf array with a discriminator object containing propertyName and a mapping from each literal value to its schema ref. Non-qualifying unions (primitives, inline objects, no common literal property) must continue to emit anyOf. For OAS 3.0 nullable discriminated unions must include both the discriminator and the nullable flag. For OAS 3.1 nullable discriminated unions must add a null type member in the oneOf array instead of nullable.
For Swagger 2.0, detected discriminated unions must use a new allOf inheritance pattern: the union type alias becomes a base schema with a discriminator string property, and each member schema wraps its own properties in an allOf that extends the base. Member schemas must not duplicate the discriminant property in their own allOf block; only the base schema declares it. Non-discriminated unions must continue to degrade to a plain object type.
Route model propagation must include discriminator metadata on the union schema -- a propertyName and a mapping from each literal value to its model ref -- so that ValidationService can use it at runtime. A new discriminator-aware validation path must be added so that the discriminant value routes directly to the matching variant. If the discriminant value does not match any known variant, a specific error must be reported that includes the offending discriminant value in its message. If the input is not an object, validation must fall back to sequential union matching even when a discriminator is configured.

Implementation hints

Swagger 2.0 specGenerator2.ts -- allOf inheritance pattern (most complex part):
- In Swagger 2.0, `discriminator` on a schema is a plain STRING (the property name), NOT an object. E.g. for Shape the definition should have `discriminator: 'kind'`, `required: ['kind']`, `properties: { kind: { type: 'string' } }`.
- The `buildDefinitions()` method must use a TWO-PASS approach: first scan ALL refAlias entries in `metadata.referenceTypeMap` to find which ones resolve to a union type with a discriminator, then build a membership map from each member refObject name to its parent union name and discriminator propertyName. When processing refObject definitions in the second pass, if that object is a discriminated union member, emit an allOf schema `[{ $ref: '#/definitions/<UnionName>' }, { type: 'object', properties: { ...ownProps }, required: [...] }]` instead of a normal flat object definition. The member's own properties in the allOf block must EXCLUDE the discriminant property -- only the base union schema declares it.
- The union's base schema (e.g. Shape) is built during `getSwaggerTypeForUnionType` → `buildSwagger2DiscriminatedUnion` and must be MERGED into the definitions map after all types are processed. Use an instance field (e.g. a Map) to collect base schemas during type processing, plus a `currentRefAliasName` string field set before calling `getSwaggerType` for refAlias entries so the discriminated union builder knows which alias name to register the base schema under.
- In `getSwaggerTypeForUnionType`, the existing `else if (process.env.NODE_ENV !== 'tsoa_test')` guard must be BROKEN into separate if-blocks: first check `type.discriminator` and call the Swagger 2 builder, THEN fall through to the console.warn / `{ type: 'object' }` fallback. Keeping these chained in an else-if means discriminated unions never reach the builder.
- The `Swagger.Schema2` TypeScript interface in `packages/runtime/src/swagger/swagger.ts` must have an `allOf` field added: `allOf?: (BaseSchema | Schema2)[]`. Without this the build fails with a type error on member definitions.

OpenAPI 3.1 specGenerator31.ts -- nullable discriminated unions:
- Override `getSwaggerTypeForUnionType` from the OAS 3.0 base class. For nullable discriminated unions, add `{ type: 'null' }` as a MEMBER of the oneOf array and do NOT set a `nullable` flag. For non-nullable discriminated unions, emit `oneOf` + `discriminator` (same as 3.0 but without nullable).
- The discriminator `mapping` values must be full component refs: `#/components/schemas/<RefName>`.

OpenAPI 3.0 specGenerator3.ts -- anyOf to oneOf conversion:
- Add an `applyDiscriminator` helper that, given a result object and the discriminator metadata, renames `anyOf` to `oneOf` and injects a `discriminator` object with `propertyName` and `mapping` (with full `#/components/schemas/` refs). Call this in BOTH the nullable and non-nullable branches of `getSwaggerTypeForUnionType` when `type.discriminator` is set.

Runtime validation in templateHelpers.ts:
- In the `validateUnion` method of `ValidationService`, add discriminator-aware routing BEFORE the existing sequential union matching loop. Check `property.discriminator`, verify value is a non-null non-array object, read the discriminant field, look up the mapping to find the target ref, find the matching subSchema by ref, and validate against just that variant. If the discriminant value is a string but doesn't match any mapping key, set a fieldError with a message that INCLUDES the offending discriminant value (e.g. `Invalid discriminant value '${discriminantValue}'...`). If the value is not an object (primitives, arrays, null), skip the discriminator path entirely and fall through to sequential matching.
