import requests
import git
conter = 0
token = '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'
headers = {
    'Authorization': f'Bearer {token}'}
# respons=requests.get('https://api.github.com/users/Amirznd/repos')
# print(respons.json())
url = "https://api.github.com/repos/Amirznd/digitallab/commits"
respons_commits = requests.get(url)
jsonresponse = respons_commits.json()
print(jsonresponse[0]['commit']['author']['name'])
for i in respons_commits.json():
    if i['commit']['author']['name'] == 'Amirznd':
        conter += 1
print(conter)
