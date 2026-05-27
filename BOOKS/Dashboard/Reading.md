# Reading Tracker

## In Progress

```dataview
TABLE progress + "%" AS "Progress", pages
FROM "BOOKS/Books"
WHERE status = "reading"
SORT progress DESC
```

## Backlog

```dataview
TABLE priority, genres
FROM "BOOKS/Books"
WHERE status = "to-read"
SORT priority DESC
```