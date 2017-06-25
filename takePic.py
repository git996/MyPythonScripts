import cv2
import sys
from datetime import datetime
import logging as log
import datetime as dt
from time import sleep

today = datetime.now()
todaystr = today.strftime("%Y%m%d-%H%M%S")
video_capture = cv2.VideoCapture(0)
anterior = 0
camera_port = 0
ramp_frames = 30
def get_image():
 # read is the easiest way to get a full image out of a VideoCapture object.
 retval, im = video_capture.read()
 return im
 
# Ramp the camera - these frames will be discarded and are only used to allow v4l2
# to adjust light levels, if necessary
for i in range(ramp_frames):
 temp = get_image()
print("Taking image...")
# Take the actual image we want to keep
camera_capture = get_image()

file = "C:/Users/New/Pictures/imagelog/%s.png" %todaystr
print(file)
# A nice feature of the imwrite method is that it will automatically choose the
# correct format based on the file extension you provide. Convenient!
cv2.imwrite(file, camera_capture)
print("\nImage Saved")
video_capture.release()
