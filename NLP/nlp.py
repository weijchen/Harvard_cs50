# -*- coding: utf-8 -*-
# PN: NLTP tutorial, Created Jun. 2017
# Ver: 1.0
# Link: 
# --------------------------------------------------- libs import
from nltk.corpus import twitter_samples
from nltk.tag import pos_tag_sents
# --------------------------------------------------- program

# # -- Print used sample files --
# print(twitter_samples.fileids())

# # -- Print files contents --
# print(twitter_samples.strings('tweets.20150430-223406.json'))

tweets = twitter_samples.strings('positive_tweets.json')

# -- Tokenize sentence into pieces --
tweets_tokens = twitter_samples.tokenized('positive_tweets.json')

# -- tag POS to each word, i.e. Noun, Verb, Adject, Adverb --
# -- Single Noun (NN), Plural Nouns (NNS), Adjective (JJ) --
tweets_tagged = pos_tag_sents(tweets_tokens)

JJ_count = 0
NN_count = 0

for tweets in tweets_tagged:
	for tweet in tweets:
		if tweet[1] == 'JJ':
			JJ_count += 1
		elif tweet[1] == 'NN':
			NN_count += 1

print('Total Adjective = ', JJ_count)
print('Total Nouns = ', NN_count)