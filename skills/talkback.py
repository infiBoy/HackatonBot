import  tweepy
import random
import credential
#Do the credential


#Here is the running skill
def run(BotCred):
    #Get a bad tweet

    curr_keyword= random.choice(["freegaza","westbank","isrhell","israel","humanRights"])
    results = BotCred.search(q=curr_keyword, )
    for result in results:

        text = result._json["text"]
        #If the classifier not like it ....
        id = result._json["id"]
        BotCred.retweet(id)

        BotCred.update_status( "Fake News", in_reply_to_status_id=id)

        print result


    #generate tweet against..
    print "Done talk to bad tweet"
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