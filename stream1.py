import numpy as np
import cv2
import imutils
from imutils.video import FPS

cap = cv2.VideoCapture('rtsp://admin:gspe12345@192.168.0.26:554/PSIA/streaming/channels/301')
cap.set(cv2.CAP_PROP_FPS, 10)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
fps = cap.get(cv2.CAP_PROP_FPS)
print ("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

while(cap.isOpened()):

    ret, frame = cap.read()
    # frame = imutils.resize(frame, width=640)
    if ret==True:
        # write the flipped frame
        out.write(frame)
        cv2.imshow('frame',frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release everything if job is finished
cap.release()
out.release()
cv2.destroyAllWindows()
