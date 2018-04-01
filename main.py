#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet

cap = cv2.VideoCapture('data/crowd.mp4')

cap.set(cv2.CAP_PROP_POS_FRAMES, 250)

ret, frame = cap.read()

frame = darknet.MarshalOCV2Yolo(frame)

# cv2.imwrite("lol.jpg", frame)