import  tweepy
import random
import credential2
#Do the credential
import libs.classifier as classifier

#Here is the running skill
def run(BotCred):
    #search tweet
    #check if positive
    #make like

    curr_keyword= random.choice(["standwithus","israel","israel defence","LoveIsrael","BestOfIsrael","IDF","FIDF"])
    results = BotCred.search(q=curr_keyword, )
    cl = classifier.openObject()
    for result in results:

        text = result._json["text"]
        id = result._json["id"]

        screen_name1 = result._json["user"]["screen_name"]

        #If the classifier like it.... Do the retweet

        output = classifier.classify(cl,text)
        print text
        print output
        if output=="Positive\n":
            BotCred.retweet(id)
            BotCred.create_favorite(id)
            print "Retweet for a good tweet"
            return
    #BotCred.update_status("success"+str(random.randint(1,100)))
    pass




#To support debugging a unique skill
if __name__ == '__main__':
    #Twitter credentials
    CONSUMER_KEY = credential2.CONSUMER_KEY
    CONSUMER_SECRET = credential2.CONSUMER_SECRET
    ACCESS_KEY = credential2.ACCESS_KEY
    ACCESS_SECRET = credential2.ACCESS_SECRET
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    BotCred = tweepy.API(auth)
    run(BotCred)