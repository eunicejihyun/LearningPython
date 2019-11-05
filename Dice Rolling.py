import time

import random
min =0
max =5

roll_again = "yes"

pictures = ['   |   |\n   | o |\n   |   |   1\n', '   |o  |\n   |   |\n   |  o|   2\n', '   |o  |\n   | o |\n   |  o|   3\n', '   |o o|\n   |   |\n   |o o|   4\n','   |o o|\n   | o |\n   |o o|   5\n','   |o o|\n   |o o|\n   |o o|   6\n']

while roll_again == "yes" or roll_again =="y":
    for letter in "Rolling the dice...":
        print(letter, end='')
        time.sleep(.05)
    print ("\n")
    print (pictures[random.randint(min,max)])
    print (pictures[random.randint(min,max)])

    roll_again = input("Roll the dice again? \n")
    print("\n")
