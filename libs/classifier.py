import random
from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import cPickle as pickle
import os.path

def createDataFromFile(fileName):
    twitts = []

    with open(fileName) as f:
        input = f.readlines()
        for twitt in input :
            twitts.append((twitt.split("|||")[0], twitt.split("|||")[1]))
        return twitts

def learnAndSave(twitts) :
    cl = None
    if(os.path.isfile('trainedBrain.pkl')) :
        with open('trainedBrain.pkl', 'rb') as input:
            cl = pickle.load(input)

    if(cl == None) :
        print "going to train " + str(twitts.__len__())
        cl = NaiveBayesClassifier(tweets)
        print "finish training"
    else :
        cl.update(twitts)

    with open('trainedBrain.pkl', 'wb') as output:
        pickle.dump(cl, output, pickle.HIGHEST_PROTOCOL)

    return cl

def openObject() :
    if(os.path.isfile('trainedBrain.pkl')) :
        with open('trainedBrain.pkl', 'rb') as input:
            return pickle.load(input)

def classify(cl, tweet) :
    if(TextBlob(tweet).detect_language() == "en") :
        return cl.classify(tweet)
    else :
        cl.classify(TextBlob(tweet).translate(from_lang="en"))

if __name__ == '__main__':
    tweets = createDataFromFile("clearSenteces.json")
    random.seed(1)
    random.shuffle(tweets)
    cl = learnAndSave(tweets[:int(tweets.__len__() * 0.7)])
    #cl = openObject()
    cl.show_informative_features()
    print cl.accuracy(tweets[int(tweets.__len__() * 0.7 + 1):])