#  part 1 done
# sort files by (A-Z) : done
# find *-icon.* , *-icon-l.*
from pathlib import Path


def searchSorting(address):
    return sorted(addrs.glob("*"))


# Path.exists():
#     pass
addrs = Path('../front/images/')
# pathInput = input("Please Enter your Path: ")
# address = Path.glob(addrs,recursive=True ,include_hidden=True )
sorted_list = searchSorting(addrs)
# for i in sorted_list:
#     print(i)
# print(sorted_list)

icon = addrs.glob("*icon*")
with open("icon.txt", 'w') as file:

    for i in icon:
        file.write(str(i)+"\n")


newfile = Path('.') / "icon.txt"
with newfile.open("w") as f:
    f.write()

a = newfile.touch()
a.write_text()


path = Path.cwd() / "shopping_list.md"
with path.open(mode="r", encoding="utf-8") as md_file:
    content = md_file.read()
    groceries = [line for line in content.splitlines() if line.startswith("*")]
print("\n".join(groceries))

# write_text() opens the path and writes string data to it


source = Path("hello.py")
destination = Path("goodbye.py")

if not destination.exists():
    source.replace(destination)
