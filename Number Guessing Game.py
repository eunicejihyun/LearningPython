# Number Guessing Game as seen on Al's YouTube Channel
#This version has been updated to modify game level before each new play.

    
def game():
    print ('How challenging do you want this game to be?')
    while True:
        try:
            maximum = int(input('Level 1 - 1000 : '))
            if maximum not in range (1,1001):
                raise ValueError
            break
        except ValueError:
            print ('Choose a number from 1 to 1000')
            continue
    import random

    number = random.randint(1,int(maximum))

    print ('I am thinking of a number between 1 and ' + str(maximum) + '. What is it?')

    for attempts in range(1,11): #10 tries
        global guess
        while True:
            try:
                guess = int(input('Guess: '))
                if guess < 1 or guess > maximum:
                    raise ValueError
                break
            except ValueError:
                print ('Use numbers from 1 to ' + str(maximum) + '. Try again.')
                continue          
        if guess > number:
            print ('Too high.')
        elif guess < number:
            print ('Too low.')
        elif guess == number:
            print ('Great job! You got it right in ' + str(attempts) + ' tries!')
            break
     
    if attempts == 10 and guess != number:
        print ('Nice try, but the number was ' + str(number) + '. Want to play another round? y/n')
    else:
       print  ('Great job! Want to play another round? y/n')


def respond():
    while True:
        global response
        response = input()
        try:
            if response not in ['y', 'n']:
                raise ValueError
            break
        except ValueError:
            print ('Please use either y or n.')

response = 'y'

while response == 'y':
    game()
    respond()


print ('Thanks for playing')
