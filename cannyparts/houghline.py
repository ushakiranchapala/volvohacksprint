import numpy as np
import matplotlib.pyplot as plt
import cv2

from skimage import data, color
from skimage.transform import hough_circle, hough_circle_peaks
from skimage.feature import canny
from skimage.draw import circle_perimeter
from skimage.util import img_as_ubyte
from skimage import io
from skimage.io import imread
image = io.imread(r'''C:\Users\ushakiran\Documents\viil\cannyedge\uprollround.png''')

#im = io.imread(r'''C:\Users\ushakiran\Documents\viil\cannyedge\uprollround.png''')
#im = cv2.imread(r'''C:\Users\ushakiran\Documents\viil\cannyedge\uprollround.png''')
#im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
#image = greycomatrix(im, [1], [0], 256, symmetric=False, normed=True)

# Load picture and detect edges
#image = img_as_ubyte(data.coins()[160:230, 70:270])
#image = img_as_ubyte(cv2.imread('uprollround.png')[160:230, 70:270])
edges = canny(image, sigma=3, low_threshold=10, high_threshold=50)


# Detect two radii
hough_radii = np.arange(20, 35, 2)
hough_res = hough_circle(edges, hough_radii)

# Select the most prominent 5 circles
accums, cx, cy, radii = hough_circle_peaks(hough_res, hough_radii,
                                           total_num_peaks=3)

# Draw them
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 4))
image = color.gray2rgb(image)
for center_y, center_x, radius in zip(cy, cx, radii):
    circy, circx = circle_perimeter(center_y, center_x, radius)
    image[circy, circx] = (220, 20, 20)

ax.imshow(image, cmap=plt.cm.gray)
plt.show()
