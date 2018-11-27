import numpy as np
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
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

    """# Saves image of the current frame in jpg file
    name = './data/frame' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, mask)"""

    # To stop duplicate images
    currentFrame += 1
    
    
    img = cv2.imread(frame)
    elipic = img.copy()
    image, contours, hier = cv2.findContours(mask, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
    contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
    biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
    ellipse = cv2.fitEllipse(biggest_contour)
    print(ellipse.size.height())
    cv2.ellipse(elipic,ellipse,(206, 0, 209),2)
    cv2.imshow("elispsecounter",elipic)
    
    


    
 
    cv2.imshow("Frame", frame)
    cv2.imshow("mask", mask)
    # To stop duplicate images
    currentFrame += 1
 
    key = cv2.waitKey(30)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()
