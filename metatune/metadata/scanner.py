from pathlib import Path
from .flac_reader import read_flac


def scan_folder(folder: Path):
    tracks = []
    for flac in folder.rglob("*.flac"):
        try:
            tracks.append(read_flac(flac))
        except Exception as e:
            print(f"Failed to read {flac.name}: {e}")
    return tracks
