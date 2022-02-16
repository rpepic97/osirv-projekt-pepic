import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def normalize(intensity, original_min, original_max):
    ps = intensity
    a = 0
    b = 255
    c = original_min
    d = original_max
    pn = ((ps - c) * ((b - a) / (d - c))) + a
    return pn


image = cv.imread("test.jpg")
image = cv.cvtColor(image, cv.COLOR_BGR2RGB)

plt.figure()
plt.imshow(image)
plt.show()

plt.figure()
plt.hist(image.ravel(),255,[0,255])
plt.show()

R = image[:, :, 0]
G = image[:, :, 1]
B = image[:, :, 2]

#Crveni kanal
rMin = np.amin(R)
rMax = np.amax(R)
for i in range(R.shape[0]):
    for j in range(R.shape[1]):
        R[i, j] = normalize(R[i, j], rMin, rMax)

#Zeleni kanal
gMin = np.amin(G)
gMax = np.amax(G)
for i in range(G.shape[0]):
    for j in range(G.shape[1]):
        G[i, j] = normalize(G[i, j], gMin, gMax)

#Plavi kanal
bMin = np.amin(B)
bMax = np.amax(B)
for i in range(B.shape[0]):
    for j in range(B.shape[1]):
        B[i, j] = normalize(B[i, j], bMin, bMax)


result = cv.merge([R, G, B])

plt.imshow(result)
plt.show()

plt.figure()
plt.hist(result.ravel(),256,[0,256])
plt.show()