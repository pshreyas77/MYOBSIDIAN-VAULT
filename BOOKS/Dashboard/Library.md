# Library

## Currently Reading

```dataview
TABLE author, progress + "%" AS "Progress", pages
FROM "BOOKS/Books"
WHERE status = "reading"
SORT date_started DESC
```

## To Read (High Priority)

```dataview
TABLE author, priority
FROM "BOOKS/Books"
WHERE status = "to-read" AND priority = "high"
SORT date_added DESC
```

## Recently Completed

```dataview
TABLE author, rating, date_completed
FROM "BOOKS/Books"
WHERE status = "completed"
SORT date_completed DESC
LIMIT 10
```

## All Books

```dataview
TABLE author, status, rating, genres
FROM "BOOKS/Books"
SORT file.name ASC
```