import requests

TOKEN_URL = "https://opentdb.com/api_token.php"
TRIVIA_URL = "https://opentdb.com/api.php"


def get_token() -> str:
    payload = {"command": "request"}
    response = requests.get(url=TOKEN_URL, params=payload)
    response.raise_for_status()
    token = response.json()["token"]
    return token


def get_data(amount=10, **kwargs) -> list:
    payload = kwargs
    payload["amount"] = amount
    response = requests.get(url=TRIVIA_URL, params=payload)
    response.raise_for_status()
    data = response.json()["results"]
    return data


