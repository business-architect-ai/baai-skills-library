# DISCOVERY.md Template

Use this template when creating the Discovery document (Phase 3). This becomes the **top authority** document - all other artifacts defer to it.

---

```markdown
# <Project Name> - Discovery Document

**Created**: <date>
**Status**: <In Progress | Complete>
**Rounds of Q&A**: <N>

---

## 1. <Domain Category>

**D1: <Question>**
A: <User's answer>

**D2: <Question>**
A: <User's answer>

---

## 2. <Domain Category>

**D3: <Question>**
A: <User's answer>

**D4: <Question>**
A: <User's answer>

---

## N. <Domain Category>

...
```

---

## Guidelines for Discovery Questions

### What to Ask About

1. **Vision and Goals** - What is this? Who is it for? What does success look like?
2. **Scope and Boundaries** - What's IN scope? What's explicitly OUT? What's deferred?
3. **Technical Stack** - Preferences for languages, frameworks, databases, hosting?
4. **UX and Design** - Visual style, layout, navigation, branding, responsive needs?
5. **Data Model** - What entities exist? Relationships? Key constraints?
6. **External Services** - Payments, email, analytics, auth providers, APIs?
7. **Auth and Security** - Auth method, roles, permissions, data sensitivity?
8. **Testing and Deployment** - CI/CD, staging environments, testing philosophy?
9. **Edge Cases** - Error handling, offline behavior, concurrent users?
10. **Domain-Specific** - Any questions unique to the project's domain

### Question Style

- **Ask specific, decision-forcing questions** - not "tell me about auth" but "email+password, social OAuth, or magic link?"
- **Offer options when relevant** - "Option A: X. Option B: Y. Which do you prefer?"
- **Ask follow-ups** - don't accept vague answers, drill down to specifics
- **Number every decision** - D1, D2, D3... for easy cross-referencing
- **Group by domain** - makes the document scannable

### Critical Rules

- **DISCOVERY.md is the top authority** - it overrides PRD, research files, and all other docs
- **Store EVERY question and answer** - even "obvious" ones, for completeness
- **Don't stop too early** - keep asking until you have enough detail to build production software
- **Include scope exclusions** - "what's NOT in scope" decisions are as important as inclusions
- **After all Q&A, update the status** to "Complete" and record total rounds
