#!/usr/bin/env python
# -*- coding: utf-8 -*-


from TwitterSearch import *


fileName ="Pro"


import credential
try:
    while True:
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.set_keywords(['israel', 'crime']) # let's define all words we would like to have a look for
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
            print tweet['text']
            with open( fileName+ '.json', 'a') as f:

                f.write(tweet['text'].encode('ascii', 'ignore').decode('ascii') + "|||Positive \n") #Changeme for negative

            #print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)