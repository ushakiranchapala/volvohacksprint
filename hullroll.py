import cv2
import numpy as np
import sys

if __name__ == "__main__":
    if(len(sys.argv)) < 2:
        file_path = "uprollround.png"
    else:
        file_path = sys.argv[1]

    # read image
    src = cv2.imread(file_path, 1)
    
    # show source image
    cv2.imshow("Source", src)

    # convert image to gray scale
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    
    #cv2.imshow("Source",gray)
     
    # blur the image
    blur = cv2.blur(gray, (3, 3))

    #cv2.imshow("source",blur)
    
    # binary thresholding of the image
    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)
    
    # find contours
    im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
            cv2.CHAIN_APPROX_SIMPLE)

    #approximation elipse
    epsilon = 0.01 * cv2.arcLength(contours, True)
    approx = cv2.approxPolyDP(contours, epsilon, True)
    lines = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0, False)
        area = np.abs(cv2.contourArea(contour))
 
        if self.area_min.get() < area < self.area_max.get():
            line_values = cv2.fitLine(approx, cv.CV_DIST_L2, 0, 0.01, 0.01)
            rect = cv2.boundingRect(approx)
            t = math.sqrt((rect[2] ** 2 + rect[3] ** 2) / 2.0)
            lines.append((line_values, t))
            
    
    
    # create hull array for convexHull points
    hull = []
    
    # calculate points for each contour
    for i in range(len(contours)):
        hull.append(cv2.convexHull(contours[i], False))
    
    # create an empty black image
    drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
    
    # draw contours and hull points
    for i in range(len(contours)):
        color_contours = (0, 255, 0) # color for contours
        color = (255, 255, 255) # color for convex hull
        # draw contours
        #cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
        # draw convex hull
        #cv2.drawContours(drawing, hull, i, color, 2, 8)
        cv2.drawContours(drawing, lines, i, color, 2, 8)

    cv2.imshow("Output", drawing)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
