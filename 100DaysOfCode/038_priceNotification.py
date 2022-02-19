import json
import requests
from bs4 import BeautifulSoup
import lxml
import smtplib as s
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

PRODUCT_LIST = "products.json"
FROM_GMAIL = "your@gmail.com"
PASSWORD = "your_password"
EMAIL_LIST = ["your_list_of_emails"]

# HTTP Header from http://myhttpheader.com/
UserAgent = "your_header"
AcceptLanguage = "en-US,en;q=0.9"
headers = {
    "User-Agent": UserAgent,
    "Accept-Language": AcceptLanguage
}

try:
    with open(PRODUCT_LIST, mode="r") as file:
        products = json.load(file)
except FileNotFoundError:
    products = {}

print(products)

product_url = ""
highest_price = 0

while True:
    response = input("\nWould you like to add a product to your search list? (y/n) ").lower()
    if "y" not in response:
        break

    # Ensuring that the product URL contains .com
    while True:
        try:
            product_url = input("Product URL: ")
            assert "amazon.com" in product_url, "Ensure your URL contains 'amazon.com'"
        except AssertionError as e:
            print(e)
        else:
            break

    # Ensuring the highest price is a number
    while True:
        try:
            highest_price = float(input("What's the most you're willing to pay for it? "))
        except ValueError:
            print("Please type a number")
        else:
            break

    products.update({product_url: {"max_price": highest_price}})

for product in products:
    response = requests.get(product, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, "lxml")
    latest_price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
    product_name = soup.find(id="productTitle").getText()
    products[product]["latest_price"] = latest_price
    products[product]["name"] = product_name

with open(PRODUCT_LIST, mode="w") as file:
    json.dump(products, file, indent=4)


links = ""
html_code = ""
for product in products:
    if products[product]["max_price"] >= products[product]["latest_price"]:
        links += f"{products[product]['name']}: {product}\n\n"
        html_code += f"<p><a href=\"product\">{products[product]['name']}</a> : {products[product]['latest_price']}</p><br>\n"

# EMAIL PORTION

message = MIMEMultipart("alternative")
message['Subject'] = "Price Drop Alert!"
message['From'] = FROM_GMAIL
message['To'] = ", ".join(EMAIL_LIST)

text = f"""\
The following products are below your target price.\n\n
{links}
"""

html = f"""\
<html>
  <head></head>
  <body style="font-family: Courier New">
    {html_code}
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
