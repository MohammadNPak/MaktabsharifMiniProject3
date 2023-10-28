#  part 1 done 
# sort files by (A-Z)
from pathlib import Path



from glob import glob
  
address = '/Users/SMD/Desktop/GW2/MaktabsharifMiniProject3/front/images/*'

def searchSorting (address): 
    yield (name for name in sorted(glob(address)))     


sorted_list = searchSorting(address=address)

print(sorted_list)