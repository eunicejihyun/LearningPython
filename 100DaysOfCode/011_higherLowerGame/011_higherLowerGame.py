from art import logo, vs
from game_data import *
from random import randint

#display comparison candidate
def display(option):
    if option == a:
        print(f"Compare A: {option['name']}, a {option['description']}, from {option['country']}")
    else:
        print(f"Against B: {option['name']}, a {option['description']}, from {option['country']}")

#qa string input
def qa_input(prompt, options):
    while True:
        try:
            response = input(prompt).lower()
            assert response in options, "Please type a valid response."
        except AssertionError as e:
            print(e)
        else:
            return response

#evaluate comparison - see which account has a higher follower count
def evaluate():
    if a['follower_count'] > b['follower_count']:
        answer = 'a'
    else:
        answer = 'b'
    return answer


while True:
    comparisons = []
    print(logo)
    score = 0
    a = {}
    b = {}
    while True:
        print(vs)

        comparisons.append([a, b])
        comparisons.append([b, a])

        #Ensure that same combinations are not replayed
        while True:
            try:
                a = data[randint(1, len(data)) - 1]
                b = data[randint(1, len(data)) - 1]
                assert [a,b] not in comparisons and [b,a] not in comparisons and (a!=b), "Not a unique combination."
            except:
                continue
            else:
                break

        display(a)
        display(b)

        answer = evaluate()
        guess = qa_input("Who has more followers? Type 'a' or 'b': ", ['a', 'b'])

        if guess == answer:
            score += 1
            print(f"  ==> Great job! You got it right. Current score: {score}" + "\n" * 3)
        else:
            print(f"  ==> Uh oh! That's wrong. Better luck next time. Final score: {score}" + "\n" * 3)
            score = 0
            break
    replay = qa_input("Would you like to play another round? Type 'y' or 'n': ", ['y', 'n'])

    if replay == 'y':
        continue
    else:
        input("Press enter to close the program.")
        break
