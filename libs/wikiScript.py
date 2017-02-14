import re
import wikipedia

  

def wikicomment(subject):
    data = wikipedia.page("israel")
    try:
        newContent = data.content.split("== Background ==")
        newContent = newContent[1][:130]
        print newContent
    except:
        print "No wikipedia Background"

