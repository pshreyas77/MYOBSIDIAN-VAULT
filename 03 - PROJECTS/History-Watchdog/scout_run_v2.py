import json, urllib.request, urllib.parse, sys, os

out_path = "E:/_Knowledge/ObsidianVault/03 - PROJECTS/History-Watchdog/raw/2026-07-14-scout.json"

categories = {
    "aryan_migration": [
        ("ancient DNA South Asia genome 2024", 8),
        ("Rakhigarhi genome India genetics 2024", 5),
        ("Indus Valley Civilization ancient DNA 2024", 6),
        ("steppe ancestry South Asia India genetics 2024", 5),
        ("Indo-Aryan migration linguistics archaeology 2024", 4),
        ("Harappan genetics migration ancient DNA 2024", 5),
        ("South Asia Bronze Age archaeology genetics 2024", 4),
    ],
    "dravidian_politics": [
        ("Dravidian politics Tamil Nadu 2024 2025", 5),
        ("Tamil Nadu reservation policy OBC 2024", 4),
        ("Justice Party Dravidian Periyar 2024", 3),
        ("Tamil Nadu caste politics social movements 2024", 4),
    ],
    "rss_hindutva": [
        ("RSS Sangh Parivar funding diaspora Hindutva 2024", 5),
        ("BJP South India election strategy 2025", 4),
        ("Sewa International Hindu funding 2024", 3),
    ],
    "anti_caste": [
        ("Shramana Buddhist Jain anti-caste India 2024", 4),
        ("Buddhism Dalit India empowerment 2024", 4),
    ]
}

def search_oa(query, limit):
    url = f"https://api.openalex.org/works?search={urllib.parse.quote(query)}&filter=publication_year:2024-2026&per-page={limit}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read())
        count = data.get('meta',{}).get('count',0)
        papers = []
        for p in data.get('results',[])[:limit]:
            loc = p.get('primary_location') or {}
            src = (loc.get('source') or {}).get('display_name') or '?'
            authors = [(a.get('author') or {}).get('display_name','?') for a in p.get('authorships',[])[:3]]
            papers.append({
                "title": p.get('title','?'),
                "year": p.get('publication_year','?'),
                "venue": src,
                "cited_by": p.get('cited_by_count',0),
                "doi": p.get('doi','?'),
                "authors": authors,
                "abstract": (p.get('abstract') or '')[:200]
            })
        return count, papers
    except Exception as e:
        print(f"ERR {query[:40]}: {e}", file=sys.stderr)
        return 0, []

results = {}
all_papers = []
for cat, queries in categories.items():
    cat_results = []
    total = 0
    for q, lim in queries:
        cnt, pprs = search_oa(q, lim)
        total += cnt
        for p in pprs:
            p['query'] = q
            p['source'] = 'OpenAlex'
        cat_results.append({'query': q, 'total_results': cnt, 'papers': pprs})
        all_papers.extend(pprs)
        print(f"  {cat}: {q[:50]} -> {len(pprs)} papers (matched: {cnt})", file=sys.stderr)
    results[cat] = {'queries_run': len(queries), 'data': cat_results, 'total_matched': total}

print(f"\nTotal papers: {len(all_papers)}", file=sys.stderr)

tier1_venues = {"Science","Cell","Nature","Nature Genetics","PNAS","Current Biology","American Journal of Human Genetics","PLOS Genetics","Nature Ecology & Evolution","Nature Communications","Scientific Data"}

tier1_papers = []
output = {
    "run_date": "2026-07-14",
    "queries_run": sum(len(v) for v in categories.values()),
    "papers_found": len(all_papers),
    "by_category": {},
    "notes": "OpenAlex API used as primary source. Elicit.org requires login. Undermind.ai/DeepSeek.com unreachable via browser. Perplexity blocked by Cloudflare. Kimi.com requires login. Semantic Scholar returning 405 errors. 2 queries returned NoneType errors (political category)."
}

for cat, v in results.items():
    cat_papers = []
    for r in v['data']:
        for p in r['papers']:
            vp = p.copy()
            is_t1 = any(t in vp.get('venue','?') for t in tier1_venues)
            vp['is_tier1'] = is_t1
            if is_t1:
                tier1_papers.append(vp)
            cat_papers.append(vp)
    top = sorted([p for p in cat_papers if p.get('cited_by',0) > 3], key=lambda x: x.get('cited_by',0), reverse=True)[:5]
    output['by_category'][cat] = {
        'queries': v['queries_run'], 'papers': len(cat_papers),
        'top_papers': [{'title':t['title'],'year':t['year'],'venue':t['venue'],'cited_by':t['cited_by'],'doi':t['doi'],'authors':t['authors']} for t in top]
    }

output['tier1_papers'] = [{'title':p['title'],'year':p['year'],'venue':p['venue'],'cited_by':p['cited_by'],'doi':p['doi'],'authors':p['authors']} for p in tier1_papers[:10]]
output['notes'] += f" | Tier1 papers: {len(tier1_papers)}"

with open(out_path, 'w', encoding='utf-8', errors='replace') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
print(f"SAVED: {out_path}", file=sys.stderr)
print(json.dumps({"saved": True, "papers": len(all_papers), "tier1": len(tier1_papers)}))