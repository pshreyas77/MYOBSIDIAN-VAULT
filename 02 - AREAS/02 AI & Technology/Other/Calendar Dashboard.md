---
tags: [dashboard, calendar, tracking, hub]
date: 2026-04-11
created: 2026-04-11
---

# 📅 Calendar Dashboard

Your personal tracking hub for daily use patterns, habits, and productivity.

---

## 🗓️ Quick Navigation

### Daily
- [[{{yesterday:YYYY-MM-DD}}|← Yesterday]]
- [[{{date:YYYY-MM-DD}}|Today]]
- [[{{tomorrow:YYYY-MM-DD}}|Tomorrow →]]

### Weekly
- [[Weekly Review {{date:YYYY-[W]WW}}|This Week]]
- [[Weekly Review {{lastWeek:YYYY-[W]WW}}|Last Week]]
- [[Weekly Review {{nextWeek:YYYY-[W]WW}}|Next Week]]

### Monthly
- [[Monthly Review {{date:YYYY-MM}}|{{date:MMMM}}]]
- [[Monthly Review {{lastMonth:YYYY-MM}}|{{lastMonth:MMMM}}]]
- [[Monthly Review {{nextMonth:YYYY-MM}}|{{nextMonth:MMMM}}]]

### Yearly
- [[Yearly Review {{date:YYYY}}|{{date:YYYY}} Goals]]

---

## 📊 This Week's Stats

```dataview
TABLE WITHOUT ID
  file.link AS "Date",
  day AS "Day",
  choice(contains(file.outlinks, [[{{yesterday:YYYY-MM-DD}}]]), "✅", "❌") AS "Previous Day",
  energy AS "Energy",
  productivity AS "Productivity",
  mood AS "Mood"
FROM "03 - Resources/Daily Tracking"
WHERE date >= date({{sunday:YYYY-MM-DD}}) AND date <= date({{saturday:YYYY-MM-DD}})
SORT date ASC
```

---

## 📈 Monthly Heatmap

### Activity Streak
```dataviewjs
const notes = dv.pages('"03 - Resources/Daily Tracking"')
  .where(p => p.date && p.date >= moment().startOf('month').format('YYYY-MM-DD'));

const daysInMonth = moment().daysInMonth();
let output = "| Sun | Mon | Tue | Wed | Thu | Fri | Sat |\n";
output += "|:---:|:---:|:---:|:---:|:---:|:---::|\n";

let day = 1;
let weekStart = moment().startOf('month').day();

// Padding for first week
for (let i = 0; i < 7; i++) {
  if (i < weekStart) {
    output += "|   ";
  } else {
    output += "| " + day + " ";
    day++;
  }
}
output += "|\n";

// Rest of month
let weekDay = 0;
while (day <= daysInMonth) {
  if (weekDay === 0) output += "|";
  output += " " + day + " ";
  if (weekDay === 6) output += "|\n";
  day++;
  weekDay = (weekDay + 1) % 7;
}

// Close row
if (weekDay !== 0) {
  for (let i = weekDay; i < 7; i++) {
    output += "|   ";
  }
  output += "|\n";
}

dv.paragraph(output);
```

---

## ✅ Habit Tracker

| Habit | Mon | Tue | Wed | Thu | Fri | Sat | Sun | Total |
|-------|-----|-----|-----|-----|-----|-----|-----|-------|
| 🧘 Meditation | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 0/7 |
| 📚 Reading | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 0/7 |
| 💪 Exercise | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 0/7 |
| 📝 Journal | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 0/7 |
| 🎯 Deep Work | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | ☐ | 0/7 |

---

## 🏆 Monthly Highlights

### Top Achievements This Month



### Learning Highlights



### Challenges Overcome



---

## 📁 Recent Daily Notes

```dataview
LIST date
FROM "03 - Resources/Daily Tracking"
SORT date DESC
LIMIT 7
```

---

## 🔗 All Trackers

- [[Habit Tracker]]
- [[Energy Tracker]]
- [[Productivity Tracker]]
- [[Mood Journal]]
- [[Weekly Reports]]
- [[Monthly Reports]]

---

## 🛠️ Templates

- [[Daily Note Template|➕ New Daily Note]]
- [[Weekly Review Template|➕ New Weekly Review]]
- [[Monthly Review Template|➕ New Monthly Review]]

---

*Dashboard updated: 2026-04-11*
