---
type: community
cohesion: 0.09
members: 28
---

# Community 40

**Cohesion:** 0.09 - loosely connected
**Members:** 28 nodes

## Members
- [[collectRustBindings()]] - code - GitNexus/gitnexus/src/core/ingestion/named-bindings/rust.ts
- [[extractCapturedPatternBindings()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractDeclaration()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractForLoopBinding()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractInitializer()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractParameter()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractPatternBinding()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractPendingAssignment()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractRustAnnotations()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[extractRustElementTypeFromTypeNode()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[extractRustMethodName()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[extractRustNamedBindings()]] - code - GitNexus/gitnexus/src/core/ingestion/named-bindings/rust.ts
- [[extractRustParameters()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[extractRustReceiverType()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[extractRustReturnType()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[extractRustVisibility()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[extractStructPatternType()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[findEnclosingImplType()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[findRustParamElementType()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[hasMutKeyword()]] - code - GitNexus/gitnexus/src/core/ingestion/variable-extractors/configs/rust.ts
- [[hasVisibilityModifier()]] - code - GitNexus/gitnexus/src/core/ingestion/variable-extractors/configs/rust.ts
- [[isRustAsync()]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[resolveRustImportInternal()]] - code - GitNexus/gitnexus/src/core/ingestion/import-resolvers/rust.ts
- [[rust.ts]] - code - GitNexus/gitnexus/src/core/ingestion/method-extractors/configs/rust.ts
- [[rustExtractFunctionName()]] - code - GitNexus/gitnexus/src/core/ingestion/languages/rust.ts
- [[rustModuleStrategy()]] - code - GitNexus/gitnexus/src/core/ingestion/import-resolvers/configs/rust.ts
- [[scanConstructorBinding()]] - code - GitNexus/gitnexus/src/core/ingestion/type-extractors/rust.ts
- [[tryRustModulePath()]] - code - GitNexus/gitnexus/src/core/ingestion/import-resolvers/rust.ts

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_40
SORT file.name ASC
```
