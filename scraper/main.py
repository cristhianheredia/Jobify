#!/usr/bin/env python3
"""
Jobify scraper — aggregates remote job listings from multiple sources.

Usage:
    python -m scraper.main              # run all scrapers
    python -m scraper.main --sources remoteok remotive
    python -m scraper.main --list
"""
import argparse
import sys
from typing import List, Optional
from .sources import ALL_SCRAPERS
from .storage import get_db, save_job, job_count


def run(scraper_names: Optional[List[str]] = None):
    scrapers = (
        ALL_SCRAPERS
        if not scraper_names
        else [s for s in ALL_SCRAPERS if s.name in scraper_names]
    )
    if not scrapers:
        print(f"No scrapers matched: {scraper_names}", file=sys.stderr)
        sys.exit(1)

    with get_db() as conn:
        before = job_count(conn)
        for ScraperClass in scrapers:
            scraper = ScraperClass()
            new, errors = 0, 0
            print(f"[{scraper.name}] scraping...", end=" ", flush=True)
            try:
                with scraper:
                    for job in scraper.scrape():
                        if not job.role or not job.url:
                            continue
                        if save_job(conn, job):
                            new += 1
            except Exception as e:
                print(f"ERROR — {e}")
                errors += 1
                continue
            status = f"{new} new"
            if errors:
                status += f", {errors} errors"
            print(status)
        after = job_count(conn)

    print(f"\nDone. Total jobs in DB: {after} (+{after - before} this run)")


def main():
    parser = argparse.ArgumentParser(description="Jobify scraper")
    parser.add_argument(
        "--sources",
        nargs="+",
        metavar="NAME",
        help="Only run these scrapers (default: all)",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available scrapers and exit",
    )
    args = parser.parse_args()

    if args.list:
        for s in ALL_SCRAPERS:
            print(f"  {s.name}")
        return

    run(args.sources)


if __name__ == "__main__":
    main()
