#!/usr/bin/env python3
"""Audit Run — Week 2026-W33 (2026-08-16)
Comprehensive vault health scan: duplicates, orphans, broken links, missing frontmatter, stale claims, quality sampling.
"""
import os
import re
import json
from pathlib import Path
from collections import defaultdict, Counter
from datetime import datetime, timedelta

VAULT_ROOT = Path(r"E:\_Knowledge\ObsidianVault")
TODAY = datetime(2026, 8, 16)
SIX_MONTHS_AGO = TODAY - timedelta(days=183)  # 2026-02-14

# Directories to scan
SCAN_DIRS = [
    "2-atoms",
    "02 - PERMANENT",
    "wiki",
    "01 - LITERATURE",
    "03 - PROJECTS",
    "05 - MAPS",
    "04 - DAILY",
    "Daily Notes",
    "0-raw",
    "1-desk",
    "06 - OUTPUTS",
    "07 - SYSTEM",
]

# Skip these (generated/temp/tooling)
SKIP_DIRS = {
    ".git", ".obsidian", ".smart-env", ".qwen", ".ua", "node_modules",
    "genericagent", "temp_autoresearch", "QwenVault", "ruflo",
    "agentic-os", "GitNexus", "tolaria", "Understand-Anything",
    "SafeBrain", "project_OB__AI", "autoresearch", "graphify-repo",
    "graphify-out", "pegasus", "all canvas", "philsophy-website",
    "philosophy-website", "Knowledge", "%SystemDrive%",
    ".openclaude", ".opencode", ".claude", ".claude-plugin", ".raw",
}

results = {
    "total_files": 0,
    "files_scanned": 0,
    "files_with_frontmatter": 0,
    "files_missing_frontmatter": [],
    "all_wikilinks": [],          # (source_path, target)
    "all_notes": [],              # list of (path, title)
    "orphan_candidates": [],      # 0 incoming, 7+ days old
    "broken_links": [],
    "stale_claims": [],
    "quarantine_atoms": [],
    "duplicates": [],
    "link_counts": defaultdict(int),  # target -> number of incoming links
    "wikilinks_per_file": defaultdict(list),
}

# Recency marker regex
RECENCY_RE = re.compile(r"\(as of (\d{4})-(\d{2})(?:,\s*([^)]+))?\)")
FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)

# Stale claim indicators
STALE_PATTERNS = [
    (re.compile(r"\bis\s+(?:the\s+)?(?:CEO|founder|president|director|chairman)\b", re.IGNORECASE), "role"),
    (re.compile(r"\b(?:works?|working)\s+(?:at|for)\s+", re.IGNORECASE), "role"),
    (re.compile(r"\b(?:raised|funding|valuation|valued at)\s+\$", re.IGNORECASE), "funding"),
    (re.compile(r"\b(?:has\s+\d+[KMB]?\s+(?:users|customers|downloads))", re.IGNORECASE), "number"),
    (re.compile(r"\b(?:is\s+(?:currently|developing|building|launching))", re.IGNORECASE), "status"),
    (re.compile(r"\bChief Minister\b", re.IGNORECASE), "role"),
]

def should_skip(path: Path) -> bool:
    parts = set(path.parts)
    return bool(parts & SKIP_DIRS)

def parse_frontmatter(text: str):
    """Return (frontmatter_dict, body_start_idx) or ({}, 0)"""
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, 0
    fm_text = m.group(1)
    fm = {}
    for line in fm_text.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip()
    return fm, m.end()

def extract_wikilinks(text: str):
    """Extract [[Target]] or [[Target|alias]] or [[Target#Anchor]]"""
    links = re.findall(r"\[\[([^\]\|#]+)(?:#[^\]\|]+)?(?:\|[^\]]+)?\]\]", text)
    return [l.strip() for l in links if l.strip()]

def extract_title(path: Path, fm: dict) -> str:
    if "title" in fm:
        return fm["title"]
    return path.stem

def get_note_date(path: Path, fm: dict, text: str) -> datetime:
    """Best-effort note date."""
    for key in ("date", "created", "date_read"):
        if key in fm:
            try:
                return datetime.fromisoformat(fm[key])
            except (ValueError, TypeError):
                pass
    # Try first heading
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    if m:
        # Use file mtime as fallback
        pass
    try:
        return datetime.fromtimestamp(path.stat().st_mtime)
    except Exception:
        return TODAY

def has_future_claude_preamble(text: str) -> bool:
    return bool(re.search(r"##\s+For\s+future\s+Claude", text, re.IGNORECASE))

def has_confidence_marker(text: str, fm: dict) -> bool:
    """Check for confidence markers anywhere in frontmatter or text."""
    if "confidence" in fm:
        return True
    return bool(re.search(r"\b(?:stated|high|medium|speculation)\b\s+(?:confidence|conf)", text, re.IGNORECASE) or
                re.search(r"\(confidence:\s*(?:stated|high|medium|speculation)\)", text, re.IGNORECASE) or
                re.search(r"\bConfidence:\s*(?:stated|high|medium|speculation)\b", text, re.IGNORECASE))

