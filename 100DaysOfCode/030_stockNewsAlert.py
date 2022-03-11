# This program sends a text to the receipient if the stock they chose changed by at least 5% between the last two closing times.

import requests as r
from datetime import datetime, timedelta
from twilio.rest import Client

STOCK = "SNAP"
COMPANY_NAME = "snapchat"

# Alpha Vantage Stock API
AV_API_KEY = "YOUR API KEY"
AV_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": AV_API_KEY
}

# News API
NEWS_API_KEY = "YOUR API KEY"
NEWS_PARAMS = {
    "q": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

# Twilio API
account_sid = "YOUR ACCOUNT INFO"
auth_token = "YOUR TOKEN"
YOUR_NUMBER = 'YOUR NUMBER'
TRIAL_NUMBER = 'YOUR TRIAL NUMBER'
client = Client(account_sid, auth_token)

# Get the date for yesterday and two days ago.
yesterday = datetime.now().date() - timedelta(1)
two_days_ago = datetime.now().date() - timedelta(2)

response = r.get("https://www.alphavantage.co/query", params=AV_PARAMS)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]

yesterday_close = float(stock_data[str(yesterday)]["4. close"])
two_days_ago_close = float(stock_data[str(two_days_ago)]["4. close"])

print(yesterday_close, two_days_ago_close)

pct_change = (yesterday_close - two_days_ago_close) / yesterday_close

if pct_change >= 0.05 or pct_change < -0.05:

    # Get News
    response = r.get("https://newsapi.org/v2/everything", params=NEWS_PARAMS)
    response.raise_for_status()
    news_data = response.json()["articles"][:3]

    if pct_change > 0:
        msg = f"{STOCK} 🔺"
    else:
        msg = f"{STOCK} 🔻"

    msg += "{:.2%}".format(pct_change) + "\n"

    formatted_articles = [f"Headline: {article['title']} \nBrief: {article['description']}" for article in
                          news_data]
    for article in formatted_articles:
        message = client.messages.create(
            body=msg + article,
            from_=TRIAL_NUMBER,
            to=YOUR_NUMBER
        )
        print(message.status)
