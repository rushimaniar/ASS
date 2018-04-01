#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base
import rules
from logger import *
from random import *
import string

interval = 1

vid = base.VideoReader('data/crowd.mp4',interval)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',interval)
yolo_c.loadClassifier()
mob = rules.MobGatheringRule(interval)

dataset = []

while True:
    frame = vid.next()
    if frame is False:
        break
    r = yolo_c.detect(frame)
    dataset.append(r)
    mob.eval(r)

mob.learn(dataset)