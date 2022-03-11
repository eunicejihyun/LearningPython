import pandas as p

data = p.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_code():
    word = input("Type a word that you'd like the phonetic codes for: ").upper()
    try:
        nato_codes = [alphabet[letter] for letter in word]
    except KeyError:
        print("Letters only please!")
        generate_code()
    else:
        print(nato_codes)


generate_code()

input("\nPress [ENTER] to close the program.")
