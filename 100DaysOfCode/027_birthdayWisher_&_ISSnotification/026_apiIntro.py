# ######################################################################################################################
# # ISS Station overhead!

import requests as r
import datetime as d
import smtplib as s

# CONSTANTS
MY_LAT = 100
MY_LONG = 100
FROM_GMAIL = "from_email"
PASSWORD = "from_pass"
TO_EMAIL = "to_email"
API_PARAMS = {
    "lat": MY_LAT,
    "long": MY_LONG,
    "formatted": 0
}


def is_overhead():
    response = r.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()["iss_position"]

    longitude = float(data["longitude"])
    latitude = float(data["latitude"])
    iss_position = (latitude, longitude)
    print(iss_position)

    return abs(latitude - MY_LAT) < 5 and abs(longitude - MY_LONG)


def is_night():
    response = r.get("https://api.sunrise-sunset.org/json", params=API_PARAMS)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = int(data["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["sunset"].split("T")[1].split(":")[0])

    now = d.datetime.now()
    hour = now.hour
    print(hour)

    return now.hour < sunrise or now.hour > sunset


if is_night() and is_overhead():
    with s.SMTP("smtp.gmail.com") as connection:
        # This line makes the connection secure
        connection.starttls()
        connection.login(user=FROM_GMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=FROM_GMAIL,
            to_addrs=TO_EMAIL,
            msg=f"Subject:Look up!\n\nThe ISS is overhead!"
        )

# ######################################################################################################################
# # Kanye Quotes API
#
# from tkinter import *
# import requests as r
#
#
# def get_quote():
#     response = r.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     quote = response.json()["quote"]
#     canvas.itemconfig(quote_text, text=quote)
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Click on Kanye for a new quote!", width=250, font=("Arial", 20, "bold"),
#                                 fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, border=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()
