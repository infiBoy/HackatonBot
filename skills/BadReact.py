import  tweepy
import random
import credential3 as credential
#Do the credential
import libs.classifier as classifier
import libs.utilities as utilities

#Here is the running skill
def run(BotCred):
    #search tweet
    #check if positive
    #make like

    curr_keyword= random.choice(["FreeGaza","palestine","west bank","apparteid","BDS"])
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
        print type(output)


        if (output=="Negative \n"):
            print "Negative"
            status = utilities.rand_line("./NegativeRect.txt")
            link = utilities.rand_line("./links.txt")
            print screen_name1
            BotCred.update_status((status+"  @{} "+str(random.randint(1,75))).format(link,screen_name1), in_reply_to_status_id=id)
            break

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