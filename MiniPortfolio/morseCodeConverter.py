# Morse Code Dictionary from here: https://gist.github.com/mohayonao/094c71af14fe4791c5dd
morse_code = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}

end_of_sentence = ['.', '?', '!']

while True:
    text_to_convert = input("\nType the text that you'd like to convert into morse code: ").lower()
    output = ""
    ignored = []
    for char in text_to_convert:
        if char in morse_code:
            output += morse_code[char] + " "
            if char in end_of_sentence:
                output += "\n"
        elif char == ' ' and prev_char not in end_of_sentence:
            output += "   "
        elif char != ' ' and char not in ignored:
            ignored.append(char)
        prev_char = char

    print(output)

    if len(ignored) > 0:
        unrecognized_characters = ""
        for character in ignored:
            unrecognized_characters += character + " "
        print("The following characters were not recognized and were not converted: " + unrecognized_characters)

    response = input("\nWould you like to convert another piece of text? Type y/n\n").lower()
    if response != 'y':
        input("Goodbye! Press enter to close.")
        break
