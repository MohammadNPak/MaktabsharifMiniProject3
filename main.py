from pathlib import Path
import glob
import re
path_icon = str(Path.cwd().joinpath("front","images"))
files = sorted(glob.glob('*icon*.png',root_dir=path_icon,recursive=True,include_hidden=True))
with open('Icons.txt','w') as iconfile:
    for file in files:
        iconfile.write(f"{path_icon}\{file}'\n'")

path_html = str(Path.cwd().joinpath("front"))
files_html = glob.glob('*.html',root_dir=path_html,recursive=True,include_hidden=True)
content_html = []
file_lst_trimmed =[]
for file_html in files_html:
    finally_path = f"{path_html}/{file_html}"
    with open(finally_path,"r") as html:
         file_lst_trimmed = [re.sub(r'"img/([[A-Za-z]+]+\.(png))"', 'icons', file) for file in html]
    with open(finally_path,'w') as html:
        for item in file_lst_trimmed:
            print(item)
            html.write(item)
print(file_lst_trimmed[0])