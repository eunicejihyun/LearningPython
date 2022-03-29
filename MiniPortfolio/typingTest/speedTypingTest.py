from tkinter import *
import json
import random
from time import time
from bs4 import BeautifulSoup
import requests
import json

WORDS_URL = "https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt"
WORD_FILE = '500words.json'
TOTAL_WORD_COUNT = 30
BLUE = "#91CAFF"
GREEN = "#019267"
RED = "#FD5D5D"
BLACK = "#3A3845"
WORD_FONT = ("Consolas", 12)

response = requests.get(WORDS_URL)
html = response.text
soup = BeautifulSoup(html, "html.parser")
words = soup.find_all(name="td", class_="blob-code")


class TestUI:

    def __init__(self):
        self.all_words = {word.getText(): "" for word in words}

        self.display_dict = {}
        self.word_count = 0
        self.start_time = ""
        self.typing_entry = ""

        self.word_list = list(self.all_words)
        self.test_words = []

        # setup tkinter window
        self.window = Tk()
        self.window.title("Speed Typing Test")
        self.window.config(padx=5, pady=5, bg=BLUE)

        # instructions & result display
        instructions = "Welcome!\nClick START to\nbegin the test."
        self.helper_display = Label(text=instructions, bg=BLUE, font=WORD_FONT, wraplength=200)
        self.helper_display.grid(row=6, column=0, columnspan=3)

        # app image
        self.canvas = Canvas(width=200, height=160, bg=BLUE, highlightthickness=0)
        self.photo = PhotoImage(file='typing.png')
        self.canvas.create_image(100, 80, image=self.photo)
        self.canvas.grid(row=5, column=3, columnspan=3, rowspan=3)

        # start/new test button
        self.start_btn = Button(text="START", bg=BLACK, fg="white", font=WORD_FONT, width=20, borderwidth=0,
                                command=self.start_new_test)
        self.start_btn.grid(row=7, column=0, columnspan=3)

        self.window.bind('<space>', self.submit_word)

        self.window.mainloop()

    def start_new_test(self):
        # reset
        self.word_count = 0
        self.all_words = {key: "" for (key, value) in self.all_words.items()}
        random.shuffle(self.word_list)
        self.test_words = self.word_list[:TOTAL_WORD_COUNT]

        # clear displayed words from previous test
        for x in self.display_dict:
            self.display_dict[x].grid_remove()
        self.display_dict = {}

        self.setup()
        self.start_time = time()
        self.helper_display.config(text="Press space after each word.")
        self.start_btn.grid_remove()

    def setup(self):
        # typing entry
        self.typing_entry = Entry(width=20, justify=CENTER, font=WORD_FONT)
        self.typing_entry.grid(row=5, column=0, columnspan=3)
        self.typing_entry.focus_force()

        # display words
        for x in range(TOTAL_WORD_COUNT):
            displayed_word = Label(text=self.test_words[x], bg=BLUE, font=WORD_FONT)
            self.display_dict[self.test_words[x]] = displayed_word
            displayed_word.grid(row=x // 6, column=x % 6, sticky="w", padx=(10, 10))

    def submit_word(self, event):
        if self.word_count < TOTAL_WORD_COUNT:

            self.all_words[self.test_words[self.word_count]] = self.typing_entry.get().strip()
            self.typing_entry.delete(0, 'end')

            for x in range(TOTAL_WORD_COUNT):
                test_word = self.test_words[x]
                if test_word == self.all_words[test_word]:
                    self.display_dict[test_word].config(fg=GREEN)
                elif self.all_words[test_word] != "":
                    self.display_dict[test_word].config(fg=RED, text=self.all_words[self.test_words[x]])

            self.word_count += 1

        # code for when the test is complete
        if self.word_count == 30:
            end_time = time()
            correct_words = 0
            for word in self.all_words:
                if word == self.all_words[word]:
                    correct_words += 1
            wpm = correct_words * 60 / (end_time - self.start_time)
            self.helper_display.config(text=f"WPM: {round(wpm, 2)}")
            self.start_btn.grid()
            self.start_btn.config(text='START NEW TEST')


TestUI()
