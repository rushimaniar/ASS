from base import Rule
from logger import log, WARN, ERROR, INFO

class MobGatheringRule(Rule):

    def __init__(self, interval):
        # Ruleset.
        self.RULE_SET = {
            'person_count':9,
            'seconds':3
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
        # If the last (interval*seconds) frames contain more than the specified person count, alert.
        persons = self._countPersons(y_result)
        if persons > self.RULE_SET['person_count']:
            self.POS_FRAMES += 1
        else:
            self.POS_FRAMES = 0

        if self.POS_FRAMES > self.THRESHOLD:
            log(ERROR, "Mob Detected")
            return True
        else:
            return False

    def learn(self, dataset):
        for data in dataset:
            self.PERSONS += self._countPersons(data)
        log(INFO,self.PERSONS)
        log(INFO,len(dataset))
        count = int(self.PERSONS / len(dataset))
        log(WARN, "New threshold for mob: "+str(count))
        return
