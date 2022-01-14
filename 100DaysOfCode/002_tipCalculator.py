
print("Welcome to the tip calculator.\n")

while True:
    try:
        total = float(input("What was the total bill?\n   "))
    except:
        print("  --> Please input a number.\n")
    else:
        break

while True:
    try:
        percentage_tip = float(input("What % tip would you like to give?\n   "))
        assert percentage_tip > 1, "  --> Please input a number greater than 1.\n"
        tip = percentage_tip * 0.01
    except ValueError:
        print("  --> Please input a number.\n")
    except AssertionError as message:
        print(message)
    else:
        break

while True:
    try:
        people = int(input("How many people are splitting the bill?\n   "))
    except ValueError:
        print("  --> Please input a number.\n")
    except ZeroDivisionError:
        print("  --> The number of people must be at least 1.\n")
    else:
        break

individual_total = round((total + total * tip) / people, 2)

print(f"\n----------\nEach person should pay: ${individual_total}")

