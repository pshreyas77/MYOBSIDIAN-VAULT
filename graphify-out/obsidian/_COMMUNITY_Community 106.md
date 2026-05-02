---
type: community
cohesion: 0.26
members: 13
---

# Community 106

**Cohesion:** 0.26 - loosely connected
**Members:** 13 nodes

## Members
- [[End-to-end pipeline test detect → extract → build → cluster → analyze → report]] - rationale - graphify-repo/tests/test_pipeline.py
- [[Run the full pipeline on the fixtures directory. Returns a dict of outputs.]] - rationale - graphify-repo/tests/test_pipeline.py
- [[Second run on unchanged corpus should produce identical nodeedge counts.]] - rationale - graphify-repo/tests/test_pipeline.py
- [[run_pipeline()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline.py]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_all_nodes_have_community()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_detection_finds_code_and_docs()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_extraction_confidence_labels()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_graph_has_edges()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_incremental_update()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_no_self_loops()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_report_mentions_top_god_node()]] - code - graphify-repo/tests/test_pipeline.py
- [[test_pipeline_runs_end_to_end()]] - code - graphify-repo/tests/test_pipeline.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_106
SORT file.name ASC
```
