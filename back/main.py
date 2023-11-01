from pathlib import Path
from bs4 import BeautifulSoup
import re


class PathNotFoundError(Exception):
    def __init__(self):
        msg = "Path dosn't exist"
    def __str__(self):
        return self.msg


def searchSorting (address): 
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

addrs = getaddress('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/images/')
# pathInput = input("Please Enter your Path: ")

sorted_list = searchSorting(addrs)



icon = addrs.glob("*icon*")
print(witre_on_txt(icon))

def replace_icon_dir(html):
    with open(html , "r")as file:
        a = file.read()
    return a
    # icons = re.findall('*icon*', a)
    # return icons
    



# html = replace_icon_dir('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/about.html')


with open('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/index.html',"r") as f:
    data = f.read()
    images = re.findall('(images.*-icon.*png)',data)
    
   
    print(images)
   
    
