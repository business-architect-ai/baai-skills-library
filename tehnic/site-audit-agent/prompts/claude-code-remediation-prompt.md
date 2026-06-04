# Claude Code Remediation Prompt: ClarAsig

Use this prompt inside the ClarAsig website repository in Claude Code.

```text
Am atasat raportul de audit pentru https://clarasig.ro/.

Te rog sa remediezi problemele P0/P1 mai intai, fara redesign major si fara schimbari de continut care nu sunt necesare.

Prioritati:

1. Accessibility errors
   - Fix unlabeled inputs, checkboxes, radios, and icon/buttons.
   - Fix focusable elements inside aria-hidden.
   - Fix broken ARIA ID references, especially generated/Radix IDs.
   - Ensure every form control has a visible label or a correct accessible name.
   - Ensure hidden honeypot fields are not keyboard-focusable and are removed from the accessibility tree.

2. Canonical URLs
   - Add canonical URLs on all routes.
   - Use absolute canonical URLs, for example https://clarasig.ro/rca.
   - Keep trailing slash behavior consistent.

3. Security headers
   - Add Content-Security-Policy, initially report-only if needed.
   - Add X-Frame-Options: DENY or SAMEORIGIN.
   - Add Referrer-Policy: strict-origin-when-cross-origin.
   - Add Permissions-Policy with conservative defaults.
   - Preserve existing HSTS.

4. Public form protection
   - Add bot protection, rate limiting, or stronger server-side validation to public forms.
   - If CAPTCHA is undesirable, use honeypot + rate limiting + server validation.

5. LCP and image optimization
   - Mark true hero/LCP images with Next/Image priority.
   - Do not lazy-load above-fold images.
   - Add width/height or stable dimensions to partner logos and other images that can cause CLS.
   - Review the large JS chunk if there is an obvious low-risk split.

Working rules:

- Keep the existing ClarAsig visual style.
- Do not redesign the site.
- Prefer existing project conventions and components.
- Make scoped changes only.
- After each group of changes, run the available build/lint/test commands.
- If something is ambiguous, inspect the code and make a conservative fix.

Expected output:

- Summary of files changed.
- What each fix addresses from the audit.
- Commands run and results.
- Any items that still need manual/browser verification.
- A short checklist for re-running the audit after deploy.

After deploy, re-run:

npm run audit -- https://clarasig.ro/ --name clarasig-after-fixes
```

