# Books Dashboard

> [!INFO] Vault Books Gallery
> `$= const books = dv.pages('"BOOKS"').where(p => p.file.frontmatter?.status); this.container.querySelector('.markdown-rendered').innerHTML = '<div class="book-gallery"><p style="color:#666;font-size:0.85rem;">⚠️ Enable the Dataview plugin and create notes in BOOKS/ folder using the Book Template.</p></div>'; "" `

## All Books

```dataview
TABLE WITHOUT ID
  file.link AS Title,
  authors AS Author,
  status AS Status,
  rating AS Rating,
  genre AS Genre
FROM "BOOKS"
WHERE status
SORT status ASC, rating DESC
```

## Reading Now

```dataview
TABLE WITHOUT ID
  file.link AS Title,
  authors AS Author,
  started AS Started,
  pages AS Pages
FROM "BOOKS"
WHERE status = "Reading"
SORT file.ctime DESC
```

## To Read Next

```dataview
TABLE WITHOUT ID
  file.link AS Title,
  authors AS Author,
  genre AS Genre,
  rating AS Interest
FROM "BOOKS"
WHERE status = "To Read"
SORT rating DESC
```

## Completed

```dataview
TABLE WITHOUT ID
  file.link AS Title,
  authors AS Author,
  finished AS Finished,
  rating AS Rating
FROM "BOOKS"
WHERE status = "Read"
SORT finished DESC
```

## Stats

> [!PANDAS]- Books Statistics
> **Total books:** `$= dv.pages('"BOOKS"').length`
> **Read:** `$= dv.pages('"BOOKS"').where(p => p.status === "Read").length`
> **Reading:** `$= dv.pages('"BOOKS"').where(p => p.status === "Reading").length`
> **To Read:** `$= dv.pages('"BOOKS"').where(p => p.status === "To Read").length`

---

*Use the **Book Template** in Templates/ to add new books. Enable the **book-gallery.css** snippet in Settings → Appearance → CSS snippets.*