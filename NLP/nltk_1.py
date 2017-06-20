# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Tokenization), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/tokenizing-words-sentences-nltk-tutorial/
# --------------------------------------------------- libs import
from nltk.tokenize import sent_tokenize, word_tokenize
# --------------------------------------------------- program
example_text = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

# print(sent_tokenize(example_text))
# print(word_tokenize(example_text))

for i in word_tokenize(example_text):
	print(i)