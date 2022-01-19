from art import gavel

print(gavel + "\nWelcome to the Silent Auction.")

add_participant = True

auction_bids = {}

while add_participant:

    name = input("Please enter your name.\n    ").title()

    while True:
        try:
            bid = int(input("Please enter your bid.\n    $"))
        except ValueError:
            print("Please enter whole numbers only.\n    $")
        else:
            break

    auction_bids[name] = bid

    if input("Are there more bidders? Please type 'yes' or 'no'.\n    ").lower() == 'no':
        add_participant = False

    print("\n"*500 + gavel)

winner = ''
winning_bid = 0
for name in auction_bids:
    if auction_bids[name] > winning_bid:
        winning_bid = auction_bids[name]
        winner = name

print(f"The winner of this silent auction is {winner} with a bid of ${winning_bid}.")


