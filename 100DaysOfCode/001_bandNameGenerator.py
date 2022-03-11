import random

print("Welcome to the Band Name Generator!\n")

city = input("Which city are you from?\n    ")
pet = input("What's your pet's name?\n    ")
color = input("What's your favorite color?\n    ")
number = str(input("What's your favorite number?\n    "))
food = input("What's your favorite food?\n    ")
season = input("What's your favorite season?\n    ")
animal = input("What's your favorite animal?\n    ")

info = [city, pet, color, number, food, season, animal]

bandNames = []

# Print multiple options for band names
for i in range(5):
    x = random.randrange(len(info))
    y = random.randrange(len(info))
    # Ensure that x != y
    while y == x:
        y = random.randrange(6)
        print(y)
    bandNames.append(info[x]+" "+info[y])

print("\nPotential Band Names:")
for i in bandNames:
    print(" " + i)

input("\nPress [ENTER] to close the program.")
