import requests
from datetime import datetime as dt

APP_ID_NUTRITIONIX = "YOUR APP ID"
KEY_NUTRITIONIX = "YOUR KEY"
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "your sheety endpoint"
GENDER = 'your gender'
WEIGHT = 'your weight'
HEIGHT = 'your height'
AGE = 'your age'
QUERY = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID_NUTRITIONIX,
    "x-app-key": KEY_NUTRITIONIX,
    "Content-Type": "application/json"
}

params = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
data = response.json()["exercises"]
print(data)

DATE = dt.now().date().strftime("%m/%d/%Y")
TIME = dt.now().time().strftime("%H:%M")

for row in data:
    update = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": row["name"].title(),
            "duration": row["duration_min"],
            "calories": row["nf_calories"],
        }
    }
    print(update)
    response = requests.post(url=SHEETY_ENDPOINT, json=update)
    print(response.text)
