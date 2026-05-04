# Configurable URL Canonification Rules

Repository
https://github.com/karlicoss/promnesia
Commit: f102b0acd63b27a8053002c1e3de3cccd48c5adb

The built-in URL canonification rules cover a fixed set of domains; there is no way to extend them for private intranets or niche services without modifying the library source.

Please add two optional fields to Config. EXTRA_SPECS is a dict[str, promnesia.cannon.Spec] mapping domain strings to canonification rules. Domain key lookup uses the same suffix-matching as the built-in specs (e.g. a key 'corp.com' also matches 'jira.corp.com' but not 'corp.net'; a single-label key like 'corp' matches only domains whose TLD is that label; 'www.' and 'amp.' are stripped before lookup). A custom Spec fully replaces any built-in rule for that domain. When qkeep is a list, the default params (id, t, p) are always included first, with user-specified params appended in definition order. When qkeep=True, all params are kept and sorted alphabetically by key with no special precedence for the defaults. EXTRA_DOMAIN_SUBSTITUTIONS is a list[tuple[str, str]] of (from_prefix, to_prefix) pairs applied as prefix substitutions to the domain before spec lookup. The list uses first-match semantics: the first matching entry fires and scanning stops, so definition order wins over specificity, and duplicate prefixes only trigger the first occurrence. After the custom list resolves, the built-in substitution list runs against the result, meaning a custom entry can chain into a built-in mapping.

Both fields should compose naturally, default to empty (no-op), take effect immediately when config is set, and leave no trace after config is removed. Changes must propagate through the full indexing pipeline.
