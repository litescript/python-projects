from art import logo
import os

done = False
auction = {}
winner = ""
highest_bid = 0

def clear():
    os.system("cls" if os.name == "nt" else "clear")

print(logo)
print("Welcome to the silent auction\n")

while not done:
    name = input("What is your name? ")
    while True:
        bid_str = input("What is your bid? $")
        if bid_str.isdigit():
            bid = int(bid_str)
            break
        print("Please enter a whole number.")
    auction[name] = bid
    others = input("Are there any other people still to bid? (y/n) ").casefold()
    if others not in ("y", "yes"):
        done = True
    else:
        # PyCharm IDE used for the project does not support os.system terminal clears,
        # had to leave the new-line trick to make it work in PyCharm.
        # Left the call to clear() so it actually clears in real terminal emulators.
        clear()
        print("\n" * 20)

for key, value in auction.items():
    if value > highest_bid:
        highest_bid = value
        winner = key

print(f"The winner is {winner} with a bid of ${highest_bid}")
