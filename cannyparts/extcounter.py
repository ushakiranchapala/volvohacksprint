import cv2
import numpy as np
import matplotlib.pyplot as plt
 
# read and scale down image
img = cv2.pyrDown(cv2.imread('mask72.jpg', cv2.IMREAD_UNCHANGED))
elippic = img.copy()
elipic = img.copy()

# threshold image
ret, threshed_img = cv2.threshold(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY),
                127, 255, cv2.THRESH_BINARY)
# find contours and get the external one
image, contours, hier = cv2.findContours(threshed_img, cv2.RETR_EXTERNAL,
                cv2.CHAIN_APPROX_SIMPLE)
#contours = sorted(contours, key = cv2.contourArea, reverse = True)[:5]
contour_sizes = [(cv2.contourArea(contour), contour) for contour in contours]
biggest_contour = max(contour_sizes, key=lambda x: x[0])[1]
#counter center
s = cv2.HuMoments(cv2.moments(biggest_contour)).flatten()
M = cv2.moments(biggest_contour)
cX = int(M["m10"] / M["m00"])
cY = int(M["m01"] / M["m00"])


cv2.drawContours(img, [biggest_contour], -1, (0, 255, 0), 2)
cv2.circle(elippic, (cX, cY), 7, (45, 90, 7), -1)
cv2.imshow("center",elippic)




mask = np.zeros(img.shape, np.uint8)
cv2.drawContours(mask, [biggest_contour], -1, 255, -1)
cv2.imshow("bigcontours", mask)
#ret, threshed_img = cv2.threshold(cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY),
 #               127, 255, cv2.THRESH_BINARY)

#res = cv2.bitwise_and(img,img,mask = mask)


gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
ellipse = cv2.fitEllipse(biggest_contour)
cv2.ellipse(elipic,ellipse,(0,255,0),3)
cv2.imshow("elispsecounter",elipic)


########

"""circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)
 
# ensure at least some circles were found
output = gray.copy()
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype("int")
 
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv2.circle(output, (x, y), r, (0, 255, 0), 4)
		cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
 
	# show the output image
cv2.imshow("output", output)"""


#####



for c in contours:
    # get the bounding rect
    x, y, w, h = cv2.boundingRect(c)
    # draw a green rectangle to visualize the bounding rect
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
 
    # get the min area rect
    rect = cv2.minAreaRect(c)
    
    box = cv2.boxPoints(rect)
    # convert all coordinates floating point values to int
    box = np.int0(box)
    # draw a red 'nghien' rectangle
    cv2.drawContours(img, [box], 0, (0, 0, 255))
    
 
    # finally, get the min enclosing circle
    (x, y), radius = cv2.minEnclosingCircle(c)
    # convert all values to int
    center = (int(x), int(y))
    radius = int(radius)
    # and draw the circle in blue
    img = cv2.circle(img, center, radius, (255, 0, 0), 2)
 
print(len(contours))
cv2.drawContours(img, contours, -1, (255, 255, 0), 1)
 
#cv2.imshow("contours", img)
 

