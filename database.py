import sqlite3
import os
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_NAME = os.path.join(BASE_DIR, "spotit.db")


def get_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
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


def create_report(report_id, category, description, location, date="", time="", image_path=""):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO reports (
                report_id, category, description, location,
                date, time, image_path, status, created_at
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


def get_report(report_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports WHERE report_id = ?", (report_id,))
    row = cursor.fetchone()

    conn.close()

    if row:
        return dict(row)
    return None


def get_all_reports():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM reports ORDER BY created_at DESC")
    rows = cursor.fetchall()

    conn.close()

    return [dict(row) for row in rows]


def update_status(report_id, status):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE reports SET status = ? WHERE report_id = ?",
            (status, report_id)
        )

        conn.commit()
        updated = cursor.rowcount > 0
        conn.close()

        return updated

    except sqlite3.Error as error:
        print("Database error:", error)
        return False


def delete_report(report_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM reports WHERE report_id = ?", (report_id,))

        conn.commit()
        deleted = cursor.rowcount > 0
        conn.close()

        return deleted

    except sqlite3.Error as error:
        print("Database error:", error)
        return False


def get_report_stats():
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


def get_reports_by_category():
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