from pathlib import Path
import re
from exception import PathNotFoundError


def searchSorting (addrs): 
    return  sorted(addrs.glob("*"))

def getaddress(address):
    ad = Path(address)
    if not ad.exists():
        raise PathNotFoundError
    return ad

def witre_on_txt(filetext):
    with open("icon.txt" , 'w') as file:
        for i in filetext :
            file.write(str(i)+"\n")
    return "done"

def replace_icon_dir(html):
    with open(html,"r") as f:
        data = f.readlines()
    with open(html, "w") as file_data:
        pattern = re.compile('(images.*-icon.*png)')
        for i in data:
            if re.search(pattern,i): 
                file_data.writelines(i.replace("images","icon"))
            else:
                file_data.writelines(i)
            


icon_adr = getaddress('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/images/')
html_adr = getaddress('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front')
sorted_list = searchSorting(icon_adr)
icon = icon_adr.glob("*icon*")
html_files = html_adr.glob("*.html")

for i in html_files:
    replace_icon_dir(i)
    print(f'{i} has been repalced')

print(witre_on_txt(icon))

    
    

