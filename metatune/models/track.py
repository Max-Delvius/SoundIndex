from dataclasses import dataclass, field
from pathlib import Path
from typing import List

from .credit import PersonCredit

@dataclass
class Track:
    title: str
    track_artist: List[str]          # performers on this track
    album: str
    album_artist: str                # main album artist
    disc_number: int
    track_number: int
    path: Path

    composers: List[PersonCredit] = field(default_factory=list)
    lyricists: List[PersonCredit] = field(default_factory=list)
    producers: List[PersonCredit] = field(default_factory=list)

    isrc: str | None = None
    explicit: bool | None = None
