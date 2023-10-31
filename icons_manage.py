from pathlib import Path
import re

def find_icon_dir():
    try:
        png_path = Path.cwd().joinpath("front", "images")

        for file_path in sorted(png_path.glob("*.png")):
            print(file_path.name)

        icons = ""
        for icon_path in png_path.glob("*icon*.png"):
            icons += f"{icon_path}\n"
            # Path.unlink(icon_path)

        Path('Icons.txt').write_text(icons)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    find_icon_dir()
