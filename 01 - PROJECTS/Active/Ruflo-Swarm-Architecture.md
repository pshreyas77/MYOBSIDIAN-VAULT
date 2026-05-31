# Ruflo Swarm Architecture for AI Agents

```mermaid
flowchart TD
    %% Core Orchestration
    subgraph Orchestration Layer
        SWARM[Swarm Orchestrator<br/>(claude-flow)] --> MEMORY[Memory System<br/>(AgentDB + HNSW)]
        SWARM --> COORDINATOR[Coordinator Agent]
        SWARM --> TASK_ORCH[Task Orchestrator]
    end
    
    %% Agent Types
    subgraph Agent Pool
        COORDINATOR --> CODER[Coder Agent]
        COORDINATOR --> REVIEWER[Reviewer Agent]
        COORDINATOR --> ARCHITECT[Architect Agent]
        COORDINATOR --> TESTER[Tester Agent]
        COORDINATOR --> RESEARCHER[Researcher Agent]
        COORDINATOR --> SEC_ARCH[Security Architect Agent]
    end
    
    %% MCP Tools Interface
    subgraph MCP Tools
        MEMORY_SEARCH[memory_search] -->|Semantic Query| MEMORY
        MEMORY_STORE[memory_store] -->|Pattern Storage| MEMORY
        SWARM_INIT[swarm_init] -->|Topology Config| SWARM
        AGENT_SPAWN[agent_spawn] -->|Agent Registration| SWARM
        TASK_ORCHESTRATE[task_orchestrate] -->|Task Coordination| TASK_ORCH
    end
    
    %% External Systems
    subgraph External Systems
        OBSIDIAN[Obsidian Vault] -->|Files/Notes| CODER
        OBSIDIAN -->|Knowledge Base| RESEARCHER
        GITHUB[GitHub Repos] -->|Code/PRs| REVIEWER
        TERMINAL[Shell/Commands] -->|Execution| CODER
    end
    
    %% Data Flow
    MEMORY -->|Context Retrieval| CODER
    MEMORY -->|Pattern Learning| RESEARCHER
    CODER -->|Code Changes| GITHUB
    REVIEWER -->|Feedback| CODER
    TESTER -->|Validation| CODER
    ARCHITECT -->|Design Specs| CODER
    RESEARCHER -->|Findings| CODER
    
    %% Styling
    classDef orchestrator fill:#e3f2fd,stroke:#1565c0,stroke-width:2px;
    classDef agent fill:#f3e5f5,stroke:#6a1b9a,stroke-width:1px;
    classDef mcp fill:#e8f5e8,stroke:#2e7d32,stroke-width:1px;
    classDef external fill:#fff3e0,stroke:#ef6c00,stroke-width:1px;
    
    class SWARM,MEMORY,COORDINATOR,TASK_ORCH orchestrator
    class CODER,REVIEWER,ARCHITECT,TESTER,RESEARCHER,SEC_ARCH agent
    class MEMORY_SEARCH,MEMORY_STORE,SWARM_INIT,AGENT_SPAWN,TASK_ORCHESTRATE mcp
    class OBSIDIAN,GITHUB,TERMINAL external
```

## Ruflo Swarm Architecture Explanation

This diagram shows how Ruflo implements swarm-based AI agent orchestration:

**Orchestration Layer**: The swarm orchestrator manages agent lifecycle, coordinates tasks, and integrates with the memory system for contextual learning.

**Agent Pool**: Specialized agents (Coder, Reviewer, Architect, Tester, Researcher, Security Architect) that can be spawned based on task requirements.

**MCP Tools Interface**: Model Context Protocol tools enable semantic memory search, pattern storage, swarm initialization, agent spawning, and task orchestration.

**External Systems**: Integration with Obsidian vault for knowledge storage, GitHub for code collaboration, and terminal for command execution.

**Data Flow**: Bidirectional communication between agents and memory enables context engineering, while agent interactions support collaborative problem-solving patterns like the ReAct loop.

This architecture supports the AI AGENT project goals by providing:
- Context engineering through persistent memory and semantic search
- Task decomposition via specialized agent roles
- Multi-agent coordination patterns (hierarchical, mesh, adaptive)
- Observability through memory tracking and agent metrics
- Guardrail implementation via reviewer and security architect agents