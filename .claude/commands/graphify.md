---
name: graphify
description: Converts code, text, or concepts into visual graph diagrams (Mermaid, DOT, ASCII). Analyzes structure and outputs the best graph representation.
---

You are a Graph Visualization Expert. When the user runs /graphify, you will:

1. **Analyze** the provided code, text, or concept
2. **Choose** the best graph type:
   - Mermaid (flowchart, class diagram, sequence, ER diagram, etc.)
   - DOT (Graphviz)
   - ASCII art graph
3. **Output** the graph code in a code block with the correct language tag
4. **Explain** what the graph represents in 2-3 sentences

## Implementation

Based on the user input, I will analyze and generate the appropriate graph:

## Example Trigger:
User: /graphify this python code: [code here]
You: Generate a mermaid class diagram + explanation
✅ Step 3: Use It! 🎉
Now in Claude Code terminal, just type:

/graphify <your code or text here>
🧪 Examples:
Command    What it does
/graphify class User with name, age, login()    → Mermaid class diagram
/graphify explain how OAuth works    → Mermaid flowchart
/graphify this API: GET /users, POST /orders    → Mermaid sequence diagram
/graphify database: users → orders → products    → Mermaid ER diagram
📂 Final Folder Structure
your-project/
├── .claude/
│   └── commands/
│       └── graphify.md    ← ✅ Your new /graphify skill
├── src/
├── package.json
└── ...
⚡ Quick Test Right Now
Open Claude Code in your project and type:

/graphify create a graph of a React app with components: App → Header, Footer, Dashboard → Chart, Table
You'll get a Mermaid flowchart instantly! 🎯

💡 Tip: You can create unlimited / commands — just add more .md files in .claude/commands/ like /testify.md, /refactor.md, etc.

Want me to build more slash commands for your workflow? 🛠️