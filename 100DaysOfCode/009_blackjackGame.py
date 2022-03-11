import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                           _/ /                
      `------'                          |__/  @eunicejihyun     
"""

cards = {
    "A": 11,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
}


def qa_int_input(question, maximum):
    while True:
        try:
            qa_value = int(input(question))
            assert qa_value > 0 and qa_value < maximum, f"   ERROR: Type a number between 0 and {maximum}\n."
        except ValueError:
            print("   ERROR: Use numbers only.\n")
        except AssertionError as e:
            print(e)
        else:
            break
    return qa_value


def qa_str_input(question, options):
    while True:
        try:
            qa_value = input(question).lower()
            assert qa_value in options, "Please select a valid option."
        except AssertionError as e:
            print(e)
        else:
            break
    return qa_value


def shuffle():
    deck_count = qa_int_input("How many decks would you like to play with? Type a number 1 - 8: ", 9)
    deck = list(cards) * 4 * deck_count
    random.shuffle(deck)
    return deck


def bet():
    bet_amount = qa_int_input(f"You have ${bank} available. How much would you like to bet? $", bank + 1)
    return bet_amount


def deal():
    player = deck[:2]
    dealer = deck[2:4]
    updated_deck = deck[4:]
    return updated_deck, player, dealer


def calculate(hand):
    score = 0
    for i in hand:
        score += cards[i]
    if score > 21 and ("A" in hand):
        score -= 10
    return (score)


def display():
    player_score = calculate(player)
    dealer_score = calculate(dealer)

    spacing = " " * (24 - len(player) * 2)

    if round_on == True:
        print("\n----------------------------------------")
        print(f"PLAYER ({player_score} pts)          DEALER ({cards[dealer[0]]} pts)", )
        print(*player, f"{spacing} {dealer[0]} ?")
        print("----------------------------------------\n")
    else:
        print("\n----------------------------------------")
        print(f"PLAYER ({player_score} pts)          DEALER ({dealer_score} pts)", )
        print(*player, spacing, *dealer, "")
        print("----------------------------------------\n")

    return player_score, dealer_score


def hit(hand):
    updated_hand = hand + deck[:1]
    updated_deck = deck[1:]
    return updated_deck, updated_hand


def round_over(outcome):
    bet_value = bet_amount
    if outcome == "lose":
        bet_value *= -1
    updated_bank = bank + bet_value
    print(f"  => This round: You {outcome} ${bet_amount}!\n")
    return updated_bank


# SETUP
game_on = True
round_on = True
bank = 1000
player_score = 0
dealer_score = 0
round = 1
print(logo)
deck = shuffle()

while game_on:
    print(f"\nROUND {round}")
    bet_amount = bet()
    deck, player, dealer = deal()
    player_score, dealer_score = display()

    while round_on == True:
        if player_score == 21:
            print("  BLACKJACK!\nRevealing Dealer's hand...")
            round_on = False
        elif player_score > 21:
            print("  BUST!\nRevealing Dealer's hand...")
            round_on = False
        else:
            move = qa_str_input("Hit or Stand? ", ('hit', 'stand')).lower()
            if move == "hit":
                deck, player = hit(player)
                player_score, dealer_score = display()
            else:
                round_on = False
                print("Revealing Dealer's hand...")

    player_score, dealer_score = display()

    while dealer_score < 17:
        print("Dealer hit below 17. Dealer is taking a card...")
        deck, dealer = hit(dealer)
        player_score, dealer_score = display()

    ## End of Round
    if player_score == dealer_score:
        print("  => This round: PUSH\n")
    elif player_score > 21 and dealer_score > 21:
        print("  => This round: PUSH\n")
    elif player_score > 21:
        bank = round_over("lose")
    elif dealer_score == 21:
        print("  DEALER BLACKJACK!\n")
        bank = round_over("lose")
    elif dealer_score > 21:
        print("  DEALER BUST!\n")
        bank = round_over("win")
    elif player_score > dealer_score:
        bank = round_over("win")
    else:
        bank = round_over("lose")

    if bank > 0 and len(deck) > 8:
        next_round = qa_str_input("Would you like to play another round? Type 'y' or 'n'. ", ('y', 'n'))
        if next_round == 'y':
            round_on = True
            print("\n" * 50, logo)
            round += 1
        else:
            game_on = False
            print(f"Good game! You finished with ${bank}.")
    else:
        print(f"Game over! You finished with ${bank}.")
        game_on = False

input("\nPress [ENTER] to close the program.")
