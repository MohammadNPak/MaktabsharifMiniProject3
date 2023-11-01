from pathlib import Path



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

def witre_on_txt(icon):
    try: 
        crdr = Path.cwd()/"icon.txt"
        if not crdr.exists():
            with open("icon.txt" , 'w') as file:
                for i in icon :
                    file.write(str(i)+"\n")
            return "done"
        else:
            raise IOError  
    except IOError as e:
        return e
        

addrs = getaddress('/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/images/')
# pathInput = input("Please Enter your Path: ")

sorted_list = searchSorting(addrs)
icon = addrs.glob("*icon*")
witre_on_txt(icon)



# source = Path("hello.py")
# destination = Path("goodbye.py")

# if not destination.exists():
#     source.replace(destination)

# create_icon = Path.cwd()/"icon.txt"
# print(create_icon.exists())
# if not create_icon.exists():
#     Path.touch("icon.txt")

# create_icon = Path.cwd()/"icon.txt"
# icontxt = [i for i in create_icon]
# with newfile.open("w") as f: f.write()
# print(icontxt)


# for i in icon:
# create_icon.write_text(f"{i}")
# print(create_icon)
# create_icon.write

# a = newfile.touch()
# a.write_text()



# path = Path.cwd() / "shopping_list.md"
# with path.open(mode="r", encoding="utf-8") as md_file:
#     content = md_file.read()
#     groceries = [line for line in content.splitlines() if line.startswith("*")]
# print("\n".join(groceries))


