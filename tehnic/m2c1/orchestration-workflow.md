# M2C1 Orchestration Workflow

12-phase protocol from brain dump to fully tested, deployed software. Each phase references artifact templates in `artifact-templates/`.

---

## Phase 0: Setup

**Actor:** Main agent

1. Verify Playwright MCP is available (hard prerequisite - do not proceed without it)
2. Create orchestration folder: `.claude/orchestration-<auto-slug>/` where slug is auto-generated from the project idea (e.g., `orchestration-task-manager`, `orchestration-ecommerce-api`)
3. Create subfolders: `research/`, `tasks/`, `skills/`

---

## Phase 1: Brain Dump to PRD

**Actor:** Main agent

1. Receive the user's brain dump (could be a paragraph, a conversation, a doc, or a rambling voice-to-text)
2. Read template: `artifact-templates/prd.md`
3. Synthesize into a structured PRD, strictly under 500 lines
4. Save to: `.claude/orchestration-<slug>/PRD.md`
5. Present PRD to user for quick confirmation before proceeding

**Output:** `PRD.md`

---

## Phase 2: First Research Wave

**Actor:** Parallel background subagents (one per domain)

The number of subagents depends on how many distinct domains the project spans. Each subagent researches one angle of the PRD.

1. Main agent reads the PRD and identifies distinct research domains (e.g., "authentication", "payment processing", "data modeling", "frontend framework", "deployment")
2. For each domain, spawn a background subagent with this prompt pattern:

```
You are a research agent for the "<domain>" aspect of this project.

Read the PRD at: .claude/orchestration-<slug>/PRD.md

Research thoroughly:
- Current best practices for <domain>
- Available libraries, frameworks, tools
- Common pitfalls and edge cases
- Architecture patterns that work well
- Any relevant APIs, services, or integrations

Store your complete research in a single file at:
.claude/orchestration-<slug>/research/<domain-slug>.md

Follow the research file template at: ~/.claude/skills/m2c1/artifact-templates/research-file.md

Be thorough - this research will inform all implementation decisions.
```

3. Wait for all research subagents to complete

**Output:** Multiple files in `research/` folder

---

## Phase 3: Discovery Questions

**Actor:** Main agent

This is the most critical phase. The agent asks the user MANY questions to fully clarify scope, preferences, constraints, and decisions. The goal is production-ready clarity - every ambiguity resolved, every edge case addressed, every integration specified.

### 3a. User's Workspace Research

Before asking questions, research the user's broader workspace for business context:

1. Explore the user's project directory structure, any existing CLAUDE.md files, README files, or documentation
2. Identify existing projects, communities, business context, revenue streams, audiences
3. Find existing code, tools, style guides, or assets that could be leveraged
4. Understand the user's workflow patterns, communication style, and technical preferences
5. This context informs smarter, more relevant discovery questions

### 3b. Comprehensive Q&A

1. Read ALL research files from Phase 2
2. Read template: `artifact-templates/discovery.md`
3. Ask the user a comprehensive series of questions, organized by domain:
   - Vision and goals
   - Scope and boundaries (what's IN, what's OUT)
   - Technical stack preferences
   - UX and design decisions
   - Data model and architecture
   - External services and integrations
   - Testing and deployment strategy
   - Edge cases and error handling
   - Performance and scale requirements
   - Content strategy and output formats (if applicable)
   - Error alerting and monitoring
   - Security and secrets management
   - CLI/API interface design
   - Breaking/edge case workflows
   - Weekend/scheduling behavior
   - Quality gates and acceptance criteria
   - Analytics and feedback loops
   - Any domain-specific decisions
4. Use AskUserQuestion tool for each batch of questions
5. After EVERY question is answered, store the Q&A in DISCOVERY.md
6. Continue asking until the full scope is clear - err on the side of asking too many questions
7. Number every decision (D1, D2, D3...) for cross-referencing

### 3c. Discovery Completeness Check (MANDATORY)

**Before moving to Phase 4, the agent MUST perform a self-audit.** This is not optional.

1. Re-read the complete DISCOVERY.md and all research files
2. For EACH of the following categories, verify that sufficient decisions exist. If any category has gaps, ask MORE questions before proceeding:

   | Category | Check |
   |----------|-------|
   | **Data model** | Are all entities, schemas, and relationships defined? |
   | **Every external service** | Is every API, tool, and integration fully specified (auth method, endpoints, rate limits, fallback)? |
   | **Every content type/output** | Is the exact format, length, tone, and structure defined? |
   | **Error handling** | What happens when each component fails? Alerting strategy? |
   | **Security** | How are secrets stored? What access patterns exist? |
   | **Testing strategy** | How will each component be tested? What does "working" mean? |
   | **Edge cases** | Slow days, breaking events, partial failures, retries, rate limits? |
   | **Performance** | Speed requirements, cost budgets, concurrency limits? |
   | **User workflow** | How does the user interact with the system day-to-day? |
   | **Deployment** | Where does it run? How is it triggered? How is it monitored? |
   | **Platform-specific constraints** | Character limits, media specs, API quirks per platform? |
   | **Existing assets** | What code, templates, accounts, credentials already exist? |

