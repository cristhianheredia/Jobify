from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Job:
    role: str
    company: str
    url: str
    source: str
    location: str = "Remote"
    salary: Optional[str] = None
    description: Optional[str] = None
    posted_date: Optional[str] = None
