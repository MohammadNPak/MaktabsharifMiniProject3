import requests
token = "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"
headers = {'Authorization':f'Bearer {token}','accept': 'application/vnd.github+json'}
url = "https://api.github.com/repos/ehsan-asg/MaktabsharifMiniProject3/commits"
login = requests.get(url,headers=headers)
print(login.json())