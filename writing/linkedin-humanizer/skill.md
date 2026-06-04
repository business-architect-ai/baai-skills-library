---
name: linkedin-humanizer
compatibility: codex-and-claude-code
description: 'Scrub AI tells from any text draft OR audit a finished post against the 2026 algorithm heuristic checklist. Tier-based rewriter (forensic / strict / aesthetic / all) plus --mode audit for detection-only pass-fail review covering length, hook, CTA, format penalties, AI vocab. Triggers on "humanize", "de-AI", "review this draft", "audit before posting", "is this ready".'
source: https://github.com/sergebulaev/linkedin-skills (MIT License)
---

# LinkedIn Humanizer V2

Rescrie orice text pentru a elimina semnele AI. Bazat pe taxonomia Wikipedia "Signs of AI writing" plus pattern-uri LinkedIn-specifice 2026. V2: regulile sunt acum împărțite în 3 tiere.

## When to use

- Before publishing any AI-drafted post or comment (rewrite mode)
- Pre-publish review of a finished draft (audit mode)
- When a draft feels off and you can't pinpoint why

## Modes

```
# Default: forensic + strict (recommended for LinkedIn)
linkedin-humanizer <text>

# Forensic only — minimum-touch, just kill the leakage
linkedin-humanizer --mode forensic <text>

# Strict — forensic + corporate-speak
linkedin-humanizer --mode strict <text>

# Aesthetic — strict + style rules (em dashes, rule of three)
linkedin-humanizer --mode aesthetic <text>

# All — every rule. Maximum scrub.
linkedin-humanizer --mode all <text>

# Audit — detection-only pass-fail review. No rewrite.
linkedin-humanizer --mode audit <text>
```

## The three passes

### Pass 1 — SCRUB (delete or replace)

**FORENSIC tier** (always on): real model leakage no human produces.
- AI tool markers (oaicite, contentReference, turn0search0)
- Knowledge-cutoff disclaimers ("As of my last update...")
- Phrasal templates ([Your Name], 2025-XX-XX)
- Em dash overuse (3+ in <300 words)
- Outline-formula closers ("Despite its X... Looking ahead...")

**STRICT tier** (default on): corporate-speak bad on LinkedIn regardless of origin.
- Vocabulary swaps: leverage->use, utilize->use, delve->look, harness->use, foster->build
- Filler-adverb deletion: fundamentally, essentially, ultimately, crucially, notably
- Phrase cleanup: "in today's fast-paced world", "game-changer", "deep dive", "move the needle"
- All 6 forms of negative parallelism
- Cliché closers: "What do you think?", "Tag someone who needs this"

**AESTHETIC tier** (opt-in only, will flatten literary writing):
- Single em dash use
- Rule-of-three triplets
- Vocab: robust->solid, cultivate->grow, vibrant->alive, garner->get
- Passive voice

### Pass 2 — BREAK (force burstiness)

Target: Flesch reading ease >55. Sentence length variance >40%.

- If all sentences are 15-22 words, force-break at least 1 in 3 into <8-word sentences
- Add at least one sentence fragment ("Worth it.", "Every time.")
- Break perfect parallel structures with one asymmetric sentence
- Alternate long sentences with short ones

### Pass 3 — ADD (human fingerprints)

Require at least:
- 1 specific number per 100 words (replace "many" / "significant" / "massive")
- 1 named entity (real person, company, date, city)
- 1 first-person sensory detail
- 1 contradiction or self-correction
- 1 moment of vulnerability or stakes

If the input lacks these, ask the user for a specific number or anecdote to plug in. Don't fabricate.

## Non-negotiable rules

- Preserve the user's actual claim. Humanizing does not mean changing meaning.
- Never introduce facts that weren't in the input. If a number is missing, ask.
- Keep the user's sentence-level voice quirks (lowercase starts, `..` soft pauses).
- Negative parallelism is a HARD ban: the strict tier always strips all 6 forms.

## Output

- Rewritten text with AI tells removed
- Diff showing what changed and why
- Confidence: "human", "mixed", "AI-likely"
- Tier applied

## Related skills

- `linkedin-post-writer` — generates drafts that already pass the humanizer
- `linkedin-hook-extractor` — reverse-engineer a hook from a viral post
