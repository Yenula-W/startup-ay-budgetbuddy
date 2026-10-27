# BudgetBuddy

BudgetBuddy is a small Python command-line spending and allowance tracker. It loads a JSON account, shows your balance, records transactions, and provides basic summaries. This is the Elite 101 course project, not a deployed financial service.

## Requirements and quick start

- Python 3 with no third-party dependencies.
- From the repository root, run `python main.py` (or `python3 main.py` on macOS).
- At `Pick an option:`, enter a menu number. Enter `0` to quit.
- Run the existing tests with `python -m unittest` (or `python3 -m unittest`).

## Current menu (from `main`)

| Option | Behavior |
| --- | --- |
| `1` | Display the starting balance plus signed transaction amounts. |
| `2` | List transactions with their IDs, descriptions, and amounts. |
| `3` | Add a transaction and save the updated JSON file. Negative amounts represent expenses; positive amounts represent income. New entries use the `general` category. |
| `4` | Show transactions matching a category string exactly. |
| `5` | Show the latest transaction's description (requires at least one transaction). |
| `6` | Count transactions by category. |
| `7` | Show total spending from negative amounts, transaction count, and average signed transaction amount. |
| `8` | Show the account name and transaction count. |
| `0` | Quit. |

## Sample data and storage

The initial account is in `data/budgetbuddy.json`, including `account_name`, `starting_balance`, and a `transactions` list. Each transaction has `id`, `description`, `amount`, and `category`. The sample file starts with a $50 opening balance and six transactions. **Option 3 modifies this tracked JSON file**, so use a copy if you want to preserve the sample data.

## Repository layout

| Path | Purpose |
| --- | --- |
| `main.py` | CLI menu and input loop |
| `storage.py` | JSON loading and saving |
| `features/core.py` | Balances, transaction helpers, and category counts |
| `features/reports.py` | Account summary and an unfinished category-report stub |
| `data/budgetbuddy.json` | Example account data and transaction history |
| `tests/test_core.py` | Two starter tests: opening balance and new transaction ID |
| `docs/RELEASE_NOTES.md` | Current release scope and known limits |

## Known limitations

- `features/reports.py:category_report` is not implemented; it returns an empty dictionary and is not a working category-total report.
- The add-transaction menu accepts only description and amount; it assigns the default category `general`.
- Invalid numeric input is not caught by the menu, and option 5 assumes the transaction list is nonempty.
- This is a local CLI that stores data in one JSON file; there is no authentication, hosted deployment, or bank integration.
- Lesson-specific bug fixes and additional report tests in open PRs are **not included in `main`** until reviewed and merged. See the release notes.

## Contributing and review

Use a feature branch and pull request rather than committing directly to `main`. Read `CONTRIBUTING.md` for the ticket, tests, docs, and review checklist. This v1.0 release preparation lives on `release/v1.0` and should be reviewed before merge.
