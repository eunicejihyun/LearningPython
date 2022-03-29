from tkinter import *
import tkinter.messagebox as mb
import pyperclip as pc
import pandas
import random
import json

# TODO: CONSTANTS ______________________________________________________________________________________________________
BACKGROUND_COLOR = "#B1DDC6"
PADDING = 20
CSV_FILE = "chinese_characters.csv"
JSON_FILE = "chinese_study.json"
LANG_FONT = ("Georgia", 25, "italic")
WORD_FONT = ("Helvetica", 70, "bold")
DEF_FONT = ("Helvetica", 50, "bold")
PRO_FONT = ("Helvetica", 20, "italic")
MISC_FONT = ("Helvetica", 10, "bold")

language = "Language"
word = "word"
side = "front"
entry = []

# TODO: IMPORT WORDS ___________________________________________________________________________________________________

try:
    with open(JSON_FILE, mode="r") as file:
        data_dict = json.load(file)

except FileNotFoundError:
    data = pandas.read_csv(CSV_FILE)
    data_dict = {row.character: {"def": row.definition, "pro": row.pronounciation, "incorrect": 0,
                                 "correct": 0, "lifetime_score": [0, 0]} for (index, row) in data.iterrows()}


# TODO: SAVE PROGRESS & CLOSE ___________________________________________________________________________________________________

def save_and_show_report():
    report = ""

    for word in data_dict:
        if data_dict[word]["incorrect"] > 0:
            report += f"{word} - {data_dict[word]['def']}\n"
        data_dict[word]["lifetime_score"][0] += data_dict[word]["correct"]
        data_dict[word]["lifetime_score"][1] += data_dict[word]["correct"] + data_dict[word]["incorrect"]
        data_dict[word]["incorrect"] = 0
        data_dict[word]["correct"] = 0

    with open(JSON_FILE, mode="w") as file:
        json.dump(data_dict, file, indent=4)

    mb.showinfo(title="Session Report", message="These are the characters you should study:\n\n"+report)


def full_report():
    report = ""
    for word in data_dict:
        data_dict[word]["lifetime_score"][0] += data_dict[word]["correct"]
        data_dict[word]["lifetime_score"][1] += data_dict[word]["incorrect"]

        if data_dict[word]["lifetime_score"][0] + data_dict[word]["lifetime_score"][1] > 0:
            report += f"{word} {data_dict[word]['def']} | {data_dict[word]['lifetime_score'][0]}/{data_dict[word]['lifetime_score'][1]}\n"

    if len(report)>1:
        pc.copy(report)
        mb.showinfo(title="Lifetime Report", message="Your report has been copied to the clipboard.\n\n" + report)
    else:
        mb.showinfo(title="Lifetime Report", message="No records available. Study more!")


def clear_history():
    for word in data_dict:
        data_dict[word]["lifetime_score"][0] = 0
        data_dict[word]["lifetime_score"][1] = 0
        data_dict[word]["incorrect"] = 0
        data_dict[word]["correct"] = 0


# TODO: DISPLAY WORD ___________________________________________________________________________________________________

def next_word():
    global entry
    entry = random.choice(list(data_dict.items()))
    show_front()


def flip(*arg):
    if side == "front":
        show_back()
    else:
        show_front()


def show_front():
    global side
    side = "front"
    character = entry[0]

    canvas.itemconfig(flashcard, image=CARD_FRONT_IMG)

    canvas.itemconfig(language_text, text="Chinese")
    canvas.itemconfig(word_text, text=character, font=WORD_FONT)
    canvas.itemconfig(pron_text, text="")


def show_back():
    global side
    side = "back"
    definition = entry[1]["def"]
    pronunciation = entry[1]["pro"]
    # displayed = entry[1]["displayed"]
    # correct = entry[1]["displayed"]

    canvas.itemconfig(flashcard, image=CARD_BACK_IMG)
    canvas.itemconfig(language_text, text="English")
    canvas.itemconfig(word_text, text=definition, font=DEF_FONT)
    canvas.itemconfig(pron_text, text=pronunciation)


# TODO: TRACK CORRECT/INCORRECT ________________________________________________________________________________________

def correct():
    character = entry[0]
    data_dict[character]["correct"] += 1
    next_word()


def incorrect():
    character = entry[0]
    data_dict[character]["incorrect"] += 1
    next_word()


# TODO: CREATE WINDOW __________________________________________________________________________________________________
window = Tk()
window.title("Study Mandarin with EJ!")
window.config(padx=PADDING, pady=PADDING, bg=BACKGROUND_COLOR)

# TODO: IMAGES _________________________________________________________________________________________________________
CARD_BACK_IMG = PhotoImage(file="images/card_back.png")
CARD_FRONT_IMG = PhotoImage(file="images/card_front.png")
RIGHT_IMG = PhotoImage(file="images/right.png")
WRONG_IMG = PhotoImage(file="images/wrong.png")

# TODO: UI _____________________________________________________________________________________________________________
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flashcard = canvas.create_image(400, 263, image=CARD_FRONT_IMG)
canvas.tag_bind(flashcard, '<ButtonPress-1>', flip)
canvas.grid(row=1, column=0, columnspan=3)
language_text = canvas.create_text(400, 150, text="language", fill="black", font=LANG_FONT)
word_text = canvas.create_text(400, 263, text="word", fill="black", font=WORD_FONT)
pron_text = canvas.create_text(400, 380, text="pronounciation", font=PRO_FONT)

wrong = Button(image=WRONG_IMG, highlightthickness=0, border=0, command=incorrect)
wrong.grid(row=2, column=0)

right = Button(image=RIGHT_IMG, highlightthickness=0, border=0, command=correct)
right.grid(row=2, column=2)

report = Button(text="VIEW LIFETIME REPORT", highlightthickness=0, border=0, bg=BACKGROUND_COLOR, font=MISC_FONT,
                command=full_report)
report.grid(row=0, column=0)

clear = Button(text="CLEAR HISTORY", highlightthickness=0, border=0, bg=BACKGROUND_COLOR, font=MISC_FONT,
               command=clear_history)
clear.grid(row=0, column=1)

save_close = Button(text="SAVE PROGRESS", highlightthickness=0, border=0, bg=BACKGROUND_COLOR, font=MISC_FONT,
                    command=save_and_show_report)
save_close.grid(row=0, column=2)

# TODO: STUDY! _________________________________________________________________________________________________________

next_word()

window.mainloop()
