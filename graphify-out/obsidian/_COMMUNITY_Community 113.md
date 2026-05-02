---
type: community
cohesion: 0.18
members: 12
---

# Community 113

**Cohesion:** 0.18 - loosely connected
**Members:** 12 nodes

## Members
- [[_next_report_number()]] - code - genericagent/memory/autonomous_operation_sop/helper.py
- [[autonomous_task.py - 自主行动任务管理API 放置 memoryautonomous_operation_sop 用法 import]] - rationale - genericagent/memory/autonomous_operation_sop/helper.py
- [[complete_task()]] - code - genericagent/memory/autonomous_operation_sop/helper.py
- [[get_history()]] - code - genericagent/memory/autonomous_operation_sop/helper.py
- [[get_todo()]] - code - genericagent/memory/autonomous_operation_sop/helper.py
- [[helper.py]] - code - genericagent/memory/autonomous_operation_sop/helper.py
- [[set_todo()]] - code - genericagent/memory/autonomous_operation_sop/helper.py
- [[完成任务的原子操作：     1. 移动 report_path → autonomous_reportsR{XX}_{taskname}.md（自动编号）]] - rationale - genericagent/memory/autonomous_operation_sop/helper.py
- [[扫 history.txt 第一行提取最大 RXX 编号，返回下一个]] - rationale - genericagent/memory/autonomous_operation_sop/helper.py
- [[返回 TODO.txt 的内容。若文件不存在返回提示。]] - rationale - genericagent/memory/autonomous_operation_sop/helper.py
- [[返回 TODO.txt 的真实绝对路径，供 agent子agent 自行读写。]] - rationale - genericagent/memory/autonomous_operation_sop/helper.py
- [[返回 history.txt 的前 n 行（最新在前）。]] - rationale - genericagent/memory/autonomous_operation_sop/helper.py

## Live Query (requires Dataview plugin)

```dataview
TABLE source_file, type FROM #community/Community_113
SORT file.name ASC
```
