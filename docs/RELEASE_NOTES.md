# BudgetBuddy Release Notes

## v1.0 — 2026-11-18 (release candidate; peer review pending)

These changes are on `release/v1.0` in PR #9, not yet on `main`.

### Added
- Finished signed totals by category (`tickets/ticket-02-category-report.md`), including empty accounts and rounding after summing.
- The add-transaction menu now accepts a category; blank categories default to `general`.
- Regression tests exercise totals, input validation, empty history, cancelled input, saving, and the balance/report user path.
- A repeatable demo walkthrough and final submission checklist in `docs/DEMO.md`.

### Fixed
- Invalid numeric input, `nan`, and infinity no longer create invalid transactions or crash the menu.
- Empty descriptions are rejected before changing or saving account data.
- Showing the latest transaction on an empty account no longer crashes.
- End-of-input during transaction entry cancels without saving a partial entry.

### Changed
- Category breakdown (option 6) now displays signed money totals rather than transaction counts.
- Updated the product guide to describe this branch's actual behavior and limitations.

### Validation
- `python3 -m unittest discover -s . -p 'test_*.py' -v`: 16 tests passed locally.
- Real CLI smoke test in a temporary copy verifies all menu options, saving and reloading an expense, and rejection of invalid input. The tracked sample data is preserved.

### Remaining release gates and limitations
- One peer approval is still required by `CONTRIBUTING.md`; this candidate has not been merged or submitted.
- Lesson 11/13 exercise branches and the separate average-balance PR #2 remain independent; they have not been silently merged.
- JSON must match the bundled schema. Filesystem failures are not automatically recovered. Core balances use floats; this is an educational local CLI, not a financial service.

---

## v1.0 — 2026-10-27 (release candidate; awaiting PR review)

This release candidate documents what currently exists on the repository's `main` branch. The release PR updates documentation only; it does not merge code from lesson branches.

### Added
- Command-line menu for viewing the current balance (opening balance plus transactions), listing transactions, and adding a signed income or expense entry.
- Filters and summaries: exact category filter, latest transaction, counts by category, expense spending total, and account-name summary.
- JSON-backed local data storage and two starter unit tests covering balance and transaction IDs.

### Changed
- Expanded the README with actual menu behavior, run/test commands, data structure, and limits (#8).

### Fixed
- No application-code fixes are introduced by this docs-only release candidate.

### Known limitations
- The `category_report` function remains a stub; it does not calculate category totals.
- New CLI transactions use the `general` category, and the menu does not validate bad numeric input.
- Showing the latest transaction assumes at least one transaction exists.
- Changes in open lesson PRs have not been merged into `main` as part of this candidate.

### Tracked, not included in v1.0
- Bug Bash Issues #3, #4, #5, and #6 describe deliberately seeded problems on `lesson/13-start`. Proposed fixes and regression tests are in open PR #7, which targets that lesson branch; do not count these as newly shipped in `main`.
- PR #1 targets `lesson/11-start` for traceback exercises; PR #2 proposes additional report tests against `main` and is still open.
- Release preparation and review are tracked in Issue #8. Keep the release PR open until review.
