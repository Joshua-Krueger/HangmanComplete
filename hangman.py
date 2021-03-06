import random  # used to pick a random word from the list of all words
from word_list import game_words  # so I can access all of the words
import wiktionaryparser  # for looking up the definitions
# Terminal hangman made by Joshua Krueger March 10, 2021
# Use as you wish with credit given.

hangman_image = ["_______\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
                 "_______\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
                 "_______\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
                 "_______\n|     |\n|     O\n|\n|\n|\n|\n=======",
                 "_______\n|     |\n|\n|\n|\n|\n|\n======="]  # copied from a google search. Builds the gallows for each position. Head, body, arm, arm, leg, leg.


def get_definition(word, language="english"):  # takes a word and language, is going to search it on Wiktionary
    parser = wiktionaryparser.WiktionaryParser()  # creates a new parser object so it can interact with the program
    parser.set_default_language(language)  # defaults the language to English
    definition = parser.fetch(word)  # looks for the word
    try:  # try except needed just in case it's a weird/old word that isn't on Wiktionary
        def_list = definition[0]["definitions"][0]["text"]  # creates a list of the definitions after digging them up
        for i in def_list: print(f"\n {i}")  # prints them each on new lines
    except IndexError as _:
        print("sorry there's no definition available")  # in case there's no definition


def game(option):  # main game function. Running this will start the game.
    if option.lower() == "y":  # if user wants to pick their own word
        word = input("What word shall we play with?")  # sets the game word to their choice
    else:
        word = game_words[random.randint(0, len(game_words)-1)]  # sets the game word to a random word from the English language
    answer = list(word)  # Converts the answer to a list so it can be compared to the progress and guesses
    progress = list("_" * len(answer))  # Creates a string of underscores to represent the amount of letters and then makes it a list so it can be easily edited and compared.
    guessed_letters = []  # Keeps track of letters guessed
    fails = 6  # Counter to keep track of attempts remaining
    while fails > 0:  # central game loop, essentially saying "as long as there is at least one limb left, go again."
        if progress == answer:  # if they are correct
            print(f"you did it!\nThe word was {word}")  # tells the user the word
            get_definition(word)  # gives the user definitions of the word
            new_game(input("Would you like to play again? (y/n) ").lower())  # if they want to play again
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
    get_definition(word)  # gives the user definitions of the word
    new_game(input("Would you like to try again? (y/n) ").lower())  # asks if they would like to play again


def new_game(choice):  # for the user to play again if they want to
    if choice == "y":  # checks whether or not they said yes
        game(input("Would you like to provide your own word?(y/n) "))  # runs the game again
    else:
        quit()  # quits


game(input("Would you like to provide your own word?(y/n) "))  # Calls the main game function
