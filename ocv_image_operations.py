import cv2
import numpy as np

img = cv2.imread('roi.jpg')

b,g,r = cv2.split(img)

cv2.imshow('iimmgg', cv2.merge((g,r,g)))

while True:
    k = cv2.waitKey(20)
    if k == 27 or k == ord('q'):
        break

cv2.destroyAllWindows()