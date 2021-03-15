import nltk  # imports libraries needed to have all of the words that have ever been in the English language
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context    # workaround to grab the needed package
nltk.download('words')

from nltk.corpus import words   # imports all the words and dumps them into word_list
game_words = words.words()