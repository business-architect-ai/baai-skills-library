# PHASES.md Template

Use this template when creating the master implementation plan (Phase 9). This is the blueprint that gets sharded into individual task files.

---

```markdown
# <Project Name> - Implementation Phases

**Target**: <Date or milestone>
**Execution**: Sequential phases, autonomous subagent execution
**Authority**: DISCOVERY.md overrides everything

---

## Scope Constraints (from DISCOVERY.md)

These are OUT of scope. Do NOT implement:
- <Excluded feature 1>
- <Excluded feature 2>
- ...

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| <Layer> | <Technology> |
| ... | ... |

---

## Skills Reference

All skills at `.claude/skills/`. Agents MUST read relevant skills before starting a task.

| Skill | Use When |
|-------|----------|
| `<skill-name>` | <When to use> |
| ... | ... |

---

## Tools Reference

| Server/Tool | Use For | Key Operations |
|-------------|---------|----------------|
| **Playwright** | Browser testing (localhost + production), external dashboard config | navigate, click, fill, upload, screenshot, evaluate, console |
| <Tool> | <Purpose> | <Key operations> |
| ... | ... | ... |

---

## Testing Methods

| Method | Tool | Description |
|--------|------|-------------|
| Unit tests | <Framework> | Service, controller, utility tests |
| Integration tests | <Framework> | Database, API endpoint tests |
| Browser testing (local) | Playwright MCP | Navigate localhost, test UI flows |
| Browser testing (live) | Playwright MCP | Navigate deployed URL for regression |
| API testing | <curl/httpie/MCP> | Direct API endpoint verification |
| Log checking | <Tool> | Backend/service error log verification |
| External service logs | <MCP/Dashboard> | Verify integrations work |
| ... | ... | ... |

---

## Phase Overview

| Phase | Goal | Tasks |
|-------|------|-------|
| 1: <Name> | <Goal> | <N> |
| 2: <Name> | <Goal> | <N> |
| ... | ... | ... |
| N: E2E Testing | Comprehensive multi-angle testing on live deployment | <N> |
| **Total** | | **<Total>** |

---

## Phase 1: <Name>

**Goal**: <What this phase achieves>

### Task 1.1: <Title>
- **Objective**: <What this task builds>
- **Dependencies**: <Blocking tasks, or "None">
- **Blocked by**: <What must complete first>
- **Files**: <Key files to create/modify>
- **Contracts**: <Data shapes, API endpoints, or interfaces shared with other tasks>
- **Acceptance Criteria**:
  - [ ] <Criterion>
  - [ ] <Criterion>
- **Testing**:
  - [ ] <Test type>: <What to test>
  - [ ] <Test type>: <What to test>
- **Skills**: <Skill names to read>

### Task 1.2: <Title>
...

### Task 1.R: Phase 1 Regression
- **Objective**: Full regression test of all Phase 1 tasks
- **Dependencies**: All Phase 1 tasks complete
- **Testing**:
  - [ ] Deploy to closest-to-live environment
  - [ ] Run all unit/integration tests
  - [ ] Full Playwright e2e on deployed URL
  - [ ] External service log verification
  - [ ] Screenshot key screens as evidence

---

## Phase 2: <Name>
...

---

## Phase N: Comprehensive E2E Testing

**Goal**: Multi-angle end-to-end testing on the fully deployed, live software

### Task N.1: <Testing Focus Area>
- Test every user path
- Verify all integrations
- Edge cases and error handling
- Performance validation

### Task N.2: <Another Testing Focus>
...

---

## Dependency Graph

```
1.1 -> 1.2 -> 1.3
              |
              v
       2.1 -> 2.2
              |
              v
       3.1 -> 3.2
```

---

## Task Execution Protocol

### For each task:
1. **Orient**: Read task file, skills, PROGRESS.md
2. **Plan**: Explore codebase, plan approach
3. **Implement**: Feature branch, write code, write tests
4. **Test**: Run all applicable testing methods locally
5. **Complete**: Update PROGRESS.md, commit, merge to target branch

### For regression tasks:
1. Deploy to live/staging environment
2. Run ALL task tests from the phase
3. Full e2e testing from every angle
4. Fix any failures, redeploy, retest
5. Merge phase branch to main

### For final phase:
1. All tasks are e2e testing on fully deployed live software
2. Every user path and edge case covered
3. Every testing method applied
4. Iterate on main/target branch until all green
```

---

## Guidelines for PHASES.md Creation

- **Read DISCOVERY.md first** - it's the top authority
- **Order phases by dependency** - foundation first, polish last, e2e testing always final
- **Every phase ends with regression** - the last task tests everything in that phase
- **Every task has acceptance criteria** - measurable, verifiable conditions
- **Every task has testing criteria** - specific tests to run
- **Document contracts** - API shapes and data formats shared between tasks
- **Include the dependency graph** - visual representation of task ordering
- **List skills per task** - agents read these before starting
- **The final phase is always e2e testing** - comprehensive, multi-angle, on live software
