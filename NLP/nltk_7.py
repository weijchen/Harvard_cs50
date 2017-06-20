# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Named Entity Recognition), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/part-of-speech-tagging-nltk-tutorial/
# --------------------------------------------------- libs import
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# --------------------------------------------------- NE list
'''
NE Type and Examples

ORGANIZATION - Georgia-Pacific Corp., WHO
PERSON - Eddy Bonte, President Obama
LOCATION - Murray River, Mount Everest
DATE - June, 2008-06-29
TIME - two fifty a m, 1:30 p.m.
MONEY - 175 million Canadian Dollars, GBP 10.40
PERCENT - twenty pct, 18.75 %
FACILITY - Washington Monument, Stonehenge
GPE - South East Asia, Midlothian
'''
# --------------------------------------------------- program
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(sample_text)

def process_content():
	try:
		for i in tokenized[5:]:
			words = nltk.word_tokenize(i)
			tagged = nltk.pos_tag(words)
			namedEnt = nltk.ne_chunk(tagged, binary=0)	# binary = TRUE: set all NE type items as NE
			namedEnt.draw()
	except Exception as e:
		raise e

process_content()