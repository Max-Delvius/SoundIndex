from collections import defaultdict
from typing import List

from metatune.models.album import Album
from metatune.models.track import Track


def build_albums(tracks: List[Track]) -> List[Album]:
    albums_map = {}

    for track in tracks:
        album_key = (track.album, track.album_artist)

        if album_key not in albums_map:
            albums_map[album_key] = Album(
                name=track.album,
                album_artist=track.album_artist
            )

        albums_map[album_key].add_track(track)

    # Sort tracks inside each disc
    for album in albums_map.values():
        for disc_number, disc_tracks in album.discs.items():
            album.discs[disc_number] = sorted(
                disc_tracks, key=lambda t: t.track_number
            )

    return list(albums_map.values())
