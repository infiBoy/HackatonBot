import random
#from nltk.corpus import movie_reviews
from textblob.classifiers import NaiveBayesClassifier
import cPickle as pickle
import os.path

cl = None
if(os.path.isfile('trainedBrain.pkl')) :
    with open('trainedBrain.pkl', 'rb') as input:
        cl = pickle.load(input)

random.seed(1)

# Grab some movie review data
#reviews = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#             for fileid in movie_reviews.fileids(category)]
#random.shuffle(reviews)
#train, test = reviews[0:1000], reviews[1001:1400]

twitts = [];

with open("twitts.txt") as f:
    input = f.readlines()
    for twitt in input :
         twitts.append((twitt.split("|||||")[0], twitt.split("|||||")[1]))

random.shuffle(twitts)
train, test = twitts[0:twitts.__len__() * 0.7], twitts[twitts.__len__() * 0.7 + 1:twitts.__len__()]


if(cl == None) :
    cl = NaiveBayesClassifier(train)
else :
    cl.update(train)

# Compute accuracy
accuracy = cl.accuracy(test)
print("Accuracy: {0}".format(accuracy))

# Show 5 most informative features
cl.show_informative_features(5)

with open('trainedBrain.pkl', 'wb') as output:
    pickle.dump(cl, output, pickle.HIGHEST_PROTOCOL)
