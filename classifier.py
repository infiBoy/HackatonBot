import random
from textblob.classifiers import NaiveBayesClassifier
import cPickle as pickle
import os.path

class classifier :
    def __init__(self, fileName):
        twitts = self.createDataFromFile(fileName)
        self.cl = self.learnAndSave(twitts)

    def createDataFromFile(self, fileName):
        twitts = [];

        with open(fileName) as f:
            input = f.readlines()
            for twitt in input :
                twitts.append((twitt.split("|||||")[0], twitt.split("|||||")[1]))
            return twitts

    def learnAndSave(self, twitts) :
        if(os.path.isfile('trainedBrain.pkl') and self.cl == None) :
            with open('trainedBrain.pkl', 'rb') as input:
                self.cl = pickle.load(input)

        random.seed(1)

        random.shuffle(twitts)
        train, test = twitts[0:twitts.__len__() * 0.7], twitts[twitts.__len__() * 0.7 + 1:twitts.__len__()]

        if(self.cl == None) :
            self.cl = NaiveBayesClassifier(train)
        else :
            self.cl.update(train)

        with open('trainedBrain.pkl', 'wb') as output:
            pickle.dump(self.cl, output, pickle.HIGHEST_PROTOCOL)

    def classify(self, twitt):
        return self.cl.classify(twitt)