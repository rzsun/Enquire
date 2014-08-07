import nltk.classify.util
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import movie_reviews
import os.path
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
nltk.data.path.append(os.path.join(BASE_DIR, 'nltk_data/'))
import pickle

class sentClassifier:
    # creates a classifier from the movie review corpus
    def __init__(self, load = False, loadFile = ""):
        if(load):
            self.loadClassifier(loadFile)
        else:
            negids = movie_reviews.fileids('neg')
            posids = movie_reviews.fileids('pos')
            negfeats = [(self.word_feats(movie_reviews.words(fileids=[f])), 'neg') for f in movie_reviews.fileids('neg')]
            posfeats = [(self.word_feats(movie_reviews.words(fileids=[f])), 'pos') for f in movie_reviews.fileids('pos')]
            trainfeats = negfeats + posfeats
            self.classifier = NaiveBayesClassifier.train(trainfeats)
    
    # classifies a string    
    def __call__(self, tweetString):
        return self.classifier.classify(self.word_feats(tweetString.split()))
    
    def showMostInformativeFeatures(self, n):
        self.classifier.show_most_informative_features(n)
    
    # extracts features from a list of words
    def word_feats(self, words):
        return dict([(word.lower(), True) for word in words])
    
    # saves the classifier to a binary file    
    def saveClassifier(self, filename):
        f = open(filename, 'wb')
        pickle.dump(self.classifier, f)
        f.close()
        
    def loadClassifier(self, filename):
        f = open(filename, 'rb')
        self.classifier = pickle.load(f)
        f.close()
