#!/usr/bin/env python3
"""
Filter raw_jobs applying dealbreaker rules and pre-scoring,
then insert passing jobs into curated_jobs.
"""
import sqlite3
import re
from pathlib import Path

DB_PATH = Path(__file__).parent.parent / "jobs.db"

# --- Keyword lists ---

REMOTE_PASS = ["remote", "distributed", "work from home", "wfh", "work from anywhere", "remote-first", "fully remote", "worldwide", "anywhere"]
ONSITE_REJECT = ["on-site", "onsite", "in-office", "office-based", "must be based in", "office required", "relocation required", "in person"]

JUNIOR_REJECT = ["junior", "associate designer", "entry-level", "entry level", "intern"]
SENIOR_PASS = ["senior", "lead", "principal", "staff", "head of"]

NON_DESIGN_REJECT = ["graphic designer", "motion designer", "illustrator", "brand designer", "marketing designer"]
DESIGN_PASS = ["product designer", "ux designer", "ui/ux", "ui designer", "experience designer", "design lead", "product design"]

AGENCY_REJECT = ["join our talent pool", "register with us", "future opportunities"]
AGENCY_NAME = ["agency", "studio", "consultancy", "consulting"]

B2B_KEYWORDS = ["b2b", "saas", "enterprise", "fintech", "financial", "payment", "platform", "api", "developer tools", "workflow", "dashboard", "analytics", "data visualization", "data-heavy", "complex product"]
REMOTE_FIRST = ["remote-first", "distributed team", "fully remote", "async culture", "remote first"]
SERIES = ["series a", "series b", "series c", "well-funded", "backed by", "venture"]
DESIGN_SYS = ["design system", "scale design", "first design hire", "build design culture", "design ops"]
RED_FLAGS = ["fast-paced environment", "wear many hats", "startup mentality", "move fast and break things"]
EQUITY = ["equity", "stock options", "esop", "vesting"]
FINTECH = ["fintech", "financial services", "payments", "banking", "lending", "investment", "trading"]
COMPLEXITY = ["complex", "data-heavy", "enterprise", "technical users", "b2b"]


def text(*fields) -> str:
    return " ".join((f or "").lower() for f in fields)


def contains_any(haystack: str, needles: list) -> list:
    return [n for n in needles if n in haystack]


def check_dealbreakers(role: str, company: str, location: str, description: str, salary: str):
    """Returns (rejected: bool, reason: str)"""
    t = text(role, company, location, description)
    loc = text(location)
    desc = text(description)

    # 1. On-site
    if contains_any(t, ONSITE_REJECT) and not contains_any(loc, REMOTE_PASS):
        if not contains_any(desc, REMOTE_PASS):
            return True, "on_site"

    # 2. No remote signal at all (location is a specific city with no remote mention)
    if location and not contains_any(loc, REMOTE_PASS) and not contains_any(desc, REMOTE_PASS):
        # If location looks like a specific city (no "remote" anywhere)
        if not any(x in loc for x in ["remote", "worldwide", "anywhere", "global"]):
            return True, "on_site"

    # 3. Junior / non-senior
    role_lower = (role or "").lower()
    if contains_any(role_lower, JUNIOR_REJECT):
        return True, "seniority_mismatch"

    # 4. Must be a design/UX/product design role
    design_role_keywords = ["designer", "ux", "ui", "experience design", "product design", "design lead", "head of design", "design manager"]
    if not contains_any(role_lower, design_role_keywords):
        return True, "off_role"
    if contains_any(role_lower, NON_DESIGN_REJECT):
        return True, "off_role"

    # 5. Agency with no project
    if contains_any(text(company), AGENCY_REJECT) or contains_any(desc, AGENCY_REJECT):
        return True, "agency_no_project"

    # 6. Salary below minimum
    if salary:
        amount = parse_salary(salary)
        if amount and amount < 2000:
            return True, "salary_below_minimum"

    return False, ""


def parse_salary(salary_str: str):
    """Try to extract a monthly USD figure from salary string."""
    s = salary_str.lower().replace(",", "")
    nums = re.findall(r"\d+", s)
    if not nums:
        return None
    amount = int(nums[0])
    if "year" in s or "yr" in s or "annual" in s or "annu" in s or amount > 10000:
        return amount / 12
    return amount


