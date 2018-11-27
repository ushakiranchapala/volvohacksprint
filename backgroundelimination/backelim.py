import numpy as np
import cv2
import os

cap = cv2.VideoCapture("sideroll2.mp4")

try:
    if not os.path.exists('data'):
        os.makedirs('data')
except OSError:
    print ('Error: Creating directory of data')
 
subtractor = cv2.createBackgroundSubtractorMOG2(history=20, varThreshold=25, detectShadows=True)

currentFrame = 0

while True:
    _, frame = cap.read()
 
    mask = subtractor.apply(frame)

    # Saves image of the current frame in jpg file
    name = './data/mask' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, mask)
    #save frrame
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)
    # To stop duplicate images
    currentFrame += 1

    
 
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
 
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
