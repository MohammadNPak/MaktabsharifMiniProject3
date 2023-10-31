import requests
import json
from typing import Optional
class ApiClient:
    url = "https://api.github.com/repos/MohRezam/MaktabsharifMiniProject3/branches"
    def __init__(self,api_token:str) -> None:
        self.api_token = api_token
        self.session = requests.session()
    def connect(self) -> None:
        self.session.headers.update({'Authorization':f'Bearer {self.api_token}','accept': 'application/vnd.github+json'})
    def disconnect(self) -> None:
        self.session.close()
    def get_commit_data(self) -> dict:
        commit_data = requests.get(self.url)
        commit_data.raise_for_status()
        return commit_data.json()[0]["commit"]
class ApiClientConnection:
    def __init__(self,api_token:str) -> None:
        self.api_token = api_token
        self.api_client: Optional[ApiClient]=None
    def __enter__(self) -> ApiClient:
        self.api_client = ApiClient(self.api_token)
        self.api_client.connect()
        return self.api_client
    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        self.api_client.disconnect()

with ApiClientConnection("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") as api:
    print(api.get_commit_data())
