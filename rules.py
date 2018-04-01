from base import Rule

class MobGatheringRule(Rule):

    def __init__(self, interval):
        # Ruleset.
        self.RULE_SET = {
            'person_count':5,
            'seconds':5
            }
        # Number of positively matched frames.
        self.POS_FRAMES = 0
        Rule.__init__(self,'Mob Gathering Rule', self.RULE_SET)
        self.INTERVAL = interval
        self.THRESHOLD = interval * self.RULE_SET['seconds']

    def _countPersons(self, y_result):
        i = 0
        for result in y_result:
            if result[0] == 'person':
            i += 1
        return i 

    def eval(self, frame, y_result, interval):
        # If the last (interval*seconds) frames contain more than the specified person count, alert.
        persons = self._countPersons(y_result)
        if persons > self.RULE_SET['person_count']:
            self.POS_FRAMES += 1
        else:
            self.POS_FRAMES = 0

        if self.POS_FRAMES > self.THRESHOLD:
            return True
        else:
            return False

    def learn(self):
        print('Lol Learning...')
        return
