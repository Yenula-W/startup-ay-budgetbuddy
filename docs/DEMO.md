# BudgetBuddy demo and submission checklist

## Run the candidate

Use the repository root with Python 3. No packages are required.

```sh
git switch release/v1.0
python3 -m unittest -v
python3 main.py
```

`main` does not contain the candidate until the PR is reviewed and merged.

## Rehearse one real path

Use a disposable copy of `data/budgetbuddy.json`: adding an entry saves to that file.
The untouched sample has six transactions and a $60.50 balance.

1. Start with the app running. Option `8` shows the account and transaction count.
2. Option `1` shows `$60.50`.
3. Option `3`: description `Demo lunch`, amount `-5.25`, category `food`.
4. Option `1`: the balance is now `$55.25`.
5. Option `4`, category `food`: the list includes `Lunch`, `Snack`, and `Demo lunch`.
6. Option `6`: `food: $-15.25`, `fun: $-12.00`, `income: $35.00`, `transport: $-2.50`.
7. Quit with `0`. Restart and use `5` to confirm `Demo lunch` was saved.

These numbers assume the untouched sample and exactly one demo addition. Repeated additions change them.

## One-minute recording outline

- 0–10 seconds: show the running CLI and explain who would use a spending/allowance tracker.
- 10–35 seconds: show adding an expense, the updated balance, and the category totals.
- 35–50 seconds: explain the category feature and a challenge you actually understand and worked on. A useful code-review topic is rejecting bad input before changing or saving data.
- 50–60 seconds: name one next step and give your own honest reflection.

Use your own narration and describe AI assistance accurately. Do not claim unmerged changes are on `main`, or invent personal debugging experiences.

## Final gates

- [ ] Review the release diff and understand the changes.
- [ ] Check the PR's automated test results.
- [ ] Obtain one squadmate's review and approval as required by `CONTRIBUTING.md`.
- [ ] Merge only after approval, then verify the version used for the recording.
- [ ] Record your screen with your voice (aim for a minute; two minutes maximum).
- [ ] Upload the video to Drive with link access or YouTube Unlisted; confirm it plays in a private window.
- [ ] Post the accessible video link as a Demo post titled BudgetBuddy, following Lesson 17.
- [ ] Complete your own reflections and peer appreciations, then submit the lesson.
