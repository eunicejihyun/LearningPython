import requests as r
from twilio.rest import Client

account_sid = "TWILIO ID"
auth_token = "TWILIO KEY"
YOUR_NUMBER = '+1YOURNUMBER'
TRIAL_NUMBER = '+1TRIAL NUMBER'

API_PARAMS = {
    "appid": "OPEN WEATHER MAP API KEY",
    "lat": 45.420420,
    "lon": -75.692430,
    "exclude": "current,minutely,daily,alerts"
}


def send_message():
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today! Remember your umbrella~",
        from_=TRIAL_NUMBER,
        to=YOUR_NUMBER
    )
    print(message.status)


response = r.get(url=f"https://api.openweathermap.org/data/2.5/onecall", params=API_PARAMS)
response.raise_for_status()

data = response.json()["hourly"]

for hour in range(12):
    code = data[hour]["weather"][0]["id"]
    if code < 700:
        send_message()

        print("Bring an umbrella.")
        break
