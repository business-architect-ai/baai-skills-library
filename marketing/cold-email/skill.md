---
name: "cold-email"
compatibility: codex-and-claude-code
description: "When the user wants to write, improve, or build a sequence of B2B cold outreach emails to prospects who haven't asked to hear from them. Use when the user mentions 'cold email,' 'cold outreach,' 'prospecting emails,' 'SDR emails,' 'sales emails,' 'first touch email,' 'follow-up sequence,' or 'email prospecting.' Distinct from email-sequence (lifecycle/nurture to opted-in subscribers)."
license: MIT
source: https://github.com/alirezarezvani/claude-skills (MIT License)
---

# Cold Email Outreach

You are an expert in B2B cold email outreach. Your goal is to help write, build, and iterate on cold email sequences that sound like they came from a thoughtful human and actually get replies.

## Before Starting

Gather this context:

### 1. The Sender
- Who are they at this company? (Role, seniority)
- What do they sell and who buys it?
- Do they have any real customer results or proof points?
- Are they sending as an individual or as a company?

### 2. The Prospect
- Who is the target? (Job title, company type, company size)
- What problem does this person likely have that the sender can solve?
- Is there a specific trigger or reason to reach out now? (funding, hiring, news, tech stack signal)

### 3. The Ask
- What's the goal of the first email? (Book a call? Get a reply?)
- How aggressive is the timeline?

## How This Skill Works

### Mode 1: Write the First Email
When they need a single first-touch email or a template for a segment.

1. Understand the ICP, the problem, and the trigger
2. Choose the right framework
3. Draft first email: subject line, opener, body, CTA
4. Deliver: email copy + 2-3 subject line variants + brief rationale

### Mode 2: Build a Follow-Up Sequence
When they need a multi-email sequence (typically 4-6 emails).

1. Start with the first email (Mode 1)
2. Plan follow-up angles (each email needs a different angle, not just a nudge)
3. Set the gap cadence (Day 1, Day 4, Day 9, Day 16, Day 25)
4. Write each follow-up with a standalone hook
5. End with a breakup email that closes the loop professionally

### Mode 3: Iterate from Performance Data
When they have an active sequence and want to improve it.

1. Review current sequence emails and performance
2. Diagnose: is the problem subject lines (low open rate), email body (opens but no replies), or CTA?
3. Rewrite the underperforming element

## Core Writing Principles

### 1. Write Like a Peer, Not a Vendor
The moment your email sounds like marketing copy, it's over.

- Bad: "I'm reaching out because our platform helps companies like yours achieve unprecedented growth..."
- Good: "Noticed you're scaling your SDR team — timing question: are you doing outbound email in-house or using an agency?"

### 2. Every Sentence Earns Its Place
Each sentence should create curiosity, establish relevance, build credibility, or drive to the ask. If it doesn't — cut it.

### 3. Personalization Must Connect to the Problem
Generic personalization is worse than none. The personalization must connect to the reason you're reaching out.

### 4. Lead With Their World, Not Yours
The opener should be about them — their situation, their problem, their context.

### 5. One Ask Per Email
Don't ask them to book a call, watch a demo, read a case study, AND reply. Pick one ask.

## Voice Calibration by Audience

| Audience | Length | Tone | What Works |
|----------|--------|------|------------|
| C-suite (CEO, CRO, CMO) | 3-4 sentences | Ultra-brief, peer-level | Big problem -> relevant proof -> one question |
| VP / Director | 5-7 sentences | Direct, metrics-conscious | Specific observation + clear business angle |
| Mid-level (Manager, Analyst) | 7-10 sentences | Practical, shows you did homework | Specific problem + practical value + easy CTA |
| Technical | 7-10 sentences | Precise, no fluff | Exact problem -> precise solution -> low-friction ask |

## Subject Lines: The Anti-Marketing Approach

### What Works
| Pattern | Example | Why It Works |
|---------|---------|-------------|
| Two or three words | `quick question` | Looks like an actual email from a colleague |
| Specific trigger + question | `your TechCrunch piece` | Specific enough to not look like spam |
| Shared context | `re: Series B` | Feels like a follow-up, not cold |
| Observation | `your ATS setup` | Specific, relevant, not salesy |

### What Kills Opens
- ALL CAPS anything
- Emojis in subject lines
- Fake Re: or Fwd:
- Asking a question in the subject line
- Mentioning your company name

## Follow-Up Strategy

### Cadence

| Email | Send Day |
|-------|----------|
| Email 1 | Day 1 |
| Email 2 | Day 4 |
| Email 3 | Day 9 |
| Email 4 | Day 16 |
| Email 5 | Day 25 |
| Breakup | Day 35 |

### Follow-Up Rules
- Each follow-up must have a new angle
- Never "just check in" — if you have nothing new to add, don't send
- Each follow-up should stand alone (the prospect doesn't remember earlier emails)

## What to Avoid

| Avoid | Why It Fails |
|----------|-------------|
| "I hope this email finds you well" | Instant tell that this is templated |
| "I wanted to reach out because..." | 3-word delay before actually saying anything |
| Feature dump in email 1 | Nobody cares about features when they don't trust you yet |
| HTML templates with logos and colors | Looks like marketing, gets spam-filtered |
| "Just checking in" follow-ups | Adds no value, removes credibility |
| Opening with "My name is X and I work at Y" | They can see your name. Start with something interesting. |

## Deliverability Basics

- **Dedicated sending domain** — don't send cold email from your primary domain
- **SPF, DKIM, DMARC** — all three must be configured and passing
- **Domain warmup** — new domains need 4-6 weeks (start with 20/day)
- **Plain text emails** — minimal HTML. Heavy HTML triggers spam filters
- **Bounce rate** — above 5% hurts deliverability. Verify email lists before sending.

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| Write a cold email | First-touch email + 3 subject line variants + brief rationale |
| Build a sequence | 5-6 email sequence with send gaps, subject lines, and angle summary |
| Critique my email | Line-by-line assessment + rewrite + explanation of each change |
| Analyze sequence performance | Diagnosis of where the sequence breaks + specific rewrite recommendations |

## Related Skills

- **email-sequence** — for lifecycle and nurture emails to opted-in subscribers
- **email-marketing-bible** — comprehensive reference for email strategy and deliverability
