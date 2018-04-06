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
from multiprocessing import Process, Lock

interval = 0.5

lobby_cap = base.VideoReader('data/crowd.mp4',interval)
hotel_cap = base.VideoReader('data/crowd.mp4',interval)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',0.5)
yolo_c.loadClassifier()

lobby = base.ASurveillance("Lobby", lobby_cap, yolo_c, rules.MobGatheringRule(interval))
hall = base.ASurveillance("Hall", hotel_cap, yolo_c, rules.MobGatheringRule(interval))

lobby_process = Process(target = lobby.run)
hall_process = Process(target = hall.run)

lobby_process.start()
hall_process.start()

lobby_process.join()
hall_process.join()