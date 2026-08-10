# Task File Template

Use this template when creating detailed task files (Phase 10). Each task file IS the complete prompt that an execution subagent receives. It must contain everything the agent needs to work autonomously.

---

```markdown
# Task N.M: <Title>

## Objective

<Clear, concise description of what this task builds or achieves. 2-3 sentences.>

## Context

<How this task fits into the broader phase and project. What came before it and what depends on it.>

## Dependencies

- <Task X.Y> - <What it provides that this task needs>
- Or: None (first task)

## Blocked By

- <List of tasks that must complete before this one starts>

## Research Findings

Key findings from research files relevant to this task:

- From `<research-file>.md`: <Key finding>
- From `<research-file>.md`: <Key finding>

## Implementation Plan

### Step 1: <Name>

<Detailed implementation guidance. Include:>
- What to create or modify
- Code patterns to follow
- Configuration details
- Key decisions from DISCOVERY.md that apply

### Step 2: <Name>

<Detailed implementation guidance>

### Step N: <Name>

<Detailed implementation guidance>

## Files to Create

- `<path/to/file>` - <Purpose>
- ...

## Files to Modify

- `<path/to/file>` - <What to change>
- ...

## Contracts

### Provides (for downstream tasks)

- <API endpoint>: `<method> <path>` - <Request/Response shape>
- <Data model>: <Schema or interface>
- <Shared type>: <Type definition>

### Consumes (from upstream tasks)

- <API endpoint from Task X.Y>: <How this task uses it>
- <Data model from Task X.Y>: <How this task depends on it>

## Acceptance Criteria

- [ ] <Measurable criterion>
- [ ] <Measurable criterion>
- [ ] <Measurable criterion>
- [ ] All tests pass
- [ ] Build succeeds

## Testing Protocol

### Unit/Integration Tests

- Test file: `<path/to/test/file>`
- Test cases:
  - [ ] <Specific test case>
  - [ ] <Specific test case>

### API/Script Testing

- <Endpoint or script to test>
- Expected behavior: <What should happen>

### Browser Testing (Playwright MCP)

- Start: <How to start dev servers>
- Navigate to: <URL>
- Actions: <What to do in the browser>
- Verify: <What to check>
- User-emulating flow: <Step-by-step as a real user would>
- Test assets: <Files to upload, data to input>
- Screenshot: <Key screens to capture>

### External Service Verification

- <Service>: <How to verify integration works>

### Build/Lint/Type Checks

- [ ] `<build command>` succeeds
- [ ] `<lint command>` passes (if applicable)
- [ ] `<type check command>` passes

## Skills to Read

- `<skill-name>` - <Why>
- `<skill-name>` - <Why>

## Research Files to Read

- `.claude/orchestration-<slug>/research/<file>.md` - <Why>

## Git

- Branch: `<branch-naming-pattern>`
- Commit message prefix: `Task N.M:`
```

---

## Guidelines for Task File Creation

- **Self-contained** - the execution agent should need nothing beyond this file, the referenced skills, and the codebase
- **Specific** - include exact file paths, API shapes, config values
- **Testing is comprehensive** - every testable aspect has a test method specified
- **User-emulating tests** - for any UI, describe the exact steps a real user would take (navigate, click, type, upload, verify)
- **Include test assets** - if the user would upload a file, specify what test file to create or use
- **Reference skills and research** - point to the exact files the agent should read
- **Include contracts** - what this task provides to and consumes from other tasks
- **Git conventions** - branch name and commit prefix are specified
- **Step-by-step implementation** - guide the agent through the work, don't just state requirements
- **Include edge cases** - don't just test the happy path
