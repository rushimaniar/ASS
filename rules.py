from base import Rule
from logger import *

class MobGatheringRule(Rule):

    def __init__(self, interval):
        # Ruleset.
        self.RULE_SET = {
            'person_count':5,
            'seconds':2
            }
        # Number of positively matched frames.
        self.POS_FRAMES = 0
        Rule.__init__(self,'Mob Gathering Rule', self.RULE_SET)
        self.INTERVAL = interval
        # In number of frames
        self.THRESHOLD = int(self.RULE_SET['seconds'] / interval)

        # Learning inits
        self.PERSONS = 0
        self.TUPLES = 0


    def _countPersons(self, y_result):
        i = 0
        for result in y_result:
            if result[0] == 'person':
                i += 1
        return i 

    def eval(self, y_result):
        # log(WARN,self.INTERVAL)
        # If the last (interval*seconds) frames contain more than the specified person count, alert.
        persons = self._countPersons(y_result)
        clog(INFO, self.CAMERA,"Number of persons: " + str(persons))
        # log(WARN,persons)
        if persons >= self.RULE_SET['person_count']:
            self.POS_FRAMES += 1
        else:
            self.POS_FRAMES = 0

        if self.POS_FRAMES >= self.THRESHOLD:
            clog(ERROR, self.CAMERA,  "Mob Detected")
            return True
        else:
            return False

    def learn(self, dataset):
        clog(WARN, self.CAMERA, "Beginning training cycle....")
        for data in dataset:
            count = self._countPersons(data)
            self.PERSONS += count
            if count != 0:
                self.TUPLES += 1
        if self.PERSONS != 0 and self.TUPLES != 0:
            self.RULE_SET['person_count'] = int(self.PERSONS / self.TUPLES)
        clog(WARN, self.CAMERA, "New threshold for mob: "+str(self.RULE_SET['person_count']))
        return