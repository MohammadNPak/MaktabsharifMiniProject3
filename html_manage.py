from pathlib import Path
import re
from Exceptions import FileOpenError
def find_html_files_and_update_icons():
    old_path = "images/"
    new_path = "Icons/"
    all_html_path = Path.cwd().joinpath("front")
    
    for html_file in all_html_path.glob("*.html"):
        try:
            html_data = html_file.read_text()
            
            pattern = re.compile(r'(?<=")' + re.escape(old_path) + r'(?=.*[-]icon[-]?1?)([^"]*)')
            new_html_content = re.sub(pattern, new_path + r'\1', html_data)
            html_path = Path(f"{all_html_path}\{html_file.name}")
            html_path.write_text(new_html_content)
        except FileOpenError as e:
            raise (f"An error occurred while processing {html_file}: {e}")
    print("find html file successfully")

if __name__ == "__main__":
    find_html_files_and_update_icons()
