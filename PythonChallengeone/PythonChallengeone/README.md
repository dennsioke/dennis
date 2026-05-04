# Configurable URL Canonification Rules

Repository
https://github.com/karlicoss/promnesia
Commit: f102b0acd63b27a8053002c1e3de3cccd48c5adb

The built-in URL canonification rules cover a fixed set of well-known domains, but users working with private intranets, self-hosted tools, or niche services have no way to teach the library which query parameters matter for those domains. As a result, meaningful parameters get stripped and unrelated visits incorrectly collapse into the same normalised URL.

It would be useful to extend the config with two optional fields: one for per-domain canonification rules, and one for domain alias mappings. Per-domain rules should follow the same semantics as the existing built-in ones - controlling which query params are retained, including a keep-all mode. When a custom rule exists for a domain it should fully replace any built-in rule for that domain. The globally-kept default params (id, t, p) should still be included alongside any user-specified ones, with user-specified params ordered after the defaults. Domain alias mappings should let users redirect variant prefixes (mobile subdomains, staging environments, etc.) to their canonical form, with custom mappings taking priority over built-in ones. A mapping and a per-domain rule should compose naturally: after a domain is remapped, the rule for the resulting domain applies.

Setting either field to an empty value should be a no-op. The rules must take effect immediately when config is set and must not persist once config is removed. Changes must propagate through the full indexing pipeline so that visits reflect the active config during canonification.
