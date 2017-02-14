import  tweepy
import random
import credential
#Do the credential
import libs.utilities as utilities
import os

import wikipedia


#Here is the running skill
def run(BotCred):


    print "post"
    text = utilities.rand_line("ProSentences.txt")
    randomword =random.choice(text.split(" "))
    testword =utilities.is_it_stop_word(randomword)
    while (testword==False):
        randomword = random.choice(text.split(" "))
        testword = utilities.is_it_stop_word(randomword)

    print randomword

    randomword= random.choice(["Israel","IDF","Good","like","Best","love","support","INYOURFACE"])
    print utilities.get_gif_from_tenor(randomword)

    BotCred.update_with_media("./curr.gif",text)#, in_reply_to_status_id=combined_status.id)

    #search it on gif...


def rand_line(file_path):
    file= open(file_path,'r')
    lines=file.readlines()
    indx= random.randint(1,len(lines)-1)
    curr_line = lines[indx].rstrip('\n')
    return curr_line

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