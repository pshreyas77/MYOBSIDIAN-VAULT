# Statistics

## Total Books

```dataview
TABLE length(rows) AS "Total"
FROM "BOOKS/Books"
WHERE type = "book"
```

## By Status

```dataview
TABLE length(rows) AS Count
FROM "BOOKS/Books"
GROUP BY status
```

## By Genre

```dataview
TABLE length(rows) AS Count
FROM "BOOKS/Books"
FLATTEN genres
GROUP BY genres
SORT Count DESC
```

## Average Rating

```dataview
TABLE round(avg(rating),2) AS "Average Rating"
FROM "BOOKS/Books"
WHERE rating > 0
```

## Reading Duration (Completed)

```dataview
TABLE (date(date_completed) - date(date_started)) AS "Days"
FROM "BOOKS/Books"
WHERE status = "completed" AND date_started AND date_completed
```