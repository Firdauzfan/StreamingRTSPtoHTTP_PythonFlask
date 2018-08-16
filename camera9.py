
import cv2
import imutils

class VideoCamera(object):
    def __init__(self):
        # Using OpenCV to capture from device 0. If you have trouble capturing
        # from a webcam, comment the line below out and use a video file
        # instead.
        self.video = cv2.VideoCapture('rtsp://admin:gspe12345@192.168.0.26:554/PSIA/streaming/channels/901')
        # If you decide to use video.mp4, you must have this file in the folder
        # as the main.py.
        # self.video = cv2.VideoCapture('video.mp4')

    def __del__(self):
        self.video.release()

    def get_frame(self):
        while(self.video.isOpened()):
            success, image = self.video.read()
            image = imutils.resize(image, width=640)
            print(image.shape)
            if success==True:
            # We are using Motion JPEG, but OpenCV defaults to capture raw images,
            # so we must encode it into JPEG in order to correctly display the
            # video stream.
                ret, jpeg = cv2.imencode('.jpg', image)
                return jpeg.tostring()
