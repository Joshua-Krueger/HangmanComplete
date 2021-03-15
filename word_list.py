import nltk  # imports libraries needed to have all of the words that have ever been in the English language
import ssl

"""try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context    # workaround to grab the needed package
nltk.download('words')"""  # You only have to run this whole thing every once in a while as the list updates, but once it has run once the list will be on your computer

from nltk.corpus import words   # imports all the words and dumps them into word_list
game_words = words.words()