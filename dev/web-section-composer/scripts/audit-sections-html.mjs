#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { basename } from 'node:path';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node audit-sections-html.mjs path/to/page.html');
  process.exit(2);
}

const html = readFileSync(file, 'utf8');
const issues = [];
const warnings = [];

function lineFor(index) {
  return html.slice(0, index).split(/\r?\n/).length;
}

function attrs(tag) {
  const result = {};
  const re = /([:@\w-]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?/g;
  let match;
  while ((match = re.exec(tag))) {
    const [, key, dq, sq, bare] = match;
    if (/^(section|div|article|a|button|img|h[1-6])$/i.test(key)) continue;
    result[key.toLowerCase()] = dq ?? sq ?? bare ?? '';
  }
  return result;
}

function stripTags(value) {
  return value
    .replace(/<script\b[\s\S]*?<\/script>/gi, ' ')
    .replace(/<style\b[\s\S]*?<\/style>/gi, ' ')
    .replace(/<[^>]+>/g, ' ')
    .replace(/&nbsp;/gi, ' ')
    .replace(/\s+/g, ' ')
    .trim();
}

function wordCount(value) {
  const text = stripTags(value);
  return text ? text.split(/\s+/).length : 0;
}

function findAll(re, source = html) {
  const matches = [];
  let match;
  while ((match = re.exec(source))) matches.push(match);
  return matches;
}

const sectionRe = /<(section|article)\b[^>]*>[\s\S]*?<\/\1>/gi;
const sections = findAll(sectionRe);

if (sections.length === 0) {
  warnings.push('page: no <section> or <article> elements found; semantic grouping may be weak');
}

sections.forEach((match, index) => {
  const block = match[0];
  const line = lineFor(match.index);
  const label = `section #${index + 1} line ${line}`;
  const words = wordCount(block);
  const headingCount = (block.match(/<h[1-6]\b/gi) || []).length;
  const ctaCount =
    (block.match(/<button\b/gi) || []).length +
    (block.match(/<a\b[^>]*(class=["'][^"']*(btn|button|cta)[^"']*["']|role=["']button["'])/gi) || []).length;
  const cardCount = (block.match(/class=["'][^"']*(card|panel|tile)[^"']*["']/gi) || []).length;
  const imgCount = (block.match(/<img\b/gi) || []).length;

  if (headingCount === 0 && words > 20) issues.push(`${label}: content section has no heading`);
  if (headingCount > 5 && words < 120) warnings.push(`${label}: many headings for little content`);
  if (ctaCount > 2) warnings.push(`${label}: ${ctaCount} CTA-like controls; check action hierarchy`);
  if (cardCount > 8) warnings.push(`${label}: ${cardCount} card-like elements; consider grouping, table, or denser layout`);
  if (imgCount > 0 && words < 25 && !/gallery|portfolio|logo|image|media/i.test(block)) {
    warnings.push(`${label}: media-heavy section with little explanatory text; confirm image role`);
  }
  if (words > 260 && cardCount > 0) warnings.push(`${label}: long text inside card/panel-heavy section; consider splitting or simplifying`);
});

const headings = findAll(/<h([1-6])\b[^>]*>([\s\S]*?)<\/h\1>/gi);
let previousLevel = 0;
let h1Count = 0;
headings.forEach((match) => {
  const level = Number(match[1]);
  const text = stripTags(match[2]);
  const line = lineFor(match.index);
  if (level === 1) h1Count += 1;
  if (previousLevel && level > previousLevel + 1) {
    issues.push(`heading line ${line}: jumps from h${previousLevel} to h${level}`);
  }
  if (/^(beneficii|features|soluții|solutii|performanță|performanta|calitate|servicii|despre noi)$/i.test(text)) {
    warnings.push(`heading line ${line}: generic heading "${text}"; make it more specific`);
  }
  previousLevel = level;
});
if (h1Count > 1) warnings.push(`page: ${h1Count} h1 elements found; confirm page hierarchy`);

const buttonLike = findAll(/<(a|button)\b[^>]*>([\s\S]*?)<\/\1>/gi);
buttonLike.forEach((match) => {
  const text = stripTags(match[2]).toLowerCase();
  const line = lineFor(match.index);
  if (/^(click aici|apasă aici|apasa aici|află mai multe|afla mai multe|learn more|more|read more|submit)$/i.test(text)) {
    warnings.push(`control line ${line}: generic CTA text "${stripTags(match[2])}"`);
  }
});

const imgTags = findAll(/<img\b[^>]*>/gi);
imgTags.forEach((match, index) => {
  const a = attrs(match[0]);
  const label = `img #${index + 1} line ${lineFor(match.index)}`;
  if (!a.width) issues.push(`${label}: missing width`);
  if (!a.height) issues.push(`${label}: missing height`);
  if (!Object.prototype.hasOwnProperty.call(a, 'alt')) issues.push(`${label}: missing alt`);
  if (a.alt && /^(imagine|foto|poza|poză)(\s+cu)?\b/i.test(a.alt.trim())) {
    warnings.push(`${label}: alt starts with generic wording`);
  }
});

const inlineStyleCount = (html.match(/\sstyle=/gi) || []).length;
if (inlineStyleCount > 20) {
  warnings.push(`page: ${inlineStyleCount} inline style attributes; consider extracting repeated section styles`);
}

const carouselCount = (html.match(/carousel|swiper|slick-slider|splide|slider/gi) || []).length;
if (carouselCount > 0) {
  warnings.push('page: carousel/slider wording detected; confirm critical content is not hidden in a carousel');
}

const nestedCardRe = /<([a-z0-9-]+)\b[^>]*class=["'][^"']*(card|panel)[^"']*["'][^>]*>(?:(?!<\/\1>).)*<([a-z0-9-]+)\b[^>]*class=["'][^"']*(card|panel)[^"']*["']/gis;
if (nestedCardRe.test(html)) warnings.push('page: possible card/panel nesting detected; avoid cards inside cards unless it is a functional app panel');

if (issues.length || warnings.length) {
  console.log(`Section audit for ${basename(file)}:`);
  if (issues.length) {
    console.log('\nIssues:');
    for (const issue of issues) console.log(`- ${issue}`);
  }
  if (warnings.length) {
    console.log('\nWarnings:');
    for (const warning of warnings) console.log(`- ${warning}`);
  }
  process.exit(issues.length ? 1 : 0);
}

console.log(`Section audit passed for ${basename(file)}.`);
