from core.library_scanner import scan_music_folder
from core.tag_reader import read_tags

music_folder = "C:/Users/KSC/Downloads/Kansas - Point Of Know Return (Expanded Edition)"

files = scan_music_folder(music_folder)

print("Found files:", len(files))

for f in files[:5]:   # show first 5 files
    tags = read_tags(f)

    print("\nFile:", f)
    print(tags)