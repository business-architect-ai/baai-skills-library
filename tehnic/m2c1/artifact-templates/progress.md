# PROGRESS.md Template

Use this template when creating the progress tracker (Phase 12). This file enables session continuity - any new session reads it to know where things stand.

---

```markdown
# <Project Name> - Implementation Progress

**Target**: <Date or milestone>
**Current Phase**: <Phase N: Name> (Task N.M in progress)

---

## Phase Overview

| Phase | Status | Tasks Done | Total | Notes |
|-------|--------|------------|-------|-------|
| 1: <Name> | pending | 0 | <N> | |
| 2: <Name> | pending | 0 | <N> | |
| ... | | | | |
| N: E2E Testing | pending | 0 | <N> | |
| **Total** | | **0** | **<Total>** | |

---

## Task Progress

### Phase 1: <Name>

| Task | Title | Status | Branch | Date | Notes |
|------|-------|--------|--------|------|-------|
| 1.1 | <Title> | pending | | | |
| 1.2 | <Title> | pending | | | |
| ... | | | | | |
| 1.R | Phase 1 Regression | pending | | | |

### Phase 2: <Name>

| Task | Title | Status | Branch | Date | Notes |
|------|-------|--------|--------|------|-------|
| 2.1 | <Title> | pending | | | |
| ... | | | | | |

### Phase N: E2E Testing

| Task | Title | Status | Branch | Date | Notes |
|------|-------|--------|--------|------|-------|
| N.1 | <Title> | pending | | | |
| ... | | | | | |

---

## Regression Results

### Phase 1 Regression
- Status: pending
- Results: <TBD>

### Phase 2 Regression
- Status: pending
- Results: <TBD>

---

## Tool Setup Status

| Tool/Service | Status | Notes |
|-------------|--------|-------|
| <Tool> | pending | <Setup required> |
| ... | | |

---

## Blockers

| Blocker | Type | Status | Resolution |
|---------|------|--------|------------|
| <None> | | | |
```

---

## Guidelines for PROGRESS.md

- **This is the source of truth** for what's done, what's in progress, and what's next
- **Update after every task** - status, branch name, date, and notes
- **Status values**: `pending`, `in-progress`, `done`, `blocked`, `failed`
- **Notes should be substantive** - include key metrics (tests passing, files created, bugs fixed)
- **Regression results** - detailed pass/fail per check, not just "passed"
- **Session continuity** - a new session reads this file first to understand current state
- **Keep it current** - stale PROGRESS.md leads to duplicate work or missed tasks
