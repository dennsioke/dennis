# Configurable URL Canonification Rules

Repository
https://github.com/karlicoss/promnesia
Commit: f102b0acd63b27a8053002c1e3de3cccd48c5adb

The built-in URL canonification rules cover a fixed set of well-known domains, but users working with private intranets, self-hosted tools, or niche services have no way to teach the library which query parameters matter for those domains. As a result, meaningful parameters get stripped and unrelated visits incorrectly collapse into the same normalised URL.
It would be useful to extend the Config with two optional fields. The first, EXTRA_SPECS, is a dict mapping domain strings to promnesia.cannon.Spec objects, following the same semantics as the built-in specs. When a custom Spec exists for a domain it fully replaces any built-in rule for that exact domain; a rule for wiki.corp.com does not apply to blog.corp.com. The default params (id, t, p) are always included alongside any user-specified qkeep params, with user-specified params ordered after the defaults in definition order; when qkeep=True and the params have no explicit order, non-default params are sorted by key. The second field, EXTRA_DOMAIN_SUBSTITUTIONS, is a list of (from_prefix, to_prefix) string tuples applied as prefix substitutions to the domain portion of the URL only, before spec lookup. Custom substitutions take priority over built-in ones.
A mapping and a per-domain rule compose naturally: after a domain is remapped, the Spec for the resulting domain applies. Setting either field to an empty value should be a no-op. The rules must take effect immediately when config is set and must not persist once config is removed. Changes must propagate through the full indexing pipeline so that visits reflect the active config during canonification.
