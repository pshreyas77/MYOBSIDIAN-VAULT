"""History Watchdog Scout Run — 2026-08-10.
Primary source: OpenAlex API (free, no auth).
All 24 queries from queries.yaml.
"""
import json, urllib.request, urllib.parse, sys, os
from datetime import date

today = date.today().isoformat()
vault = "E:/_Knowledge/ObsidianVault"
out_dir = f"{vault}/03 - PROJECTS/History-Watchdog/raw"
os.makedirs(out_dir, exist_ok=True)

# All 24 queries from queries.yaml (or queries specifically named there)
queries_by_cat = {
    "aryan_migration": [
        ("ancient DNA South Asia genome", 8),
        ("Rakhigarhi genome India genetics analysis", 5),
        ("Indus Valley Civilization ancient DNA Harappan", 6),
        ("steppe ancestry South Asia India Bronze Age", 5),
        ("Indo-Aryan migration linguistics archaeology", 4),
        ("Mitanni Indo-Iranian Anatolia Bronze Age treaty", 2),
        ("Harappan genetics migration ancient DNA", 5),
        ("South Asia Bronze Age archaeology genetics", 4),
    ],
    "dravidian_politics": [
        ("Dravidian politics Tamil Nadu", 8),
        ("DMK AIADMK election Tamil Nadu", 6),
        ("Tamil Nadu reservation policy OBC internal quota", 4),
        ("Justice Party Dravidian movement non-Brahmin", 3),
        ("Periyar EV Ramasamy biography scholarship", 3),
        ("Dravidian ideology Tamil nationalism identity", 4),
        ("Tamil Nadu caste politics social movements", 5),
        ("Ambedkar Periyar relationship anti-Brahmin", 3),
    ],
    "rss_hindutva": [
        ("RSS Rashtriya Swayamsevak Sangh funding finance", 5),
        ("Sangh Parivar diaspora funding Hindu American", 4),
        ("BJP South India strategy Tamil Nadu Kerala", 5),
        ("Hindutva organization ideology scholarship", 4),
        ("Sewa International diaspora funding Hindu", 2),
        ("Bhutada foundation RSS India funding", 2),
    ],
    "anti_caste": [
        ("Shramana tradition Buddhism Jainism India", 4),
        ("anti-caste movement India new research scholarship", 5),
        ("Buddhism Dalit conversion India scholarship", 4),
        ("Seva International Hindu diaspora funding India", 2),
    ],
}

tier1_venues = {
    "Science", "Cell", "Nature", "Nature Genetics", "PNAS",
    "Current Biology", "American Journal of Human Genetics", "PLOS Genetics",
    "Nature Ecology & Evolution", "Nature Communications", "Scientific Data",
    "Nature Human Behaviour", "Cell Reports",
}
tier2_venues = {
    "Annual Review of Linguistics", "Journal of South Asian Studies",
    "Economic and Political Weekly", "Modern Asian Studies",
    "Journal of Asian Studies", "Cambridge Archaeological Journal",
    "South Asia Multidisciplinary Academic Journal", "Studies in History",
    "Indian Economic and Social History Review",
}


def oa_search(query, limit, year_from=2024, year_to=2026):
    """OpenAlex works search. Returns (total_matched, papers_list)."""
    url = (
        f"https://api.openalex.org/works?"
        f"search={urllib.parse.quote(query)}"
        f"&filter=publication_year:{year_from}-{year_to}"
        f"&per-page={limit}&sort=relevance_score:desc"
    )
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read())
        count = data.get('meta', {}).get('count', 0)
        papers = []
        for p in data.get('results', [])[:limit]:
            loc = p.get('primary_location') or {}
            src = (loc.get('source') or {}).get('display_name') or '?'
            authors = [
                (a.get('author') or {}).get('display_name', '?')
                for a in (p.get('authorships') or [])[:3]
            ]
            abst_inv = p.get('abstract_inverted_index') or {}
            if abst_inv:
                max_pos = max(max(positions) for positions in abst_inv.values())
                words = [''] * (max_pos + 1)
                for word, positions in abst_inv.items():
                    for pos in positions:
                        words[pos] = word
                abstract = ' '.join(w for w in words if w)[:300]
            else:
                abstract = ''
            papers.append({
                "title": p.get('title') or '?',
                "year": p.get('publication_year') or '?',
                "venue": src,
                "cited_by": p.get('cited_by_count') or 0,
                "doi": p.get('doi') or '?',
                "authors": authors,
                "abstract": abstract,
                "openalex_id": p.get('id'),
                "type": p.get('type'),
            })
        return count, papers
    except Exception as e:
        print(f"ERR '{query[:40]}': {e}", file=sys.stderr)
        return 0, []


# Run all queries
results = {}
all_papers = []
for cat, qs in queries_by_cat.items():
    cat_results = []
    total = 0
    for q, lim in qs:
        cnt, papers = oa_search(q, lim)
        total += cnt
        for p in papers:
            p['query'] = q
            p['source'] = 'OpenAlex'
            p['category'] = cat
        cat_results.append({'query': q, 'total_results': cnt, 'papers': papers})
        all_papers.extend(papers)
    results[cat] = {'queries_run': len(qs), 'total_matched': total, 'data': cat_results}
    print(f"{cat}: {total} matched across {len(qs)} queries", file=sys.stderr)

print(f"\nTotal papers (with dups): {len(all_papers)}", file=sys.stderr)

# Dedup by openalex_id
seen = set()
deduped = []
for p in all_papers:
    oid = p.get('openalex_id')
    if oid:
        if oid in seen:
            continue
        seen.add(oid)
    deduped.append(p)
print(f"After dedup: {len(deduped)}", file=sys.stderr)


# Tier classification — STRICT: exact equality or canonical-prefix match
# (avoids spurious matches like "International Journal of ... Science and Management" → Nature/Science).
def tier_of(venue):
    if not venue or venue == '?':
        return None
    v = venue.strip()
    for t in tier1_venues:
        if v == t or v.startswith(t + " "):
            return 'tier1'
    for t in tier2_venues:
        if v == t or v.startswith(t + " "):
            return 'tier2'
    return 'tier3'


for p in deduped:
    p['tier'] = tier_of(p.get('venue', '?'))

tier1_papers = [p for p in deduped if p['tier'] == 'tier1']
tier2_papers = [p for p in deduped if p['tier'] == 'tier2']

# Save intermediate
with open(f"{out_dir}/temp_papers_2026-08-10.json", "w", encoding="utf-8", errors="replace") as f:
    json.dump({
        "deduped": deduped,
        "tier1": tier1_papers,
        "tier2": tier2_papers,
        "results_by_cat": results,
    }, f, ensure_ascii=False, indent=2)

print(f"\nTier1: {len(tier1_papers)} | Tier2: {len(tier2_papers)}", file=sys.stderr)
print(f"Queries attempted: {sum(len(v) for v in queries_by_cat.values())}")
print(f"Categories: {list(queries_by_cat.keys())}")
