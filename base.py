#~/usr/bin/env python

'''
Y_Classifier will classifiy each frame for the required classes
VideoReader will be used to read the video and to emit a certain frame based on the framerate that is chosen
VideoReader should run multithreaded with Y_Classifier as a shared resource, multiple video feeds can be simultaneously analyzed.
Rules class must include the necessary objects for the interaction to take place properly. 
Rules class must be given a dictionary of ('class':count) for classification. This is for cars and mobs.

Intrusion detection will have a different class. Based on person and boundary.
Left luggage ka baadme dekh lenge ab. Kuch nahi toh HAAR karenge. Else, we will train a classifier just for luggage.
'''
import darknet
import cv2
import numpy as np

class Y_Classifier:

    def __init__(self, NET_PATH, META_PATH, WEIGHTS_PATH, THRESH):
        self.NET_PATH = NET_PATH
        self.META_PATH = META_PATH
        self.WEIGHTS_PATH = WEIGHTS_PATH
        self.THRESH = THRESH

    def loadClassifier(self):
        self.NET = darknet.load_net(self.NET_PATH, self.WEIGHTS_PATH, 0)
        self.META = darknet.load_net(self.META_PATH)
        return

    def detect(self, frame):
        # Frame should be loaded using darknet library
        return darknet.classify(self.NET, self.META, frame)


class VideoReader:
    
    def __init__(self, fr, video):
        self.FRAMERATE = fr
        self.VIDEO = video
        self.SEEK = 0

    def initCV(self):
        # Initialize OpenCV for video
        return

    def emitFrame(self, seek=self.SEEK):
        ## Math
        return

    def next(self)
        # Invoke emitFrame with added SEEK
        return


# Class has to be inherited and its methods are to be treated as interfaces for each rule
class Rule:

    def __init__(self, name, ruleset={}):
        self.RULE_NAME = name
        self.RULESET = ruleset

    def eval(self):
        # Write Evaluation logic
        return

    def learn(self):
        # Write Learning logic
        return

# Driver class
class ASurveillance:

    def __init__(self, name, capture, y_classifier, rule):
        self.NAME = name
        # VideoReader Object
        self.VIDEO = videoReader
        # YOLO Classifier Object
        self.Y_CLASSIFIER = y_classifier
        # Rule object
        self.RULE = rule

    def start(self):
        # Logic for performing surveillance based on data given.