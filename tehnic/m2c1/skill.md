---
name: m2c1
compatibility: claude-code-only
description: Meta orchestration framework for autonomous software development. Use when building any software project from scratch or extending existing codebases. Converts brain dumps into phased implementation plans with parallel research, discovery questioning, tool setup, task sharding, synergy review, and multi-angle testing at every level. 12-phase workflow from idea to fully tested, deployed software. Se declanșează și la formulări în română de tipul "construiește-mi aplicația de la zero", "orchestrează tot proiectul", "vreau execuție autonomă pe proiectul ăsta".
license: MIT
source: https://github.com/grandamenium/m2c1 (MIT License)
---

# M2C1 - Meta Orchestration Framework

A generalizable framework for autonomous software development. Converts a user's brain dump into a fully orchestrated, phased implementation plan that subagents execute autonomously with comprehensive testing at every level.

## When to Use

- User has a software idea and wants to build it end-to-end
- User wants to add a major feature set to an existing project
- Any project that benefits from structured research, planning, and autonomous execution

## Hard Prerequisites

- **Playwright MCP** must be available (browser automation for testing and tool setup)
- User must be able to provide brain dump or PRD of the idea

## Core Files

| File | Purpose |
|------|---------|
| `orchestration-workflow.md` | Complete 12-phase protocol - the master process |
| `artifact-templates/prd.md` | Initial PRD template (<500 lines) |
| `artifact-templates/research-file.md` | Research output file format |
| `artifact-templates/discovery.md` | DISCOVERY.md Q&A format |
| `artifact-templates/phases.md` | PHASES.md structure |
| `artifact-templates/task-file.md` | Individual task file template (the prompt each execution agent receives) |
| `artifact-templates/progress.md` | PROGRESS.md tracking format |
| `artifact-templates/start.md` | START.md orchestrator protocol |
| `artifact-templates/claude-md-section.md` | CLAUDE.md orchestration section template |

## Key Principles

1. **Every artifact has a template** - agents read the template before creating any artifact
2. **Parallel by default** - subagents run in background wherever independent
3. **Multi-angle testing at every level** - task-local, phase regression, final comprehensive e2e
4. **Human-emulating testing** - agents test as users would via Playwright + simulated assets
5. **Tool-aware** - researches and configures MCP servers, CLIs, external services
6. **Agent-autonomous** - agents do "human steps" in browser, only truly manual steps require user
7. **Generalizable** - works for any software type (SaaS, API, CLI, mobile, etc.)
8. **Discovery completeness** - self-audits discovery questions before proceeding; asks "could an agent implement this without guessing?"
9. **Mandatory tool setup** - agent autonomously configures all tools via Playwright + CLI, not just lists requirements
10. **Mandatory skill creation** - every tool, research domain, external source, testing strategy, and unique framework gets a dedicated skill file for execution agents to read

## Quick Start

Read `orchestration-workflow.md` for the full 12-phase protocol. Each phase references the relevant artifact templates.
