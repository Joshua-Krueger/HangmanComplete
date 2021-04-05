import discord  # might need for bot as well
from discord.ext import commands  # Allows me to use discord for the bot
import random  # imports the random library for picking the word
from word_list import game_words  # from my own .py for the list of all words
import wiktionaryparser  # Needed to ge the definitions of words

hangbot = commands.Bot(command_prefix="-")  # sets the bot command key to -
TOKEN = "TOKEN"  # bot token. the one in the code is just a placeholder


def get_definition(word, language="english"):  # takes a word and language, is going to search it on Wiktionary
    parser = wiktionaryparser.WiktionaryParser()  # creates a new parser object so it can interact with the program
    parser.set_default_language(language)  # defaults the language to English
    definition = parser.fetch(word)  # looks for the word
    try:  # try except needed just in case there are no available definitions
        def_list = definition[0]["definitions"][0]["text"]  # creates a list of the definitions after digging them up
        if len(def_list) > 5:  # if the definition list is longer than five items
            def_list = def_list[0:4]  # limits the definitions to four just in case it has many
            return def_list  # gives the list back to the main game function so it can be printed
    except IndexError as _:
        return ["sorry there's no definition available"]  # in case there's no definition


@hangbot.event
async def on_ready():
    print(f"{hangbot.user.name} is ready!")  # lets me know when bot is ready to rumble
    await hangbot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="For -commands"))  # sets the bot's server status to tell them to type -commands in order to see what it is capable of


@hangbot.command(name="define")  # Defines any given word
async def define(ctx, word):
    return await ctx.send(get_definition(word))  # takes a user's request for a word then gives definitions for it


@hangbot.command(name="commands")  # if they need help with the commands, then it will show them the commands
async def commands(ctx):
    await ctx.send("\n-start: Starts a game of hangman."
                   "\n-define *word*: Defines a word."
                   "\n-generate *x*: Produces *x* number of random words up to 100.")  # prints the commands and what they do


@hangbot.command(name="generate")  # prints out random words up to one hundred
async def generate(ctx, num_words):
    if int(num_words) > 100:  # more than 100 words is asking a lot of the machine and floods discord
        return await ctx.send("Woah there partner. Too many words")  # tells them too many
    else:
        for _ in range(int(num_words)):  # for loop to print out however many words they asked for
            word = game_words[random.randint(0, len(game_words) - 1)]  # generates a random word
            await ctx.send(word)  # prints a random word to discord


@hangbot.command(name="start")
async def start(ctx):  # main game function
    hangman = ["\\_\\_\\_\\_\\_\\_\\_\n|     |\n|     O\n|    -|-\n|     |\n|    / \\ \n|\n=======",
               "\\_\\_\\_\\_\\_\\_\\_\n|     |\n|     O\n|    -|-\n|     |\n|    /\n|\n=======",
               "\\_\\_\\_\\_\\_\\_\\_\n|     |\n|     O\n|    -|-\n|     |\n|\n|\n=======",
               "\\_\\_\\_\\_\\_\\_\\_\n|     |\n|     O\n|    -|\n|     |\n|\n|\n=======",
               "\\_\\_\\_\\_\\_\\_\\_\n|     |\n|     O\n|     |\n|     |\n|\n|\n=======",
               "\\_\\_\\_\\_\\_\\_\\_\n|     |\n|     O\n|\n|\n|\n|\n=======",
               "\\_\\_\\_\\_\\_\\_\\_\n|     |\n|\n|\n|\n|\n|\n=======",
               ]  # prints out the hangman station
    answer = game_words[random.randint(0, len(game_words)-1)]  # sets the game word to a random word from the English language
    word = answer  # for safekeeping as the word is about to become a list
    answer = list(answer)  # converts the answer to a list so it can be compared to the progress and guesses
    progress = ["\\_" for _ in range(len(answer))]  # creates a string of underscores to show each position in the word to the user
    guessed_letters = []  # keeps track of their guesses
    fails = 6  # keeps track of attempts that remain
    while fails > 0:  # central game loop, essentially saying "as long as there is at least one limb left, go again."
        if progress == answer:  # checks if they are right
            await ctx.send(f"You did it!\nThe word was {word}")  # prints the congratulation and word to discord
            for i in get_definition(word): await ctx.send(f"\n {i}")  # sends the definitions
            break  # stops before it loops through the whole thing again
        await ctx.send(f"\n{hangman[fails]}"
                       f"\nyou have {fails} tries left"
                       f"\nYour word so far is {' '.join(progress)}"
                       f"\nYou've guessed {guessed_letters}")  # gives them the info they need to play the game
        initial_input = await hangbot.wait_for("message")  # waits for the user to type in a guess
        current_guess = initial_input.content.lower()  # stores the users guess for comparison
        if len(current_guess) == 1 and current_guess.isalpha():  # ensures their guess is only one letter
            if current_guess in guessed_letters:  # checks if the user guessed that letter already
                await ctx.send(f"You already guessed {current_guess}!")  # tells the user they already guessed that and sends them to guess again
            elif current_guess in answer:  # checks if the guess is in the answer
                for index, character in enumerate(answer):  # enumerates answer making two dicts full of values for the answer list.
                    progress = list(progress)  # Ensures that only one letter is added where it should be each time.
                    if character == current_guess:  # checks the guess against each letter in answer
                        progress[index] = current_guess  # sets the underscore at the right position to the guess
            elif current_guess not in answer:  # checks if the guess is not in the answer
                fails -= 1  # they lose one attempt and a limb is added
            guessed_letters.append(current_guess) # adds the letter that was guessed to guessed letters
        else:
            await ctx.send("Only single letter guesses allowed")  # in case they try to guess more than a letter
    if fails <= 0:  # checks if their game has ended
        await ctx.send(hangman[0])  # only occurs when they lose and the loop ends, prints the final position of the gallows
        await ctx.send(f"\nSorry, you failed to save the man"
                       f"\nYour word was {word}, better luck next time!")  # closing messages
        for i in get_definition(word): await ctx.send(f"\n {i}")  # Gives the definition of the word


hangbot.run(TOKEN)  # runs the bot
