---
type: community
cohesion: 0.04
members: 72
---

# Community 17

**Cohesion:** 0.04 - loosely connected
**Members:** 72 nodes

## Members
- [[A .graphifyignore at the git repo root is included when scanning a subdir.]] - rationale - graphify-repo/tests/test_detect.py
- [[A .graphifyignore in a parent directory applies to subdirectory scans.]] - rationale - graphify-repo/tests/test_detect.py
- [[A .md file with enough paper signals should classify as PAPER.]] - rationale - graphify-repo/tests/test_detect.py
- [[A plain .md file without paper signals should stay DOCUMENT.]] - rationale - graphify-repo/tests/test_detect.py
- [[Comment lines in .graphifyignore are not treated as patterns.]] - rationale - graphify-repo/tests/test_detect.py
- [[Convert a .docx file to markdown text using python-docx.]] - rationale - graphify-repo/graphify/detect.py
- [[Convert a .docx or .xlsx to a markdown sidecar in out_dir.      Returns the path]] - rationale - graphify-repo/graphify/detect.py
- [[Convert an .xlsx file to markdown text using openpyxl.]] - rationale - graphify-repo/graphify/detect.py
- [[Extract plain text from a PDF file using pypdf.]] - rationale - graphify-repo/graphify/detect.py
- [[FileType]] - code - graphify-repo/graphify/detect.py
- [[Files matching .graphifyignore patterns are excluded from detect().]] - rationale - graphify-repo/tests/test_detect.py
- [[Heuristic does this text file read like an academic paper]] - rationale - graphify-repo/graphify/detect.py
- [[Like detect(), but returns only new or modified files since the last run.      C]] - rationale - graphify-repo/graphify/detect.py
- [[Load the file modification time manifest from a previous run.]] - rationale - graphify-repo/graphify/detect.py
- [[No .graphifyignore is not an error.]] - rationale - graphify-repo/tests/test_detect.py
- [[Read .graphifyignore from root and ancestor directories.      Returns a list]] - rationale - graphify-repo/graphify/detect.py
- [[Return True if path matches any .graphifyignore pattern.]] - rationale - graphify-repo/graphify/detect.py
- [[Return True if this directory name looks like a venv, cache, or dep dir.]] - rationale - graphify-repo/graphify/detect.py
- [[Return True if this file likely contains secrets and should be skipped.]] - rationale - graphify-repo/graphify/detect.py
- [[Save current file mtimes so the next --update run can diff against them.]] - rationale - graphify-repo/graphify/detect.py
- [[The real attention paper file should be classified as PAPER.]] - rationale - graphify-repo/tests/test_detect.py
- [[Upward search stops at the git repo root (.git directory).]] - rationale - graphify-repo/tests/test_detect.py
- [[Video and audio file extensions should classify as VIDEO.]] - rationale - graphify-repo/tests/test_detect.py
- [[Video files do not contribute to total_words.]] - rationale - graphify-repo/tests/test_detect.py
- [[_is_ignored()]] - code - graphify-repo/graphify/detect.py
- [[_is_noise_dir()]] - code - graphify-repo/graphify/detect.py
- [[_is_sensitive()]] - code - graphify-repo/graphify/detect.py
- [[_load_graphifyignore()]] - code - graphify-repo/graphify/detect.py
- [[_looks_like_paper()]] - code - graphify-repo/graphify/detect.py
- [[classify_file()]] - code - graphify-repo/graphify/detect.py
- [[convert_office_file()]] - code - graphify-repo/graphify/detect.py
- [[count_words()]] - code - graphify-repo/graphify/detect.py
- [[detect()]] - code - graphify-repo/graphify/detect.py
- [[detect() correctly counts video files and does not add them to word count.]] - rationale - graphify-repo/tests/test_detect.py
- [[detect() result always includes a 'video' key even with no video files.]] - rationale - graphify-repo/tests/test_detect.py
- [[detect.py]] - code - graphify-repo/graphify/detect.py
- [[detect_incremental()]] - code - graphify-repo/graphify/detect.py
- [[docx_to_markdown()]] - code - graphify-repo/graphify/detect.py
- [[extract_pdf_text()]] - code - graphify-repo/graphify/detect.py
- [[load_manifest()]] - code - graphify-repo/graphify/detect.py
- [[save_manifest()]] - code - graphify-repo/graphify/detect.py
- [[str]] - code
- [[test_classify_attention_paper()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_image()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_markdown()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_md_doc_without_signals()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_md_paper_by_signals()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_pdf()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_pdf_in_xcassets_root_skipped()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_pdf_in_xcassets_skipped()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_python()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_typescript()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_unknown_returns_none()]] - code - graphify-repo/tests/test_detect.py
- [[test_classify_video_extensions()]] - code - graphify-repo/tests/test_detect.py
- [[test_count_words_sample_md()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect.py]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_finds_fixtures()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_finds_video_files()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_follows_symlinked_directory()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_follows_symlinked_file()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_handles_circular_symlinks()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_includes_video_key()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_skips_dotfiles()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_video_not_in_words()]] - code - graphify-repo/tests/test_detect.py
- [[test_detect_warns_small_corpus()]] - code - graphify-repo/tests/test_detect.py
- [[test_graphifyignore_at_git_root_is_included()]] - code - graphify-repo/tests/test_detect.py
- [[test_graphifyignore_comments_ignored()]] - code - graphify-repo/tests/test_detect.py
- [[test_graphifyignore_discovered_from_parent()]] - code - graphify-repo/tests/test_detect.py
- [[test_graphifyignore_excludes_file()]] - code - graphify-repo/tests/test_detect.py
- [[test_graphifyignore_missing_is_fine()]] - code - graphify-repo/tests/test_detect.py
- [[test_graphifyignore_stops_at_git_boundary()]] - code - graphify-repo/tests/test_detect.py
- [[xlsx_to_markdown()]] - code - graphify-repo/graphify/detect.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_17
SORT file.name ASC
```

## Connections to other communities
- 3 edges to [[_COMMUNITY_Community 12]]

## Top bridge nodes
- [[detect.py]] - degree 17, connects to 1 community
- [[FileType]] - degree 16, connects to 1 community
- [[str]] - degree 9, connects to 1 community