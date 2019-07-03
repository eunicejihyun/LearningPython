# Number Guessing Game as seen on Al's YouTube Channel


print ('What is your name, friend?')
name = input()
    
def game():      
    import random

    number = random.randint(1,20)

    print (number)

    print ('I am thinking of a number between 1 and 20, ' + name + '. What is it?')

    for attempts in range(1,6): #5 tries
        global guess
        try:
            guess = int(input())
        except ValueError:
            print ('Use numbers. Try again.')
            guess = int(input())
        if guess > number:
            print ('Too high.')
        elif guess < number:
            print ('Too low.')
        elif guess == number:
            print ('Great job! You got it right in ' + str(attempts) + ' tries!')
            break
     
    if attempts == 5 and guess != number:
        print ('The number was ' + str(number) + '. Want to play another round? y/n')
    else:
        print  ('Want to play another round? y/n')

game()


response = input()

while response == 'y':
    game()
    response = input()


print ('Thanks for playing')
