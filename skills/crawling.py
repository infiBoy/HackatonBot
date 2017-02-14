
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import  tweepy
import random
import credential
import json
#Do the credential
#override tweepy.StreamListener to add logic to on_status


StreamingString= 'toujours sur lui au cas'


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        with open( StreamingString+ '.json', 'a') as f:
            print status.text
            f.write(status.text.encode('utf-8').strip())


    def on_direct_message(self, status):
        print "Get data"
        print status
        #api.send_direct_message()
    def on_error(self, status):
        print(status)
        return True


#Here is the running skill
def run(BotCred):
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=BotCred.auth, listener=myStreamListener)
    myStream.userstream()
    myStream.filter(track=[StreamingString], async=True)
    while True:
        pass



#To support debugging a unique skill
if __name__ == '__main__':
    #Twitter credentials
    CONSUMER_KEY = credential.CONSUMER_KEY
    CONSUMER_SECRET = credential.CONSUMER_SECRET
    ACCESS_KEY = credential.ACCESS_KEY
    ACCESS_SECRET = credential.ACCESS_SECRET
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    BotCred = tweepy.API(auth)
    run(BotCred)