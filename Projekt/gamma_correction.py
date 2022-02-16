import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

image = cv.imread('test2.jpg')
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

plt.plot()
plt.imshow(image)
plt.show()

def adjust_gamma(image, gamma=1):
    invertedGamma = 1.0/gamma
    table = np.array([((i/255)**invertedGamma)*255 for i in np.arange(0, 256)])
    lut_img = cv.LUT(image.astype(np.uint8), table.astype(np.uint8))
    return lut_img

image = adjust_gamma(image, gamma=0.5)
plt.plot()
plt.imshow(image)
plt.show()

image = adjust_gamma(image, gamma=3)
plt.plot()
plt.imshow(image)
plt.show()