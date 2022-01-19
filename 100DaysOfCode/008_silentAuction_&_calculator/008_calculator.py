from art import calculator


#Defining calculation functions in this section
def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

#Creating a dictionary with the symbols as the key and functions as the value
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

#Ensuring that only numbers are entered
def get_number(clarification):
    while True:
        try:
            number = float(input(f"Enter your {clarification} number: "))
        except ValueError:
            print("Numbers only please.")
        else:
            return number

def calculate():
    print(calculator)
    n1 = get_number("first")

    continue_calc = True
    while continue_calc:

        #Ensuring only valid operations are selected
        while True:
            try:
                op = input(" + - * / Pick an operation: ")
                assert op in operations, "Please choose an operation from the list."
            except AssertionError as e:
                print(e)
            else:
                break

        n2 = get_number("next")
        result = operations[op](n1, n2)
        print(f"   {n1} {op} {n2} = {result}\n")

        keep_going = input(f"Type 'y' to continue your calc with {result} or 'n' to start a new calculation. ").lower()

        if keep_going == 'y':
            n1 = result
        else:
            continue_calc = False
            calculate()

calculate()