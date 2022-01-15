# Coding game given instructions.

print("Welcome to Treasure Island. \nYour mission is to find the treasure.")

while True:
    try:
        choice1 = input("1) You've approached a fork in the road. Which way will you go? (L or R)\n     ").upper()
        assert choice1 == "L" or choice1 == "R", "Please type L or R.\n"
    except AssertionError as e:
        print(e)
    else:
        break

if choice1 == "R":
    print("You fell into a hole. Game over.")
    exit()
else:
    while True:
        try:
            choice2 = input("2) You've arrived at a lake. Will you swim or wait?\n     ").upper()
            assert choice2 == "SWIM" or choice2 == "WAIT", "Please type swim or wait.\n"
        except AssertionError as e:
            print(e)
        else:
            break

    if choice2 == "SWIM":
        print("You were eaten by piranha. Game over.")
        exit()
    else:
        choice3 = input("3) You've arrived at a hall of doors. Which color door will you take?\n     ").upper()
        if choice3 == "RED":
            print("You were burned by fire. Game over.")
        elif choice3 == "BLUE":
            print("You were eaten by beasts. Game over.")
        elif choice3 == "YELLOW":
            print("You win!!! Great job.")
        else:
            print("Game over.")
