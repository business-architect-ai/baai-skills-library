#!/usr/bin/env node

import { access, mkdir, writeFile } from "node:fs/promises";
import { constants } from "node:fs";
import { spawn } from "node:child_process";
import path from "node:path";
import process from "node:process";

const args = process.argv.slice(2);

function usage() {
  return `Usage:
  audit-site <url> [--name run-name] [--out runs]

Examples:
  npm run audit -- https://example.com
  SQUIRRLSCAN_CMD="squirrel audit" npm run audit -- https://example.com --name example
`;
}

function parseArgs(argv) {
  const parsed = { url: null, name: null, out: "runs" };
  for (let i = 0; i < argv.length; i += 1) {
    const value = argv[i];
    if (value === "--name") {
      parsed.name = argv[++i];
    } else if (value === "--out") {
      parsed.out = argv[++i];
    } else if (!parsed.url) {
      parsed.url = value;
    } else {
      throw new Error(`Unknown argument: ${value}`);
    }
  }
  return parsed;
}

function assertUrl(raw) {
  try {
    const url = new URL(raw);
    if (!["http:", "https:"].includes(url.protocol)) {
      throw new Error("URL must start with http:// or https://");
    }
    return url;
  } catch {
    throw new Error(`Invalid URL: ${raw}`);
  }
}

