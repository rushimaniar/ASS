#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base

# cap = cv2.VideoCapture('data/crowd.mp4')

# cap.set(cv2.CAP_PROP_POS_FRAMES, 250)

# ret, frame = cap.read()

# frame = darknet.MarshalOCV2Yolo(frame)

# print(cap.get(cv2.CAP_PROP_FPS))

# cv2.imwrite("lol.jpg", frame)

vid = base.VideoReader('data/crowd.mp4',0.5)
frame = vid.next()
cv2.imshow("LOL", frame)
cv2.waitKey(0)