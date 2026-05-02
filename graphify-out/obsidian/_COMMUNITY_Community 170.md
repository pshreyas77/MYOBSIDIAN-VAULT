---
type: community
cohesion: 0.29
members: 7
---

# Community 170

**Cohesion:** 0.29 - loosely connected
**Members:** 7 nodes

## Members
- [[cache-stats.ts]] - code - GitNexus/gitnexus/src/core/ingestion/languages/python/cache-stats.ts
- [[getCsharpCaptureCacheStats()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/csharp/cache-stats.ts
- [[getPythonCaptureCacheStats()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/python/cache-stats.ts
- [[recordCacheHit()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/python/cache-stats.ts
- [[recordCacheMiss()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/python/cache-stats.ts
- [[resetCsharpCaptureCacheStats()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/csharp/cache-stats.ts
- [[resetPythonCaptureCacheStats()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/python/cache-stats.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_170
SORT file.name ASC
```
