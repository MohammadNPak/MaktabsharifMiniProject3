import requests
import json
token = "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"
headers = {'Authorization':f'Bearer {token}','accept': 'application/vnd.github+json'}
url = "https://api.github.com/repos/MohRezam/MaktabsharifMiniProject3/commits/ehsan-asgari"
login = requests.get(url,headers=headers)
print(login.text)