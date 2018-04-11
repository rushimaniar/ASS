#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base
import rules
import logger
import argparse
import os

'''
interval = 1

hotel_cap = base.VideoReader('data/lobby2.mp4',interval)

yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',0.5)
yolo_c.loadClassifier()

hall = base.ASurveillance("Hall camera", hotel_cap, yolo_c, [rules.AreaIntrusion(interval), rules.MobGatheringRule(interval)])

hall.start() 
'''

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--video', help='Address to the video feed')
    parser.add_argument('-c', '--camera', help='Specify camera name')
    parser.add_argument('-r', '--rules', help='Specify the rules to apply', type=str, nargs='+')
    parser.add_argument('-l', '--list', help='List available rules', action='store_true')
    parser.add_argument('-d', '--debug-levels', help="Specify debug levels. Can be (D)ebug, (R)ule, (C)amera, (A)ll. Enter space separated.", type=str, nargs='+')

    args = parser.parse_args()

    print args

    if args.list:
        print "The available rules are:"
        for rule in rules.RULES:
            print "\t- " + rule
        exit()

    if args.debug_levels:
        for level in args.debug_levels:
            if level == 'A':
                logger.DEBUG = True
                logger.R_DEBUG = True
                logger.C_DEBUG = True
                break
            if level == 'D':
                logger.DEBUG = True
            if level == 'C':
                logger.C_DEBUG = True
            if level == 'R':
                logger.R_DEBUG = True
    
    if args.camera is None or args.video is None or args.rules is None:
        print "Please view help for proper usage."
        exit()

    interval = 1
    rules_list = []
    for rule in args.rules:
        if rule == rules.RULES[0]:
            rules_list.append(rules.MobGatheringRule(interval))
        if rule == rules.RULES[1]:
            rules_list.append(rules.LeftLuggageRule(interval))
        if rule == rules.RULES[2]:
            rules_list.append(rules.AreaIntrusionRule(interval))
        if rule == rules.RULES[3]:
            rules_list.append(rules.ParkingCarsUtilityRule(interval))

    if len(rules_list) == 0:
        print "Specify correct rule."
        exit()

    if not os.path.exists(args.video):
        print "Video feed does not exist. Exiting..."
        exit()

    # Load Video
    cap = base.VideoReader(args.video,interval)

    # Load and initialize the classifier
    yolo_c = base.Y_Classifier('cfg/yolov3.cfg','cfg/coco.data','yolov3.weights',0.5)
    yolo_c.loadClassifier()

    # Initialize and start Surveillance Thread
    aSur = base.ASurveillance(args.camera, cap, yolo_c, rules_list)
    aSur.start()