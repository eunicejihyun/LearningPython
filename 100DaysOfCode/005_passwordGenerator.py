import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n   "))
nr_symbols = int(input(f"How many symbols would you like?\n   "))
nr_numbers = int(input(f"How many numbers would you like?\n   "))

# Eazy Level - Order of characters not randomised:

# password = ''
#
# for i in range(nr_letters):
#     password += random.choice(letters)
#
# for i in range(nr_symbols):
#     password += random.choice(symbols)
#
# for i in range(nr_numbers):
#     password += random.choice(numbers)
#
# print(password)

# Hard Level - Order of characters randomised:

password = ''

options = [letters, symbols, numbers]
nrs = [nr_letters, nr_symbols, nr_numbers]

while len(password) < nr_letters + nr_symbols + nr_numbers:
    a = random.randint(0, 2)
    if nrs[a] > 0:
        password += random.choice(options[a])
        nrs[a] -= 1

print(f"Suggested password: {password}")

input("\nPress [ENTER] to close the program.")
