from pathlib import Path
from metatune.metadata.scanner import scan_folder
from metatune.metadata.album_builder import build_albums


def main():
    test_folder = Path(__file__).resolve().parent.parent / "test_flac"

    tracks = scan_folder(test_folder)
    albums = build_albums(tracks)

    for album in albums:
        print(f"\nAlbum: {album.name}")
        print(f"Album Artist: {album.album_artist}")

        for disc, disc_tracks in sorted(album.discs.items()):
            print(f"  Disc {disc}")
            for t in disc_tracks:
                print(f"    {t.track_number}. {t.title}")


if __name__ == "__main__":
    main()
