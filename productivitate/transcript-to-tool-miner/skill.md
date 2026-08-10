---
name: transcript-to-tool-miner
compatibility: codex-and-claude-code
description: Use when a user wants reusable tools, operational principles, workflows, evaluators, or skill candidates extracted from transcripts, videos, podcasts, interviews, notes, or research corpora, especially when product news and vendor details obscure transferable patterns.
---

# Transcript-to-Tool Miner

## Core rule

Convert source evidence into durable operational assets, not a general summary or product recommendation. Preserve traceability; never claim to have read unavailable material or fill gaps from memory.

## When not to use

Do not use for ordinary summarization, translation, transcription, fact-checking, or automatic implementation. Do not publish, message, install integrations, or imitate a person's identity or voice.

## Input scope

Accept pasted text, one file, an explicit file list, or a folder. If scope is ambiguous, ask for the source or path; never expand one requested file to its directory. In corpus mode, process batches of at most 25 files and track processed, skipped, incomplete, and unreadable sources. Follow the user's language.

## Workflow

1. **Source inventory:** record identifiers, paths when available, language, and coverage limits.
2. **Evidence extraction:** retain passages describing repeatable procedures, decisions, checks, transformations, reusable roles, or measurable feedback loops. Treat source-specific counts and thresholds as evidence, not universal requirements unless independently supported.
3. **Capability abstraction:** name the transferable capability; keep products, models, prices, benchmarks, interface steps, announcements, and reviewer impressions as evidence or rejected noise. Label time-sensitive public claims unverified unless separately verified.
4. **Asset classification:** assign exactly one primary type: `instrument`, `principle`, `workflow`, or `eval`. Separate independently invokable capabilities and evaluation gates; connect them through compositions when useful.
5. **Toolizability gate:** require the applicable contract in the output reference; reject incomplete signals and name each missing element.
6. **Durability filter:** penalize volatile or vendor-dependent packaging; disclose any dependency.
7. **Deduplication:** merge only materially equivalent candidates while preserving every supporting source.
8. **Composition:** when two or more distinct candidates can cooperate, record at least one ordered composition without collapsing them.
9. **Scoring:** apply every rubric dimension and exclusion rule.
10. **Shortlist:** rank at most five eligible candidates by expected value relative to build effort.
11. **Coverage disclosure:** state what was processed, skipped, unreadable, incomplete, or revised and why.

## Acceptance gates

Every accepted item must have one primary type, source evidence, confidence, and the full type-specific contract. Conflicts remain explicit. A later corpus batch may revise an item only with new evidence and a recorded reason. If nothing qualifies, say so and report the strongest rejected signals.

## Output

Before producing the report, read `references/output-contract.md` and `references/scoring-rubric.md` completely. Follow their required order, fields, scoring, deduplication, and shortlist rules. Return it in conversation unless a file is requested. Without a supplied path, use `tool-extractions/YYYY-MM-DD-<source-slug>.md` in the current workspace.

## Self-check

Confirm all seven headings appear in order; every accepted candidate is traceable, typed, operational, validated, scored, and dependency-aware; distinct assets remain separate; volatile claims are classified; the shortlist is eligible and deduplicated; coverage is honest.
