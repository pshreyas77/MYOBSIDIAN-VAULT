---
type: author
tags: [author]
---

<% tp.file.title %>

## Biography

## Books by this Author

```dataview
TABLE status, rating
FROM "BOOKS/Books"
WHERE author = this.file.name
SORT rating DESC
```