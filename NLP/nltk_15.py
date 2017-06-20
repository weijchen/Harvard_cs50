# -*- coding: utf-8 -*-
# PN: NLTP tutorial (Scikit-Learn incorporation), Created Jun. 2017
# Ver: 1.0
# Link: 
# https://pythonprogramming.net/sklearn-scikit-learn-nltk-tutorial/
# --------------------------------------------------- libs import
import nltk
import random	# shuffle DB
from nltk.corpus import movie_reviews
import pickle
# --------------------------------------------------- program

## -- Create to training --
documents = []
for category in movie_reviews.categories():
	for fileid in movie_reviews.fileids(category):
		documents.append((list(movie_reviews.words(fileid)), category))

random.shuffle(documents)
# print(documents[1])

all_words = []
# -- Ignore higher-lower-case problems --
for w in movie_reviews.words():
	all_words.append(w.lower())

## -- Calculate frequency --
all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(15))
## -- Calculate freq of specific word --
# print(all_words["stupid"])

# pick most frequent 3000 words in movie_reviews
word_features = list(all_words.keys())[:3000]

def find_features(document):
	words = set(document)
	features = {}
	for w in word_features:
		features[w] = (w in words)	# if one of top 3000 word_features in document set, return TRUE
	return features
# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev), category) for (rev, category) in documents]
print(featuresets[0])

training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# posterior = prior occurences * likelihood / evidence

# # -- Load classifier from nltk DB --
# classifier = nltk.NaiveBayesClassifier.train(training_set)

# # -- Load classifier from pickle file --
# classifier_f = open("naivebayes.pickle", "rb")
# classifier = pickle.load(classifier_f)
# classifier_f.close()

# print("Naive Bayes Algo accuracy: ", (nltk.classify.accuracy(classifier, testing_set))*100)
# classifier.show_most_informative_features(15)

## -- Create pickle file to save classifier --
# save_classifier = open("naivebayes.pickle", "wb")
# pickle.dump(classifier, save_classifier)
# save_classifier.close()