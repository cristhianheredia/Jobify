from typing import Iterator
from ..base import BaseScraper
from ..models import Job


class RemotiveScraper(BaseScraper):
    name = "remotive"
    URL = "https://remotive.com/api/remote-jobs"

    def scrape(self) -> Iterator[Job]:
        data = self.get(self.URL).json()
        for item in data.get("jobs", []):
            yield Job(
                role=item.get("title", "").strip(),
                company=item.get("company_name", "").strip(),
                url=item.get("url", ""),
                source=self.name,
                location=item.get("candidate_required_location") or "Remote",
                salary=item.get("salary") or None,
                description=item.get("description", "")[:500] if item.get("description") else None,
                posted_date=item.get("publication_date"),
            )
