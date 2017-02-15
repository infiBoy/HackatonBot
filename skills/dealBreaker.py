import tweepy
import random
import credential6 as credential
import os
#Do the credential
import libs.classifier as classifier
import libs.FaceRecognition as fr
import libs.searchProfiles as sp
import libs.utilities as util
from PIL import Image as image
from SimpleCV import *
import libs.utilities as utilities

def generate_pic_rockets(person_path='person.jpg'):

    img = image.open('rockets.jpg', 'r')
    img2 = image.open(person_path,'r')


    img_w, img_h = img.size
    print img.size


    img_w1, img_h2 = img2.size


    new_width  = 60
    new_height = new_width * img_h2/ img_w1

    new_height = 60
    new_width  = new_height * img_w1 / img_h2

    img_h2 = new_height
    img_w1 = new_width

    img2 = img2.resize((new_width, new_height), image.ANTIALIAS)


    background = image.new('RGBA', (img_w, img_h), (255, 255, 255, 255))
    bg_w, bg_h = background.size

    offset = ((bg_w - img_w) / 2, (bg_h - img_h) / 2)

    offsetx = 560
    offsety =140

    box = (offsetx,offsety,img_w1+offsetx,img_h2+offsety)

    print box
    region = img.crop(box)

    background.paste(img)
    background.paste(img2,box=box)

    background.save('out.png')

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
            util.download_file(sp.sechProfile(BotCred, screen_name1))
            img = Image("/home/guy/PycharmProjects/HackatonBotGit/skills/curr.gif")
            print screen_name1
            img.save("person.jpg")
            generate_pic_rockets()
            picture_path = os.getcwd() + "/out.png"
            status ="Don't be mistaken. By posting that, You SUPPORT TERROR!"
            BotCred.update_with_media(picture_path, (status + " @{}").format( screen_name1))
            break




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


