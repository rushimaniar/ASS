#!/usr/bin/env python

# Treated as a script to test stuff on for now.

import cv2
import darknet
import base
from logger import log, WARN, ERROR, INFO

vid = base.VideoReader('data/crowd.mp4',0.5)
frame = vid.next()