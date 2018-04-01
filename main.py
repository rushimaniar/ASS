#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base
from logger import tlog, WARN, ERROR, INFO

vid = base.VideoReader('data/crowd.mp4',0.5)
frame = vid.next()
tlog(INFO,"Print any key to exit.")
# cv2.imshow("LOL", frame)
# cv2.waitKey(0)