import os

SUPPORTED_FORMATS = (".mp3", ".flac", ".m4a", ".ogg", ".wav")


def scan_music_folder(folder_path):
    music_files = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(SUPPORTED_FORMATS):
                full_path = os.path.join(root, file)
                music_files.append(full_path)

    return music_files