3. Ask yourself: **"If an execution agent read only DISCOVERY.md, could it make every implementation decision without guessing?"** If the answer is NO, identify the gaps and ask more questions.

4. Only proceed to Phase 4 when the answer is YES.

**Output:** `DISCOVERY.md` - the top authority document for all decisions, verified complete

---

## Phase 4: Second Research Wave

**Actor:** Parallel background subagents

Now that the user's clarifications exist in DISCOVERY.md, deploy a second wave of research subagents. These research with a new lens - through the user's answers.

1. Main agent identifies new research domains needed post-discovery. This wave focuses on:
   - **Implementation-focused research** - how to build what was decided, filtered by DISCOVERY.md
   - **Tool and MCP research** - what MCP servers, CLIs, external services would enable autonomous agent development
   - **Human action research** - what API keys, accounts, configurations, tokens need to be set up (the agent will do these in browser via Playwright where possible)
   - **Testing strategy research** - what assets, fixtures, simulated inputs, and strategies are needed for agents to test the software as a real user would (uploading files, navigating flows, filling forms, triggering edge cases)
   - **Deployment research** - how to get the software live for testing (hosting, CI/CD, domains, etc.)

2. For each domain, spawn a background subagent:

```
You are a second-wave research agent for "<domain>".

FIRST, read these files:
- DISCOVERY.md at: .claude/orchestration-<slug>/DISCOVERY.md
- Relevant first-wave research at: .claude/orchestration-<slug>/research/<relevant-files>

Then research with the lens of the user's clarified decisions:
- Implementation approaches that align with DISCOVERY.md decisions
- Specific tools, MCP servers, CLIs that would enable autonomous development
- What accounts/API keys/tokens need to be configured (and how to configure them)
- Testing strategies: what assets or fixtures are needed to test as a real user would
- How to deploy/publish for live testing

Store output at: .claude/orchestration-<slug>/research/<domain-slug>-implementation.md
Follow template: ~/.claude/skills/m2c1/artifact-templates/research-file.md
```

3. Wait for all subagents to complete

**Output:** Additional files in `research/` folder (implementation-focused)

---

## Phase 5: Tool Setup

**Actor:** Main agent (with user providing login credentials when needed)

**This phase is MANDATORY.** The agent must actually configure every tool - not just list what's needed. The agent autonomously completes all "human steps" via Playwright browser automation, only asking the user for credentials it cannot obtain on its own.

### 5a. Tool Inventory

1. Read all second-wave research files
2. Compile a comprehensive inventory of EVERY tool, service, API, and configuration needed:

   | Category | Examples |
   |----------|----------|
   | **MCP servers** | Any new MCP servers to install and configure |
   | **API keys** | Every external API that needs a key/token |
   | **Accounts** | Services where accounts need to be created |
   | **Browser sessions** | Services requiring login cookies for Playwright |
   | **CLI tools** | Any CLI tools to install (npm, pip, brew, etc.) |
   | **Environment variables** | Every .env variable the project needs |
   | **Configuration files** | Any config files to create (JSON, YAML, etc.) |

3. For each tool, classify the setup action:
   - **Agent can do autonomously** - install via CLI, generate config files, etc.
   - **Agent can do via Playwright** - sign up, generate API keys, configure settings in browser dashboards
   - **Requires user credentials** - user must provide login credentials for the agent to use in Playwright
   - **User must do manually** - truly cannot be automated (e.g., phone verification, payment)

### 5b. Credential Collection

1. Present the user with a clear list of credentials needed:
   - Which services need login (username/password or existing browser session)
   - Which API keys the user already has
   - Which accounts need to be created (agent will create them if possible)
2. Ask the user to provide credentials or log into services so the agent can capture session cookies

### 5c. Autonomous Configuration

The agent MUST execute these steps, not just document them:

