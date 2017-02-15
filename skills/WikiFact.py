import re
import wikipedia
import  tweepy
import random
import credential3
import libs.classifier as classifier

def wikicomment(subject):
    data = wikipedia.page("israel")
    try:
        newContent = data.content.split("== Background ==")
        newContent = newContent[1][:130]
        print newContent
    except:
        print "No wikipedia Background"

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
            data = wikipedia.page(curr_keyword)
            try:
                newContent = data.content.split("== Background ==")
                newContent = newContent[1][:100]
                print newContent
                print screen_name1
                BotCred.update_status(("Hey @{} , Do you know that " + data).format(screen_name1), in_reply_to_status_id=id)
                break
            except:
                print "No wikipedia Background"

    #BotCred.update_status("success"+str(random.randint(1,100)))
    pass




#To support debugging a unique skill
if __name__ == '__main__':
    #Twitter credentials
    CONSUMER_KEY = credential3.CONSUMER_KEY
    CONSUMER_SECRET = credential3.CONSUMER_SECRET
    ACCESS_KEY = credential3.ACCESS_KEY
    ACCESS_SECRET = credential3.ACCESS_SECRET
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    BotCred = tweepy.API(auth)
    run(BotCred)