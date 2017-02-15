from SimpleCV import *
import os
def getFace(img) :
    faces = img.findHaarFeatures("/home/guy/PycharmProjects/HackatonBotGit/libs/haarcascade_frontalface_default.xml")
    if faces:
        return faces[0].points
    else :
        return None

if __name__ == '__main__':
    path = os.getcwd() + "/mustafa.jpg"
    image = Image(path)
    getFace(image)