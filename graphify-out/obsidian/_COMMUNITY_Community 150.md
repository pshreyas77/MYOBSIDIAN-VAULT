---
type: community
cohesion: 0.25
members: 8
---

# Community 150

**Cohesion:** 0.25 - loosely connected
**Members:** 8 nodes

## Members
- [[call-analysis.ts]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[countCallArguments()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[extractCallArgTypes()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[extractCallChain()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[extractMixedChain()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[extractReceiverName()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[extractReceiverNode()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts
- [[inferCallForm()]] - code - GitNexus/gitnexus/src/core/ingestion/utils/call-analysis.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_150
SORT file.name ASC
```
