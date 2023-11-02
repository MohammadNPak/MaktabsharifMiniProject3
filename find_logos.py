from pathlib import Path

def sort_file(path : Path, pattern):
    return sorted(path.glob(pattern))

directory_path = Path("front/images")
pattern = "*.png"
sort_file(directory_path, pattern)

file_pattern = "*-icon.png"
second_file_pattern = "*-icon-1.png"
matched_files = ""

matching_files = directory_path.glob(file_pattern)

for file_path in matching_files:
    matched_files += f"{str(file_path)}\n"

matching_files = directory_path.glob(second_file_pattern)
for file_path in matching_files:
    matched_files += f"{str(file_path)}\n"
    
Path('Icons.txt').write_text(str(matched_files))
