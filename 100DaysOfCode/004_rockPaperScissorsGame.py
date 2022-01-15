import random

illustration = {
"rock" : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

"paper" : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

"scissors" : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

options = list(illustration.keys())

computer = random.choice(options)

while True:
    try:
        player = input("Make your move! Type 'rock', 'paper', or 'scissors'.\n     ").lower()
        assert player in options, "Please type 'rock', 'paper', or 'scissors'. \n"
    except AssertionError as e:
        print(e)
    else:
        break

print("\nYour Move:")
print(illustration.get(player))

print("Computer's Move:")
print(illustration.get(computer))

play = {"computer": computer,
    "player": player}

key_list = list(play.keys())
val_list = list(play.values())


if all(x in val_list for x in ["rock", "paper"]):
    winner = key_list[val_list.index("paper")]
elif all(x in val_list  for x in ["scissors", "paper"]):
    winner = key_list[val_list.index("scissors")]
elif all(x in val_list for x in ["scissors", "rock"]):
    winner = key_list[val_list.index("rock")]
else:
    print("This round ends in a draw.")
    quit()

print(f"{winner.capitalize()} wins this round. ")
if winner == 'computer':
    print("Better luck next time.")
else:
    print("Great job!")