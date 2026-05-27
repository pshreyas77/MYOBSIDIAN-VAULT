# Graph Exploration Queries for Obsidian Vault

These queries help you explore your knowledge graph based on the God Nodes and community structure identified in the graphify analysis.

## 🔑 God Node Exploration

### Find Notes Related to Each God Node
```dataview
TABLE file.link as "Note", 
      length(file.outlinks) + length(file.inlinks) as "Total Connections",
      file.folder as "Location"
FROM ""
WHERE contains(lower(file.name), "now()")
SORT length(file.outlinks) + length(file.inlinks) DESC
```

```dataview
TABLE file.link as "Note", 
      length(file.outlinks) + length(file.inlinks) as "Total Connections",
      file.folder as "Location"
FROM ""
WHERE contains(lower(file.name), "map()")
SORT length(file.outlinks) + length(file.inlinks) DESC
```

```dataview
TABLE file.link as "Note", 
      length(file.outlinks) + length(file.inlinks) as "Total Connections",
      file.folder as "Location"
FROM ""
WHERE contains(lower(file.name), "error()")
SORT length(file.outlinks) + length(file.inlinks) DESC
```

```dataview
TABLE file.link as "Note", 
      length(file.outlinks) + length(file.inlinks) as "Total Connections",
      file.folder as "Location"
FROM ""
WHERE contains(lower(file.name), "values()")
SORT length(file.outlinks) + length(file.inlinks) DESC
```

```dataview
TABLE file.link as "Note", 
      length(file.outlinks) + length(file.inlinks) as "Total Connections",
      file.folder as "Location"
FROM ""
WHERE contains(lower(file.name), "task")
SORT length(file.outlinks) + length(file.inlinks) DESC
```

### Find Notes Connecting Multiple God Notes
```dataview
TABLE file.link as "Note",
      (length(filter(file.outlinks, (l) => contains(l.file.name, "now()"))) +
       length(filter(file.outlinks, (l) => contains(l.file.name, "map()"))) +
       length(filter(file.outlinks, (l) => contains(l.file.name, "error()"))) +
       length(filter(file.outlinks, (l) => contains(l.file.name, "values()"))) +
       length(filter(file.outlinks, (l) => contains(l.file.name, "task")))) as "God Node Connections"
FROM ""
WHERE (length(filter(file.outlinks, (l) => contains(l.file.name, "now()") OR 
                                contains(l.file.name, "map()") OR 
                                contains(l.file.name, "error()") OR 
                                contains(l.file.name, "values()") OR 
                                contains(l.file.name, "task"))) >= 2)
SORT (length(filter(file.outlinks, (l) => contains(l.file.name, "now()"))) +
      length(filter(file.outlinks, (l) => contains(l.file.name, "map()"))) +
      length(filter(file.outlinks, (l) => contains(l.file.name, "error()"))) +
      length(filter(file.outlinks, (l) => contains(l.file.name, "values()"))) +
      length(filter(file.outlinks, (l) => contains(l.file.name, "task")))) DESC
```

## 🌉 Bridge Note Discovery

### Technical ↔ Philosophy Connections
```dataview
TABLE file.link as "Note",
      length(file.outlinks) + length(file.inlinks) as "Connections",
      file.folder as "Location"
FROM ""
WHERE (contains(lower(file.content), "philosophy") OR 
       contains(lower(file.content), "ethic") OR 
       contains(lower(file.content), "value") OR 
       contains(lower(file.content), "belief") OR 
       contains(lower(file.content), "principle"))
  AND (contains(lower(file.content), "map") OR 
       contains(lower(file.content), "error") OR 
       contains(lower(file.content), "now") OR 
       contains(lower(file.content), "task") OR 
       contains(lower(file.content), "function") OR 
       contains(lower(file.content), "async") OR 
       contains(lower(file.content), "promise"))
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 20
```

### Technical ↔ Political Analysis Connections
```dataview
TABLE file.link as "Note",
      length(file.outlinks) + length(file.inlinks) as "Connections",
      file.folder as "Location"
FROM ""
WHERE (contains(lower(file.content), "political") OR 
       contains(lower(file.content), "power") OR 
       contains(lower(file.content), "governance") OR 
       contains(lower(file.content), "policy") OR 
       contains(lower(file.content), "authority") OR 
       contains(lower(file.content), "democracy") OR 
       contains(lower(file.content), "justice") OR 
       contains(lower(file.content), "rights") OR 
       contains(lower(file.content), "freedom") OR 
       contains(lower(file.content), "equality"))
  AND (contains(lower(file.content), "map") OR 
       contains(lower(file.content), "error") OR 
       contains(lower(file.content), "now") OR 
       contains(lower(file.content), "task") OR 
       contains(lower(file.content), "function") OR 
       contains(lower(file.content), "async") OR 
       contains(lower(file.content), "promise") OR
       contains(lower(file.content), "includes") OR
       contains(lower(file.content), "filter") OR
       contains(lower(file.content), "reduce"))
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 20
```

