# Practice: delivery exception report

All records are fictional. Review date: **2026-10-23**, regardless of today's date.

Send this prompt with input.csv:

> Check these deliveries as of 2026-10-23. For completed deliveries, do not assess lateness. An open delivery is overdue if its planned date is earlier than the review date; count calendar days. Flag a missing date without guessing. Produce a short report covering every row. Save it under workspace/projects/first-task/results/supply-check.md if you have file access. Do not send messages or change external systems.

First make your own attempt; then compare with [expected-result.md](expected-result.md).

## Test the exception

Now add conflict.csv. Neither source is declared authoritative. The assistant must show the two dates for TEST-01 and request a decision, rather than silently use one. TEST-02 remains completed and TEST-03 remains missing a date.

## What the model does

The rule and date arithmetic determine the classification. The assistant helps clarify the task and explain the result. A language model is not required for the arithmetic itself. Optional maintainers can run the deterministic reference implementation in tools/supply_check.py.

## Success criteria

All three rows accounted for; two-day calculation correct; no date invented; completed status not misrepresented as proof of historical timeliness; conflicting sources not silently resolved. Record actual checks separately from the answer key.
