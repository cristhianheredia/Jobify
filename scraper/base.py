from abc import ABC, abstractmethod
from typing import Iterator
import httpx
from .models import Job

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; JobifyBot/1.0; job search aggregator)"
}


class BaseScraper(ABC):
    name: str

    def __init__(self):
        self.client = httpx.Client(headers=HEADERS, timeout=30, follow_redirects=True)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.client.close()

    @abstractmethod
    def scrape(self) -> Iterator[Job]:
        ...

    def get(self, url: str, **kwargs) -> httpx.Response:
        response = self.client.get(url, **kwargs)
        response.raise_for_status()
        return response
