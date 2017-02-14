#Very simple logic
import os ,re ,random ,json , sys
import tweepy, time
import credential
import glob


#Twitter credentials
CONSUMER_KEY = credential.CONSUMER_KEY
CONSUMER_SECRET = credential.CONSUMER_SECRET
ACCESS_KEY = credential.ACCESS_KEY
ACCESS_SECRET = credential.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Get the list of all the packages...
pkgfiles = glob.glob(os.getcwd() + "/skills/*.py")[:-1]  # exlude the __init__ python file
skills = []
for pkg in pkgfiles:
    skills.append(pkg.split("/")[-1].split(".")[0])
print "loaded current skills:" + str(skills)

while True:
    try:
        #Now Dynamic load and execute each package randomly
        #Todo: make it more elegant... Try to avoid loading multiplyig  modules..(altought python handle it ok)
        name = "skills." + random.choice(skills) #Choose random skill
        mod = __import__(name, fromlist=[''])
        mod.run(api) #run the skill.


        #Now go to sleep.(15-20 minutes..)
        time.sleep(random.randint(1500, 2000))


    except: #todo:handle the error better
        e = sys.exc_info()[0]
        print str(e)
        pass