"""Deterministic reference for the fictional delivery exercise; no external I/O."""
from datetime import date


def classify(row, review_date, conflicting_dates=()):
    status = row.get('status', '')
    if status == 'completed':
        return {'status': 'excluded', 'days_overdue': None}
    if status != 'open':
        return {'status': 'invalid_status', 'days_overdue': None}
    values = {str(v).strip() for v in conflicting_dates if str(v).strip()}
    planned = str(row.get('planned_date') or '').strip()
    if planned:
        values.add(planned)
    if len(values) > 1:
        return {'status': 'conflict', 'days_overdue': None}
    # A supplemental source does not silently fill a missing canonical date.
    if not planned:
        return {'status': 'missing_date', 'days_overdue': None}
    try:
        delta = (date.fromisoformat(review_date) - date.fromisoformat(planned)).days
    except ValueError:
        return {'status': 'invalid_date', 'days_overdue': None}
    return {'status': 'overdue' if delta > 0 else 'not_due',
            'days_overdue': max(delta, 0)}
