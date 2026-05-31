---
source_file: "genericagent/agent_loop.py"
type: "code"
community: "Community None"
location: "L14"
tags:
  - graphify/code
  - graphify/INFERRED
  - community/Community_None
---

# BaseHandler

## Connections
- [[.dispatch()_1]] - `method` [EXTRACTED]
- [[.tool_after_callback()]] - `method` [EXTRACTED]
- [[.tool_before_callback()]] - `method` [EXTRACTED]
- [[.turn_end_callback()]] - `method` [EXTRACTED]
- [[Agent觉得当前任务完成后有重要信息需要记忆时调用此工具。]] - `uses` [INFERRED]
- [[Generic Agent 工具库，包含多种工具的实现。工具函数自动加上了 do_ 前缀。实际工具名没有前缀。]] - `uses` [INFERRED]
- [[GenericAgentHandler]] - `uses` [INFERRED]
- [[agent_loop.py]] - `contains` [EXTRACTED]
- [[question 向用户提出的问题。candidates 可选的候选项列表]] - `uses` [INFERRED]
- [[web情况下的优先使用工具，执行任何js达成对浏览器的完全控制。支持将结果保存到文件供后续读取分析。]] - `uses` [INFERRED]
- [[代码执行器     python 运行复杂的 .py 脚本（文件模式）     powershellbash 运行单行指令（命令模式）     优先使用p]] - `uses` [INFERRED]
- [[在文件中寻找唯一的 old_content 块并替换为 new_content]] - `uses` [INFERRED]
- [[展开文本中的 {{file路径起始行结束行}} 引用为实际文件内容。     可与普通文本混排。展开失败抛 ValueError。     base_di]] - `uses` [INFERRED]
- [[执行 JS 脚本来控制浏览器，并捕获结果和页面变化]] - `uses` [INFERRED]
- [[执行代码片段，有长度限制，不允许代码中放大量数据，如有需要应当通过文件读取进行。]] - `uses` [INFERRED]
- [[用于对整个文件的大量处理，精细修改要用file_patch。         需要将要写入的内容放在file_content标签内，或者放在代码块中]] - `uses` [INFERRED]
- [[获取当前页面内容和标签页列表。也可用于切换标签页。         注意：HTML经过简化，边栏浮动元素等可能被过滤。如需查看被过滤的内容请用execute_]] - `uses` [INFERRED]
- [[获取当前页面的简化HTML内容和标签页列表。注意：简化过程会过滤边栏、浮动元素等非主体内容。     tabs_only 仅返回标签页列表，不获取HTML内容]] - `uses` [INFERRED]
- [[读取文件内容。从第start行开始读取。如有keyword则返回第一个keyword(忽略大小写)周边内容]] - `uses` [INFERRED]
- [[这是一个特殊工具，由引擎自主调用，不要包含在TOOLS_SCHEMA里。         当模型在一轮中未显式调用任何工具时，由引擎自动触发。]] - `uses` [INFERRED]

#graphify/code #graphify/INFERRED #community/Community_None