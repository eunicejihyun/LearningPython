positions = {
    "a": " ",
    "b": " ",
    "c": " ",
    "d": " ",
    "e": " ",
    "f": " ",
    "g": " ",
    "h": " ",
    "i": " "
}

player_1 = "X"
player_2 = "O"

winning_combos = [['a', 'b', 'c'], ['a', 'd', 'g'], ['a', 'e', 'i'], ['b', 'e', 'h'], ['c', 'e', 'g'], ['c', 'f', 'i'],
                  ['d', 'e', 'f'], ['g', 'h', 'i']]

board = ""


def draw_board():
    global board
    board = f"""
     a | b | c       {positions['a']} | {positions['b']} | {positions['c']}
    ---+---+---     ---+---+---
     d | e | f       {positions['d']} | {positions['e']} | {positions['f']}
    ---+---+---     ---+---+---
     g | h | i       {positions['g']} | {positions['h']} | {positions['i']}
    """
    print(board)
    return


def take_a_turn(character):
    global positions
    choice = input(f"Where would you like to draw an {character}? ").lower()
    if choice in positions and positions[choice] not in [player_1, player_2]:
        positions[choice] = character
        draw_board()
        return
    else:
        print("Move not allowed. Please select a valid option.\n")
        take_a_turn(character)


def examine_board():
    for combo in winning_combos:
        if positions[combo[0]] == positions[combo[1]] == positions[combo[2]] \
                and positions[combo[0]] in [player_1, player_2]:
            print(f'{positions[combo[0]]} wins! Congratulations~')
            game_over()
    for pos in positions:
        if positions[pos] == " ":
            return
    print('Tie! Good Game~')
    game_over()
    return False


def game_over():
    response = input("\nWould you like to play again? Type 'y' for another round. ").lower()
    if response == 'y':
        new_game()
    else:
        input("Thanks for playing! Press Enter to exit.")
        quit()


def clear_board():
    global positions
    positions = {
        "a": " ",
        "b": " ",
        "c": " ",
        "d": " ",
        "e": " ",
        "f": " ",
        "g": " ",
        "h": " ",
        "i": " "
    }
    draw_board()


def new_game():
    clear_board()
    while True:
        take_a_turn(player_1)
        examine_board()
        take_a_turn(player_2)
        examine_board()


new_game()
