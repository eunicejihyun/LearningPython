from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def cipher(plain_text, shift_number, instruction):
    new_string = ''
    shift_number %= len(alphabet)
    new_letter_index = 0

    if instruction == 'decode':
        shift_number *= -1

    for letter in plain_text:
        if letter in alphabet:
            new_letter_index = alphabet.index(letter) + shift_number
            if alphabet.index(letter) + shift_number >= len(alphabet):
                new_letter_index -= len(alphabet)
            new_string += alphabet[new_letter_index]
        else:
            new_string += letter

    print(f"The {instruction}d text is: {new_string}")

print(logo)

computer_on = True

while computer_on:

    while True:
        try:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n    ").lower()
            assert direction == 'encode' or direction == 'decode', "ERROR: Please type 'encode' or 'decode'.\n"
        except AssertionError as e:
            print(e)
        else:
            break

    text = input("Type your message.\n    ").lower()
    while True:
        try:
            shift = int(input("Type the shift number:\n    "))
        except ValueError:
            print("ERROR: Please type an integer for the shift number.")
            print(f"\n\n\nInstruction: {direction}\nMessage: {text}")
        else:
            break

    cipher(text, shift, direction)

    another_time = input("Do you have another text to encode/decode? Type 'y' or 'n'.\n    ").lower()

    if another_time == 'y':
        print("\n")
    else:
        computer_on = False
        print("Adios!")