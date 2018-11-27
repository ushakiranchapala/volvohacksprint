import numpy as np
import cv2
import numpy as np
import os

cap = cv2.VideoCapture("zoombottle1.mp4")

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

    #img = cv2.pyrDown(cv2.imread('uprollround.png', cv2.IMREAD_UNCHANGED))
 
    """# threshold image
    ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)"""
    # find contours and get the external one
    image, contours, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
 
    cv2.drawContours(mask, contours, -1, (255, 255, 0), 1)

    #cv2.imshow("contours", img)

    # Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, mask)

    # To stop duplicate images
    currentFrame += 1

    
 
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
 
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
