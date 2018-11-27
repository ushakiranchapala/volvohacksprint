import numpy
import cv2 
 
# read and downscale image
img = cv2.pyrDown(cv2.imread('uprollround.png', cv2.IMREAD_UNCHANGED))
# threshold image
# this step is neccessary when you work with contours

ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                        127, 255, cv2.THRESH_BINARY)
# find contours in image
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)
 
for cnt in contours:
    # calculate epsilon base on contour's perimeter
    # contour's perimeter is returned by cv2.arcLength
    epsilon = 0.01 * cv2.arcLength(cnt, True)
    # get approx polygons
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    # draw approx polygons
    cv2.drawContours(img, [approx], -1, (0, 255, 0), 1)
 
    # hull is convex shape as a polygon
    hull = cv2.convexHull(cnt)
    cv2.drawContours(img, [hull], -1, (0, 0, 255))
 
cv2.imshow('contours', img)
