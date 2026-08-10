# CLAUDE.md Orchestration Section Template

Use this template when adding the orchestration section to the project's CLAUDE.md (Phase 12). This section gives any agent (or new session) immediate context about the orchestration system.

---

```markdown
# <Project Name>

<One-line description of the project>

## Quick Reference

| What | Where |
|------|-------|
| **Top authority** | `.claude/orchestration-<slug>/DISCOVERY.md` - all product/tech/scope decisions |
| **Implementation plan** | `.claude/orchestration-<slug>/PHASES.md` - <N> tasks across <N> phases |
| **Progress tracker** | `PROGRESS.md` - task status, phase status |
| **Task files** | `.claude/orchestration-<slug>/tasks/phase-N/task-N-M.md` - per-task specs |
| **Orchestrator** | `.claude/orchestration-<slug>/START.md` - how to run the system |
| **Research** | `.claude/orchestration-<slug>/research/` - <N> research files |

## Authority Rule

DISCOVERY.md overrides everything. If a research file, skill, or this document contradicts DISCOVERY.md, follow DISCOVERY.md. If still unsure, ask the human.

## Tech Stack

| Layer | Technology |
|-------|-----------|
| <Layer> | <Technology> |
| ... | ... |

## Scope Constraints (DO NOT implement)

<Comma-separated list of excluded features from DISCOVERY.md>

## Git Workflow

- Feature branches from <target-branch>: `task/N-M-<short-description>`
- Merge to <target-branch> after tests pass
- <Any deploy triggers>

## Testing

Every task requires:
1. Tests per task file testing protocol
2. Playwright MCP browser test (for UI tasks)
3. Backend/service log check - no errors

## Skills

Agents MUST read relevant skill files before starting a task.

<List of project skills with one-line descriptions>

## MCP Servers

| Server | Purpose |
|--------|---------|
| Playwright | Browser testing + external dashboard config |
| <Server> | <Purpose> |
| ... | ... |

## For Subagents

If you are a subagent spawned to execute a task:
1. Read your task file at `.claude/orchestration-<slug>/tasks/phase-N/task-N-M.md` first
2. Follow the Task Execution Protocol in `.claude/orchestration-<slug>/PHASES.md`
3. Read ALL skills listed in your task's Skills field
4. Check PROGRESS.md for current state before starting
5. Update PROGRESS.md when done
```

---

## Guidelines for CLAUDE.md Section

- **Concise** - this is a quick reference, not the full spec
- **Ephemeral** - this section is specific to the orchestration run, not permanent
- **Points to files** - don't duplicate content, just reference the right files
- **Includes subagent instructions** - every subagent reads CLAUDE.md, so include their protocol
- **Tech stack and scope** - quick-scannable for any agent entering the project
