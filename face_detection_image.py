import numpy as np
import cv2

faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

font = cv2.FONT_HERSHEY_SIMPLEX
#make sure you have an umage of at least 470 pix wide and in the same folder as your python code. Rename as needed.
img2=cv2.imread('cat.png', cv2.IMREAD_COLOR)  
alpha = 0.8

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    print(faces)
    if faces == ():
        print("no one home")
        #cv2.putText(img, 'I am here', (50,250), font, 2, (255, 255, 0), 1, cv2.LINE_AA)    # this would show text on the screen instead of an image
        #the numbers 0:470 determine how much of the image shows and how big the window is. Your number cannot be bigger than the number of pixels in the image.
        output = cv2.addWeighted(img2[0:470,0:470,:],alpha,img[0:470,0:470,:],1-alpha,0)  
    else:
        output = img
        
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    
    cv2.imshow('video',output)
    

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
