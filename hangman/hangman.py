import random
word_list = [
    "aardvark", "baboon", "camel", "alligator", "elephant", "giraffe", "hippopotamus",
    "rhinoceros", "chimpanzee", "kangaroo", "dolphin", "porcupine", "salamander",
    "penguin", "flamingo", "armadillo", "chameleon", "hedgehog", "platypus", "meerkat",

    "computer", "keyboard", "monitor", "headphones", "microphone", "processor",
    "internet", "database", "terminal", "python", "variable", "function", "iterator",
    "condition", "parameter", "argument", "exception", "compiler", "interpreter",

    "mountain", "river", "ocean", "desert", "volcano", "waterfall", "glacier",
    "forest", "jungle", "savanna", "tundra", "canyon", "island", "peninsula",
    "archipelago", "continent", "hemisphere",

    "bicycle", "airplane", "helicopter", "submarine", "spaceship", "locomotive",
    "motorcycle", "skateboard", "scooter", "sailboat", "spacesuit",

    "adventure", "mystery", "treasure", "labyrinth", "puzzle", "strategy",
    "victory", "defeat", "champion", "challenge", "discovery", "exploration",

    "algorithm", "encryption", "compression", "simulation", "visualization",
    "optimization", "abstraction", "architecture", "synchronization",

    "umbrella", "backpack", "notebook", "flashlight", "telescope", "microscope",
    "compass", "binoculars", "thermometer", "calculator", "calendar",

    "sandwich", "pancake", "spaghetti", "hamburger", "lasagna", "omelette",
    "chocolate", "strawberry", "blueberry", "pineapple", "avocado", "cucumber",

    "galaxy", "asteroid", "comet", "nebula", "supernova", "satellite", "telescope",
    "orbit", "gravity", "eclipse", "constellation"
]

def start_game():
    init_gameover = False
    init_guesses = 5
    init_do_over = ""

    init_chosen_word = random.choice(word_list)
    init_chosen_word_list = list(init_chosen_word)

    init_charcount = len(init_chosen_word)
    init_placeholder = []

    for x in range(init_charcount):
        init_placeholder.append("_")

    return init_gameover, init_guesses, init_do_over, init_chosen_word, init_chosen_word_list, init_charcount, init_placeholder

gameover, guesses, do_over, chosen_word, chosen_word_list, charcount, placeholder = start_game()

while not gameover:
    placeholder_string = "".join(placeholder)
    if guesses != 1:
        print(f"Hangman! You have {guesses} guesses left.")
    else:
        print(f"Hangman! You have {guesses} guess left.")

    print(placeholder_string)
    if placeholder_string == chosen_word and guesses != 0:
        gameover = True
        print("Game Over, you win!")
        do_over = input("Play again? (y/n) ").casefold()
    elif guesses == 0:
        gameover = True
        print("Game Over, you lose!")
        do_over = input("Play again? (y/n) ").casefold()
    else:
        guess = input("Guess a letter: ").casefold()
        for i in range(charcount):
            if guess == chosen_word_list[i]:
                placeholder[i] = guess

        if guess in chosen_word:
            print("Right")
        else:
            guesses -= 1

    if do_over == "y":
        gameover, guesses, do_over, chosen_word, chosen_word_list, charcount, placeholder = start_game()
