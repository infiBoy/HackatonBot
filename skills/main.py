#Very simple logic
import os ,re ,random ,json , sys
import tweepy, time
import credential6 as credentail
import glob


#Twitter credentials
CONSUMER_KEY = credentail.CONSUMER_KEY
CONSUMER_SECRET = credentail.CONSUMER_SECRET
ACCESS_KEY = credentail.ACCESS_KEY
ACCESS_SECRET = credentail.ACCESS_SECRET
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

#Get the list of all the packages...
pkgfiles = glob.glob(os.getcwd() + "/*.py")[:-1]  # exlude the __init__ python file
skills = []
for pkg in pkgfiles:
    if(pkg != "/home/guy/PycharmProjects/HackatonBotGit/skills/main.py") :
        skills.append(pkg.split("/")[-1].split(".")[0])
print "loaded current skills:" + str(skills)

while True:
    try:
        #Now Dynamic load and execute each package randomly
        #Todo: make it more elegant... Try to avoid loading multiplyig  modules..(altought python handle it ok)
        name = "skills." + random.choice(skills) #Choose random skill
        mod = __import__(name, fromlist=[''])
        print name
        mod.run(api) #run the skill.


        #Now go to sleep.(5-10 minutes..)
        time.sleep(random.randint(120, 121))


    except: #todo:handle the error better
        e = sys.exc_info()[0]
        print str(e)
        pass