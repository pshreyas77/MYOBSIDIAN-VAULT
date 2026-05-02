---
type: community
cohesion: 0.11
members: 27
---

# Community 44

**Cohesion:** 0.11 - loosely connected
**Members:** 27 nodes

## Members
- [[AMBIGUOUS edge should score higher than an otherwise identical EXTRACTED edge.]] - rationale - graphify-repo/tests/test_analyze.py
- [[Code↔paper edge should score higher than code↔code edge.]] - rationale - graphify-repo/tests/test_analyze.py
- [[Concept nodes (empty source_file) must not appear in surprises.]] - rationale - graphify-repo/tests/test_analyze.py
- [[Helper build a small nx.Graph from nodeedge specs.]] - rationale - graphify-repo/tests/test_analyze.py
- [[Multi-file graph should find cross-file edges between real entities.]] - rationale - graphify-repo/tests/test_analyze.py
- [[Single-file graph should return cross-community edges, not empty list.]] - rationale - graphify-repo/tests/test_analyze.py
- [[Tests for analyze.py.]] - rationale - graphify-repo/tests/test_analyze.py
- [[_make_simple_graph()]] - code - graphify-repo/tests/test_analyze.py
- [[make_graph()_1]] - code - graphify-repo/tests/test_analyze.py
- [[test_analyze.py]] - code - graphify-repo/tests/test_analyze.py
- [[test_file_category()]] - code - graphify-repo/tests/test_analyze.py
- [[test_god_nodes_have_required_keys()]] - code - graphify-repo/tests/test_analyze.py
- [[test_god_nodes_returns_list()]] - code - graphify-repo/tests/test_analyze.py
- [[test_god_nodes_sorted_by_degree()]] - code - graphify-repo/tests/test_analyze.py
- [[test_graph_diff_empty_diff()]] - code - graphify-repo/tests/test_analyze.py
- [[test_graph_diff_new_edges()]] - code - graphify-repo/tests/test_analyze.py
- [[test_graph_diff_new_nodes()]] - code - graphify-repo/tests/test_analyze.py
- [[test_graph_diff_removed_nodes()]] - code - graphify-repo/tests/test_analyze.py
- [[test_is_concept_node_empty_source()]] - code - graphify-repo/tests/test_analyze.py
- [[test_is_concept_node_real_file()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_ambiguous_scores_higher_than_extracted()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_cross_source_multi_file()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_cross_type_scores_higher()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_excludes_concept_nodes()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_have_required_keys()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_have_why_field()]] - code - graphify-repo/tests/test_analyze.py
- [[test_surprising_connections_single_file_uses_community_bridges()]] - code - graphify-repo/tests/test_analyze.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_44
SORT file.name ASC
```
