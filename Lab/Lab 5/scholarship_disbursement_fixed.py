
"""Manage scholarship awards and track disbursements."""

import sqlite3

CONNECTION = sqlite3.connect(":memory:")
CONNECTION.execute(
    """
    CREATE TABLE awards (
        id INTEGER PRIMARY KEY,
        student TEXT,
        scheme TEXT,
        amount INTEGER,
        disbursed INTEGER
    )
    """
)


def grant(student, scheme, amount, audit=None):
    """Create a scholarship award and record the student in the audit list."""
    if audit is None:
        audit = []

    CONNECTION.execute(
        """
        INSERT INTO awards (student, scheme, amount, disbursed)
        VALUES (?, ?, ?, 0)
        """,
        (student, scheme, amount),
    )
    audit.append(student)
    return audit


def disburse(award_id):
    """Mark an award as disbursed and return its amount, or None if missing."""
    row = CONNECTION.execute(
        "SELECT amount FROM awards WHERE id = ?",
        (award_id,),
    ).fetchone()

    if row is None:
        return None

    CONNECTION.execute(
        "UPDATE awards SET disbursed = 1 WHERE id = ?",
        (award_id,),
    )
    return row[0]


def archive():
    """Report that the award archive operation was requested."""
    print("Archiving awards")


def by_scheme_count(scheme):
    """Return the number of awards for a scheme, or zero for None."""
    if scheme is None:
        return 0

    return CONNECTION.execute(
        "SELECT COUNT(*) FROM awards WHERE scheme = ?",
        (scheme,),
    ).fetchone()[0]


def main():
    """Create sample awards and demonstrate scholarship operations."""
    grant("Ishaan", "Merit", 50000)
    grant("Divya", "Need-based", 75000)

    print(disburse(1), disburse(9))
    total_disbursed = CONNECTION.execute(
        "SELECT COALESCE(SUM(amount), 0) FROM awards WHERE disbursed = 1"
    ).fetchone()[0]

    print(by_scheme_count("Merit"), total_disbursed)
    archive()


if __name__ == "__main__":
    main()
