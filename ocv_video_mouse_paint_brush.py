import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

# mouse callback function
def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), 10, (255, 0, 0), -1)

# create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv2.namedWindow('mouse-image')
cv2.setMouseCallback('mouse-image', draw_circle)

while(1):
    cv2.imshow('mouse-image', img)
    if cv2.waitKey(20) & 0xff == ord('q'):
        break
cv2.destroyAllWindows()
