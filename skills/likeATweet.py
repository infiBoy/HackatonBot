import  tweepy
import random
import credential
#Do the credential
import libs.classifier as classifier


#Here is the running skill
def run(BotCred):
    #search tweet
    #check if positive
    #make like

    curr_keyword= random.choice(["standwithus","israel","israel defence","LoveIsrael","BestOfIsrael","IDF","FIDF"])
    results = BotCred.search(q=curr_keyword, )
    for result in results:

        text = result._json["text"]
        id = result._json["id"]

        screen_name1 = result._json["user"]["screen_name"]

        #If the classifier like it.... Do the retweet
        cl =  classifier.openObject()

        output = classifier.classify(cl,text)
        print text
        print output
        if output=="Positive":
            BotCred.retweet(id)
            print "Retweet for a good tweet"
        else:
            BotCred.update_status("Fake News @{}".format(screen_name1), in_reply_to_status_id=id)
            print  id
            print "nit's negative one.."

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