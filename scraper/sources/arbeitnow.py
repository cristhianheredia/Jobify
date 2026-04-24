from typing import Iterator
from datetime import datetime
from ..base import BaseScraper
from ..models import Job


class ArbeitnowScraper(BaseScraper):
    name = "arbeitnow"
    URL = "https://www.arbeitnow.com/api/job-board-api"

    def scrape(self) -> Iterator[Job]:
        page = 1
        while True:
            data = self.get(self.URL, params={"page": page}).json()
            jobs = data.get("data", [])
            if not jobs:
                break
            for item in jobs:
                posted_date = None
                if item.get("created_at"):
                    try:
                        posted_date = datetime.fromtimestamp(item["created_at"]).isoformat()
                    except Exception:
                        pass
                yield Job(
                    role=item.get("title", "").strip(),
                    company=item.get("company_name", "").strip(),
                    url=item.get("url", ""),
                    source=self.name,
                    location=item.get("location") or "Remote",
                    description=item.get("description", "")[:500] if item.get("description") else None,
                    posted_date=posted_date,
                )
            if page >= 3:
                break
            page += 1
