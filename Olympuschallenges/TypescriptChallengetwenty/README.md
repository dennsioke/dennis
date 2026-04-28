Repository
https://github.com/unplugin/unplugin-vue-components
Commit: 5e2addf639894c3a3d3369502d735f0a19223094

Title
Resolver result cache with LRU eviction

Add a resolverCache option to Context that, when configured with a maxSize, caches successful resolver results so that repeated findComponent calls for the same name and type skip resolver invocation entirely.
The cache must hold at most maxSize entries; when full, the least-recently-used entry must be evicted before a new one is inserted.
When a filesystem component is registered whose name matches a cached resolver entry, that cache entry must be immediately invalidated so the filesystem component takes precedence on the next lookup.
Context must expose a clearResolverCache() method that synchronously empties the live cache.
