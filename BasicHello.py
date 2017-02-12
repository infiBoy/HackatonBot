#Very simple logic
import  twitter
import os ,re ,random ,json
import tweepy, time
import credential
#Do the credential

#Twitter credentials
CONSUMER_KEY = credential.CONSUMER_KEY
CONSUMER_SECRET = credential.CONSUMER_SECRET
ACCESS_KEY = credential.ACCESS_KEY
ACCESS_SECRET = credential.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#-3 options:
#post tweets with gifs...
while True:
    try:
        case_int = random.randint(1,1)
        #case_int=2
        if (case_int ==1):
            status = "with cred" +str(random.randint(1,100))
            print status
            api.update_status(status)

        time.sleep(10000)
    except:
        pass

print "hi)))"