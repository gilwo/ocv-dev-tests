import numpy as np
import cv2 as cv


def ims(img, key, windows_name='dummy'):
    cv.destroyAllWindows()
    cv.imshow(windows_name, img)
    k = 0
    while k != ord(key):
        k = cv.waitKey(10)
    cv.destroyAllWindows()

# blue = np.zeros((300,512,3), np.uint8)
# img = cv.imread('messi5.jpg')

# main image
img = cv.imread('messi5.jpg')
ims(img, 'q', 'img')

# overlay image
ovl = cv.imread('logo.png')
ims(ovl, 'q', 'ovl')

# create ROI (region of image) on top left corner at the size of the overlay
rows, cols,channels = ovl.shape
roi = img[0:rows, 0:cols]
ims(roi, 'q', 'roi of img')

# Now create a mask of logo and create its inverse mask also
# get overlay grayscale
ovlgray = cv.cvtColor(ovl,cv.COLOR_BGR2GRAY)
ims(ovlgray, 'q', 'ovl in grayscale')
# get bi-level image out of the grayscale
ret, ovlmask = cv.threshold(ovlgray, 10, 255, cv.THRESH_BINARY)
ims(ovlmask, 'q', 'mask after thresholding')
# invert and get the actual overlay mask
ovlmask_inv = cv.bitwise_not(ovlmask)
ims(ovlmask_inv, 'q', 'inverted mask')

# Now black-out the area of overlay in ROI
roi_bg = cv.bitwise_and(roi, roi, mask=ovlmask_inv)
ims(roi_bg, 'q', 'roi bitwise with inverted mask')

# Take only region of logo from logo image.
ovl_fg = cv.bitwise_and(ovl, ovl, mask=ovlmask)
ims(ovl_fg, 'q', 'overlay bitwise with mask')


# Put overlay in ROI and modify the main image
dst = cv.add(roi_bg, ovl_fg)
ims(dst, 'q', 'roi bg with ovl fg')

img[0:rows, 0:cols] = dst

ims(img, 'q', 'final result')


