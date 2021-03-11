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
        if progress == answer:
            print(f"you did it!\nThe word was {word}")
            exit()
        print(f"\n{hangman_image[fails]}"
              f"\nYou have {fails} tries left"
              f"\nYour word so far is {progress}"
              f"\nYou've guessed {guessed_letters}")  # Gives them the necessary info to play the game
        current_guess = input("Guess a letter: ").lower()  # asks for their guess, ensures lowercase for safety
        if len(current_guess) == 1 and current_guess.isalpha():  # ensures guess is a letter and is only one letter
            if current_guess in guessed_letters:
                print(f"You already guessed {current_guess}!")  # stops the user from wasting a limb on a letter they've already tried
            elif current_guess in answer:  # only happens if the guessed letter is in the answer
                for index, character in enumerate(answer):  # enumerates answer making two dicts full of values for the answer list.
                    progress = list(progress)  # Ensures that only one letter is added where it should be each time.
                    if character == current_guess:  # checks the guess against each letter in answer
                        progress[index] = current_guess  # sets that spot in the list of underscores to the guess if correct
            elif current_guess not in answer:  # checks if the guess is not in the answer
                fails -= 1  # they lose one attempt and a limb is added
            guessed_letters.append(current_guess)  # adds the letter that was guessed to guessed letters
        else:
            print("Only single letter guesses allowed.")  # in case they try to guess more than a letter
    print(f"{hangman_image[0]}"  # only occurs when they lose and the loop ends, prints the final position of the gallows
          f"\nSorry, you failed to save the person"
          f"\nYour word was {word}, better luck next time!")  # Closing messages


game(input("What word shall we test? "))  # Calls the main game function asking for a word
