from typing import Iterator
from ..base import BaseScraper
from ..models import Job


class RemoteOKScraper(BaseScraper):
    name = "remoteok"
    URL = "https://remoteok.com/api"

    def scrape(self) -> Iterator[Job]:
        data = self.get(self.URL).json()
        for item in data[1:]:
            if not isinstance(item, dict):
                continue
            yield Job(
                role=item.get("position", "").strip(),
                company=item.get("company", "").strip(),
                url=item.get("url") or f"https://remoteok.com/remote-jobs/{item.get('id', '')}",
                source=self.name,
                location=item.get("location") or "Remote",
                salary=item.get("salary") or None,
                description=item.get("description", "")[:500] if item.get("description") else None,
                posted_date=item.get("date"),
            )
