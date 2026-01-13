import musicbrainzngs as mb

mb.set_useragent(
    "SoundIndex",
    "0.1",
    "https://github.com/yourname/soundindex"
)

def search_album(album_name: str):
    result = mb.search_releases(
        release=album_name,
        limit=5
    )
    return result["release-list"]