def calculate_score(role: str, company: str, location: str, description: str, salary: str):
    """Returns (score, green_flags, yellow_flags, red_flags, keywords_matched)"""
    score = 5
    green, yellow, red, keywords = [], [], [], []

    t = text(role, company, location, description)
    role_lower = (role or "").lower()
    desc_lower = (description or "").lower()
    loc_lower = (location or "").lower()

    # +2 B2B/SaaS/Fintech
    matched_b2b = contains_any(t, B2B_KEYWORDS)
    if matched_b2b:
        score += 2
        green.append(f"B2B/SaaS/Fintech signals: {', '.join(matched_b2b[:3])}")
        keywords.extend(matched_b2b[:3])

    # +2 Seniority match
    if contains_any(role_lower, SENIOR_PASS):
        score += 2
        green.append("Senior/Lead/Principal role")
    else:
        score -= 2
        red.append("No seniority indicator in title")

    # +2 Remote-first
    if contains_any(t, REMOTE_FIRST):
        score += 2
        green.append("Remote-first culture")
    elif contains_any(loc_lower, REMOTE_PASS):
        score += 1
        green.append("Remote allowed")

    # +1 Series A+
    if contains_any(t, SERIES):
        score += 1
        green.append("Funded company (Series A+)")
        keywords.append("funded")

    # +1 Salary transparency
    if salary and salary.strip():
        score += 1
        green.append(f"Salary disclosed: {salary}")
    else:
        score -= 1
        yellow.append("No salary info")

    # +1 Design systems / leadership
    if contains_any(t, DESIGN_SYS):
        score += 1
        green.append("Design systems or leadership opportunity")
        keywords.append("design system")

    # +1 Equity
    if contains_any(t, EQUITY):
        score += 1
        green.append("Equity offered")

    # -1 Hybrid Ecuador
    if "hybrid" in loc_lower or "hybrid" in desc_lower:
        score -= 1
        red.append("Hybrid (not fully remote)")

    # -2 Agency
    company_lower = (company or "").lower()
    if contains_any(company_lower, AGENCY_NAME):
        score -= 2
        red.append("Agency/consultancy model")

    # -1 B2C
    if any(x in t for x in ["b2c", "consumer app", "consumer product", "e-commerce", "ecommerce"]):
        score -= 1
        red.append("B2C focus")

    # -3 Red flag phrases
    matched_rf = contains_any(t, RED_FLAGS)
    if matched_rf:
        score -= min(3, len(matched_rf))
        red.append(f"Red flag language: {', '.join(matched_rf)}")

    score = max(1, min(10, score))
    return score, green, yellow, red, keywords


def priority(score: int) -> str:
    if score >= 8:
        return "high"
    if score >= 6:
        return "medium"
    return "low"


def run():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys=ON")

    rows = conn.execute(
        "SELECT id, company, role, url, location, salary, description, source "
        "FROM raw_jobs WHERE status = 'unprocessed'"
    ).fetchall()

    print(f"Processing {len(rows)} unprocessed jobs...")

    passed = 0
    rejected = 0
    reject_reasons = {}

    for row in rows:
        rejected_flag, reason = check_dealbreakers(
            row["role"], row["company"], row["location"], row["description"], row["salary"]
        )

        if rejected_flag:
            conn.execute(
                "UPDATE raw_jobs SET status='filtered_reject', rejection_reason=? WHERE id=?",
                (reason, row["id"])
            )
            reject_reasons[reason] = reject_reasons.get(reason, 0) + 1
            rejected += 1
        else:
            score, green, yellow, red, keywords = calculate_score(
                row["role"], row["company"], row["location"], row["description"], row["salary"]
            )

            if score < 5:
                conn.execute(
                    "UPDATE raw_jobs SET status='filtered_reject', rejection_reason=? WHERE id=?",
                    ("low_score", row["id"])
                )
                reject_reasons["low_score"] = reject_reasons.get("low_score", 0) + 1
                rejected += 1
                continue

            try:
                conn.execute(
                    """INSERT INTO curated_jobs
                    (raw_job_id, company, role, url, description, location, salary,
                     pre_score, priority, keywords_matched, green_flags, yellow_flags, red_flags)
                    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (
                        row["id"],
                        row["company"], row["role"], row["url"],
                        row["description"], row["location"], row["salary"],
                        score, priority(score),
                        ", ".join(keywords),
                        "\n".join(f"✅ {g}" for g in green),
                        "\n".join(f"⚠️ {y}" for y in yellow),
                        "\n".join(f"🚩 {r}" for r in red),
                    )
                )
                conn.execute(
                    "UPDATE raw_jobs SET status='filtered_pass' WHERE id=?", (row["id"],)
                )
                passed += 1
            except sqlite3.IntegrityError:
                pass

    conn.commit()
    conn.close()

    print(f"\n{'='*40}")
    print(f"Procesados:  {len(rows)}")
    print(f"Pasaron:     {passed} → curated_jobs")
    print(f"Rechazados:  {rejected}")
    for reason, count in sorted(reject_reasons.items(), key=lambda x: -x[1]):
        print(f"  - {reason}: {count}")

    # Top 10 by score
    conn2 = sqlite3.connect(DB_PATH)
    conn2.row_factory = sqlite3.Row
    top = conn2.execute(
        "SELECT role, company, pre_score, priority, salary FROM curated_jobs ORDER BY pre_score DESC LIMIT 10"
    ).fetchall()
    conn2.close()

    print(f"\nTop 10 por pre-score:")
    for i, j in enumerate(top, 1):
        sal = f" — {j['salary']}" if j['salary'] else ""
        print(f"  {i}. [{j['pre_score']}/10 {j['priority'].upper()}] {j['role']} @ {j['company']}{sal}")


if __name__ == "__main__":
    run()
