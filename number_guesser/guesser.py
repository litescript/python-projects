import random
from art import logo

play_again = True

def which_mode(mode):
    if mode in ("easy", "e"):
        return 10
    elif mode in ("hard", "h"):
        return 5
    else:
        return False

while play_again:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    guesses = which_mode(input("Choose a difficulty. Type 'easy' or 'hard': ").strip().casefold())
    while not guesses:
        guesses = which_mode(input("Choose a difficulty. Type 'easy' or 'hard': ").strip().casefold())
    rand_num = random.randint(1, 100)
    while guesses > 0:
        if guesses == 1:
            print("You are on your last guess!")
        else:
            print(f"You have {guesses} guesses left.")
        guess = int(input("Make a guess: ").strip())
        if guess == rand_num:
            print("You got it!")
            break
        elif guess > rand_num:
            print("Too high!")
        else:
            print("Too low!")
        guesses -= 1
    else:
        print(f"Game over. The number was {rand_num}.")
    choice = input("Do you want to play again? (y/n): ").strip().casefold()
    if choice not in ("y", "yes"):
        play_again = False
