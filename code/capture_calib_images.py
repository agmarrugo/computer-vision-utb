#! /usr/local/bin/python

import numpy as np
import cv2
import os

path = 'captured/'
try:
    os.mkdir(path)
except:
    print("Already exists.")

cap = cv2.VideoCapture(1)

i = 0
while (True):
    # Capture frame-by-frame
    (ret, frame) = cap.read()

    # Get frame size
    width = cap.get(3)
    height = cap.get(4)
    # print(width, height)

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # # Test if it can do a laplacian filter in a loop
    # lap = cv2.Laplacian(gray, cv2.CV_64F)
    # lap = np.uint8(np.absolute(lap))
    # cv2.imshow(lap, 'Laplacian')

    # Display the resulting frame
    # cv2.imshow('frame', frame)
    # cv2.imshow(frame, 'frame')
    cv2.imshow('frame', gray)
    # cv2.imshow('frame',lap)
    
    # Capture the frame
    if cv2.waitKey(1) & 0XFF == ord('c'):
        cv2.imwrite('captured/image{:02d}.png'.format(i), gray)
        i += 1
    
    # The & 0XFF is a so-called mask.
    if cv2.waitKey(1) & 0XFF == ord('q'):
        break

# cv2.imwrite('ball.png', frame)

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()
