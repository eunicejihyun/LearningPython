from tkinter import *
import tkinter.messagebox as mb
from random import randint, shuffle, choice
import pyperclip as pc
import json

BLUE = "#313552"
GREEN = "#2EB086"
WHITE = "#F9F9F9"
font = ("Courier", 10)
EMAIL = "your@email.com"
DB = "creds.json"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pw():
    password.delete(0, END)

    pw_letters = [choice(letters) for _ in range(randint(7, 10))]
    pw_numbers = [choice(numbers) for _ in range(randint(1, 2))]
    pw_symbols = [choice(symbols) for _ in range(randint(1, 2))]

    pw_characters = pw_letters + pw_numbers + pw_symbols
    shuffle(pw_characters)

    pw = "".join(pw_characters)
    password.insert(0, pw)
    pc.copy(pw)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_info():
    web = website.get().upper()
    un = username.get()
    pw = password.get()
    new_data = {
        web: {
            "username": un,
            "password": pw,
        }}

    if pw == "" or un == "" or web=="":
        mb.showerror(title="Pay attention!", message="Please complete all fields before attempting to save.")

    else:
        try:
            with open(DB, mode="r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(DB, mode="w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open(DB, mode="w") as file:
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


# ---------------------------- Search Password ------------------------------- #

def search():
    web = website.get().upper()

    try:

        with open(DB, mode="r") as file:
            data = json.load(file)

        un = data[web]["username"]
        pw = data[web]["password"]
    except FileNotFoundError:
        mb.showerror(title="Error", message="No credentials have been saved yet.")
    except KeyError:
        mb.showerror(title="Error", message=f"No credentials have been found for {web}.")
    else:
        mb.showinfo(title=f"{web} Credentials", message=f"Username: {un}\n Password: {pw}")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=WHITE)

# Place logo on the screen
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=0, columnspan=3)

# Text Labels
website_text = Label(text="Website: ", bg=WHITE, font=font)
website_text.grid(row=1, column=0, sticky='e')

username_text = Label(text="Username: ", bg=WHITE, font=font)
username_text.grid(row=2, column=0, sticky='e')

password_text = Label(text="Password: ", bg=WHITE, font=font)
password_text.grid(row=3, column=0, sticky='e')

# Input Fields
website = Entry(width=23)
website.grid(row=1, column=1, sticky='w')
username = Entry(width=35)
username.grid(row=2, column=1, columnspan=2, sticky='w')
username.insert(0, EMAIL)
password = Entry(width=23)
password.grid(row=3, column=1, sticky='w')

# Buttons
search = Button(text="search", font=("Helvetica", 8), bg=GREEN, width=10, borderwidth=0, command=search)
search.grid(row=1, column=2)
generate = Button(text="generate", font=("Helvetica", 8), bg=GREEN, width=10, borderwidth=0, command=generate_pw)
generate.grid(row=3, column=2, sticky='e')
add = Button(text="add", font=("Helvetica", 8), bg=BLUE, fg=WHITE, width=35, borderwidth=0, command=save_info)
add.grid(row=4, column=1, columnspan=2, sticky='w')

window.mainloop()
