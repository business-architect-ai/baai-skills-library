# Common Fix Patterns

Use project conventions first. These examples show the shape of good fixes, not a required framework.

## Loading and Feedback

- Disable submit/action buttons while async work is running.
- Add visible button text such as "Saving..." or a spinner with accessible text.
- Use `aria-busy` for busy regions.
- Show success feedback after save/copy/delete.
- Use skeletons or reserved dimensions to avoid layout shift.

```jsx
<button disabled={isSaving} aria-busy={isSaving}>
  {isSaving ? "Saving..." : "Save"}
</button>
```

## Forms and Errors

- Pair every input with a visible `<label>`.
- Use `aria-invalid` and `aria-describedby` for field errors.
- Keep form data after failed submission.
- Put errors near the field and include recovery guidance.
- Use `inputmode`, `autocomplete`, `min`, `max`, `maxlength`, and `pattern` where useful.

```jsx
<label htmlFor="email">Email address</label>
<input
  id="email"
  name="email"
  type="email"
  aria-invalid={error ? "true" : undefined}
  aria-describedby={error ? "email-error" : "email-hint"}
/>
<p id="email-hint">Use the email where we can reach you.</p>
{error && <p id="email-error" role="alert">{error}</p>}
```

## Destructive Actions

- Require confirmation for irreversible actions.
- Make the consequence explicit.
- Prefer undo for reversible destructive actions.
- Keep cancel as the safest/focused action.

## Navigation

- Add `aria-current="page"` and visible current-page styling.
- Keep nav placement consistent.
- Use breadcrumbs for deep flows.
- Ensure mobile nav has large touch targets and a clear close action.

## Modals and Popovers

- Add `role="dialog"` or use native `<dialog>` where appropriate.
- Provide `aria-labelledby`.
- Close with Escape and a visible close/cancel control.
- Trap focus while open and return focus after close.
- Do not hide essential content in tooltips only.

## Visual Design

- Establish a clear type scale and do not make headings/body look too similar.
- Use consistent spacing tokens; group related items by proximity.
- Keep one primary action visually dominant.
- Use color semantically and sparingly.
- Make hover, focus, active, selected, and disabled states visibly distinct.

## Accessibility

- Use semantic elements before ARIA.
- Add visible focus styles.
- Keep contrast at WCAG AA where possible.
- Label icon-only buttons with accessible names.
- Ensure keyboard navigation reaches every control in a logical order.
