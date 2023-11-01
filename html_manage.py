from pathlib import Path
import re

def find_html_files_and_update_icons():
    old_path = "images/"
    new_path = "Icons/"
    all_html_path = Path.cwd().joinpath("front")
    
    for html_file in all_html_path.glob("*.html"):
        try:
            html_data = html_file.read_text()
            
            pattern = re.compile(r'(?<=")' + re.escape(old_path) + r'(?=.*[-]icon[-]?1?)([^"]*)')
            new_html_content = re.sub(pattern, new_path + r'\1', html_data)
            
            new_html_file = Path(html_file.name)
            new_html_file.write_text(new_html_content)
        except Exception as e:
            print(f"An error occurred while processing {html_file}: {e}")

if __name__ == "__main":
    find_html_files_and_update_icons()
