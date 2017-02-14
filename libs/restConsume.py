#!/usr/bin/env python
# -*- coding: utf-8 -*-



import json
from nltk.tokenize import word_tokenize
import re
import operator
from collections import Counter
from nltk.corpus import stopwords
import string
from nltk  import bigrams


#Tomer/ haim -edit me only...
searchTerms = ["israel" ,"love"]
fileName ="Pro"



temp = "nan"
punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation +['#RT','#rt','rt','RT', 'via']  + \
       [temp] + ["#" + temp] + [u'\u2026']


emoticons_str = r"""
    (?:
        [:=;] # Eyes
        [oO\-]? # Nose (optional)
        [D\)\]\(\]/\\OpP] # Mouth
    )"""

regex_str = [

    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-mentions
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs

    #r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    #r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    #r'(?:[\w_]+)',  # other words
    #r'(?:\S)'  # anything else
]

tokens_re = re.compile(r'(' + '|'.join(regex_str) + ')', re.VERBOSE | re.IGNORECASE)
emoticon_re = re.compile(r'^' + emoticons_str + '$', re.VERBOSE | re.IGNORECASE)


def tokenize(s):
    return tokens_re.findall(s)


def preprocess(s, lowercase=False):
    lowercase=True
    #s= s.encode('ascii', 'ignore').decode('ascii') # Shoud remove for hebrew..
    #s = re.sub(r'[^\u3000-\u307F]+', "",s) #remove
    tokens = tokenize(s)
    if lowercase:
        tokens = [token if emoticon_re.search(token) else token.lower() for token in tokens]
    tokens = list(set(tokens)- set(stop))

    return tokens



def proccessTweet(str):
    querywords = str.split()

    resultwords = [word for word in querywords if word.lower() not in (stop or tokens_re)]
    returnstring = ' '.join(resultwords)

    #now remove the regex
    #print returnstring
    for reg_stop in regex_str:
        new_string =re.sub(reg_stop,'', returnstring)
        new_string =re.sub('@.*? ', '', new_string)
    #print new_string


    return new_string

'''
    for word in querywords:
        if word.lower() not in stop:
            print word
'''

from TwitterSearch import *




import credential
try:

    while True:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(searchTerms) # let's define all words we would like to have a look for
        tso.set_language('en') # we want to see German tweets only
        tso.set_include_entities(False) # and don't give us all those entity information

        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(

            consumer_key = credential.CONSUMER_KEY,
            consumer_secret = credential.CONSUMER_SECRET,
            access_token = credential.ACCESS_KEY,
            access_token_secret = credential.ACCESS_SECRET
         )

         # this is where the fun actually starts :)

        for tweet in ts.search_tweets_iterable(tso):
            #print tweet['text']
            #tokens = preprocess(tweet['text'])
            sentecesProcces = proccessTweet(tweet['text'])

            #Save lines with preproccess
            with open(fileName + 'senteces.json', 'a') as f:
                print sentecesProcces
                f.write(sentecesProcces.encode('ascii', 'ignore').decode('ascii') + "|||Positive \n")





except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)

print "dsds"

'''
            #save lines
            with open( fileName+ '.json', 'a') as f:

                f.write(tweet['text'].encode('ascii', 'ignore').decode('ascii') + "|||Positive \n") #Changeme for negative


            #Save the token
            with open(fileName + 'Tokens.json', 'a') as f:
                for tok in tokens:
                    f.write(tok.encode('ascii', 'ignore').decode('ascii')  + " ")
            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
'''