import random
import hangman_art
import hangman_words

print(hangman_art.logo)

stages = hangman_art.stages
word = random.choice(hangman_words.word_list)
lives = 6

guessed_letters = []

display = []
for letter in word:
    display += "_"

def redraw():
    print(stages[lives])
    print(f"{' '.join(display)}\n")

redraw()

while "_" in display and lives > 0:

    guess = input("Guess a letter.\n    ").lower()

    if guess not in guessed_letters:
        guessed_letters += guess

        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print('\n' * 150)

        if guess not in word:
            lives -= 1
            print(f"Nice try, but the letter {guess} is not in the word.")
        else:
            print("Great job!")

        redraw()

    else:
        print(f"You've already guessed the letter, {guess}.")


if "_" not in display:
    print("Great job! You win!!")
else:
    print(f"The word was {word}. Better luck next time.")
