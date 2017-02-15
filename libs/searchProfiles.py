import requests
import credential
import  tweepy
import random
import re
import libs.classifier as classifier



def sechProfile(BotCred, name):


        nameProfile = name
        #print text
        print id
        #print nameProfil
        userURL = "https://twitter.com/"+nameProfile
        userHtml = requests.get(userURL)
        print str(userHtml.content)
        #print text
        '''
        with open("staticHTML.txt") as f:
            text = f.readlines()
            '''
        expresion = '(https:\/\/pbs.twimg.com\/profile_images\/'+str(id)+')+([A-Z]|[a-z]|.|\w+)+\w'
        #userURLProfile = re.findall(r'(https:\/\/pbs.twimg.com\/profile_images\/)+([A-Z]|[a-z]|.|\w+)+\w',str(userHtml.content) )
        #userURLProfile = re.findall(r''.format(expresion),str(userHtml.content) )
        #userURLProfile = re.findall(r'(https:\/\/pbs.twimg.com\/profile_images\/'')+([A-Z]|[a-z]|.|\w+)+\w',str(userHtml.content) )

        userURLProfile = re.findall(r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&amp;+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',str(userHtml.content) )
        print userURLProfile[70]
        return userURLProfile[70]


if __name__ == '__main__':
    #Twitter credentials
    CONSUMER_KEY = credential.CONSUMER_KEY
    CONSUMER_SECRET = credential.CONSUMER_SECRET
    ACCESS_KEY = credential.ACCESS_KEY
    ACCESS_SECRET = credential.ACCESS_SECRET
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    BotCred = tweepy.API(auth)
    sechProfile(BotCred)
