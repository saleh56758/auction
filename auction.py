def clear_screen():  
    print("\n" * 125)
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

def secret_auction():
    print("Welcome to the Secret Auction Program!")    
    bidding_finished = False
    bids = {}
    while not bidding_finished:
        name = input("What is your name? ")
        bid = int(input("What is your bid? $"))
        bids[name] = bid
        should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if should_continue == "no":
            bidding_finished = True
        elif should_continue == "yes":
            clear_screen()
    winner, highest_bid = find_highest_bidder(bids)
    print(f"The winner is {winner} with a bid of ${highest_bid}.")
secret_auction()
