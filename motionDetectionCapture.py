#!/usr/bin/env python3
import cv2
import time
import os
#iterator for indexing image number
iterator = 0

#directory to save image to
dir  = str(os.getcwd())+"/savedImages"
#check if directory exists
if not os.path.isfile(dir):
    #print('Directory exists')
    os.mkdir("savedImages")

# define a video capture object
vid = cv2.VideoCapture(0)
# Capture the video frame
# by frame
ret, frame = vid.read()
ret, previous = vid.read()

while(True):
    if ret:
        #get the abs difference between last and current frame
        diff = cv2.absdiff(previous,frame)
        #convert BGR image to grayscale
        gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
        #Guassian blur to imporve segmentation
        blurr = cv2.GaussianBlur(gray,(5,5),0)
        #threshold image: consider using Otsu's method in future version
        ret,thresh1 = cv2.threshold(blurr,50,255,cv2.THRESH_BINARY)
        # Erode to make segmentation simpiler
        image1 = cv2.dilate(thresh1,None,iterations = 10)
        #find contours
        contours, _ = cv2.findContours(image1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #cv2.drawContours(frame,contours,-1,(0,255,0),2)

        #display bounding boxes 
        for c in contours:
            x,y,w,h = cv2.boundingRect(c)
            if cv2.contourArea(c) > 10000:
                #increment iterator
                iterator += 1
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                #save files if motion is detected to the directory
                cv2.imwrite(os.path.join(dir , 'smile %s.jpg' % iterator), frame)
        cv2.imshow("Critter Cam",frame)


        #mange images order
        frame = previous
        time.sleep(0.5)
        ret, previous = vid.read()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
