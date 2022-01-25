# menu, coffee_maker, money_machine modules were coded by London App Brewery
# and given to students to practice Object Oriented Programming.


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


coffee_items = Menu()
coffee_list = coffee_items.get_items().split('/')
coffee_list.remove("")
coffee_machine = CoffeeMaker()
bank = MoneyMachine()

while True:
    order = ""
    while order not in coffee_list:
        order = input(f"What would you like? ({coffee_items.get_items()}): ").lower()
        if order == "off":
            quit()
        elif order == "report":
            coffee_machine.report()
            bank.report()

    drink = coffee_items.find_drink(order)

    if coffee_machine.is_resource_sufficient(drink) and bank.make_payment(drink.cost):
        coffee_machine.make_coffee(drink)


