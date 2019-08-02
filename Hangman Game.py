#Trying my hand at the Hangman Game with some help from the good folks from @ stack exchange



import random

print ('Welcome to the Hangman Game! The following letters are available: ')

#function to identify all instances of a letter in a word
def find(word, character):
    return [i for i, letter in enumerate(word) if letter == character]

     
def game():
    
    words = ['marble', 	'horseshoe', 	'copyright', 	'wander', 	'plagiarize', 	'feminine', 	'executive', 	'earthflax', 	'confine', 	'attitude', 	'efflux', 	'reflection', 	'thinker', 	'digital', 	'passage', 	'palace', 	'censorship', 	'regular', 	'correction', 	'convert', 	'growth', 	'dynamic', 	'neighborhood', 	'trolley', 	'impact', 	'situation', 	'practical', 	'trustee', 	'microphone', 	'interrupt', 	'marriage', 	'consensus', 	'picture', 	'fitness', 	'embrace', 	'module', 	'butterfly', 	'institution', 	'retiree', 	'extent', 	'filter', 	'interface', 	'disappear', 	'sailor', 	'parade', 	'husband', 	'satisfaction', 	'budget', 	'salvation', 	'emotion', 	'persist', 	'castle', 	'manager', 	'friendly', 	'revise', 	'rainbow', 	'elephant', 	'narrow', 	'inhabitant', 	'imagine', 	'trench', 	'border', 	'squash', 	'machinery', 	'specimen', 	'suffer', 	'global', 	'function', 	'swallow', 	'technique', 	'campaign', 	'recession', 	'freckle', 	'strong', 	'software', 	'reproduction', 	'thread', 	'building', 	'consumption', 	'empirical', 	'listen', 	'elaborate', 	'central', 	'dialogue', 	'lawyer', 	'indoor', 	'handicap', 	'elegant', 	'absent', 	'constraint', 	'silver']

    #picture of hangman
    pictures = ['\n'*4, '     O  \n        \n        \n', '   \ O  \n        \n        \n', '   \ O /\n        \n        \n', '   \ O /\n    ( ) \n        \n', '   \ O /\n    ( ) \n    /   \n', '   \ O /\n    ( ) \n    / \ \n']

    solution = list(words[random.randint(0, len(words)-1)])

    #to show available letters
    alphabet = [chr(i) for i in range(97,123)]

    gameboard = list('_' * len(solution))
    wrong = 0
    while wrong < 6 and gameboard != solution:

        print (pictures[wrong])
        print (*gameboard, sep=' ')
        print (*alphabet, sep='')


        #to prevent errors and the same letter from being attempted
        while True:
            try:
                letter = input()
                if len(letter) > 1 or letter not in alphabet:
                    raise ValueError
                break
            except ValueError:
                print ('please choose a single letter that has not been used')
                continue

        del alphabet[alphabet.index(letter)]
        
        if letter in solution:
            positions = find(solution, letter)
            for x in positions:
                gameboard[x] = letter
            print ('Great!')
            print('==============================\n\n')
        else:
            wrong += 1
            print ('Nope, sorry. ')
            print('==============================\n\n')


    print (pictures[wrong])

    if wrong == 6:
        print ('Better luck next time! The word was ', *solution, sep='')

    else:
        print ('Great job! The word was ', *solution, sep='')

    print ('Want to play another round? y/n')


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
        
