import requests as r

QUESTION_COUNT = 10

params = {
    "amount": QUESTION_COUNT,
    "category": 9,
    "difficulty": "medium",
    "type": "boolean"
}

response = r.get(url="https://opentdb.com/api.php", params=params)
response.raise_for_status()
question_data = response.json()["results"]
