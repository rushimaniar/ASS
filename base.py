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
    
    def __init__(self, video, interval):
        # Path to Video
        self.VIDEO = video
        self.SEEK = 0
        # In seconds? Okay.
        self.INTERVAL = interval
        self.initCV()

    def initCV(self):
        # Initialize OpenCV for video
        self.CAP = cv2.VideoCapture(self.VIDEO)
        self.FRAMERATE = self.CAP.get(cv2.CAP_PROP_FPS)
        self.FR_COUNT = int(self.CAP.get(cv2.CAP_PROP_FRAME_COUNT))
        self.INCR_FR = int(self.FRAMERATE*self.INTERVAL)
        return

    # "Private" Function. Thank you Python (-_-')
    def _emitFrame(self, seek):
        # Get next frame based on the interaval
        self.CAP.set(cv2.CAP_PROP_POS_FRAMES, seek)
        ret, frame = self.CAP.read()
        if ret:
            return frame
        else:
            return False

    def next(self):
        # Invoke emitFrame with added SEEK
        # Check for frame out of index here, not in the emitFrame method.
        self.SEEK += self.INTERVAL
        if self.SEEK > self.FR_COUNT:
            return False
        else:
            frame = self._emitFrame(self.SEEK)

        return frame


# Base class for all rules
class Rule:

    def __init__(self, name, ruleset={}):
        self.RULE_NAME = name
        self.RULESET = ruleset

    def eval(self):
        # Write Evaluation logic
        pass

    def learn(self):
        # Write Learning logic
        pass

# Driver class, one per camera. One thread per instance
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
        return