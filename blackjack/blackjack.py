import random
from art import logo, wtf

def reset():
    """
    Create and return a fresh game state dictionary for a new round.
    """
    return {
        "player_hand": [],
        "dealer_hand": [],
        "player_total": 0,
        "dealer_total": 0,
        "game_over": False,
        "play_again": True,
    }

def show_hands(cur_state):
    """
    Display the player's full hand and the dealer's visible card.

    Parameters
    ----------
    cur_state : dict
        Current game state containing hands and totals.
    """
    print(f"Your cards: {cur_state['player_hand']}, current total: {cur_state['player_total']}")
    print(f"Dealer's card: {cur_state['dealer_hand'][0]}")

def deal(cur_state, x, who):
    """
    Deal cards into the specified hand and update its running total.

    Parameters
    ----------
    cur_state : dict
        Current game state containing hands and totals.
    x : int
        How many cards to deal into the current hand.
    who : str
        Either "player" or "dealer".
    """
    if who == 'player':
        for _ in range(x):
            cur_state['player_hand'].append(random.choice(cards))
            cur_state['player_total'] += cur_state['player_hand'][-1]
    elif who == 'dealer':
        for _ in range(x):
            cur_state['dealer_hand'].append(random.choice(cards))
            cur_state['dealer_total'] += cur_state['dealer_hand'][-1]

def adjust_aces(hand, total):
    """
    Adjust aces from 11 to 1 if the hand total exceeds 21.

    Parameters
    ----------
    hand : list
        List containing the cards of the hand of the current player.
    total : int
        Current running total of the hand of the current player.

    Returns
    -------
    int
        The recalculated total.
    """
    while total > 21 and 11 in hand:
        ace = hand.index(11)
        hand[ace] = 1
        total -= 10
    return total

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
record = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}
state = reset()

print(logo)
play = input("Would you like to play blackjack? (y/n): ").strip().casefold()
if play in ("y", "yes"):
    while state['play_again']:
        deal(state, 2, "player")
        deal(state, 2, "dealer")
        show_hands(state)
        hit_pass = input("Would you like to hit or stay? (h/s): ").strip().casefold()
        while hit_pass not in ("s", "stay", "h", "hit"):
            hit_pass = input("Invalid input received. Would you like to hit or stay? (h/s): ").strip().casefold()
        if hit_pass in ("h", "hit"):
            deal(state, 1, "player")
            state['player_total'] = adjust_aces(state['player_hand'], state['player_total'])
            if state['player_total'] > 21:
                state['game_over'] = True
            while state['player_total'] <= 21 and not state['game_over']:
                show_hands(state)
                hit_pass = input("Would you like to hit or stay? (h/s): ").strip().casefold()
                while hit_pass not in ("s", "stay", "h", "hit"):
                    hit_pass = input("Invalid input received. Would you like to hit or stay? (h/s): ").strip().casefold()
                if hit_pass in ("s", "stay"):
                    break
                deal(state, 1, "player")
                state['player_total'] = adjust_aces(state['player_hand'], state['player_total'])
                if state['player_total'] > 21:
                    state['game_over'] = True
                    break
        if not state['game_over']:
            while state['dealer_total'] < 17:
                deal(state, 1, "dealer")
                state['dealer_total'] = adjust_aces(state['dealer_hand'], state['dealer_total'])
                if state['dealer_total'] > 21:
                    state['game_over'] = True
                    break
        if state['dealer_total'] > state['player_total'] and state['dealer_total'] <= 21:
            record["losses"] += 1
            print(f"Dealer wins, their final hand: {state['dealer_hand']}, with a total score of {state['dealer_total']}")
            print(f"Your final hand: {state['player_hand']}, with a total score of {state['player_total']} ")
            print(f"Current record: {record['wins']}-{record['losses']}-{record['ties']}")
        elif state['player_total'] > 21:
            record["losses"] += 1
            print(f"Bust! Dealer wins, their final hand: {state['dealer_hand']}, with a total score of {state['dealer_total']}")
            print(f"Your final hand: {state['player_hand']}, with a total score of {state['player_total']} ")
            print(f"Current record: {record['wins']}-{record['losses']}-{record['ties']}")
        elif state['player_total'] == state['dealer_total']:
            record["ties"] += 1
            print(f"Push! Tie game.\nYour final hand: {state['player_hand']}, with a total score of {state['player_total']}")
            print(f"Dealer's final hand: {state['dealer_hand']}, with a total score of {state['dealer_total']}")
            print(f"Current record: {record['wins']}-{record['losses']}-{record['ties']}")
        else:
            record["wins"] += 1
            print(f"You win! Your final hand: {state['player_hand']}, with a total score of {state['player_total']}")
            print(f"Dealer's final hand: {state['dealer_hand']}, with a total score of {state['dealer_total']}")
            print(f"Current record: {record['wins']}-{record['losses']}-{record['ties']}")
        again = input("Do you want to play again? (y/n): ").strip().casefold()
        if again in ("y", "yes"):
            state = reset()
            print(logo)
        else:
            state["play_again"] = False
            print(logo)
            print("Thanks for playing! Goodbye!")
            print(f"Final record: {record['wins']}-{record['losses']}-{record['ties']}")
else:
    print(wtf)
    print("OK, what are we even doing here, then? Later, dog. LA-TER.")
