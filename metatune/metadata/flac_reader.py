from pathlib import Path
from mutagen.flac import FLAC

from metatune.models.track import Track
from metatune.models.credit import PersonCredit


def _get_list(audio, key):
    """Return list of values for a FLAC tag"""
    return audio.get(key, [])


def _get_first(audio, key, default=None):
    values = audio.get(key, [])
    return values[0] if values else default


def read_flac(path: Path) -> Track:
    audio = FLAC(path)

    # Track & album artists
    track_artists = _get_list(audio, "ARTIST")
    album_artist = _get_first(audio, "ALBUMARTIST", track_artists[0] if track_artists else "")

    # Credits
    composers = [
        PersonCredit(name=name, role="composer")
        for name in _get_list(audio, "COMPOSER")
    ]

    lyricists = [
        PersonCredit(name=name, role="lyricist")
        for name in (_get_list(audio, "LYRICIST") + _get_list(audio, "AUTHOR"))
    ]

    producers = [
        PersonCredit(name=name, role="producer")
        for name in _get_list(audio, "PRODUCER")
    ]

    # Build Track object
    track = Track(
        title=_get_first(audio, "TITLE", ""),
        track_artist=track_artists,
        album=_get_first(audio, "ALBUM", ""),
        album_artist=album_artist,
        disc_number=int(_get_first(audio, "DISCNUMBER", "1")),
        track_number=int(_get_first(audio, "TRACKNUMBER", "0")),
        path=path,

        composers=composers,
        lyricists=lyricists,
        producers=producers,

        isrc=_get_first(audio, "ISRC"),
        explicit=_get_first(audio, "ITUNESADVISORY")
    )

    return track
