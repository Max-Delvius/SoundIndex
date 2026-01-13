from dataclasses import dataclass, field
from typing import Dict, List
from .track import Track

@dataclass
class Album:
    name: str
    album_artist: str
    release_date: str | None = None
    label: str | None = None
    barcode: str | None = None
    total_discs: int | None = None

    discs: Dict[int, List[Track]] = field(default_factory=dict)

    def add_track(self, track: Track):
        self.discs.setdefault(track.disc_number, []).append(track)
