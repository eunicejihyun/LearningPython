##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


import datetime as dt
import pandas as p
import smtplib as s
import random as r

FROM_GMAIL = "from_email"
PASSWORD = "from_pass"
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

now = dt.datetime.now()
day = now.day
month = now.month

data = p.read_csv("birthdays.csv")
birthdays = {row.first_name: {"email": row.email, "year": row.year, "month": row.month, "day": row.day} for (index, row)
             in
             data.iterrows()}

for person in birthdays:
    if birthdays[person]["month"] == month and birthdays[person]["day"] == day:
        with open("letter_templates/" + r.choice(LETTERS), mode="r") as file:
            template = file.read()
        note = template.replace("[NAME]", person)

        with s.SMTP("smtp.gmail.com") as connection:
            # This line makes the connection secure
            connection.starttls()
            connection.login(user=FROM_GMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=FROM_GMAIL,
                to_addrs=birthdays[person]["email"],
                msg=f"Subject:Happy Birthday!\n\n{note}"
            )

# ######################################################################################################################
# Intro to smtplib and datetime
# PROJECT: Monday Motivation emails


# import smtplib as s
# import datetime as d
# import random as r
#
# FROM_GMAIL = "from_email"
# PASSWORD = "from_pass"
# TO_EMAIL = "to_email"
#
#
# now = d.datetime.now()
# dow = now.weekday()
#
# if dow == 0:
#     with open("quotes.txt", mode="r") as file:
#         quotes = file.readlines()
#
#     random_quote = r.choice(quotes)
#     print(random_quote)
#
#     with s.SMTP("smtp.gmail.com") as connection:
#         # This line makes the connection secure
#         connection.starttls()
#         connection.login(user=FROM_GMAIL, password=PASSWORD)
#         connection.sendmail(from_addr=FROM_GMAIL,
#                             to_addrs=TO_EMAIL,
#                             msg=f"Subject:Monday Motivation\n\n{random_quote}"
#                             )
# else:
#     print("Not Monday yet!")
