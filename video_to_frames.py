from cv2 import cv2
import numpy as np
import os


image = cv2.imread("blue.jpg") 
image = cv2.resize(image,(640,480))
blackimage = cv2.imread("blackimage.jpg")
blackimage = cv2.resize(blackimage,(640,480))
vidcap = cv2.VideoCapture('IMG_4532.MOV')


path = 'C:/Users/Aldrin Gwapo/Documents/Thesis 1/processed_frames'

def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,frame = vidcap.read()
    if hasFrames:
        frame = cv2.resize(frame,(640,480))
        blur = cv2.GaussianBlur(frame,(9,9),0)

    
    #grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #contours,_ = cv2.findContours(edges, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.drawContours(frame,contours, -1, (0,255,0), 3)
        hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
        l_green = np.array([47,84, 49]) 
        u_green = np.array([151, 255, 255]) 

  
        mask = cv2.inRange(hsv, l_green, u_green)
        edges = cv2.Canny(mask,150,200) 
        res = cv2.bitwise_and(frame, frame, mask = mask)
        contours,_ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    
  
        f = frame - res 
        f = np.where(f == 0, blackimage, image) 
        cv2.drawContours(f,contours, -1, (255,255,255), 3) 
        

        cv2.imwrite( os.path.join(path , "TEST"+str(count)+".jpg"), f)     # save frame as JPG file

    return hasFrames
sec = 0
frameRate =2 #//it will capture image each 15 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)