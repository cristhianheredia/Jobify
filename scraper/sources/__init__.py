from .remoteok import RemoteOKScraper
from .remotive import RemotiveScraper
from .weworkremotely import WeWorkRemotelyScraper
from .arbeitnow import ArbeitnowScraper
from .hackernews import HackerNewsScraper

ALL_SCRAPERS = [
    RemoteOKScraper,
    RemotiveScraper,
    WeWorkRemotelyScraper,
    ArbeitnowScraper,
    HackerNewsScraper,
]
