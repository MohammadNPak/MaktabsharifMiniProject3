from pathlib import Path
import re
from Exceptions import FileOpenError,CustomExceptions

def find_icon_dir():
    try:
        png_path = Path.cwd().joinpath("front", "images")
        if not png_path:
            raise FileOpenError (f"can't open file{png_path} or file{png_path} doesn't exist.")

        for file_path in sorted(png_path.glob("*.png")):
            print(file_path.name)

        icons = ""
        for icon_path in png_path.glob("*icon*.png"):
            icons += f"{icon_path}\n"
            # Path.unlink(icon_path)

        Path('Icons.txt').write_text(icons)
    except CustomExceptions as e:
        raise(f"An error occurred: {e}")

if __name__ == "__main__":
    find_icon_dir()
