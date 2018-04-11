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

# lobby_cap = base.VideoReader('data/market.mp4',interval)
hotel_cap = base.VideoReader('data/intrusion.mp4',interval)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',0.5)
yolo_c.loadClassifier()

# lobby = base.ASurveillance("Lobby", lobby_cap, yolo_c, rules.MobGatheringRule(interval))
hall = base.ASurveillance("Hall", hotel_cap, yolo_c, rules.AreaIntrusion(interval))


# lobby.start()
hall.start() 