1. **Install MCP servers** - Run `claude mcp add-json` commands, verify they load
2. **Install CLI tools** - Run install commands, verify with `--version`
3. **Generate API keys** - Navigate to service dashboards via Playwright, create API keys, copy them to `.env`
4. **Configure services** - Set up webhooks, create projects, configure settings in external dashboards via Playwright
5. **Export browser sessions** - Save Playwright `storage_state()` for services requiring persistent login
6. **Create .env file** - Write all API keys, tokens, and configuration to the project's `.env` file
7. **Create config files** - Generate any JSON/YAML configuration files needed
8. **Install dependencies** - Run package manager install commands

### 5d. Setup Verification

After each tool is configured, immediately test it:
- Make a test API call with each API key
- Verify each MCP server responds
- Verify each CLI tool runs
- Verify each browser session is valid

If any setup fails, debug and retry before moving on. Only escalate to user if truly stuck.

**Output:** All tools configured, credentials stored, dependencies installed, everything verified working

---

## Phase 6: Tool Verification

**Actor:** Main agent

**This phase is MANDATORY and cannot be skipped.** Every single tool must be verified with a real operation before proceeding. If Phase 5d already verified tools inline, this phase serves as a comprehensive re-verification and produces the formal verification report.

### Verification Protocol

For EACH tool in the inventory, perform the appropriate verification:

| Tool Type | Verification Method |
|-----------|-------------------|
| **MCP server** | Call a real read/list operation. Verify response is valid. |
| **API key** | Make a real API call (not just auth check). Verify response data. |
| **CLI tool** | Run `--version` or `--help`. Verify expected output. |
| **Browser session** | Navigate to the service dashboard via Playwright. Verify logged-in state. |
| **Database** | Create a test table, insert a row, query it, delete it. |
| **File system** | Verify all required directories exist and are writable. |
| **Config file** | Parse the config, verify all required keys are present and valid. |
| **Environment vars** | Verify all required .env variables are set and non-empty. |

### Verification Report

Create a verification report at `.claude/orchestration-<slug>/reports/tool-verification.md`:

```
| Tool | Type | Status | Test Performed | Notes |
|------|------|--------|---------------|-------|
| Playwright MCP | MCP | PASS | Navigated to google.com | - |
| Anthropic API | API Key | PASS | Listed models | - |
| ...
```

### Failure Protocol

- If ANY tool fails verification: debug, fix, and re-verify
- If a tool cannot be fixed: escalate to user with specific error details
- **Do NOT proceed to Phase 7 until ALL tools pass verification**
- The verification report must show 100% PASS before moving on

**Output:** Verification report with all tools confirmed working

---

## Phase 7: Skill Creation

**Actor:** Parallel background subagents

**This phase is MANDATORY and cannot be skipped.** Skills are the knowledge layer that execution agents read to understand HOW to use every tool, service, and pattern in the project. Without skills, execution agents operate blind - they'll guess at API shapes, miss edge cases, and produce brittle code. Every tool, every external service, every research domain, and every testing strategy MUST have a corresponding skill.

### 7a. Skill Inventory (MANDATORY)

The main agent MUST create skills for ALL of the following categories. This is not a suggestion - it is a requirement. Review each category against the project's research files and DISCOVERY.md:

| Category | What to Create | Example |
|----------|---------------|---------|
| **Each external tool/API** | One skill per external service the project integrates with | `apify-twitter-scraping`, `blotato-api`, `whisper-transcription` |
| **Each MCP server** | One skill per MCP server used in the project | `playwright-automation`, `notion-mcp` |
| **Each external data source** | One skill per data source the project reads from | `rss-feed-collection`, `reddit-praw`, `hackernews-algolia` |
| **Each research domain** | One skill per major research area from Phase 2/4 | `content-synthesis-pipeline`, `topic-clustering`, `voice-style-extraction` |
| **Each testing strategy** | One skill per unique testing approach | `pipeline-dry-run-testing`, `playwright-e2e-testing`, `api-integration-testing` |
| **Each unique framework/library** | One skill per framework that's non-trivial to use | `sentence-transformers-clustering`, `click-cli-framework`, `jinja2-templates` |
| **Each distribution channel** | One skill per platform content is distributed to | `x-articles-playwright`, `skool-posting`, `linkedin-distribution` |
| **Project architecture** | One skill documenting the overall project structure | `pulse-engine-architecture` (or project-specific equivalent) |

### 7b. Skill Content Requirements

Each skill MUST include (not optional):

1. **What it is** - Clear description of the tool/domain
2. **When to use it** - Trigger conditions for execution agents
3. **Authentication/setup** - How to authenticate, what env vars are needed
4. **Key API patterns** - Request/response formats, code examples, endpoint URLs
5. **Rate limits and constraints** - What limits exist, how to handle them
6. **Common pitfalls** - Specific things that go wrong and how to avoid them
7. **Testing strategy** - How to verify this component works, what test fixtures are needed
8. **Cost implications** - API costs, rate limit costs, any budget considerations
9. **References** - Links to research files for deeper context

