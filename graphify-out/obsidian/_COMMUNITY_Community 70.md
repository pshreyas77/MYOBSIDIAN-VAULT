---
type: community
cohesion: 0.14
members: 18
---

# Community 70

**Cohesion:** 0.14 - loosely connected
**Members:** 18 nodes

## Members
- [[AMBIGUOUS edges must have confidence_score = 0.4.]] - rationale - graphify-repo/tests/test_confidence.py
- [[EXTRACTED edges must have confidence_score == 1.0.]] - rationale - graphify-repo/tests/test_confidence.py
- [[Edges lacking confidence_score get sensible defaults in to_json.]] - rationale - graphify-repo/tests/test_confidence.py
- [[INFERRED edges must have confidence_score between 0.0 and 1.0.]] - rationale - graphify-repo/tests/test_confidence.py
- [[Report summary line should include avg confidence for INFERRED edges.]] - rationale - graphify-repo/tests/test_confidence.py
- [[Return a minimal extraction dict with one edge of each confidence type.]] - rationale - graphify-repo/tests/test_confidence.py
- [[Surprising connections section shows confidence score next to INFERRED edges.]] - rationale - graphify-repo/tests/test_confidence.py
- [[Tests for confidence_score on edges.]] - rationale - graphify-repo/tests/test_confidence.py
- [[_make_extraction()]] - code - graphify-repo/tests/test_confidence.py
- [[confidence_score survives build_from_json → to_json → JSON parse round-trip.]] - rationale - graphify-repo/tests/test_confidence.py
- [[test_ambiguous_edges_score_at_most_04()]] - code - graphify-repo/tests/test_confidence.py
- [[test_confidence.py]] - code - graphify-repo/tests/test_confidence.py
- [[test_confidence_score_round_trip()]] - code - graphify-repo/tests/test_confidence.py
- [[test_extracted_edges_have_score_1()]] - code - graphify-repo/tests/test_confidence.py
- [[test_inferred_edges_score_in_range()]] - code - graphify-repo/tests/test_confidence.py
- [[test_report_inferred_tag_with_score()]] - code - graphify-repo/tests/test_confidence.py
- [[test_report_shows_avg_confidence_for_inferred()]] - code - graphify-repo/tests/test_confidence.py
- [[test_to_json_defaults_missing_confidence_score()]] - code - graphify-repo/tests/test_confidence.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_70
SORT file.name ASC
```
