""""Blind Auction"""
from art import logo
import os


def clear():
    """Clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)

bids = {}
bidding_finishead = False

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    #bidding_record = {"Vali": 100, "Mihai": 150}.
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of $ {highest_bid}")


while not bidding_finishead:
    name = input('What is your name?')
    price = int(input('What is your bid price? $'))
    bids[name] = price
    should_continue = input("are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finishead = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()








