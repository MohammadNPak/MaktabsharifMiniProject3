from pathlib import Path
import re


class PathNotFoundError(Exception):
    def __init__(self):
        msg = "Path dosn't exist"
    def __str__(self):
        return self.msg


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

# pathInput = input("Please Enter your Path: ")

icon_adr = getaddress('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/images/')
html_adr = getaddress('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front')
sorted_list = searchSorting(icon_adr)
icon = icon_adr.glob("*icon*")
html_files = html_adr.glob(".html")
for i in html_files:
    print(i)
print(html_files)
print(witre_on_txt(icon))

def replace_icon_dir(html):
    file = '/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/index.html'
    with open(file,"r") as f:
        data = f.readlines()

    with open(file, "w") as file_data:
        pattern = re.compile('(images.*-icon.*png)')
        for i in data:

            if re.search(pattern,i): 
                file_data.writelines(i.replace("images","icon"))
            else:
                file_data.writelines(i)
            
    
    