### 7c. Skill Creation Process

1. Main agent compiles the full skill inventory from 7a
2. For each skill, spawn a background subagent:

```
Create a Claude Code skill at: .claude/skills/<skill-name>/SKILL.md

Read these files first for context:
- DISCOVERY.md at: .claude/orchestration-<slug>/DISCOVERY.md
- Relevant research files at: .claude/orchestration-<slug>/research/
- Tool verification report at: .claude/orchestration-<slug>/reports/tool-verification.md

The skill MUST document (all required):
- What the tool/domain is and when to use it
- Authentication and setup (env vars, API keys, session cookies)
- Key commands, APIs, endpoints, or patterns with code examples
- Rate limits, constraints, and cost implications
- Common pitfalls with specific mitigations
- Testing strategies and relevant test assets/fixtures
- References to research files for deeper context

Follow Claude Code skill format:
---
name: <skill-name>
description: <What it does>. Use when <trigger conditions>.
---

Save to: .claude/skills/<skill-name>/SKILL.md
```

3. Wait for ALL skill creation subagents to complete
4. Verify every skill file exists and contains all required sections

### 7d. Skill Completeness Check

Before proceeding, verify:
- Every tool from the verification report has a corresponding skill
- Every research domain has a corresponding skill
- Every testing strategy has a corresponding skill
- Every external data source has a corresponding skill
- No skill is a stub or placeholder - all contain actionable implementation guidance

**Output:** Comprehensive skills in `.claude/skills/`, one per tool/domain/strategy/source

---

## Phase 8: Context Compact

**Actor:** User

1. Prompt the user to compact the context window (the conversation is likely large at this point)
2. All critical state is in files (DISCOVERY.md, research/, skills/) so nothing is lost

**Output:** Fresh context, all state persisted in files

---

## Phase 9: PHASES.md Creation

**Actor:** Main agent

This is the master implementation plan. The main agent synthesizes everything into a phased implementation plan.

1. Read template: `artifact-templates/phases.md`
2. Read ALL of:
   - DISCOVERY.md (top authority)
   - All research files (both waves)
   - All skills created
   - PRD.md
3. Create PHASES.md with:
   - Scope constraints (what's NOT being built)
   - Tech stack summary
   - Skills reference table
   - Tools/MCP reference table
   - Testing methods table
   - Phase overview table
   - Per-phase sections with task lists
   - Each task includes: objective, acceptance criteria, files to edit/create, dependencies (blocking/blocked-by), contracts with adjacent tasks, testing criteria
   - **Last task in every phase**: full regression test of that phase's tasks from every angle on the closest-to-live version
   - **Last phase**: entirely dedicated to comprehensive multi-angle e2e testing on the fully deployed software
   - Dependency graph showing cross-phase relationships
   - Task execution protocol

4. Save to: `.claude/orchestration-<slug>/PHASES.md`

**Output:** `PHASES.md` - the master implementation plan

---

## Phase 10: Task File Sharding

**Actor:** Parallel background subagents (one per phase)

Each phase gets a subagent that expands the PHASES.md task summaries into detailed, self-contained task files.

1. For each phase, spawn a background subagent:

```
You are creating detailed task files for Phase N of the implementation.

Read these files first:
- PHASES.md at: .claude/orchestration-<slug>/PHASES.md
- DISCOVERY.md at: .claude/orchestration-<slug>/DISCOVERY.md
- Relevant research files in: .claude/orchestration-<slug>/research/
- Relevant skills in: .claude/skills/
- Task file template at: ~/.claude/skills/m2c1/artifact-templates/task-file.md

For each task in Phase N of PHASES.md:
1. Read the task summary from PHASES.md
2. Do deeper ideation into the code, architecture, and broader context
3. Read relevant skills and research files
4. Create a detailed task file following the template

Each task file is the COMPLETE prompt that an execution subagent will receive.
It must include everything the agent needs to execute the task autonomously.

Save each file to: .claude/orchestration-<slug>/tasks/phase-N/task-N-M.md
```

2. Wait for all phase subagents to complete

**Output:** Detailed task files in `tasks/phase-N/` folders

---

## Phase 11: Synergy Review

**Actor:** Parallel background subagents

Evaluate cross-phase coherence. Use as few subagents as possible while covering all phases.

1. Spawn review subagents that each cover multiple phases:

```
You are reviewing task files for synergy issues.

Read ALL task files in: .claude/orchestration-<slug>/tasks/
Read PHASES.md at: .claude/orchestration-<slug>/PHASES.md

Evaluate:
- Are there contradictions between tasks in different phases?
- Do data contracts between tasks align (API shapes, DB schemas, shared types)?
- Are dependencies correctly declared?
- Do testing strategies reference the right assets and fixtures?
- Are there gaps - things assumed but never explicitly built?
- Do later tasks correctly build on earlier tasks' outputs?

For each issue found, propose a specific fix (which file, what change).

Save your review to: .claude/orchestration-<slug>/reports/synergy-review.md
```

2. Wait for review subagents to complete
3. Present all synergy issues to user for approval
4. Apply approved fixes to task files

**Output:** Synergy-reviewed, coherent task files

---

## Phase 12: Final Artifacts

**Actor:** Main agent

Create the remaining orchestration artifacts and update project configuration.

1. Read template: `artifact-templates/progress.md`
   - Create `PROGRESS.md` with phase overview table and per-task status rows (all "pending")
   - Save to project root or orchestration folder

2. Read template: `artifact-templates/start.md`
   - Create `START.md` - the orchestrator protocol that defines how to spawn execution subagents
   - Save to: `.claude/orchestration-<slug>/START.md`

3. Read template: `artifact-templates/claude-md-section.md`
   - Add orchestration section to the project's `CLAUDE.md` (create if it doesn't exist)
   - Include: quick reference table, authority rule, tech stack, skill references, tool references, testing methods

