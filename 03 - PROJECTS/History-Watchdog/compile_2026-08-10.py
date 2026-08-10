"""Compile final scout JSON for 2026-08-10 run."""
import json, os

vault = "E:/_Knowledge/ObsidianVault"
src = f"{vault}/03 - PROJECTS/History-Watchdog/raw/temp_papers_2026-08-10.json"
out = f"{vault}/03 - PROJECTS/History-Watchdog/raw/2026-08-10-scout.json"

with open(src, encoding="utf-8") as f:
    data = json.load(f)

deduped = data["deduped"]
tier1 = data["tier1"]
tier2 = data["tier2"]
by_cat_results = data["results_by_cat"]


def slim(p):
    return {
        "title": p["title"],
        "year": p["year"],
        "venue": p["venue"],
        "cited_by": p["cited_by"],
        "doi": p["doi"],
        "authors": p["authors"],
        "abstract": p.get("abstract", "")[:250],
        "tier": p.get("tier"),
    }


output = {
    "run_date": "2026-08-10",
    "queries_run": sum(v["queries_run"] for v in by_cat_results.values()),
    "papers_found": len(deduped),
    "by_category": {},
    "tier1_papers": [],
    "notes": (
        "OpenAlex API used as primary source (free, no auth). "
        "Browser-based tools (Elicit.com, Undermind.ai, chat.deepseek.com, "
        "kimi.com) attempted but require login or hit Cloudflare bot-block; "
        "not viable for headless/cron execution. "
        "All 26 queries from queries.yaml were attempted (vs. 16 in prior run). "
        "Mitanni query (try-fix) still returned no relevant IVC papers but did "
        "surface Bronze-Age/Mesopotamia items so retained. "
        "Tier1 papers filtered by venue (Nature/Cell/Science/etc.). "
        "Anti-caste now returns 4-5 relevant items vs. 0 prior run."
    ),
}

for cat in ["aryan_migration", "dravidian_politics", "rss_hindutva", "anti_caste"]:
    info = by_cat_results[cat]
    cat_papers = [p for p in deduped if p.get("category") == cat]
    # Top papers: tier1 first, then tier2, then tier3, by citations desc
    cat_papers_sorted = sorted(
        cat_papers,
        key=lambda p: (
            0 if p.get("tier") == "tier1" else (1 if p.get("tier") == "tier2" else 2),
            -p.get("cited_by", 0),
        ),
    )
    output["by_category"][cat] = {
        "queries": info["queries_run"],
        "papers": len(cat_papers),
        "total_matched_openalex": info["total_matched"],
        "top_papers": [slim(p) for p in cat_papers_sorted[:5]],
    }

# Tier1 papers (top by citations)
tier1_sorted = sorted(tier1, key=lambda p: -p.get("cited_by", 0))
output["tier1_papers"] = [slim(p) for p in tier1_sorted[:15]]

# Add cross-cutting: which papers cover the user's priority research targets?
# Find anything mentioning IVC, Rakhigarhi, Periyar, Justice Party, RSS, Shramana
keywords_priority = {
    "IVC/Rakhigarhi": ["rakhigarhi", "indus valley", "harappan"],
    "Periyar/Justice Party": ["periyar", "justice party", "dravidian movement", "non-brahmin"],
    "RSS/Hindutva": ["rashtriya swayamsevak", "sangh parivar", "hindutva", "sewa international", "bjp south"],
    "Shramana/Buddhist/Dalit": ["shramana", "dalit", "anti-caste", "buddhist conversion"],
}
highlights = {}
for label, kws in keywords_priority.items():
    matches = []
    for p in deduped:
        text = (p["title"] + " " + p.get("abstract", "")).lower()
        if any(k in text for k in kws):
            matches.append(slim(p))
    if matches:
        matches.sort(key=lambda p: -p.get("cited_by", 0))
        highlights[label] = matches[:3]

output["priority_research_hits"] = highlights

with open(out, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"WROTE: {out}")
print(f"Papers: {output['papers_found']} | Tier1: {len(output['tier1_papers'])} | Queries: {output['queries_run']}")
for cat, info in output["by_category"].items():
    print(f"  {cat}: {info['papers']} papers (top: {info['top_papers'][0]['title'][:60]})")
