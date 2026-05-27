# Dataview Queries for Graph Analysis

## 🔑 Essential Queries

### God Nodes Dashboard
```dataview
TABLE file.link as "Node", 
      length(incoming(file.link)) + length(outgoing(file.link)) as "Connections",
      file.folder as "Location"
FROM ""
WHERE contains(lower(file.name), "now()") OR 
      contains(lower(file.name), "map()") OR 
      contains(lower(file.name), "error()") OR 
      contains(lower(file.name), "values()") OR 
      contains(lower(file.name), "task")
SORT length(incoming(file.link)) + length(outgoing(file.link)) DESC
LIMIT 10
```

### Bridge Notes (Technical ↔ Non-Technical)
```dataview
TABLE file.link as "Bridge Note",
      length(incoming(file.link)) + length(outgoing(file.link)) as "Connections",
      file.folder as "Location"
FROM ""
WHERE (contains(lower(file.name), "map") OR 
       contains(lower(file.name), "error") OR 
       contains(lower(file.name), "now") OR 
       contains(lower(file.name), "task") OR 
       contains(lower(file.name), "values"))
  AND (contains(lower(file.content), "philosophy") OR 
       contains(lower(file.content), "ethic") OR 
       contains(lower(file.content), "value") OR 
       contains(lower(file.content), "belief") OR 
       contains(lower(file.content), "political") OR 
       contains(lower(file.content), "power") OR 
       contains(lower(file.content), "justice") OR 
       contains(lower(file.content), "religious") OR 
       contains(lower(file.content), "faith") OR 
       contains(lower(file.content), "sacred") OR 
       contains(lower(file.content), "myth") OR 
       contains(lower(file.content), "theology"))
SORT length(incoming(file.link)) + length(outgoing(file.link)) DESC
```

### Orphaned Notes Review
```dataview
TABLE file.link as "Orphan Note",
      length(incoming(file.link)) + length(outgoing(file.link)) as "Connections",
      file.folder as "Location",
      file.tags as "Tags"
FROM ""
WHERE length(incoming(file.link)) + length(outgoing(file.link)) < 5
  AND !contains(file.folder, "09 - ARCHIVES")
  AND !contains(file.folder, "00 - SYSTEM/Templates")
SORT length(incoming(file.link)) + length(outgoing(file.link)) ASC
```

### Weak Inferred Links (Needs Review)
```dataview
TABLE file.link as "Note",
      length(incoming(file.link)) + length(outgoing(file.link)) as "Total Links",
      length(filter(incoming(file.link), (l) => meta(l).section.confidence < 0.6)) as "Weak Inferred"
FROM ""
WHERE length(filter(incoming(file.link), (l) => meta(l).section.confidence < 0.6)) > 0
  OR length(filter(outgoing(file.link), (l) => meta(l).section.confidence < 0.6)) > 0
SORT length(filter(incoming(file.link), (l) => meta(l).section.confidence < 0.6)) DESC
```

### Community-Based Queries
```dataview
// Notes in largest communities
TABLE file.link as "Note", 
      file.folder as "Location"
FROM ""
WHERE contains(file.folder, "02 - AREAS/01 Philosophy & Religion") OR 
      contains(file.folder, "02 - AREAS/04 Political Analysis")
SORT file.name
LIMIT 20

// Recent activity in knowledge hub areas
TABLE file.link as "Recently Updated",
      file.day as "Date"
FROM "00 - SYSTEM" OR "02 - AREAS"
WHERE file.day >= date(today) - dur(7 days)
SORT file.day DESC
```

## 📊 Analytics Queries

### Connection Distribution
```dataview
TABLE 
      length(incoming(file.link)) + length(outgoing(file.link)) as "Connections",
      count() as "Note Count"
FROM ""
GROUP BY length(incoming(file.link)) + length(outgoing(file.link))
HAVING length(incoming(file.link)) + length(outgoing(file.link)) > 0
SORT length(incoming(file.link)) + length(outgoing(file.link)) DESC
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

### Folder Connection Strength
```dataview
TABLE 
      file.folder as "Folder",
      avg(length(incoming(file.link)) + length(outgoing(file.link))) as "Avg Connections",
      count() as "Note Count",
      sum(length(incoming(file.link)) + length(outgoing(file.link))) as "Total Connections"
