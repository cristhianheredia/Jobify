from typing import Iterator, Optional
from datetime import datetime, timezone
import re
from ..base import BaseScraper
from ..models import Job

ALGOLIA_SEARCH = "https://hn.algolia.com/api/v1/search"
ITEM_URL = "https://hacker-news.firebaseio.com/v0/item/{}.json"


class HackerNewsScraper(BaseScraper):
    name = "hackernews"

    def scrape(self) -> Iterator[Job]:
        thread_id = self._find_latest_hiring_thread()
        if not thread_id:
            return
        yield from self._parse_thread(thread_id)

    def _find_latest_hiring_thread(self) -> Optional[int]:
        params = {"query": "Ask HN: Who is Hiring?", "tags": "ask_hn", "hitsPerPage": 5}
        hits = self.get(ALGOLIA_SEARCH, params=params).json().get("hits", [])
        hiring = [h for h in hits if "hiring" in h.get("title", "").lower()]
        if not hiring:
            return None
        hiring.sort(key=lambda h: h.get("created_at_i", 0), reverse=True)
        return int(hiring[0]["objectID"])

    def _parse_thread(self, thread_id: int) -> Iterator[Job]:
        data = self.get(ITEM_URL.format(thread_id)).json()
        for kid_id in data.get("kids", [])[:100]:
            try:
                yield from self._parse_comment(kid_id)
            except Exception:
                continue

    def _parse_comment(self, comment_id: int) -> Iterator[Job]:
        data = self.get(ITEM_URL.format(comment_id)).json()
        text = data.get("text", "") or ""
        if not text or data.get("dead") or data.get("deleted"):
            return
        first_line = re.sub(r"<[^>]+>", "", text.split("\n")[0]).strip()
        parts = [p.strip() for p in re.split(r"\|", first_line)]
        company = parts[0] if parts else "Unknown"
        role = parts[1] if len(parts) > 1 else first_line[:80]
        location = parts[2] if len(parts) > 2 else "Remote"
        posted_date = None
        if data.get("time"):
            posted_date = datetime.fromtimestamp(data["time"], tz=timezone.utc).isoformat()
        yield Job(
            role=role[:120],
            company=company[:120],
            url=f"https://news.ycombinator.com/item?id={comment_id}",
            source=self.name,
            location=location[:120],
            description=re.sub(r"<[^>]+>", "", text)[:500],
            posted_date=posted_date,
        )
