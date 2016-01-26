import numpy as np
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # width
cap.set(4, 480)  # height

# Define the codec and create VideoWriter object
# fourcc = cv2.VideoWriter_fourcc(*'x264')
# out = cv2.VideoWriter('output1.avi',fourcc, 20.0, (640,480))
# out = cv2.VideoWriter('output.avi',-1, 20.0, (640,480))

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # frame = cv2.flip(frame,0)

        # write the flipped frame
        # out.write(frame)

        ref101 = cv2.copyMakeBorder(frame, 240, 240, 240, 240, cv2.BORDER_REFLECT101)


        cv2.imshow('frame',ref101)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
# out.release()
cv2.destroyAllWindows()
