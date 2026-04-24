import sqlite3
from pathlib import Path
from contextlib import contextmanager
from .models import Job

DB_PATH = Path(__file__).parent.parent / "jobs.db"

SCHEMA = """
CREATE TABLE IF NOT EXISTS raw_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    role TEXT,
    url TEXT UNIQUE,
    description TEXT,
    location TEXT,
    salary TEXT,
    posted_date TEXT,
    source TEXT,
    status TEXT DEFAULT 'unprocessed',
    rejection_reason TEXT,
    scraped_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS curated_jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    raw_job_id INTEGER UNIQUE,
    company TEXT,
    role TEXT,
    url TEXT,
    description TEXT,
    location TEXT,
    salary TEXT,
    pre_score INTEGER,
    priority TEXT,
    keywords_matched TEXT,
    green_flags TEXT,
    yellow_flags TEXT,
    red_flags TEXT,
    status TEXT DEFAULT 'pending_review',
    filtered_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    notes TEXT,
    FOREIGN KEY (raw_job_id) REFERENCES raw_jobs(id)
);
"""


@contextmanager
def get_db(path: Path = DB_PATH):
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    for statement in SCHEMA.strip().split(";"):
        if statement.strip():
            conn.execute(statement)
    conn.commit()
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()


def save_job(conn: sqlite3.Connection, job: Job) -> bool:
    """Insert job into raw_jobs, skip if URL already exists. Returns True if inserted."""
    try:
        conn.execute(
            """
            INSERT INTO raw_jobs (company, role, url, description, location, salary, posted_date, source)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job.company,
                job.role,
                job.url,
                job.description,
                job.location,
                job.salary,
                job.posted_date,
                job.source,
            ),
        )
        return True
    except sqlite3.IntegrityError:
        return False


def job_count(conn: sqlite3.Connection) -> int:
    return conn.execute("SELECT COUNT(*) FROM raw_jobs").fetchone()[0]