def has_source_citation(text: str, fm: dict) -> bool:
    if "source" in fm:
        return True
    return bool(re.search(r"\bsource[:\s]", text, re.IGNORECASE) or
                re.search(r"\bhttps?://", text) or
                re.search(r"\[\[source", text, re.IGNORECASE))

def is_quarantine_atom(path: Path, text: str) -> bool:
    """Quarantine indicator: explicit filename marker OR house-rules violation."""
    name = path.name.lower()
    if "quarantine" in name or "no source cited" in name or "no source" in name:
        return True
    return False

def is_daily_note(path: Path) -> bool:
    name = path.name
    return bool(re.match(r"\d{4}-\d{2}-\d{2}", name)) or "Daily Notes" in path.parts

def is_literature(path: Path) -> bool:
    return "LITERATURE" in path.parts or "BOOKS" in path.parts or "Research" in path.parts

def main():
    # Phase 1: enumerate files
    print("Phase 1: Enumerating vault files...")
    all_md_files = []
    for p in VAULT_ROOT.rglob("*.md"):
        if should_skip(p):
            continue
        all_md_files.append(p)
    results["total_files"] = len(all_md_files)
    print(f"  Found {len(all_md_files)} markdown files")

    # Phase 2: parse files and extract metadata
    print("Phase 2: Parsing files...")
    note_titles = {}  # title (without extension) -> path
    note_data = []    # list of dicts per file

    for path in all_md_files:
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        results["files_scanned"] += 1

        fm, _ = parse_frontmatter(text)
        title = extract_title(path, fm)
        rel = path.relative_to(VAULT_ROOT)
        note_date = get_note_date(path, fm, text)

        data = {
            "path": str(rel),
            "abs": str(path),
            "title": title,
            "frontmatter": fm,
            "has_frontmatter": bool(fm),
            "date": note_date,
            "is_quarantine": is_quarantine_atom(path, text),
            "is_daily": is_daily_note(path),
            "is_literature": is_literature(path),
            "text_len": len(text),
            "text": text,
        }
        note_data.append(data)

        # Missing frontmatter check
        required_keys = {"date", "type", "ai-first"}
        if not fm or not required_keys.issubset(set(fm.keys())):
            results["files_missing_frontmatter"].append({
                "path": str(rel),
                "missing": list(required_keys - set(fm.keys())),
                "has_fm": bool(fm),
            })

        # Track for orphan detection
        if title not in note_titles:
            note_titles[title] = path

        # Extract wikilinks
        links = extract_wikilinks(text)
        for l in links:
            results["all_wikilinks"].append((str(rel), l))
            results["link_counts"][l] += 1
            results["wikilinks_per_file"][str(rel)].append(l)

        if data["is_quarantine"]:
            results["quarantine_atoms"].append({
                "path": str(rel),
                "title": title,
                "date": note_date.isoformat(),
            })

        results["all_notes"].append({
            "path": str(rel),
            "title": title,
            "date": note_date,
            "is_daily": data["is_daily"],
            "is_literature": data["is_literature"],
        })

    # Phase 3: detect broken links
    print("Phase 3: Detecting broken wikilinks...")
    titles_set = set(note_titles.keys())
    # Also normalize: strip path prefixes (e.g. wiki/concepts/X matches "X")
    title_paths_normalized = set()
    for t, p in note_titles.items():
        title_paths_normalized.add(t)
        # Also add filename without any path
        title_paths_normalized.add(p.stem)

    broken_seen = {}
    for source, target in results["all_wikilinks"]:
        # Skip section anchors
        clean_target = target.split("|")[0].strip()
        if not clean_target:
            continue
        # Strip path prefix if present
        basename = clean_target.split("/")[-1]
        if basename in titles_set or clean_target in titles_set:
            continue
        # Skip external links
        if "://" in clean_target or clean_target.startswith("http"):
            continue
        # Track broken
        key = clean_target
        if key not in broken_seen:
            broken_seen[key] = {"target": clean_target, "referenced_by": [], "occurrences": 0}
        broken_seen[key]["referenced_by"].append(source)
        broken_seen[key]["occurrences"] += 1
    results["broken_links"] = sorted(broken_seen.values(), key=lambda x: -x["occurrences"])

    # Phase 4: orphan detection (0 incoming, 7+ days old, not daily/literature)
    print("Phase 4: Detecting orphans...")
    cutoff = TODAY - timedelta(days=7)
    for note in results["all_notes"]:
        title = note["title"]
        # Count incoming via basename match
        incoming = results["link_counts"].get(title, 0)
        # Also check if title appears via path
        if incoming == 0:
            incoming = results["link_counts"].get(note["path"].replace("\\", "/"), 0)
        # Filter
        if incoming == 0 and note["date"] < cutoff and not note["is_daily"] and not note["is_literature"]:
            # Exclude system files
            if any(s in note["path"] for s in ("07 - SYSTEM", "Templates", "_templates", "BRIEFINGS", "playbooks", "Research/")):
                continue
            # Exclude stub files
            if "stub" in note["path"].lower() or note["path"].endswith(".md") and "Stub" in note["title"]:
                continue
            # Exclude root-level files
            if "/" not in note["path"]:
                continue
            results["orphan_candidates"].append({
                "path": note["path"],
                "title": title,
                "date": note["date"].isoformat(),
                "age_days": (TODAY - note["date"]).days,
            })

    # Phase 5: stale claim detection
    print("Phase 5: Scanning for stale claims...")
    for data in note_data:
        text = data["text"]
        rel = data["path"]
        note_date = data["date"]
        # Only check 6+ months old
        if note_date >= SIX_MONTHS_AGO:
            continue
        # Skip daily/system
        if data["is_daily"] or "SYSTEM" in rel:
            continue
        # Look for time-sensitive claims without recency markers
        lines = text.splitlines()
        for i, line in enumerate(lines, 1):
            for pat, claim_type in STALE_PATTERNS:
                if pat.search(line):
                    # Check for recency marker nearby (same line or +/-1 line)
                    window_start = max(0, i - 2)
                    window_end = min(len(lines), i + 2)
                    window_text = "\n".join(lines[window_start:window_end])
                    if RECENCY_RE.search(window_text):
                        continue
                    results["stale_claims"].append({
                        "path": rel,
                        "line": i,
                        "claim": line.strip()[:200],
                        "type": claim_type,
                        "note_date": note_date.isoformat(),
                        "age_days": (TODAY - note_date).days,
                    })
                    break  # one claim per line

    # Phase 6: duplicate detection (similar titles)
    print("Phase 6: Detecting duplicate titles...")
    title_counter = Counter(n["title"] for n in results["all_notes"])
    exact_dupes = {t: c for t, c in title_counter.items() if c > 1}
    results["duplicates"] = [{"title": t, "count": c} for t, c in sorted(exact_dupes.items(), key=lambda x: -x[1])]

    # Phase 7: quality sampling (10-15 random from key dirs)
    print("Phase 7: Quality sampling...")
    import random
    random.seed(42)
    sample_dirs = ["2-atoms", "02 - PERMANENT", "wiki"]
    candidates = [d for d in note_data
                  if any(s in d["path"] for s in sample_dirs)
                  and not d["is_quarantine"]
                  and d["path"].endswith(".md")]
    sample = random.sample(candidates, min(15, len(candidates)))
    quality_results = []
    for d in sample:
        text = d["text"]
        fm = d["frontmatter"]
        wikilinks = extract_wikilinks(text)
        quality_results.append({
            "path": d["path"],
            "has_source": has_source_citation(text, fm),
            "has_future_claude": has_future_claude_preamble(text),
            "wikilink_count": len(wikilinks),
            "has_confidence": has_confidence_marker(text, fm),
            "passes": (has_source_citation(text, fm) and
                      has_future_claude_preamble(text) and
                      len(wikilinks) >= 2 and
                      has_confidence_marker(text, fm)),
        })
    pass_count = sum(1 for q in quality_results if q["passes"])
    results["quality_score"] = {
        "sample_size": len(quality_results),
        "passed": pass_count,
        "score_pct": round(100 * pass_count / max(1, len(quality_results)), 1),
        "details": quality_results,
    }

    # Save raw results
    out_path = VAULT_ROOT / "scripts" / "audit_w33_results.json"
    # Convert datetime for JSON
    def serialize(o):
        if isinstance(o, (datetime,)):
            return o.isoformat()
        if isinstance(o, defaultdict):
            return dict(o)
        if isinstance(o, set):
            return list(o)
        raise TypeError(f"Not serializable: {type(o)}")

    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, default=serialize)

    # Print summary
    print("\n========= AUDIT SUMMARY =========")
    print(f"Total files: {results['total_files']}")
    print(f"Missing frontmatter: {len(results['files_missing_frontmatter'])}")
    print(f"Orphan candidates: {len(results['orphan_candidates'])}")
    print(f"Broken links: {len(results['broken_links'])}")
    print(f"Stale claims: {len(results['stale_claims'])}")
    print(f"Quality score: {results['quality_score']['score_pct']}% ({results['quality_score']['passed']}/{results['quality_score']['sample_size']})")
    print(f"Quarantine atoms: {len(results['quarantine_atoms'])}")
    print(f"Duplicate titles: {len(results['duplicates'])}")
    print(f"Results saved to: {out_path}")

if __name__ == "__main__":
    main()
