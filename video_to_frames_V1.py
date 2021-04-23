from cv2 import cv2
import numpy as np
import os


image = cv2.imread("white.png") 
image = cv2.resize(image,(640,480))
blackimage = cv2.imread("blackimage.jpg")
blackimage = cv2.resize(blackimage,(640,480))
video = cv2.VideoCapture('vids/IMG_5048.MOV')



path = 'C:/Users/Aldrin Gwapo/Documents/Thesis 1/processed_frames' 
count = 0
ret = 1
while ret:  #CTRL C at console/terminal to force stop loop
  
    ret, frame = video.read()

    frame = cv2.resize(frame,(640,480))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    l_green = np.array([46,34, 27]) 
    u_green = np.array([82, 255, 255])
     

  
    mask = cv2.inRange(hsv, l_green, u_green)
    edges = cv2.Canny(mask,150,200) 
    res = cv2.bitwise_and(frame, frame, mask = mask)
    contours,_ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    f = frame - res 
    f = np.where(f == 0, blackimage, image)
    cv2.drawContours(f,contours, -1, (255,255,255), 3) 

    count+=1
    cv2.imwrite( os.path.join(path , "ALframe"+str(count)+".jpg"), f) 

    #CTRL C at console/terminal to force stop loop

    #cv2.imshow("video", f)           #comment out to view continous frames
    #cv2.imshow("edges", edges)


    #k=cv2.waitKey(1) 
    #if cv2.waitKey(25) == 27: #comment out if viewing frames and press escape to stop. 
    #    break 
  
#video.release() 
#cv2.destroyAllWindows() 