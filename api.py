from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "jobs.db"
FRONTEND_PATH = Path(__file__).parent / "frontend"

app = FastAPI(title="Jobify API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    return conn


@app.get("/api/jobs")
def list_jobs():
    conn = get_db()
    try:
        rows = conn.execute(
            """SELECT * FROM curated_jobs
               WHERE status = 'pending_review'
               ORDER BY pre_score DESC, filtered_at DESC"""
        ).fetchall()
        return [dict(row) for row in rows]
    finally:
        conn.close()


@app.patch("/api/jobs/{job_id}/discard")
def discard_job(job_id: int):
    conn = get_db()
    try:
        job = conn.execute(
            "SELECT id, raw_job_id FROM curated_jobs WHERE id = ?", (job_id,)
        ).fetchone()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        conn.execute(
            "UPDATE curated_jobs SET status = 'discarded' WHERE id = ?", (job_id,)
        )
        if job["raw_job_id"]:
            conn.execute(
                "UPDATE raw_jobs SET status = 'discarded' WHERE id = ?",
                (job["raw_job_id"],),
            )
        conn.commit()
        return {"ok": True}
    finally:
        conn.close()


@app.patch("/api/jobs/{job_id}/restore")
def restore_job(job_id: int):
    conn = get_db()
    try:
        job = conn.execute(
            "SELECT id, raw_job_id FROM curated_jobs WHERE id = ?", (job_id,)
        ).fetchone()
        if not job:
            raise HTTPException(status_code=404, detail="Job not found")
        conn.execute(
            "UPDATE curated_jobs SET status = 'pending_review' WHERE id = ?", (job_id,)
        )
        if job["raw_job_id"]:
            conn.execute(
                "UPDATE raw_jobs SET status = 'filtered_pass' WHERE id = ?",
                (job["raw_job_id"],),
            )
        conn.commit()
        return {"ok": True}
    finally:
        conn.close()


# Serve frontend — must be last
FRONTEND_PATH.mkdir(exist_ok=True)
app.mount("/", StaticFiles(directory=str(FRONTEND_PATH), html=True), name="static")
