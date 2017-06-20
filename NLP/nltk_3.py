# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Stemming), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/stop-words-nltk-tutorial/
# --------------------------------------------------- libs import
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
# --------------------------------------------------- program

## -- Explanation --
# I was taking a ride in the car.
# I was riding the car.
# 字根搜索 Stemming

ps = PorterStemmer()
example_words = ["python", "pythoner", "pythoning", "pythoned", 'pythonly']

# for w in example_words:
# 	print(ps.stem(w))


new_text = "It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once."

words = word_tokenize(new_text)

# for w in words:
# 	print(ps.stem(w))