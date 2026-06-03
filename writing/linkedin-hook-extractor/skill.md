---
name: linkedin-hook-extractor
description: Reverse-engineer the hook formula from a viral LinkedIn post URL. Returns which of the 10 canonical 2026 formulas it uses (anaphora, R.I.P., year-pivot, time-anchor, self-proving, odd-money, paid-vs-free, curiosity-gap, contrarian, comment-gate), why it worked, and a blank template. Use to learn from a competitor's post, not to write your own (use linkedin-post-writer).
source: https://github.com/sergebulaev/linkedin-skills (MIT License)
---

# LinkedIn Hook Extractor

Paste a viral LinkedIn post URL sau direct textul postului. Primești: ce formulă de hook folosește, structura exactă, de ce a funcționat, și un template gol mapat pe topicul tău.

## When to use

- User finds a viral post they want to study
- User wants to replicate a specific creator's pattern
- Before `linkedin-post-writer` to seed a draft with a proven structure

## Input

A LinkedIn post URL (any type: activity, share, ugcPost) or the full post text.

## Output

- **Formula identified** (F1-F10) with confidence score
- **Structural breakdown:**
  - Hook lines (first 210 chars)
  - Body architecture (sections + what each does)
  - Close pattern
  - Reaction-triggering devices (numbers, named entities, vulnerabilities)
- **Why it worked** psychologically
- **Blank template** filled with slot markers matched to the original, ready for the user's voice
- **Cautions:** anything in the original post that would fail 2026 audit (em dashes, AI vocab, outdated tactics)

## Steps

1. **Parse input.** Accept URL or pasted text.
2. **Fetch post body.** If URL is provided and Apify is available, fetch. Otherwise ask the user to paste the text.
3. **Classify.** Match against the 10 formulas using features:
   - First 2 lines: anaphoric? question? confession? number-led?
   - Body: numbered list? dated receipts? ledger? teardown?
   - Close: mirror question? identity reframe? commitment?
4. **Score confidence.** If multiple formulas fit, return top 2 with fit scores.
5. **Extract structure.** Pull each logical section and label it by formula role.
6. **Generate blank template.** Replace specifics with `{slot}` markers that match the user's topic.
7. **Audit the source.** Flag any AI tells in the original so the user doesn't copy them.

## The 10 formulas

| Code | Formula | Best for |
|---|---|---|
| F1 | Platform Risk Anaphora | Category/platform posts |
| F2 | R.I.P. Obituary | Era-ending claims |
| F3 | Year-over-Year Pivot | Identity shifts |
| F4 | Time-Anchor Confession | Vulnerability |
| F5 | Self-Proving Meta | Commitment-based |
| F6 | Comment-Gate Lead Magnet | List building |
| F7 | Odd-Precision Money Ledger | Build-logs, cost breakdowns |
| F8 | Paid-vs-Free Reversal | Free framework give-away |
| F9 | Curiosity-Gap Teaser | Behind-the-scenes |
| F10 | Contrarian + Historical Receipts | Sacred-cow takes |

## Related skills

- `linkedin-post-writer` — use the extracted template to draft your own
- `linkedin-humanizer --mode audit` — audit your draft before shipping
