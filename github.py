import requests
# user="MohRezam"

# files=requests.get(f"https://api.github.com/users/{user}/repos")
# files=files.json()
# for item in files:
#     print(item['name'])

repo="MaktabsharifMiniProject3"
usrename="MohRezam"
url=f"https://api.github.com/repos/{usrename}/{repo}/commits"

repo_commit=requests.get(url)
repo_commit=repo_commit.json()

for name in repo_commit:
    print(name['commit']['committer']['name'])