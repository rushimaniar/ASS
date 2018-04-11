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
from logger import *
from random import *
import string
import os
import threading
import time
import subprocess

class Y_Classifier:

    def __init__(self, NET_PATH, META_PATH, WEIGHTS_PATH, THRESH):
        self.NET_PATH = NET_PATH
        self.META_PATH = META_PATH
        self.WEIGHTS_PATH = WEIGHTS_PATH
        self.THRESH = THRESH

    def loadClassifier(self):
        log(INFO, "Loading YOLO.")
        self.NET = darknet.load_net(self.NET_PATH, self.WEIGHTS_PATH, 0)
        self.META = darknet.load_meta(self.META_PATH)
        log(INFO, "Loaded YOLO.")
        return

    def detect(self, frame):
        frame = 'tmp/' + frame
        im = darknet.load_image(frame, 0, 0)
        r = darknet.detect(self.NET, self.META, frame, thresh=self.THRESH)
        return r

    def clean(self, frame):
        frame = 'tmp/' + frame
        os.remove(frame)
        return


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
        #
        # Okay! New pivot. Marshalling an opencv frame to YOLO is a pain so what we will be doing is taking a very inefficient approach :).
        # This method will get the next pertinent frame and then instead of calling DN it wil save it in tmp directory.
        # The frame will be retrieved by Y_Classifier object and classified and then deleted. Simple :).
        self.SEEK += int(self.INTERVAL*self.FRAMERATE)
        # log(INFO,"SEEK: " + str(self.SEEK))
        if self.SEEK > self.FR_COUNT:
            return False
        else:
            frame = self._emitFrame(self.SEEK)
            name = ''.join(choice(string.ascii_letters) for x in range(0, 10))
            name += '.jpg'
            cv2.imwrite('tmp/' + name, frame)
        return name

'''
This project is riddled with hacks. The following is the biggest one there is.
The role of the function is to display a frame.
This is done by using an external utility feh. (add that to dependencies.)
It will first check if there is any feh instances and then kill them just to open the new instance.
Oh, remember to add this on another thread, it sleeps.
'''
def view(frame, title='Frame', timeout=1):
    check = subprocess.Popen(['ps','-a'], stdout=subprocess.PIPE)
    ps = check.communicate()[0]
    if 'feh' in ps:
        subprocess.Popen(['killall','-s','KILL','feh'])
    feh = subprocess.Popen(['feh','--title',title,frame])
    time.sleep(timeout)
    feh.terminate()
    feh.kill()

# Base class for all rules
class Rule:

    def __init__(self, name, camera = 'cam'):
        self.RULE_NAME = name
        self.CAMERA = camera
        log(INFO, "Applying rule: " + self.RULE_NAME)


    def eval(self):
        # Write Evaluation logic. Return true if triggered.
        pass

    def train(self):
        # Write Learning logic
        pass

# Driver class, one per camera. One thread per instance
class ASurveillance(threading.Thread):

    def __init__(self, name, capture, y_classifier, rule):
        threading.Thread.__init__(self)
        self.NAME = name
        # VideoReader Object
        self.VIDEO = capture
        # YOLO Classifier Object
        self.Y_CLASSIFIER = y_classifier
        # Rule object
        self.RULE = rule
        self.RULE.INTERVAL = self.VIDEO.INTERVAL
        self.RULE.CAMERA = name

    def run(self):
        # Logic for performing surveillance based on data given.
        # Soch raha tha, self learning model daal dete hain.
        dataset = []
        while True:
            if len(dataset) > 10:
                self.RULE.train(dataset)
                dataset[:] = []
            frame = self.VIDEO.next()
            if frame is False:
                break
            r = self.Y_CLASSIFIER.detect(frame)
            if self.RULE.eval(r) is True:
                view_thread = threading.Thread(target=view, args=('tmp/' + frame,), kwargs={'title':self.NAME, 'timeout':0.5})
                view_thread.run()
            self.Y_CLASSIFIER.clean(frame)
            dataset.append(r)

        return