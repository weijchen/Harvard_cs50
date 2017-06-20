# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Text Classification), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/text-classification-nltk-tutorial/
# --------------------------------------------------- libs import
import nltk
import random	# shuffle DB
from nltk.corpus import movie_reviews
# --------------------------------------------------- program

## -- Create to training in testing set
documents = []
for category in movie_reviews.categories():
	print(category)
	for fileid in movie_reviews.fileids(category):
		print(fileid)
		documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
# print(documents[1])

all_words = []
# -- Ignore higher-lower-case problems --
for w in movie_reviews.words():
	all_words.append(w.lower())

# -- Calculate frequency --
all_words = nltk.FreqDist(all_words)
# print(all_words)
# print(all_words.most_common(15))
# -- Calculate freq of specific word --
# print(all_words["stupid"])