### Technical ↔ Religious Archaeology Connections
```dataview
TABLE file.link as "Note",
      length(file.outlinks) + length(file.inlinks) as "Connections",
      file.folder as "Location"
FROM ""
WHERE (contains(lower(file.content), "religious") OR 
       contains(lower(file.content), "faith") OR 
       contains(lower(file.content), "sacred") OR 
       contains(lower(file.content), "spiritual") OR 
       contains(lower(file.content), "divine") OR 
       contains(lower(file.content), "god") OR 
       contains(lower(file.content), "ritual") OR 
       contains(lower(file.content), "myth") OR 
       contains(lower(file.content), "scripture") OR 
       contains(lower(file.content), "theology") OR
       contains(lower(file.content), "archaeology") OR
       contains(lower(file.content), "evidence") OR
       contains(lower(file.content), "artifact") OR
       contains(lower(file.content), "excavation") OR
       contains(lower(file.content), "historical"))
  AND (contains(lower(file.content), "map") OR 
       contains(lower(file.content), "error") OR 
       contains(lower(file.content), "now") OR 
       contains(lower(file.content), "task") OR 
       contains(lower(file.content), "function") OR 
       contains(lower(file.content), "async") OR 
       contains(lower(file.content), "promise") OR
       contains(lower(file.content), "includes") OR
       contains(lower(file.content), "filter") OR
       contains(lower(file.content), "reduce") OR
       contains(lower(file.content), "date") OR
       contains(lower(file.content), "time") OR
       contains(lower(file.content), "timeline") OR
       contains(lower(file.content), "chronology"))
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 20
```

## 🏝️ Community & Orphan Analysis

### Find Potentially Orphaned Notes (Low Connection Count)
```dataview
TABLE file.link as "Note",
      length(file.outlinks) + length(file.inlinks) as "Connections",
      file.folder as "Location",
      file.tags as "Tags"
FROM ""
WHERE length(file.outlinks) + length(file.inlinks) < 5
  AND !contains(file.folder, "09 - ARCHIVES")
  AND !contains(file.folder, "00 - SYSTEM/Templates")
  AND !contains(file.folder, "00 - SYSTEM/Graph Reports")
SORT length(file.outlinks) + length(file.inlinks) ASC
```

### Find Notes in Largest Communities (by checking file names/links)
```dataview
TABLE file.link as "Note",
      length(file.outlinks) + length(file.inlinks) as "Connections",
      file.folder as "Location"
FROM ""
WHERE contains(file.content, "Community 0") OR
      contains(file.content, "Community 1") OR
      contains(file.content, "Community 2") OR
      contains(file.content, "Community 3") OR
      contains(file.content, "Community 4") OR
      contains(file.content, "Community 5")
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 20
```

## 📊 Graph Statistics & Maintenance

### Connection Distribution Analysis
```dataview
TABLE 
      length(file.outlinks) + length(file.inlinks) as "Connections",
      count() as "Note Count"
FROM ""
WHERE length(file.outlinks) + length(file.inlinks) > 0
GROUP BY length(file.outlinks) + length(file.inlinks)
HAVING length(file.outlinks) + length(file.inlinks) > 0
SORT length(file.outlinks) + length(file.inlinks) DESC
```

### Tag Usage Analysis
```dataview
TABLE 
      file.tags as "Tags",
      length(file.tags) as "Tag Count",
      count() as "Notes With Tags"
FROM ""
WHERE file.tags
GROUP BY file.tags
SORT count() DESC
```

### Folder Connection Strength (PARA+ Analysis)
```dataview
TABLE 
      file.folder as "PARA+ Area",
      round(avg(length(file.outlinks) + length(file.inlinks)), 1) as "Avg Connections",
      count() as "Note Count",
      sum(length(file.outlinks) + length(file.inlinks)) as "Total Connections"
FROM ""
GROUP BY file.folder
HAVING count() > 2
SORT round(avg(length(file.outlinks) + length(file.inlinks)), 1) DESC
```

### Weekly Maintenance Queries
```dataview
-- Notes updated in the last 7 days
TABLE file.link as "Recently Updated",
      file.day as "Date",
      length(file.outlinks) + length(file.inlinks) as "Connections"
FROM ""
WHERE file.day >= date(today) - dur(7 days)
SORT file.day DESC

-- Notes never edited (created but not modified)
TABLE file.link as "Potentially Stale",
      file.created as "Created",
      length(file.outlinks) + length(file.inlinks) as "Connections"
FROM ""
WHERE file.created < date(today) - dur(30 days)
  AND (file.modified IS NULL OR file.modified = file.created)
SORT file.created ASC
```

## 💡 Pro Tips for Using These Queries

1. **Create a Dashboard Note**: Add the most useful queries to your `00 - SYSTEM/01_KNOWLEDGE_HUB.md`
2. **Weekly Review**: Run the orphaned notes query every Friday to review low-connection notes
3. **Bridge Building**: Use the bridge note queries monthly to find new interdisciplinary connections
4. **Community Development**: Focus on developing notes in communities with high potential but low current connectivity
5. **Link Optimization**: Use the connection distribution analysis to see where you might need to add more links

## 🔄 Integration with Your Workflow

### Daily Note Template Addition
```markdown
## 📈 Graph Insights (Auto-generated)
```dataview
TABLE file.link as "Updated Today",
      length(file.outlinks) + length(file.inlinks) as "Connections"
FROM ""
WHERE file.day = today
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 5
```
```

### Weekly Review Template
```markdown
# Weekly Graph Review - {{date:YYYY-MM-DD}}

## 🆕 New Connections This Week
```dataview
TABLE file.link as "Note",
      length(file.outlinks) + length(file.inlinks) as "New Links"
FROM ""
WHERE file.day >= date(today) - dur(7 days)
  AND file.day < date(today)
SORT length(file.outlinks) + length(file.inlinks) DESC
LIMIT 10
```

## 🏝️ Orphan Check (Needs Review)
```dataview
TABLE file.link as "Orphan Note",
      length(file.outlinks) + length(file.inlinks) as "Connections"
FROM ""
WHERE length(file.outlinks) + length(file.inlinks) < 5
  AND !contains(file.folder, "09 - ARCHIVES")
SORT length(file.outlinks) + length(file.inlinks) ASC
LIMIT 10
```
```

--- 

*Save this file and copy queries into your notes as needed. Update the queries periodically as your vault evolves.*