function slugify(value) {
  return value
    .toLowerCase()
    .replace(/^https?:\/\//, "")
    .replace(/[^a-z0-9]+/g, "-")
    .replace(/^-+|-+$/g, "")
    .slice(0, 80);
}

function timestamp() {
  return new Date().toISOString().replace(/[:.]/g, "-");
}

function splitCommand(command) {
  return command.match(/(?:[^\s"]+|"[^"]*")+/g)?.map((part) => part.replace(/^"|"$/g, "")) ?? [];
}

async function isExecutable(command) {
  const [bin] = splitCommand(command);
  if (!bin) return false;
  if (bin.includes("/")) {
    try {
      await access(bin, constants.X_OK);
      return true;
    } catch {
      return false;
    }
  }
  const pathEntries = (process.env.PATH || "").split(path.delimiter).filter(Boolean);
  for (const entry of pathEntries) {
    try {
      await access(path.join(entry, bin), constants.X_OK);
      return true;
    } catch {
      // Keep scanning PATH.
    }
  }
  return false;
}

async function runCommand({ label, command, args: commandArgs, cwd, stdoutFile, stderrFile }) {
  const parts = splitCommand(command);
  const bin = parts[0];
  const baseArgs = parts.slice(1);
  const fullArgs = [...baseArgs, ...commandArgs];
  const startedAt = new Date().toISOString();

  return new Promise((resolve) => {
    const child = spawn(bin, fullArgs, { cwd, shell: false });
    let stdout = "";
    let stderr = "";

    child.stdout.on("data", (chunk) => {
      stdout += chunk.toString();
    });
    child.stderr.on("data", (chunk) => {
      stderr += chunk.toString();
    });
    child.on("error", async (error) => {
      await writeFile(stderrFile, `${stderr}\n${error.message}\n`);
      resolve({ label, status: "failed", code: null, startedAt, endedAt: new Date().toISOString() });
    });
    child.on("close", async (code) => {
      await writeFile(stdoutFile, stdout || "");
      await writeFile(stderrFile, stderr || "");
      resolve({
        label,
        status: code === 0 ? "completed" : "failed",
        code,
        startedAt,
        endedAt: new Date().toISOString()
      });
    });
  });
}

function synthuxManual(url) {
  return `# Synthux Manual Audit

URL: ${url}

Run this in the Synthux Chrome extension:

1. Open the URL in Chrome.
2. Run a deep audit on desktop.
3. Run the same audit on a mobile viewport.
4. Repeat for key pages: homepage, service/product page, pricing/offers, contact/lead form, one article/page with long content.
5. Export or paste the result into this run folder as \`03-synthux-results.md\`.

Capture:

- UX heuristic issues.
- WCAG/axe-core issues.
- CTA clarity.
- Navigation friction.
- Mobile readability and tap target problems.
- Form friction.
- Visual hierarchy observations.
`;
}

function designReviewPrompt(url, runDir) {
  return `# Design Review Prompt

Use the \`design-review\` skill from \`jezweb/claude-skills\`.

Target URL: ${url}
Audit folder: ${runDir}

Review the site visually on desktop and mobile. Focus on:

- layout and composition
- typography scale and rhythm
- spacing consistency
- color usage and contrast
- visual hierarchy
- component consistency
- responsive behavior
- polish issues that make the site feel less professional

Return:

- P0/P1/P2 issues
- screenshots or page references where possible
- concrete fix recommendations
- quick wins under 1 hour
- final design quality score from 1 to 10
`;
}

function frontendAuditPrompt(url, runDir) {
  return `# Frontend Design Audit Prompt

Use \`frontend-design-audit\` after the technical and visual audit artifacts are available.

Target URL: ${url}
Audit folder: ${runDir}

Inputs to read first:

- \`01-squirrelscan.md\` or \`01-squirrelscan.txt\`
- \`02-dembrandt.md\` or \`02-dembrandt.txt\`
- \`03-synthux-results.md\`, if present
- \`04-design-review-results.md\`, if present

Goal:

1. Consolidate the actionable UI/UX issues.
2. If the website codebase is available, implement the highest-impact P0/P1 fixes.
3. Keep changes scoped and verify desktop/mobile rendering.
4. Produce a concise fix log.
`;
}

function ramsNotes(url) {
  return `# Rams PR Review Setup

Target site: ${url}

Rams is not a local CLI in this runner. Use it as a GitHub App when the project lives in GitHub.

Recommended use:

1. Install Rams on the repo.
2. Open PRs for design/UX fixes.
3. Let Rams review visual/accessibility/design issues inline.
4. Keep Rams active as a regression guard after the first audit cleanup.

Free tier usually fits public repos. Private repos need a paid plan.
`;
}

function consolidationPrompt(url, runDir) {
  return `# Consolidated Site Audit Prompt

You are auditing this website: ${url}

Read every available artifact in this folder:

${runDir}

Create a consolidated report with:

1. Executive summary.
2. Top 10 highest-impact issues.
3. SEO issues.
4. Performance issues.
5. Security/header issues.
6. Accessibility/WCAG issues.
7. UX and conversion issues.
8. Visual/design polish issues.
9. Design-system consistency issues.
10. Quick wins under 1 hour.
11. 1-2 week implementation backlog.
12. Suggested verification checklist after fixes.

Prioritize issues as:

- P0: blocks users, revenue, indexing, or compliance.
- P1: highly visible or materially hurts conversion/usability.
- P2: polish, consistency, or medium-risk improvements.
- P3: nice-to-have.

Be concrete. Include page references and exact fixes wherever possible.
`;
}

async function main() {
  const parsed = parseArgs(args);
  if (!parsed.url) {
    console.error(usage());
    process.exit(1);
  }

  const url = assertUrl(parsed.url);
  const slug = slugify(parsed.name || url.hostname);
  const runDir = path.resolve(parsed.out, `${timestamp()}-${slug}`);
  await mkdir(runDir, { recursive: true });

  const input = {
    url: url.toString(),
    createdAt: new Date().toISOString(),
    runDir,
    commands: {
      squirrelscan: process.env.SQUIRRLSCAN_CMD || "squirrel audit",
      dembrandt: process.env.DEMBRANDT_CMD || "dembrandt"
    }
  };

  await writeFile(path.join(runDir, "00-input.json"), `${JSON.stringify(input, null, 2)}\n`);

  const results = [];

  const squirrelCommand = input.commands.squirrelscan;
  if (await isExecutable(squirrelCommand)) {
    results.push(await runCommand({
      label: "squirrelscan",
      command: squirrelCommand,
      args: [url.toString()],
      cwd: process.cwd(),
      stdoutFile: path.join(runDir, "01-squirrelscan.txt"),
      stderrFile: path.join(runDir, "01-squirrelscan.stderr.txt")
    }));
  } else {
    await writeFile(path.join(runDir, "01-squirrelscan-missing.md"), `# Squirrelscan Missing

Command not found: \`${squirrelCommand}\`

Install Squirrelscan or set \`SQUIRRLSCAN_CMD\` to the command that runs it.
`);
    results.push({ label: "squirrelscan", status: "missing" });
  }

  const resolvedDembrandtCommand = process.env.DEMBRANDT_CMD || "dembrandt";
  if (await isExecutable(resolvedDembrandtCommand)) {
    results.push(await runCommand({
      label: "dembrandt",
      command: resolvedDembrandtCommand,
      args: [url.toString()],
      cwd: process.cwd(),
      stdoutFile: path.join(runDir, "02-dembrandt.txt"),
      stderrFile: path.join(runDir, "02-dembrandt.stderr.txt")
    }));
  } else {
    await writeFile(path.join(runDir, "02-dembrandt-missing.md"), `# Dembrandt Missing

Command not found: \`${resolvedDembrandtCommand}\`

Install Dembrandt or set \`DEMBRANDT_CMD\` to the command that runs it.
`);
    results.push({ label: "dembrandt", status: "missing" });
  }

  await writeFile(path.join(runDir, "03-synthux-manual.md"), synthuxManual(url.toString()));
  await writeFile(path.join(runDir, "04-design-review-prompt.md"), designReviewPrompt(url.toString(), runDir));
  await writeFile(path.join(runDir, "05-frontend-design-audit-prompt.md"), frontendAuditPrompt(url.toString(), runDir));
  await writeFile(path.join(runDir, "06-rams-pr-review.md"), ramsNotes(url.toString()));
  await writeFile(path.join(runDir, "99-consolidation-prompt.md"), consolidationPrompt(url.toString(), runDir));

  const summary = `# Audit Run Summary

URL: ${url.toString()}
Run folder: ${runDir}

## Automated Results

${results.map((result) => `- ${result.label}: ${result.status}${result.code === undefined ? "" : ` (exit ${result.code})`}`).join("\n")}

## Next Steps

1. Add Synthux results to \`03-synthux-results.md\`.
2. Run the \`04-design-review-prompt.md\` prompt with the design-review skill.
3. Run \`99-consolidation-prompt.md\` to produce the final report.
4. If the site repo is available, use \`05-frontend-design-audit-prompt.md\` for scoped fixes.
`;

  await writeFile(path.join(runDir, "SUMMARY.md"), summary);

  console.log(summary);
}

main().catch((error) => {
  console.error(error.message);
  process.exit(1);
});