4. Report to user: orchestration system is ready. Tell them to run `/start` to begin execution.

**Output:** `PROGRESS.md`, `START.md`, updated `CLAUDE.md`

---

## Execution (Post-Setup)

Once all 12 phases are complete, the system is ready for autonomous execution via `/start`:

1. Orchestrator reads PROGRESS.md to find next pending task
2. Spawns a subagent pointed at the task file
3. Subagent reads task file, relevant skills, executes, tests, commits
4. Orchestrator verifies PROGRESS.md was updated, moves to next task
5. After each phase's regression task passes, the phase is complete
6. After all phases complete, the software is fully built and tested

### Task Execution Flow (per task)

Each execution subagent follows this flow:

1. **Orient** - Read task file, read skills, read PROGRESS.md
2. **Plan** - Explore codebase, plan approach
3. **Implement** - Create feature branch, write code
4. **Test locally** - Run all applicable testing methods:
   - Unit/integration tests (Jest, pytest, etc.)
   - API calls or script triggers to verify outputs
   - Type checks, lint checks, builds (if relevant)
   - Browser logs and external service logs (if integrated)
   - Playwright UI testing with user-emulating flows (if UI exists)
   - Navigate all decision paths, input test assets, verify edge cases
5. **Complete** - Update PROGRESS.md, commit, merge to target branch

### Phase Regression Flow (last task of each phase)

1. Deploy to closest-to-live environment
2. Run ALL task tests from the phase
3. Run full e2e from every angle:
   - All unit/integration tests
   - External service log checks
   - Full user-emulating Playwright testing
   - Edge case and error path testing
4. If failures: create hotfix, fix, redeploy, retest
5. Merge phase branch to main/target

### Final Phase (always the last phase)

The final phase is entirely dedicated to comprehensive e2e testing on the fully deployed, live version:
- Every user path and edge case
- Every testing method applied
- All external service integrations verified
- Performance and error handling validated
- Iterating directly on main/target branch

---

## Naming Conventions

| Artifact | Naming Pattern |
|----------|---------------|
| Orchestration folder | `.claude/orchestration-<auto-slug>/` |
| Research files | `research/<domain-slug>.md`, `research/<domain-slug>-implementation.md` |
| Task files | `tasks/phase-N/task-N-M.md` |
| Phase branches | `phase-N/<short-description>` or `task/N-M-<short-description>` |
| Skills | `.claude/skills/<descriptive-name>/SKILL.md` |
| Reports | `reports/synergy-review.md`, `reports/phase-N-review.md` |

---

## Failure Handling (3-Tier Escalation)

**Tier 1: Subagent Self-Recovery**
- Debug and fix within its own session
- Retry failed tool calls with different parameters
- Create missing dependencies inline

**Tier 2: Orchestrator Intervention**
- Read error output and PROGRESS.md notes
- Spawn a targeted fix subagent
- Re-run original task after fix

**Tier 3: User Escalation** (last resort)
- Provide: task number, what was attempted, the error, suggested fix
- Continue with next unblocked task while waiting

---

## Session Boundaries

- PROGRESS.md enables session continuity - any new session picks up where the last left off
- If context is getting large, report progress and suggest compacting or starting fresh
- All state is in files, nothing is lost between sessions
