# -*- coding: utf-8 -*-
# PN: NLTP tutorial (WordNet), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/nltk-corpus-corpora-tutorial/
# --------------------------------------------------- libs import
from nltk.corpus import wordnet
# --------------------------------------------------- program

# -- Find synonym --
syns = wordnet.synsets("program")

# # -- synset --
# print(syns[0].name())
# # plan.n.01

# # -- word --
# print(syns[0].lemmas()[0].name())
# # plan

# # -- definition --
# print(syns[0].definition())
# # a series of steps to be carried out or goals to be accomplished

# # -- examples --
# print(syns[0].examples())
# # ['they drew up a six-step plan', 'they discussed plans for a new bond issue']


synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
	for l in syn.lemmas():
		synonyms.append(l.name())
		if l.antonyms():
			antonyms.append(l.antonyms()[0].name())

# print(set(synonyms))
# print(set(antonyms))

# -- Test similarity (in decimal) --
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cactus.n.01")
print(w1.wup_similarity(w2))















