#!/usr/bin/env node
import { readFileSync } from 'node:fs';
import { basename } from 'node:path';

const file = process.argv[2];
if (!file) {
  console.error('Usage: node audit-media-html.mjs path/to/page.html');
  process.exit(2);
}

const html = readFileSync(file, 'utf8');
const issues = [];

function attrs(tag) {
  const result = {};
  const re = /([:@\w-]+)(?:\s*=\s*(?:"([^"]*)"|'([^']*)'|([^\s"'=<>`]+)))?/g;
  let match;
  while ((match = re.exec(tag))) {
    const [, key, dq, sq, bare] = match;
    if (key === 'img' || key === 'video' || key === 'source') continue;
    result[key.toLowerCase()] = dq ?? sq ?? bare ?? '';
  }
  return result;
}

function lineFor(index) {
  return html.slice(0, index).split(/\r?\n/).length;
}

const imgRe = /<img\b[^>]*>/gi;
let imgMatch;
let imgIndex = 0;
while ((imgMatch = imgRe.exec(html))) {
  imgIndex += 1;
  const tag = imgMatch[0];
  const a = attrs(tag);
  const label = `img #${imgIndex} line ${lineFor(imgMatch.index)}`;
  const isHero = imgIndex === 1 || a.fetchpriority === 'high';
  const isAboveFold = isHero || a['data-above-fold'] === 'true';
  const isDecorative = Object.prototype.hasOwnProperty.call(a, 'alt') && a.alt === '';

  if (!a.width) issues.push(`${label}: missing width`);
  if (!a.height) issues.push(`${label}: missing height`);
  if (!Object.prototype.hasOwnProperty.call(a, 'alt')) issues.push(`${label}: missing alt`);
  if (a.alt && /^(imagine|foto|poza|poză)(\s+cu)?\b/i.test(a.alt.trim())) {
    issues.push(`${label}: alt starts with generic wording`);
  }
  if (isDecorative && a['aria-hidden'] !== 'true') issues.push(`${label}: decorative image needs aria-hidden="true"`);
  if (!isAboveFold && a.loading !== 'lazy') issues.push(`${label}: offscreen image should use loading="lazy" or data-above-fold="true" if it is visible in the first viewport`);
  if (isAboveFold && !isHero && a.loading === 'lazy') issues.push(`${label}: above-fold image must not use loading="lazy"`);
  if (isHero && a.loading === 'lazy') issues.push(`${label}: hero image must not use loading="lazy"`);
  if (isHero && a.fetchpriority !== 'high') issues.push(`${label}: hero image should use fetchpriority="high"`);
}

const pictureCount = (html.match(/<picture\b/gi) || []).length;
const webpSourceCount = (html.match(/<source\b[^>]*type=["']image\/webp["'][^>]*>/gi) || []).length;
const avifSourceCount = (html.match(/<source\b[^>]*type=["']image\/avif["'][^>]*>/gi) || []).length;
if (pictureCount > 0 && webpSourceCount === 0 && avifSourceCount === 0) {
  issues.push('picture elements exist but no image/avif or image/webp source was found');
}

const videoRe = /<video\b[^>]*>/gi;
let videoMatch;
let videoIndex = 0;
while ((videoMatch = videoRe.exec(html))) {
  videoIndex += 1;
  const tag = videoMatch[0];
  const a = attrs(tag);
  const label = `video #${videoIndex} line ${lineFor(videoMatch.index)}`;
  for (const key of ['autoplay', 'muted', 'loop', 'playsinline']) {
    if (!Object.prototype.hasOwnProperty.call(a, key)) issues.push(`${label}: missing ${key}`);
  }
  if (!a.poster) issues.push(`${label}: missing poster`);
}

for (const meta of [
  'property="og:image"',
  'property="og:image:width"',
  'property="og:image:height"',
  'name="twitter:image"',
]) {
  if (!html.includes(meta) && !html.includes(meta.replaceAll('"', "'"))) {
    issues.push(`head: missing <meta ${meta} ...>`);
  }
}

if (issues.length) {
  console.error(`Media audit failed for ${basename(file)}:`);
  for (const issue of issues) console.error(`- ${issue}`);
  process.exit(1);
}

console.log(`Media audit passed for ${basename(file)}.`);
