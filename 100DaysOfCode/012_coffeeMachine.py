# Program Requirements
# 1. Print Report (type report to generate)
# 2. Check Resources left when something is ordered
# 3. Process coins
# 4. Check if the transaction is successful (enough coins?)
# 5. Make coffee by using up resources
# 6. Turn off machine by typing off


# TODO 0 - List options and resource requirements in a dictionary

menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            },
        "price": 1.50,
        "status": "available",
        "logo": """|      |_,
|      |_|
 \____/       """,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "price": 2.50,
        "status": "available",
        "logo": f""" /    \__,
|      | |
 \____/--'    """
    },
    "cappuccino": {
        'ingredients': {
            "water": 250,
            "coffee": 24,
            "milk":  100,
        },
        "price": 3,
        "status": "available",
        "logo": """ |     |_
 |     | )
 |_____|/     """
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}


def qa_str_input(question, options):
    """Ensure only valid options are inputted for strings"""
    while True:
        try:
            response = input(question).lower()
            assert response in options, "  ERROR: Please select a valid option.\n"
        except AssertionError as e:
            print(e)
        else:
            return response


def qa_int_input(question):
    """Ensure only valid options are inputted for integers"""
    while True:
        try:
            response = int(input(question))
        except ValueError:
            print("  ERROR: Numbers only!\n")
        else:
            return response


def calculate(n, d, q):
    """Calculate the amount of money that was inserted"""
    money = n * 0.05 + d * 0.1 + q * 0.25
    return money


def coin_insert():
    """Accept and calculate total coins inserted"""
    n = qa_int_input("      Nickel count: ")
    d = qa_int_input("        Dime count: ")
    q = qa_int_input("     Quarter count: ")
    coins = calculate(n, d, q)
    return coins


def report():
    """Print report"""
    print("="*25, "\n", " "*3, "R E P O R T")
    for ingredient in resources:
        print(" "*(10-len(ingredient)),f"{ingredient}: {resources[ingredient]}")
    print(" "*5, f"money: ${bank:.2f}")
    print("="*25, "\n")


def update_menu():
    """Updates menu to show availability"""
    available_items = []
    for item in menu:
        for ingredient in menu[item]['ingredients']:
            if menu[item]['ingredients'][ingredient] > resources[ingredient]:
                menu[item]['status'] = "unavailable"
            else:
                menu[item]['status'] = "available"
        if menu[item]['status'] == "available":
            available_items.append(item)
    return available_items


# TODO 1 - Print Available Coffee Options and prices
def display_menu():
    """Prints Menu to show available coffee options and prices"""
    print("="*40,"\n"," "*9,"EUNICE'S CAFE")
    for item in menu:
        print(f"{menu[item]['logo']} {item.upper()}","." * (15 - len(item)), f"${menu[item]['price']:.2f}")
        print(" "*20,f"({menu[item]['status']})\n")
    print("="*40,"\n")


# SETUP
bank = 0
computer_on = True
options = ['off', 'report']
while computer_on:
    available = update_menu()
    display_menu()

    if available == []:
        input("Sorry! We're out of coffee. Please visit back in a bit. Press Enter to turn off the machine.")
        break

    # TODO 2 - Ask User what they'd like to drink
    order = ""
    while order not in available:
        order = qa_str_input("What would you like to order? ", list(menu) + options)
        if order == "off":
            quit()
        elif order == "report":
            report()
            print("\n")
        elif order not in available:
            print("That option is currently unavailable. Please select another one of our delicious options!")
        else:
            break


    # TODO 3 - Ask how many coins they will input (N, D, Q)
    total = menu[order]['price']
    print(f" That will be ${total:.2f}")

    # TODO 4 - Calculate total of coin input
    money_received = coin_insert()

    while money_received < total:
        print(f"You are short ${(total - money_received):.2f}. Please insert additional coins.")
        additional_money = coin_insert()
        money_received += additional_money

    change = money_received - total
    print(f"You've input ${money_received:.2f}. Your change is ${change:.2f}")

    # TODO 5 - Give change and update bank
    bank += total

    # TODO 6 - Update Coffee Resources
    for ingredient in menu[order]['ingredients']:
        resources[ingredient] -= menu[order]['ingredients'][ingredient]




    # TODO 7 - Print Report (Resource values and Bank Amount)

    # TODO 8 - Turn off machine if user types off

    # TODO Only work if there is enough ingredients and coins

    # TODO Update status of resources

