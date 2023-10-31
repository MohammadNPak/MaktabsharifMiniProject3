<<<<<<< HEAD
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
=======
import re
from pathlib import Path
import glob

old_path = "images/"
new_path = "Icons/"

path_icon = str(Path.cwd().joinpath("front", "images"))

icon_files = sorted(glob.glob('*-icon*.png', root_dir=path_icon, recursive=True, include_hidden=True))

with open('Icons.txt', 'w') as iconfile:
    for icon_file in icon_files:
        iconfile.write(f"{path_icon}/{icon_file}\n")


path_html = str(Path.cwd().joinpath("front"))

html_files = glob.glob('*.html', root_dir=path_html, recursive=True, include_hidden=True)

for file_html in html_files:
   
    final_path = f"{path_html}/{file_html}"
    
    
    with open(final_path, "r") as html:
        html_content = html.read()

    
        pattern = re.compile(r'(?<=")' + re.escape(old_path) + r'(?=.*[-]icon[-]?1?)([^"]*)')
        
        
        new_html_content = re.sub(pattern, new_path + r'\1', html_content)

    with open(final_path, 'w') as html:
        html.write(new_html_content)
>>>>>>> Ghasemi
