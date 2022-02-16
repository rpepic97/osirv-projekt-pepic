import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

image = cv.imread("test3.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

#Originalna slika
plt.figure()
plt.imshow(image)
plt.show()

#Histogram originalne slike
plt.figure()
plt.hist(image.ravel(),255,[0,255])
plt.show()


def equalize_histogram(image):

    ycrcb_img = cv.cvtColor(image, cv.COLOR_RGB2YCrCb)

    ycrcb_img[:, :, 0] = cv.equalizeHist(ycrcb_img[:, :, 0])

    equalized_img = cv.cvtColor(ycrcb_img, cv.COLOR_YCrCb2RGB)

    return equalized_img

image = equalize_histogram(image)

#Ispravljena slika
plt.figure()
plt.imshow(image)
plt.show()

#Histogram ispravljene slike
plt.figure()
plt.hist(image.ravel(),255,[0,255])
plt.show()

cv.waitKey(0)
