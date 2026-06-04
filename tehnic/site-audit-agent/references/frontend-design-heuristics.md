# Heuristic Reference

Use these checks when performing a frontend design audit.

## 1. Visibility of System Status

Look for missing loading indicators, save confirmations, active navigation states, selected states, disabled states, progress indicators, skeletons, upload progress, and feedback after user actions. Missing feedback on destructive, payment, or form actions is high severity.

## 2. Match Between System and Real World

Look for developer jargon, raw error codes, stack traces, unformatted dates/numbers, labels such as "submit" where a user-goal verb would be clearer, and field ordering that does not match the user's mental model.

## 3. User Control and Freedom

Look for destructive actions without confirmation/undo, modals without close/Escape/overlay dismissal, multi-step flows without back/cancel, forms that lose data on navigation, autoplay without controls, and forced flows without exit.

## 4. Consistency and Standards

Look for inconsistent button styles, repeated concepts with different names, different modal/dialog patterns, mixed icon families, links acting like buttons, buttons acting like links, inconsistent spacing, and hardcoded visual values where tokens exist.

## 5. Error Prevention

Look for missing inline validation, missing input constraints, no `maxlength`/`min`/`max`/`pattern`, no `inputmode` on mobile-friendly fields, submit buttons that allow double submission, and irreversible actions without confirmation.

## 6. Recognition Over Recall

Look for missing labels, hidden important context, unclear icons, missing breadcrumbs, empty states that do not guide the next action, tables/cards without enough context, and flows that require users to remember previous steps.

## 7. Flexibility and Efficiency

Look for missing keyboard support, no bulk actions for repeated tasks, no search/filter/sort where lists are large, no saved preferences, no shortcuts for expert workflows, and inefficient repeated interaction patterns.

## 8. Aesthetic and Minimalist Design

Look for weak typography hierarchy, cramped or arbitrary spacing, too many competing colors, overloaded screens, unclear visual weight, card-heavy clutter, insufficient grouping, and decorative elements that compete with task content.

## 9. Error Recovery

Look for generic error messages, errors far away from their fields, no recovery guidance, no retry action, no preserved form data after failure, no focus management after validation, and no user-facing explanation for failed async actions.

## 10. Help and Documentation

Look for missing contextual help on complex settings, unexplained acronyms, no onboarding for unfamiliar workflows, tooltips that hide essential information, and empty states without examples or next steps.

## 11. Affordances and Signifiers

Look for clickable elements that do not look clickable, non-clickable cards with hover styles, weak hover/focus/active states, tiny touch targets, icons without labels where meaning is ambiguous, and unclear primary/secondary/destructive actions.

## 12. Structure

Look for poor grouping, inconsistent section boundaries, broken mobile layout, weak page scaffolding, unpredictable navigation placement, awkward table/card responsiveness, missing landmarks, and layout that does not support scanning.

## 13. Accessibility

Look for missing alt text, bad heading hierarchy, missing labels, ARIA misuse, no visible focus, poor contrast, keyboard traps, missing landmark structure, unlabeled icon buttons, missing `aria-current`, and touch targets below 44px on mobile.

## 14. Perceptibility

Look for important states or distinctions that are too subtle: disabled vs enabled, selected vs unselected, primary vs secondary, errors vs hints, active nav vs normal nav, hover/focus differences, or content hierarchy.

## 15. Tolerance and Forgiveness

Look for input formats that are too strict, no undo, no autosave or draft preservation where needed, no forgiving search, no flexible date/phone entry, no confirmation for high-risk actions, and no recovery from accidental navigation.

## Severity Guidance

- **4 Catastrophe**: blocks task completion, causes serious error, loses data, or creates high-risk accessibility/compliance failure.
- **3 Major**: frequent, high-impact friction; users struggle or abandon.
- **2 Minor**: noticeable issue with workaround.
- **1 Cosmetic**: polish issue that does not materially block use.

Judge severity by frequency, impact, and persistence, not fix difficulty.
