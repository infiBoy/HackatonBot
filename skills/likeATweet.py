import  tweepy
import random
import credential
#Do the credential


#Here is the running skill
def run(BotCred):
    #search tweet
    #check if positive
    #make like

    curr_keyword= random.choice(["standwithus","israel","israel defence","LoveIsrael","BestOfIsrael","IDF","FIDF"])
    results = BotCred.search(q=curr_keyword, )
    for result in results:

        text = result._json["text"]
        #If the classifier like it.... Do the retweet


        id = result._json["id"]
        BotCred.retweet(id)
        print result

    print "done"
    #BotCred.update_status("success"+str(random.randint(1,100)))
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