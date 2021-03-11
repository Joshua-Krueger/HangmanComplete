hangman_image = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
                 "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
                 "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
                 "_______\n|     |\n|\n|\n|\n|\n|\n======="]  # copied from a google search. Builds the gallows for each position. Head, body, arm, arm, leg, leg.


def game(user_word):  # main game function. Running this will start the game.
    word = user_word  # this is for safekeeping as the answer is about to become a list.
    answer = list(user_word)  # Converts the answer to a list so it can be compared to the progress and guesses
    progress = list("_" * len(answer))  # Creates a string of underscores to represent the amount of letters and then makes it a list so it can be easily edited and compared.
    guessed_letters = []  # Keeps track of letters guessed
    fails = 6  # Counter to keep track of attempts remaining
    while fails > 0:  # central game loop, essentially saying "as long as there is at least one limb left, go again."
        print(f"\n{hangman_image[fails]}"
              f"\nYou have {fails} tries left"
              f"\nYour word so far is {progress}"
              f"\nYou've guessed {guessed_letters}")  # Gives them the necessary info to play the game
        current_guess = input("Guess a letter: ").lower()  # asks for their guess, ensures lowercase for safety
        if len(current_guess) == 1 and current_guess.isalpha():  # ensures guess is a letter and is only one letter
            return print("True")

game(input("What word shall we test? "))  # Calls the main game function asking for a word
