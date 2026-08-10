# START.md Template

Use this template when creating the orchestrator protocol (Phase 12). This file defines how the main agent spawns execution subagents and manages the pipeline.

---

```markdown
# <Project Name> Orchestrator

When `/start` is invoked, this orchestrator manages sequential execution of all tasks across all phases. Designed for **fully autonomous execution**.

---

## Startup Sequence

1. **Read PROGRESS.md** - Determine current state: which tasks are complete, which phase is active
2. **Read PHASES.md** at `.claude/orchestration-<slug>/PHASES.md` - Load the full implementation plan
3. **Identify next task** - Find the lowest-numbered pending task whose dependencies are all met
4. **Execute the task** - Spawn a subagent (see below)
5. **After task completes** - Verify PROGRESS.md was updated, then repeat from step 3

---

## Spawning a Subagent

For each task, spawn a `general-purpose` subagent via the Task tool:

```
You are executing Task N.M for <Project Name>.

## Your Task File
Read your full task specification at: .claude/orchestration-<slug>/tasks/phase-N/task-N-M.md

## Execution Protocol

### Phase 0: Orient
- Read PROGRESS.md to confirm this task is next
- Read your task file for full spec, acceptance criteria, files to create/modify
- Read ALL skill files listed in your task's Skills field
- Read relevant research files listed in your task

### Phase 1: Explore & Plan
- Explore existing codebase - understand what prior tasks built
- Read files you'll modify to understand current state
- Plan approach before writing code

### Phase 2: Implement
- Create feature branch: git checkout -b task/N-M-<short-description> <target-branch>
- Write code following existing patterns
- Write tests

### Phase 3: Test Locally
- Run all testing methods specified in your task file
- Unit tests, integration tests, API tests, browser tests, log checks
- For UI tasks: test as a real user would via Playwright
- Iterate until all tests pass

### Phase 4: Complete
- Update PROGRESS.md with status, branch, date, and notes
- Commit and merge to target branch
- Push to remote

## Available Tools
<List MCP servers and tools available to subagents>

## Key References
- DISCOVERY.md at .claude/orchestration-<slug>/DISCOVERY.md is top authority
- PHASES.md at .claude/orchestration-<slug>/PHASES.md for plan overview
- Skills at .claude/skills/ - read all listed in your task
- Research at .claude/orchestration-<slug>/research/
```

---

## Regression Tasks

Regression tasks use a different prompt:

```
This is a REGRESSION task. After deploying to the closest-to-live environment:
1. Deploy latest code to live/staging
2. Wait for deployment to complete
3. Run ALL tests from this phase on the deployed version
4. Test every feature built in this phase AND all prior phases
5. Check external service logs
6. Screenshot key screens as evidence
7. Update PROGRESS.md with regression results
8. If regression fails: create hotfix branch, fix, redeploy, retest until green
9. Merge phase branch to main/target
```

---

## Final Phase Tasks

The final phase tests on the fully deployed, live software:

```
This is a FINAL E2E task testing the fully deployed software.
1. Verify deployment is current and healthy
2. Test every user path and edge case
3. Apply all testing methods (unit, integration, API, browser, logs)
4. Verify all external service integrations
5. Performance and error handling validation
6. Iterate directly on main/target branch
7. Update PROGRESS.md with comprehensive results
```

---

## Orchestrator Rules

### Execution Order
- Execute ONE task at a time (sequential, not parallel)
- Follow task numbering within each phase
- Complete all tasks in a phase before moving to the next
- Regression task is always the last task in each phase

### Dependency Checking
- Before spawning, verify all dependency tasks are marked `done` in PROGRESS.md
- The only true blocker is a prior task not being complete

### Failure Handling (3-Tier Escalation)

**Tier 1: Subagent Self-Recovery** (automatic)
- Debug and fix within its own session
- Retry failed tool calls with different parameters
- Create missing dependencies inline

**Tier 2: Orchestrator Intervention** (if subagent reports failure)
- Read error output and PROGRESS.md notes
- Spawn a targeted fix subagent
- Re-run original task after fix

**Tier 3: User Escalation** (last resort)
- Provide: task number, what was attempted, the error, suggested fix
- Continue with next unblocked task while waiting

### Phase Transitions
- After regression task passes, update Phase Overview in PROGRESS.md
- Announce phase completion before starting next phase

### Session Boundaries
- If context is getting large, report progress and suggest starting fresh
- PROGRESS.md enables session continuity

---

## File Locations

| File | Path | Purpose |
|------|------|---------|
| Master plan | `.claude/orchestration-<slug>/PHASES.md` | All tasks, skills, testing methods |
| Orchestrator | `.claude/orchestration-<slug>/START.md` | This file |
| Discovery | `.claude/orchestration-<slug>/DISCOVERY.md` | Top authority for decisions |
| Research | `.claude/orchestration-<slug>/research/` | Research files |
| Task files | `.claude/orchestration-<slug>/tasks/phase-N/task-N-M.md` | Per-task specs |
| Progress | `PROGRESS.md` | Task status tracker |
| Skills | `.claude/skills/` | Project skills |
```

---

## Guidelines for START.md Creation

- **Include all available MCP tools** - list every tool the subagents can use
- **Include key file paths** - subagents need to find DISCOVERY.md, PHASES.md, research, skills
- **3-tier failure handling** - subagent self-recovery, orchestrator fix, user escalation
- **Session boundary awareness** - PROGRESS.md is the continuity mechanism
- **Customize for the project** - add project-specific tools, branches, deployment targets
