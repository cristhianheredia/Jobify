from typing import Iterator, List
import xml.etree.ElementTree as ET
from ..base import BaseScraper
from ..models import Job

FEEDS = [
    "https://weworkremotely.com/categories/remote-programming-jobs.rss",
    "https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss",
    "https://weworkremotely.com/categories/remote-design-jobs.rss",
    "https://weworkremotely.com/categories/remote-product-jobs.rss",
    "https://weworkremotely.com/categories/remote-data-science-jobs.rss",
]


class WeWorkRemotelyScraper(BaseScraper):
    name = "weworkremotely"

    def scrape(self) -> Iterator[Job]:
        for feed_url in FEEDS:
            try:
                yield from self._parse_feed(feed_url)
            except Exception:
                continue

    def _parse_feed(self, url: str) -> Iterator[Job]:
        root = ET.fromstring(self.get(url).text)
        channel = root.find("channel")
        if channel is None:
            return
        for item in channel.findall("item"):
            title_el = item.find("title")
            link_el = item.find("link")
            pubdate_el = item.find("pubDate")
            if title_el is None or link_el is None:
                continue
            raw_title = (title_el.text or "").strip()
            if ": " in raw_title:
                company, role = raw_title.split(": ", 1)
            else:
                company, role = "", raw_title
            posted_date = pubdate_el.text.strip() if pubdate_el is not None and pubdate_el.text else None
            yield Job(
                role=role.strip(),
                company=company.strip(),
                url=(link_el.text or "").strip(),
                source=self.name,
                location="Remote",
                posted_date=posted_date,
            )
