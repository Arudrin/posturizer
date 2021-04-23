from cv2 import cv2
import numpy as np
import os


image = cv2.imread("white.png") 
image = cv2.resize(image,(640,480))
blackimage = cv2.imread("blackimage.jpg")
blackimage = cv2.resize(blackimage,(640,480))
vidcap = cv2.VideoCapture('vids/IMG_5048.MOV')
subtractor = cv2.createBackgroundSubtractorMOG2(history=12)


path = 'C:/Users/Aldrin Gwapo/Documents/Thesis 1/processed_frames'

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,frame = vidcap.read()
    if hasFrames:
        frame = cv2.resize(frame,(640,480))
        #blur = cv2.GaussianBlur(frame,(13,13),0)
        #grey = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

        cv2.imwrite( os.path.join(path , "TEST"+str(count)+".jpg"), frame)

    return hasFrames


sec = 0
frameRate =10 #//it will capture image each 15 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)