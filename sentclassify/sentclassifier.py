import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import pickle
import csv

class sentClassifier:
    # creates a classifier from the movie review corpus
    def __init__(self):
        negids = movie_reviews.fileids('neg')
        posids = movie_reviews.fileids('pos')
        negfeats = [(self.word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in movie_reviews.fileids('neg')]
        posfeats = [(self.word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in movie_reviews.fileids('pos')]
        trainfeats = negfeats + posfeats
        self.classifier = NaiveBayesClassifier.train(trainfeats)
    
    # classifies a string    
    def __call__(self, feedbackString):
        return self.classifier.classify(self.word_feats(feedbackString.split()))
    
    def showMostInformativeFeatures(self, n):
        self.classifier.show_most_informative_features(n)
    
    # extracts features from a list of words
    def word_feats(self, words):
        return dict([(word, True) for word in words])
    
    # saves the classifier to a binary file    
    def saveClassifier(self, filename):
        f = open(filename, 'wb')
        pickle.dump(self, f)
        f.close()
        
    def loadClassifier(self, filename):
        f = open('classifier.pickle', 'rb')
        self = pickle.load(f)
        f.close()
