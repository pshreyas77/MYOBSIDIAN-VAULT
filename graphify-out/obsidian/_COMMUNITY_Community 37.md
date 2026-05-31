---
type: community
cohesion: 0.07
members: 30
---

# Community 37

**Cohesion:** 0.07 - loosely connected
**Members:** 30 nodes

## Members
- [[AST-resolved call edges are deterministic and should be EXTRACTED1.0.]] - rationale - graphify-repo/tests/test_extract.py
- [[After merging multiple files, no internal edges should be dangling.]] - rationale - graphify-repo/tests/test_extract.py
- [[All edge sources must reference a known node (targets may be external imports).]] - rationale - graphify-repo/tests/test_extract.py
- [[Analyzer.process() calls run_analysis() - cross class→function calls edge.]] - rationale - graphify-repo/tests/test_extract.py
- [[Call-graph pass must produce INFERRED calls edges.]] - rationale - graphify-repo/tests/test_extract.py
- [[Same caller→callee pair must appear only once even if called multiple times.]] - rationale - graphify-repo/tests/test_extract.py
- [[Same input always produces same output.]] - rationale - graphify-repo/tests/test_extract.py
- [[contains  method  inherits  imports edges must always be EXTRACTED.]] - rationale - graphify-repo/tests/test_extract.py
- [[run_analysis() calls compute_score() - must appear as a calls edge.]] - rationale - graphify-repo/tests/test_extract.py
- [[test_calls_deduplication()]] - code - graphify-repo/tests/test_extract.py
- [[test_calls_edges_are_extracted()]] - code - graphify-repo/tests/test_extract.py
- [[test_calls_edges_emitted()]] - code - graphify-repo/tests/test_extract.py
- [[test_calls_no_self_loops()]] - code - graphify-repo/tests/test_extract.py
- [[test_collect_files_follows_symlinked_directory()]] - code - graphify-repo/tests/test_extract.py
- [[test_collect_files_from_dir()]] - code - graphify-repo/tests/test_extract.py
- [[test_collect_files_handles_circular_symlinks()]] - code - graphify-repo/tests/test_extract.py
- [[test_collect_files_skips_hidden()]] - code - graphify-repo/tests/test_extract.py
- [[test_extract.py]] - code - graphify-repo/tests/test_extract.py
- [[test_extract_merges_multiple_files()]] - code - graphify-repo/tests/test_extract.py
- [[test_extract_python_finds_class()]] - code - graphify-repo/tests/test_extract.py
- [[test_extract_python_finds_methods()]] - code - graphify-repo/tests/test_extract.py
- [[test_extract_python_no_dangling_edges()]] - code - graphify-repo/tests/test_extract.py
- [[test_make_id_consistent()]] - code - graphify-repo/tests/test_extract.py
- [[test_make_id_no_leading_trailing_underscores()]] - code - graphify-repo/tests/test_extract.py
- [[test_make_id_strips_dots_and_underscores()]] - code - graphify-repo/tests/test_extract.py
- [[test_method_calls_module_function()]] - code - graphify-repo/tests/test_extract.py
- [[test_no_dangling_edges_on_extract()]] - code - graphify-repo/tests/test_extract.py
- [[test_run_analysis_calls_compute_score()]] - code - graphify-repo/tests/test_extract.py
- [[test_run_analysis_calls_normalize()]] - code - graphify-repo/tests/test_extract.py
- [[test_structural_edges_are_extracted()]] - code - graphify-repo/tests/test_extract.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_37
SORT file.name ASC
```
