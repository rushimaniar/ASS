#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base
import rules
from logger import *
from random import *
import string

vid = base.VideoReader('data/crowd.mp4',0.5)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',1.5)
yolo_c.loadClassifier()
mob = rules.MobGatheringRule(0.5)

while True:
    frame = vid.next()
    if frame is False:
        break
    r = yolo_c.detect(frame)
    mob.eval(r)