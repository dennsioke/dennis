Repository
https://github.com/exa-labs/exa-mcp-server
Commit: 7060e0efbc272dddce126e7a35dbf1722c510d08

Title
Tool Results Cache

Add a ToolResultsCache class to avoid redundant Exa API calls for identical tool invocations. It supports configurable capacity and TTL, and accepts an optional clock override so expiry behavior can be tested without real time passing. Cumulative hit and miss counts are tracked, and a size property reports only live (non-expired) entries.
Expiry is measured from the most recent write, so updating an existing entry resets its lifetime and refreshes its recency. Reads also refresh recency. When inserting a new entry would exceed capacity, the least-recently-used live entry is evicted; expired entries do not count toward the limit. Invalidation targets either all entries for a specific tool name or the entire cache when called without arguments.
Two param objects that are logically equivalent (same keys and values, regardless of insertion order, whitespace in strings, or array ordering) must resolve to the same cache entry. Keys with null or undefined values are treated as absent.
