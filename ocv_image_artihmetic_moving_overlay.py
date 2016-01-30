import numpy as np
import cv2 as cv

debug_each_step = False


def ims(img, key, windows_name='dummy'):
    if not debug_each_step:
        return
    cv.destroyWindow(windows_name)
    cv.imshow(windows_name, img)
    k = 0
    while k != ord(key):
        k = cv.waitKey(10)
    cv.destroyWindow(windows_name)

# blue = np.zeros((300,512,3), np.uint8)
# img = cv.imread('messi5.jpg')

# main image
img = cv.imread('messi6.jpg')
img_org = cv.imread('messi6.jpg')
ims(img, 'q', 'img')

# overlay image
ovl = cv.imread('logo.png')
ims(ovl, 'q', 'ovl')

# grab overlay parameters
rows, cols, channels = ovl.shape

pos_ovl_in_image_x = 0
pos_ovl_in_image_y = 0

while True:
    # create ROI (region of image) starting from pos x, y
    roi = img[pos_ovl_in_image_y:rows + pos_ovl_in_image_y,
          pos_ovl_in_image_x:cols + pos_ovl_in_image_x]
    roi_org = img_org[pos_ovl_in_image_y:rows + pos_ovl_in_image_y,
              pos_ovl_in_image_x:cols + pos_ovl_in_image_x]
    ims(roi, 'q', 'roi of img')

    # Now create a mask of logo and create its inverse mask also
    # get overlay grayscale
    ovlgray = cv.cvtColor(ovl, cv.COLOR_BGR2GRAY)
    ims(ovlgray, 'q', 'ovl in gray scale')
    # get bi-level image out of the grayscale
    ret, ovlmask = cv.threshold(ovlgray, 10, 255, cv.THRESH_BINARY)
    ims(ovlmask, 'q', 'mask after threshold cut')
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
    dst_roi = cv.add(roi_bg, ovl_fg)
    ims(dst_roi, 'q', 'roi bg with ovl fg')

    # and put it back on the img
    img[pos_ovl_in_image_y:rows + pos_ovl_in_image_y,
        pos_ovl_in_image_x:cols + pos_ovl_in_image_x] = dst_roi

    ims(img, 'q', 'test result')
    cv.imshow('final result', img)
    k = cv.waitKey(15)  # 1000 msec / 30 fps
    if k==ord('q'):
        break

    # put back the original roi ...
    img[pos_ovl_in_image_y:rows + pos_ovl_in_image_y,
        pos_ovl_in_image_x:cols + pos_ovl_in_image_x] = roi_org

    # and mov the overlay roi further
    pos_ovl_in_image_x += 10
    # print("x [%d], cols[%d]" %(pos_ovl_in_image_x, img.shape[1]))

    # drop 10 pixels down when reaching the end x (cols) if the image
    if True: # pos_ovl_in_image_x // (img.shape[1] - cols):
        pos_ovl_in_image_y += 10
        pos_ovl_in_image_y %= img.shape[0] - rows  # fix the size cuz overlay end y value may be out of bound

    pos_ovl_in_image_x %= img.shape[1] - cols  # fix the size cuz overlay end x value may be out of bound

    ims(img, 'q', 'test after set back roi')
    cv.imshow('final result', img)
    # cv.waitKey(16)
    # if k==ord('q'):
    #     break


cv.destroyAllWindows()
