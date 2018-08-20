import os
from io import BytesIO
import tarfile
import tempfile
from six.moves import urllib

from matplotlib import gridspec
from matplotlib import pyplot as plt

from datetime import datetime
from datetime import timedelta

import numpy as np
import cv2
import time

print('opening webcam')

#image_url = IMAGE_URL or _SAMPLE_URL % SAMPLE_IMAGE
#run_visualization(image_url)

# initiate camera
# (use stream later)
cap = cv2.VideoCapture(0)
showColor = False

capture_duration = 10
w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT);
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('myvid.mp4',fourcc, 15.0, (int(w),int(h)))

start_time = time.time()
while(int(time.time() - start_time) < capture_duration):
        ret, frame = cap.read()
        if ret:
            print("Shape of Frame is:",frame.shape)
            out.write(frame)
            cv2.imshow('Video Stream', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
cap.release()
out.release()
cv2.destroyAllWindows()
# while(True):
#     # capture frame by frame
#
#
#     start_time = datetime.now()
#     ret, frame = cap.read()
#
#     # our operations on the frame come here
#     resized_im, seg_map = MODEL.run(frame)
#     filter_image = resized_im.copy()
#
#     filter_image[np.where( seg_map != 1 )] = 0
#
#     dt = datetime.now() - start_time
#     fps = 1 / (dt.seconds + dt.microseconds / 1000000.0)
#
#     print('(%s) - %f ' % (seg_map.shape, fps))
#
#     if not showColor:
#         #cv2.imshow('Camera', label_to_color_image(seg_map).astype(np.uint8))
#         cv2.imshow('Camera', filter_image)
#     else:
#         cv2.imshow('Camera', cv2.addWeighted(resized_im, 0.7, label_to_color_image(seg_map).astype(np.uint8), 0.3, 0.0))
#
#
#
#     getkey = cv2.waitKey(1)
#     if getkey & 0xFF == ord('q'):
#         break
#     elif getkey & 0xFF == ord('s'):
#         showColor = not showColor
#
# cap.release()
# cv2.destroyAllWindows()
# string_video = '/Users/harshak/projects/videomob/src/examplevideo.mp4'
# string_video2 = '/Users/harshak/projects/videomob/src/airhorse.avi.mov'
# cap = cv2.VideoCapture(string_video2)
#
# fps_arr = []
#
# while(cap.isOpened()):
#     start_time = datetime.now()
#     ret, frame = cap.read()
#
#
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#     #resized_im, seg_map = MODEL.run(frame)
#
#     dt = datetime.now() - start_time
#     fps = 1 / (dt.seconds + dt.microseconds / 1000000.0)
#
#     print(fps)
#     fps_arr.append(fps)
#
#
#     cv2.imshow('frame',gray)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#
# max_value = max(fps_arr)
# min_value = min(fps_arr)
# avg_value = sum(fps_arr)/len(fps_arr)
#
# print("Max_Value" + max_value)
# print("Min_Value" + min_value)
# print("Avg_Value" + avg_value)
# cap.release()
# cv2.destroyAllWindows()
