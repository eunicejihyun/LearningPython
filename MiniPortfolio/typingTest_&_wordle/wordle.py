import json
from tkinter import *
from random import choice

BLACK = "#121213"
GRAY = "#3A3A3C"
YELLOW = "#B59F3B"
GREEN = "#538D4E"
LETTER_FONT = ("Consolas", 25)
WORD_FILE = '500words.json'

with open(WORD_FILE, mode='r') as file:
    all_words = list(json.load(file))


class UI:
    def __init__(self):
        self.display_dict = {}
        self.guessed_words = []
        self.guess = 0
        self.correct_word = ""
        self.correct = False

        self.window = Tk()
        self.window.title("Wordle")
        self.window.config(padx=25, pady=25, bg=BLACK)

        self.typing_entry = Entry(width=21, justify=CENTER, font=LETTER_FONT)
        self.typing_entry.grid(row=5, column=0, columnspan=5, pady=(10, 10))
        self.typing_entry.focus_force()

        self.note = Label(text="",
                          width=50, justify=CENTER,
                          bg=BLACK, fg='white')
        self.note.grid(row=6, column=0, columnspan=5, pady=(10, 10))

        self.restart_btn = Button(text="PLAY AGAIN", bg=GREEN, fg="white", font=LETTER_FONT, width=21, borderwidth=0,
                                  command=self.new_game)
        self.restart_btn.grid(row=5, column=0, columnspan=5, pady=(5, 5))

        self.new_game()

        self.window.bind('<Return>', self.submit_word)

        print(self.correct_word)

        self.window.mainloop()

    def new_game(self):
        # reset
        self.note.config(text="")
        self.restart_btn.grid_remove()
        self.guessed_words = []
        self.typing_entry.delete(0, 'end')
        self.guess = 0
        self.correct_word = choice(all_words).upper()
        for i in self.display_dict:
            self.display_dict[i].grid_remove()
        self.display_dict = {}
        self.typing_entry.grid()
        self.typing_entry.focus_force()
        self.correct=False

        for x in range(25):
            guess = x // 5
            letter = x % 5
            letter_box = Label(text="   ", bg=GRAY, fg='white', font=LETTER_FONT)
            self.display_dict[f'g{guess}l{letter}'] = letter_box
            letter_box.grid(row=guess, column=letter, padx=(10, 10), pady=(10, 10))

    def submit_word(self, event):
        submitted_word = self.typing_entry.get().strip().upper()
        if len(submitted_word) != 5:
            self.note.config(text="Please guess a 5 letter word.")
        elif submitted_word.lower() not in all_words:
            self.note.config(text="That is an unrecognized word.")
        elif submitted_word in self.guessed_words:
            self.note.config(text="You already guessed that word.")
        elif submitted_word == self.correct_word:
            self.correct = True
            for i in range(5):
                self.display_dict[f'g{self.guess}l{i}'].config(text=f" {submitted_word[i]} ", bg=GREEN)
        else:
            for i in range(5):
                if self.correct_word[i] == submitted_word[i]:
                    self.display_dict[f'g{self.guess}l{i}'].config(text=f" {submitted_word[i]} ", bg=GREEN)
                elif submitted_word[i] in self.correct_word:
                    self.display_dict[f'g{self.guess}l{i}'].config(text=f" {submitted_word[i]} ", bg=YELLOW)
                else:
                    self.display_dict[f'g{self.guess}l{i}'].config(text=f" {submitted_word[i]} ")
            self.guess += 1
            self.note.config(text="")

        self.guessed_words.append(submitted_word)
        self.typing_entry.delete(0, 'end')

        if self.guess == 5 and not self.correct:
            self.typing_entry.grid_remove()
            self.restart_btn.grid()
            self.note.config(text=f"Better luck next time! The word was {self.correct_word}.")
        elif self.correct:
            self.typing_entry.grid_remove()
            self.restart_btn.grid()
            self.note.config(text="Congrats! You got it!")


UI()
