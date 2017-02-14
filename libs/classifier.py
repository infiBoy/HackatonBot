import random
from textblob.classifiers import NaiveBayesClassifier
import cPickle as pickle
import os.path

def createDataFromFile(fileName):
    twitts = [];

    with open(fileName) as f:
        input = f.readlines()
        for twitt in input :
            twitts.append((twitt.split("|||")[0], twitt.split("|||")[1]))
        return twitts

def learnAndSave(twitts) :
    cl = None

    with open(os.getcwd() +'/../libs/trainedBrain.pkl', 'rb') as input:
        cl = pickle.load(input)

    if(cl == None) :
        print "going to train " + str(twitts.__len__())
        cl = NaiveBayesClassifier(twitts)
        print "finish training"
    else :
        cl.update(twitts)

    with open(os.getcwd() +'/../libs/trainedBrain.pkl', 'wb') as output:
        pickle.dump(cl, output, pickle.HIGHEST_PROTOCOL)

    return cl

def openObject() :
    with open(os.getcwd() +'/../libs/trainedBrain.pkl', 'rb') as input:
        return pickle.load(input)

def classify(cl, twitt) :
    return cl.classify(twitt)

if __name__ == '__main__':
    pro = createDataFromFile("libs/Prosenteces.json")
    neg = createDataFromFile("libs/senteces.json")
    random.seed(1)
    random.shuffle(pro)
    random.shuffle(neg)
    cl = learnAndSave(pro[:100] + neg[:100])
    cl.show_informative_features()
    print cl.accuracy(pro[101:120] + neg[101:120])