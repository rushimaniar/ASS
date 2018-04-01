#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base
from logger import *
from random import *
import string

vid = base.VideoReader('data/crowd.mp4',0.2)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',0.5)
yolo_c.loadClassifier()

for i in range(0, 15):
    frame = vid.next()
    r =  yolo_c.detect('tmp/'+frame)
    print r