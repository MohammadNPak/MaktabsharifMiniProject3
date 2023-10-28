#  part 1 done 
# sort files by (A-Z) : done
#find *-icon.* , *-icon-l.*
from pathlib import Path



  

def searchSorting (address): 
    return  sorted(Path(address).glob("*"))


addrs = '/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/images/'
# pathInput = input("Please Enter your Path: ")
# address = Path.glob(addrs,recursive=True ,include_hidden=True )
sorted_list = searchSorting(addrs)
# for i in sorted_list:
#     print(i)
# print(sorted_list)

icon = Path(addrs).glob("*icon*")
with open("icon.txt" , 'w') as file:

    for i in icon :
        file.write(str(i)+"\n")


