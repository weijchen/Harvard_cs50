# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Lemmatizing), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/lemmatizing-nltk-tutorial/
# --------------------------------------------------- libs import
import nltk
from nltk.stem import WordNetLemmatizer
# --------------------------------------------------- program

# -- Explanation: Find synonym --
lemmatizer = WordNetLemmatizer()

# print(lemmatizer.lemmatize("cats"))
# print(lemmatizer.lemmatize("cacti"))
# print(lemmatizer.lemmatize("geese"))
# print(lemmatizer.lemmatize("rocks"))
# print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("soooooo"))
print(lemmatizer.lemmatize("best", pos = 'a'))
print(lemmatizer.lemmatize("apple"))
print(lemmatizer.lemmatize("run", pos = 'n'))

# print(lemmatizer.lemmatize("better"))
