import sqlite3
from datetime import datetime
from typing import Optional, List, Dict


DB_NAME = "spotit.db"


def get_connection():
    """Create and return a SQLite database connection."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create reports table if it does not already exist."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reports (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            report_id TEXT UNIQUE NOT NULL,
            category TEXT NOT NULL,
            description TEXT NOT NULL,
            location TEXT NOT NULL,
            date TEXT,
            time TEXT,
            image_path TEXT,
            status TEXT DEFAULT 'Submitted',
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def create_report(
    report_id: str,
    category: str,
    description: str,
    location: str,
    date: str = "",
    time: str = "",
    image_path: str = ""
) -> bool:
    """Insert a new report into the database."""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO reports (
                report_id,
                category,
                description,
                location,
                date,
                time,
                image_path,
                status,
                created_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            report_id,
            category,
            description,
            location,
            date,
            time,
            image_path,
            "Submitted",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        ))

        conn.commit()
        conn.close()
        return True

    except sqlite3.Error as error:
        print("Database error:", error)
        return False


def get_report(report_id: str) -> Optional[Dict]:
    """Get one report using report ID."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM reports WHERE report_id = ?",
        (report_id,)
    )

    row = cursor.fetchone()
    conn.close()

    if row:
        return dict(row)

    return None


def get_all_reports() -> List[Dict]:
    """Get all reports from the database."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports ORDER BY created_at DESC")

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


def update_status(report_id: str, status: str) -> bool:
    """Update report status."""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE reports
            SET status = ?
            WHERE report_id = ?
        """, (status, report_id))

        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()

        return updated

    except sqlite3.Error as error:
        print("Database error:", error)
        return False


def delete_report(report_id: str) -> bool:
    """Delete a report using report ID."""
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM reports WHERE report_id = ?",
            (report_id,)
        )

        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()

        return deleted

    except sqlite3.Error as error:
        print("Database error:", error)
        return False


def get_report_stats() -> Dict:
    """Return dashboard statistics."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM reports")
    total_reports = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status = 'Submitted'")
    submitted_reports = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status = 'Under Review'")
    under_review_reports = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status = 'Verified'")
    verified_reports = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM reports WHERE status = 'Resolved'")
    resolved_reports = cursor.fetchone()[0]

    conn.close()

    return {
        "total_reports": total_reports,
        "submitted_reports": submitted_reports,
        "under_review_reports": under_review_reports,
        "verified_reports": verified_reports,
        "resolved_reports": resolved_reports
    }


def get_reports_by_category() -> List[Dict]:
    """Return report count grouped by category."""
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, COUNT(*) as count
        FROM reports
        GROUP BY category
        ORDER BY count DESC
    """)

    rows = cursor.fetchall()
    conn.close()

    return [dict(row) for row in rows]


if __name__ == "__main__":
    init_db()
    print("SpotIt database initialized successfully.")