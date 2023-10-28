from pathlib import Path
import glob
path_icon = str(Path.cwd().joinpath("front","images"))
files = sorted(glob.glob('*icon*.png',root_dir=path_icon,recursive=True,include_hidden=True))
with open('Icons.txt','w') as iconfile:
    for file in files:
        iconfile.write(file+"\n")