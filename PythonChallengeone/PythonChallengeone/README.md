# Configurable URL Canonification Rules

Repository
https://github.com/karlicoss/promnesia
Commit: f102b0acd63b27a8053002c1e3de3cccd48c5adb

Users cannot currently define per-domain URL normalization rules for domains not already built into the library. Private, internal, or niche domains (intranets, self-hosted services, company wikis) always have all query parameters dropped with no way to configure which ones are meaningful.
The configuration system must accept user-defined per-domain canonification rules that extend or override the built-in site-specific rules. When a custom rule is set for a domain, it replaces the built-in rule for that domain entirely. Custom rules must support the same query-param keep/drop semantics as existing built-in rules, including declaring specific params to keep and the keep-all mode. The default params kept for unknown domains (id, t, p) remain retained by any custom rule in addition to user-specified params; the ordering of kept params in the canonical URL reflects default params first, then user-specified params, in definition order.
The configuration system must also accept user-defined domain alias mappings that redirect variant domain prefixes (mobile, staging, alternate TLD variants) to their canonical form. Custom domain mappings are applied before the built-in mappings and take priority when both match the same domain prefix. After a domain is remapped, the per-domain canonification rules apply to the resulting canonical domain, so a domain mapping and a per-domain rule can be combined.
Providing an empty set of custom rules must not alter any existing canonification behavior. Custom rules must take effect immediately when config is set and must not persist after config is removed; the implementation must not mutate shared global state that outlives the config lifecycle.
The new configuration must work end-to-end: visits canonified during indexing must reflect the custom rules when config is active.
