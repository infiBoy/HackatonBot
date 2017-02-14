
import random
from nltk.corpus import stopwords
import string
import  urllib2
import requests
import os
from lxml import etree
import re

def rand_line(file_path):
    file= open(file_path,'r')
    lines=file.readlines()
    indx= random.randint(1,len(lines)-1)
    curr_line = lines[indx].rstrip('\n')
    return curr_line

def is_it_stop_word(word):
    punctuation = list(string.punctuation)
    for x in stopwords.words('english') + punctuation+["this","is","the"]:
        if x==word:
            return False
    return True


def get_gif_from_tenor(term):
    #term = "michelle you are so sexy"
    term = term.replace(" ","-")
    url =  "https://www.tenor.co/search/"+term+"-gifs"
    #response = urllib2.urlopen(url)
    response =requests.get(url)



    #print response.text
    #htmlparser = etree.HTMLParser()
    #tree = etree.parse(response.text, htmlparser)

    #print tree
    #label = tree.xpath("//*[@id='swapContainer']/div["+str(random.randint(1,4))+"]/a/img")
    #print tree.xpath("//*[@id='view']/div/div[1]/div/div/div[1]/figure["+str(random.randint(1,4))+"]/a/img/@src")
    #print tree.xpath("//*[@id='view']/div/div[3]/div/div/div[1]/figure[1]/a/img")
    #print label
    #print label[0]
    #print label[1]
    #gif_url = label[0].get("src")response.text
    #print label[0].get("src")
    theGif = random.choice( re.findall(r"https:\/\/media.tenor.co\/images\/[(0-9)|(a-f)]*\/raw",response.text ))
    print theGif
    #href = "https://media.tenor.co/images/73e6f82449acae7c5b8f7dde17442fd1/raw"

    return os.getcwd()+download_file(theGif)
    return "null"

def download_file(url):
    local_filename = "curr.gif"
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename



'''
    "//*[@id="view"]/div/div[3]/div/div/div[1]/figure[1]/a/img"
    "//*[@id="view"]/div/div[3]/div/div/div[2]/figure[3]/a/img"
    "//*[@id="view"]/div/div[3]/div/div/div[2]/figure[4]/a/img"
'''