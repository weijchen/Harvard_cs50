# -*- coding: utf-8 -*-
# PN: NLTP tutorial (NLTK Corpora), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/nltk-corpus-corpora-tutorial/
# --------------------------------------------------- libs import
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
# --------------------------------------------------- program
## -- Find location of nltk --
# print(nltk.__file__)

# corpora consist of text DB

sample = gutenberg.raw('bible-kjv.txt')	# read raw content of file bible-kjv
tok = sent_tokenize(sample)

print(tok[5:15])