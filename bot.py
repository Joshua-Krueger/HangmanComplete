import discord  # might need for bot as well
from discord.ext import commands  # Allows me to use discord for the bot
import random  # imports the random library for picking the word
from word_list import game_words  # from my own .py for the list of all words
import wiktionaryparser  # Needed to ge the definitions of words

hangbot = commands.Bot(command_prefix="-")  # sets the bot command key to -
TOKEN = "TOKEN"  # bot token


def get_definition(word, language="english"):  # takes a word and language, is going to search it on Wiktionary
    parser = wiktionaryparser.WiktionaryParser()  # creates a new parser object so it can interact with the program
    parser.set_default_language(language)  # defaults the language to English
    definition = parser.fetch(word)  # looks for the word
    try:  # try except needed just in case it's a weird/old word that isn't on Wiktionary
        def_list = definition[0]["definitions"][0]["text"]  # creates a list of the definitions after digging them up
        for i in def_list: print(f"\n {i}")  # prints them each on new lines
    except IndexError as _:
        print("sorry there's no definition available")  # in case there's no definition


hangbot.run(TOKEN)  # runs the bot
