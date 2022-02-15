# API Doc: https://www.thecocktaildb.com/api.php?ref=apilist.fun


import requests
import json
from datetime import datetime
import smtplib as s
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

DRINK_ENDPOINT = "https://www.thecocktaildb.com/api/json/v1/1/random.php"
DRINK_HISTORY = "drink_history.json"

FROM_GMAIL = "your@gmail.com"
PASSWORD = "yourpassword"
TO_EMAIL = ["to@gmail.com", "to@gmail.com"]

# Get today's date _____________________________________________________________________________________________________
today = datetime.today().date().strftime("%Y%m%d")

# Pull in Drink History file ___________________________________________________________________________________________
try:
    with open(DRINK_HISTORY, mode='r') as file:
        served_drinks = json.load(file)
except FileNotFoundError:
    served_drinks = {}

# Obtain Random Drink data _____________________________________________________________________________________________
drink_type = ""
drink_id = ""
attempts = 0

# Ensuring drink is alcoholic and not shared in the past _______________________________________________________________
while drink_type != "Alcoholic" and drink_id not in served_drinks and attempts < 25:
    response = requests.get(DRINK_ENDPOINT)
    response.raise_for_status()
    data = response.json()["drinks"][0]
    drink_type = data["strAlcoholic"]
    drink_id = data["idDrink"]
    attempts += 1
    times = 1

# If Drink Library exhausted or requests exceed 50 attempts, get oldest drink __________________________________________
if attempts >= 25:
    oldest_date = min([drink_info["date"] for drink_info in served_drinks.values()])
    drink_id = [drink_id for drink_id in served_drinks if served_drinks[drink_id]["date"] == oldest_date][0]
    print(drink_id)

    DRINK_ENDPOINT = f"https://www.thecocktaildb.com/api/json/v1/1/lookup.php?i={drink_id}"
    response = requests.get(DRINK_ENDPOINT)
    response.raise_for_status()
    data = response.json()["drinks"][0]
    times = served_drinks[drink_id]["times"] + 1

name = data["strDrink"]
category = data["strCategory"]
instructions = data["strInstructions"]
glass = data["strGlass"]

# Create a dictionary of ingredients and measurements __________________________________________________________________
ingredients = [value.strip() for key, value in data.items()
               if "strIngredient" in key and value is not None and value != '']
measurements = [value.strip() for key, value in data.items()
                if "strMeasure" in key and value is not None and value != '']

# recipe = dict(zip(ingredients, measurements))


spacing = max([len(x) for x in ingredients]) + 4

ingredients_msg = ""

for x in range(len(ingredients)):
    try:
        ingredients_msg += f"{ingredients[x]}" + "." * (spacing - len(ingredients[x])) + f"{measurements[x]}<br>"
    except IndexError:
        ingredients_msg += f"{ingredients[x]}<br>"

# Update Drink History File ____________________________________________________________________________________________
served_drinks.update({drink_id: {"name": name,
                                 "date": today,
                                 "times": times}})

with open(DRINK_HISTORY, mode="w") as file:
    json.dump(served_drinks, file, indent=4)

# Send Email ___________________________________________________________________________________________________________
drink_search = f"https://www.google.com/search?q={name.replace(' ', '+')}+drink"


message = MIMEMultipart("alternative")
message['Subject'] = "Cheers! Friday's here~"
message['From'] = FROM_GMAIL
message['To'] = ", ".join(EMAIL_LIST)

text = f"""\
{name.upper()}\n\n{ingredients_msg}\n{instructions}\n\n{drink_search}\n\n
Disclaimer: This email was generated using CocktailDB API. The sender has no control over the content.
"""

html = f"""\
<html>
  <head></head>
  <body style="font-family: Courier New">
    <h2><a href={drink_search}>{name.upper()}</a></h2>
    <b>Ingredients</b>
    <p>{ingredients_msg}</p>
    <b>Directions</b>
    <p>{instructions}</p>
    <img src="https://t4.ftcdn.net/jpg/04/37/05/07/360_F_437050739_2bbycIKGlxdY3vS1mq0YEYTrDIkyWXsO.jpg"></img>
    <p style="font-size: 70%">Disclaimer: The content of this email was auto-generated using the free CocktailDB API. 
{drink_id}</p>
  </body>
</html>
"""

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

message.attach(part1)
message.attach(part2)

with s.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=FROM_GMAIL, password=PASSWORD)
    connection.send_message(msg=message,
                            from_addr=FROM_GMAIL,
                            to_addrs=EMAIL_LIST)
