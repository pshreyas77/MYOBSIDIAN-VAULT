import json, urllib.request, urllib.parse, sys

vault = "E:/_Knowledge/ObsidianVault"
out_dir = f"{vault}/03 - PROJECTS/History-Watchdog/raw"

categories = {
    "aryan_migration": [
        ("ancient DNA South Asia genome 2024", 8),
        ("Rakhigarhi genome analysis India genetics 2024", 5),
        ("Indus Valley Civilization ancient DNA genetics 2024", 6),
        ("steppe ancestry South Asia India genetics 2024", 5),
        ("Indo-Aryan migration linguistics archaeology 2024", 4),
        ("Harappan genetics migration ancient DNA 2024", 5),
        ("South Asia Bronze Age archaeology genetics 2024", 4),
    ],
    "dravidian_politics": [
        ("Dravidian politics Tamil Nadu DMK AIADMK 2024 2025", 8),
        ("Tamil Nadu reservation policy OBC 2024 2025", 5),
        ("Justice Party Dravidian movement Periyar scholarship 2024", 4),
        ("Tamil Nadu caste politics social movements 2024 2025", 5),
    ],
    "rss_hindutva": [
        ("RSS Sangh Parivar funding diaspora Hindutva 2024 2025", 6),
        ("BJP South India election strategy 2024 2025", 5),
        ("Sewa International Hindu organization funding 2024", 4),
    ],
    "anti_caste": [
        ("Shramana Buddhist Jain anti-caste India scholarship 2024", 5),
        ("Buddhism Dalit empowerment India 2024 2025", 4),
    ]
}

results = {}
all_papers = []

def search_openalex(query, limit):
    url = f"https://api.openalex.org/works?search={urllib.parse.quote(query)}&filter=publication_year:2024-2026&per-page={limit}"
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            data = json.loads(r.read())
        count = data.get('meta', {}).get('count', 0)
        papers = []
        for p in data.get('results', [])[:limit]:
            title = p.get('title', '?')
            year = p.get('publication_year', '?')
            venue = p.get('primary_location', {}).get('source', {}).get('display_name', '?') or '?'
            cited = p.get('cited_by_count', 0)
            doi = p.get('doi', '?')
            authors = [a.get('author', {}).get('display_name', '?') for a in p.get('authorships', [])[:3]]
            abstract = (p.get('abstract') or '')[:200]
            papers.append({
                "title": title, "year": year, "venue": venue, "cited_by": cited,
                "doi": doi, "authors": authors[:3], "abstract": abstract,
                "query": query, "source": "OpenAlex"
            })
        return count, papers
    except Exception as e:
        print(f"ERROR for '{query}': {e}", file=sys.stderr)
        return 0, []

for cat, queries in categories.items():
    cat_results = []
    total_count = 0
    for query, limit in queries:
        count, papers = search_openalex(query, limit)
        total_count += count
        cat_results.append({"query": query, "total_results": count, "papers": papers})
        all_papers.extend(papers)
    results[cat] = {"queries_run": len(queries), "results": cat_results, "total_matched": total_count}

print("DONE. Total papers:", len(all_papers))
out = json.dumps({"results": results, "all_papers": all_papers}, indent=2)
with open(f"{out_dir}/temp_papers.json", "w", encoding="utf-8", errors="replace") as f:
    json.dump({"results": results, "all_papers": all_papers}, f, ensure_ascii=False, indent=2)
print("Saved temp_papers.json")