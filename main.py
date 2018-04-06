#!/usr/bin/env python

# Treated as a script to test stuff on for now.
# Threads are giving problems, switch to multiprocess based parellelism?


import cv2
import darknet
import base
import rules
from logger import *
from random import *
import string
from multiprocessing import Process

'''
interval = 0.5

lobby_cap = base.VideoReader('data/crowd.mp4',interval)
# hotel_cap = base.VideoReader('data/crowd.mp4',interval)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',0.5)
yolo_c.loadClassifier()

lobby = base.ASurveillance("Lobby", lobby_cap, yolo_c, rules.MobGatheringRule(interval))
# hall = base.ASurveillance("Hall", hotel_cap, yolo_c, rules.MobGatheringRule(interval))


lobby.start()
# hall.start()
'''
lol = base.multi('lol', 'This is process 1.')
lel = base.multi('lel', 'This is process 2.')

p1 = Process(target = lol.talk)
p2 = Process(target = lel.talk)

p1.start()
p2.start()