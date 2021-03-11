hangman_image = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
                 "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
                 "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
                 "_______\n|     |\n|\n|\n|\n|\n|\n======="]  # copied from a google search. Builds the gallows for each position. Head, body, arm, arm, leg, leg.


def game(answer):  # main game function. Running this will start the game.
    word = answer  # this is for safekeeping as the answer is about to become a list.
    answer = list(answer)  # Converts the answer to a list so it can be compared to the progress and guesses
    progress = list("_" * len(answer))  # Creates a string of underscores to represent the amount of letters and then makes it a list so it can be easily edited and compared.
    guessed_letters = []  # Keeps track of letters guessed
    fails = 6  # Counter to keep track of attempts remaining
    return print(f"\n {word}"
                 f"\n {answer}"
                 f"\n {progress}"
                 f"\n {guessed_letters}"
                 f"\n {fails}")  # TEST PRINTS FOR EACH VARIABLE TO ENSURE THEY WORK


game(input("What word shall we test? "))  # Calls the main game function asking for a word
