from base import Rule
from logger import log, WARN, ERROR, INFO

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
        # In number of frames
        self.THRESHOLD = int(self.RULE_SET['seconds'] / interval)

    def _countPersons(self, y_result):
        i = 0
        for result in y_result:
            if result[0] == 'person':
                i += 1
        return i 

    def eval(self, y_result, interval):
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

    def learn(self):
        log(INFO, "Commencing Learning.")
        return

mob = MobGatheringRule(0.5)
y_result = [('person', 0.9979516267776489, (359.4686584472656, 588.0189208984375, 152.2552032470703, 381.0101623535156)), ('person', 0.9972562193870544, (723.8895874023438, 589.1392211914062, 141.96469116210938, 420.5570068359375)), ('person', 0.9919537901878357, (634.1771240234375, 583.5216064453125, 116.60320281982422, 393.730712890625)), ('person', 0.9813784956932068, (155.66091918945312, 579.3514404296875, 105.69571685791016, 246.74887084960938)), ('person', 0.9754900932312012, (496.580078125, 580.6995239257812, 63.0941162109375, 222.27236938476562)), ('person', 0.9289568066596985, (50.31898498535156, 588.803466796875, 74.79957580566406, 240.45550537109375)), ('person', 0.9275311231613159, (272.94110107421875, 551.2156372070312, 55.82367706298828, 131.70127868652344)), ('person', 0.904251217842102, (434.9120788574219, 569.0701293945312, 62.29117202758789, 261.59942626953125)), ('backpack', 0.7747591137886047, (615.7361450195312, 522.2175903320312, 71.21941375732422, 142.0638427734375)), ('person', 0.7681362628936768, (541.4219360351562, 567.6240234375, 49.74648666381836, 195.9141845703125))]
