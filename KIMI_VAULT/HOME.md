---
type: dashboard
tags: [home, dashboard]
---

# ⬡ PERSONAL VAULT

> *All knowledge, one place. Powered by local AI.*

---

## ⚡ Quick Capture
> Drop thoughts here, process later → move to [[00 - Inbox]]

---

## 📂 Vault Map

| Folder | Purpose |
|--------|---------|
| [[00 - Inbox\|📥 Inbox]] | Unprocessed captures |
| [[01 - Daily Notes\|📅 Daily Notes]] | Journal & daily log |
| [[02 - Knowledge Base\|🧠 Knowledge Base]] | Permanent notes |
| [[03 - Projects\|🔨 Projects]] | Active work |
| [[04 - Research\|🔬 Research]] | Deep dives |
| [[05 - AI Conversations\|🤖 AI Chats]] | Ollama conversations |
| [[08 - OSINT\|🕵️ OSINT]] | Intelligence work |
| [[09 - Finance\|📈 Finance]] | Portfolio & markets |
| [[10 - Career\|💼 Career]] | Job search, skills |

---

## 🔌 AI Status

```dataview
TABLE date, topic FROM "05 - AI Conversations"
SORT date DESC
LIMIT 5
```

---

## 📌 Recent Notes

```dataview
TABLE file.mtime as Modified FROM ""
WHERE file.name != "HOME"
SORT file.mtime DESC
LIMIT 8
```

---

## 🏷️ Tag Cloud

```dataview
TABLE length(rows) as Count
FROM ""
WHERE tags
FLATTEN tags
GROUP BY tags
SORT length(rows) DESC
LIMIT 15
```