FROM ""
GROUP BY file.folder
HAVING count() > 2
SORT avg(length(incoming(file.link)) + length(outgoing(file.link))) DESC
```

## 🚀 Advanced: Custom Graph Analysis

### Find Notes Similar to God Nodes
```dataview
// Notes that share connections with multiple God nodes
TABLE file.link as "Note",
      (length(filter(incoming(file.link), (l) => contains(l.file.name, "now()"))) + 
       length(filter(incoming(file.link), (l) => contains(l.file.name, "map()"))) + 
       length(filter(incoming(file.link), (l) => contains(l.file.name, "error()")))) as "God Node Links"
FROM ""
WHERE length(filter(incoming(file.link), (l) => contains(l.file.name, "now()") OR 
                                contains(l.file.name, "map()") OR 
                                contains(l.file.name, "error()"))) >= 2
SORT (length(filter(incoming(file.link), (l) => contains(l.file.name, "now()"))) + 
      length(filter(incoming(file.link), (l) => contains(l.file.name, "map()"))) + 
      length(filter(incoming(file.link), (l) => contains(l.file.name, "error()")))) DESC
```

### Link Recommendation Engine
```dataview
// Suggest links based on co-occurrence in communities
TABLE file.link as "Note 1",
      file2.link as "Note 2",
      (length(incoming(file.link)) + length(outgoing(file.link))) * 
      (length(incoming(file2.link)) + length(outgoing(file2.link))) as "Connection Potential"
FROM ""
FLATTEN file.file as file2
WHERE file.link != file2.link
  AND contains(lower(file.content), lower(file2.file.name)) 
  OR contains(lower(file2.file.content), lower(file.file.name))
GROUP BY file.link, file2.link
HAVING (length(incoming(file.link)) + length(outgoing(file.link))) > 10
  AND (length(incoming(file2.link)) + length(outgoing(file2.link))) > 10
SORT (length(incoming(file.link)) + length(outgoing(file.link))) * 
     (length(incoming(file2.link)) + length(outgoing(file2.link))) DESC
LIMIT 20
```

## 💡 Usage Tips

1. **Create a Dashboard Note**: Paste the God Nodes query into your main MOC
2. **Weekly Review**: Run the Orphaned Notes query every Friday
3. **Link Building**: Use the Weak Inferred Links query to find connections to strengthen
4. **Bridge Discovery**: Run the Bridge Notes query monthly to find new interdisciplinary connections
5. **Folder Optimization**: Use the Folder Connection Strength query to see which PARA+ areas are most connected

## 🔄 Integration with Your Workflow

Add these to your daily notes or review templates:

### Daily Check-in
```dataview
TABLE file.link as "Updated Today",
      length(incoming(file.link)) + length(outgoing(file.link)) as "Connections"
FROM ""
WHERE file.day = today
SORT length(incoming(file.link)) + length(outgoing(file.link)) DESC
```

### Weekly Review Template
```markdown
# Weekly Vault Review - {{date:YYYY-MM-DD}}

## 🆕 New Connections Today
```dataview
TABLE file.link as "Note",
      length(incoming(file.link)) + length(outgoing(file.link)) as "New Links"
FROM ""
WHERE file.day >= date(today) - dur(7 days)
  AND file.day < date(today)
SORT length(incoming(file.link)) + length(outgoing(file.link)) DESC
LIMIT 10
```

## 🏝️ Orphan Check
```dataview
TABLE file.link as "Orphan Note",
      length(incoming(file.link)) + length(outgoing(file.link)) as "Connections"
FROM ""
WHERE length(incoming(file.link)) + length(outgoing(file.link)) < 5
  AND !contains(file.folder, "09 - ARCHIVES")
SORT length(incoming(file.link)) + length(outgoing(file.link)) ASC
LIMIT 10
```
```