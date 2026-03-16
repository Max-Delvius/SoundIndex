from mutagen import File


def read_tags(file_path):
    audio = File(file_path, easy=True)

    if not audio:
        return {}

    tags = {
        "title": audio.get("title", [""])[0],
        "artist": audio.get("artist", [""])[0],
        "album": audio.get("album", [""])[0],
        "date": audio.get("date", [""])[0],
        "genre": audio.get("genre", [""])[0],
    }

    return tags