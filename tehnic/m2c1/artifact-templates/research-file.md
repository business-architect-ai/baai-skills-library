# Research File Template

Use this template for all research output files (Phase 2 first wave and Phase 4 second wave).

---

```markdown
# <Research Domain> - Research

**Wave**: <First | Second>
**Researcher**: <Subagent description>
**Date**: <date>
**Status**: Complete

---

## Summary

<2-3 sentence overview of findings>

## Key Findings

### <Finding Category 1>

<Detailed findings with specifics - library names, version numbers, API endpoints, configuration patterns>

### <Finding Category 2>

<Detailed findings>

## Recommended Approach

Based on research, the recommended approach for this domain is:

1. <Specific recommendation>
2. <Specific recommendation>

## Alternatives Considered

| Option | Pros | Cons | Verdict |
|--------|------|------|---------|
| <Option A> | ... | ... | Recommended / Rejected |
| <Option B> | ... | ... | ... |

## Pitfalls and Edge Cases

- <Specific pitfall with mitigation>
- <Edge case to watch for>

## References

- <URL or source>
- <Documentation link>

---

## Second Wave Additions (if applicable)

### Implementation Details (filtered by DISCOVERY.md)

<Specific implementation guidance aligned with user's decisions>

### Tool and MCP Configuration

| Tool/Service | Purpose | Setup Required | Agent Can Self-Configure? |
|-------------|---------|----------------|---------------------------|
| <Tool> | <Why needed> | <API key / config> | Yes (Playwright) / No (user) |

### Testing Strategy

<How to test this domain as a real user would>

- Test assets needed: <list>
- Simulated inputs: <list>
- User flows to verify: <list>

### Human Actions Required

| Action | Who | How | Status |
|--------|-----|-----|--------|
| <Get API key> | User | <Instructions> | Pending |
| <Configure webhook> | Agent (Playwright) | <Steps> | Pending |
```

---

## Guidelines for Research Files

- **Be specific** - include version numbers, exact API shapes, real config snippets
- **Be thorough** - this research informs all downstream decisions
- **Distinguish facts from opinions** - clearly label recommendations vs findings
- **Second wave focuses on implementation** - how to build it, not what to build
- **Include testing angles** - what fixtures, assets, or simulated inputs would let an agent test this as a user would
- **Flag human-required actions** - what can the agent do in browser vs what truly needs the user
