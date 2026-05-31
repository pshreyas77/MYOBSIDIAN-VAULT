# Graph Report - ./BUDDHA  (2026-04-11)

## Corpus Check
- 1 files · ~14,000 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 15 nodes · 16 edges · 6 communities detected
- Extraction: 94% EXTRACTED · 6% INFERRED · 0% AMBIGUOUS · INFERRED: 1 edges (avg confidence: 0.8)
- Token cost: 3,619 input · 6,569 output

## God Nodes (most connected - your core abstractions)
1. `Tibetan Library Buddhism Research Compilation` - 10 edges
2. `Sakya Monastery` - 2 edges
3. `Ashoka's Pillars` - 2 edges
4. `Prakrit Language` - 2 edges
5. `Buddha as Vishnu Avatar` - 2 edges
6. `Pushyamitra Shunga` - 2 edges
7. `Adi Shankaracharya` - 2 edges
8. `Sam Dam Dand Bhed` - 2 edges
9. `Temple Conversions` - 2 edges
10. `Nalanda Destruction` - 1 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Communities

### Community 0 - "Ashoka & Language Evidence"
Cohesion: 0.5
Nodes (5): BR Ambedkar Analysis, Ashoka's Pillars, Nalanda Destruction, Prakrit Language, Tibetan Library Buddhism Research Compilation

### Community 1 - "Tibetan Library & Texts"
Cohesion: 1.0
Nodes (2): Buddhist Texts, Sakya Monastery

### Community 2 - "Persecution & Revivalism"
Cohesion: 1.0
Nodes (2): Buddhism Decline, Pushyamitra Shunga

### Community 3 - "Community 3"
Cohesion: 1.0
Nodes (2): Brahmanical Strategy, Sam Dam Dand Bhed

### Community 4 - "Persecution & Revivalism"
Cohesion: 1.0
Nodes (2): Adi Shankaracharya, Temple Conversions

### Community 5 - "Community 5"
Cohesion: 1.0
Nodes (2): Brahmanical Persecution, Buddha as Vishnu Avatar

## Knowledge Gaps
- **6 isolated node(s):** `Nalanda Destruction`, `BR Ambedkar Analysis`, `Brahmanical Persecution`, `Buddhism Decline`, `Brahmanical Strategy` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **Thin community `Tibetan Library & Texts`** (2 nodes): `Buddhist Texts`, `Sakya Monastery`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Persecution & Revivalism`** (2 nodes): `Buddhism Decline`, `Pushyamitra Shunga`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 3`** (2 nodes): `Brahmanical Strategy`, `Sam Dam Dand Bhed`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Persecution & Revivalism`** (2 nodes): `Adi Shankaracharya`, `Temple Conversions`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.
- **Thin community `Community 5`** (2 nodes): `Brahmanical Persecution`, `Buddha as Vishnu Avatar`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Tibetan Library Buddhism Research Compilation` connect `Ashoka & Language Evidence` to `Tibetan Library & Texts`, `Persecution & Revivalism`, `Community 3`, `Persecution & Revivalism`, `Community 5`?**
  _High betweenness centrality (0.934) - this node is a cross-community bridge._
- **Why does `Sakya Monastery` connect `Tibetan Library & Texts` to `Ashoka & Language Evidence`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **Why does `Buddha as Vishnu Avatar` connect `Community 5` to `Ashoka & Language Evidence`?**
  _High betweenness centrality (0.143) - this node is a cross-community bridge._
- **What connects `Nalanda Destruction`, `BR Ambedkar Analysis`, `Brahmanical Persecution` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._