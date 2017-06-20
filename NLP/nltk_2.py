# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Stop words), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/stop-words-nltk-tutorial/
# --------------------------------------------------- libs import
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
# --------------------------------------------------- program
example_sentence = "This is a sample sentence, showing off the stop words filtration."

stop_words = set(stopwords.words('english'))

words = word_tokenize(example_sentence)

# -- Code 1 --
filtered_sentence = []
for w in words:
	if w not in stop_words:
		filtered_sentence.append(w)

print(filtered_sentence)

# -- Code 2 --
filtered_sentence = [w for w in words if w not in stop_words]
print(filtered_sentence)
