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
from multiprocessing import Process, Lock, log_to_stderr
import logging
import subprocess

check = subprocess.Popen(['ps','-a'], stdout=subprocess.PIPE)
lol = check.communicate()[0]

kill = subprocess.Popen(['killall','-s','KILL','feh'])