from pathlib import Path
import re

directory_path = Path(r"front")
html_pattern = "*.html"

html_file_path = directory_path.glob(html_pattern)
img_pattern = r'<img src="images\/(.*)(-icon|-icon-1)\.png">'
for html_file in html_file_path:
    result = None
    with open(html_file, "r") as f:
        content = f.read()
        result = re.sub(img_pattern, r'<img src="Icons/\1\2.png">', content)
        print(type(result))
    with open(html_file, "w") as f:
        f.write(result)


