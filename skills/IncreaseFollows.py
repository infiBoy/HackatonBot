import  tweepy
import random
import credential
#Do the credential


#Here is the running skill
def run(BotCred):
    print "post"

    curr_keyword = random.choice(["train followback","Followback"])

    results = BotCred.search(q=curr_keyword, )
    for result in results:
        # Get Some details of the user that tweet with the keyword
        # it might help to do the statistics after that
        # Maybe later save all the stats to a DB
        # print  json.dumps(result._json)
        print result
        screen_name1 = result._json["user"]["screen_name"]
        BotCred.create_friendship(screen_name1)
        print "success" + screen_name1

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