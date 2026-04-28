Repository
https://github.com/exa-labs/exa-mcp-server
Commit: 7060e0efbc272dddce126e7a35dbf1722c510d08

Title
Tool Results Cache

Add a ToolResultsCache class that caches tool responses keyed by tool name and a normalized parameter fingerprint, with LRU eviction and TTL-based expiry. The constructor takes maxEntries, ttlMs, and an optional clock function (no-arg, returns milliseconds) that overrides the time source. Cumulative hit and miss counts are tracked, and a size property reports only non-expired entries.
TTL is measured from the most recent write to a key, so overwriting an existing entry resets its expiry and refreshes its recency. Reads refresh recency too. When a new entry would exceed the capacity, the least-recently-used live entry is evicted — expired entries do not count toward the limit and are not chosen for eviction. Invalidation removes all entries for a given tool name, or everything when called without arguments.
The fingerprint must treat logically equivalent param objects as the same key: object keys are sorted at every nesting level, string values are trimmed and lowercased, arrays are lexicographically sorted, and keys whose value is null or undefined are excluded.
