import numpy as np
import cv2 as cv


blue = np.zeros((300,512,3), np.uint8)
img = cv.imread('messi5.jpg')

cv.imshow('b', blue)

k = 0
while k != ord('q'):
    k = cv.waitKey(100)

cv.destroyAllWindows()