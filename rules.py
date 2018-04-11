from base import Rule
from logger import *

class MobGatheringRule(Rule):

    def __init__(self, interval):
        Rule.__init__(self,'Mob Gathering Rule')
        # Ruleset.
        self.RULE_SET = {
            'person_count':5,
            'seconds':2,
            'min_persons': 4
            }
        # Number of positively matched frames.
        self.POS_FRAMES = 0
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
        if persons > self.RULE_SET['person_count']:
            self.POS_FRAMES += 1
        else:
            self.POS_FRAMES = 0

        if self.POS_FRAMES >= self.THRESHOLD:
            clog(ERROR, self.CAMERA,  "Mob Detected")
            return True
        else:
            return False

    def train(self, dataset):
        clog(WARN, self.CAMERA, "Beginning training cycle....")
        for data in dataset:
            count = self._countPersons(data)
            self.PERSONS += count
            if count != 0:
                self.TUPLES += 1
        if self.PERSONS != 0 and self.TUPLES != 0:
            self.RULE_SET['person_count'] = int(self.PERSONS / self.TUPLES)
            if self.RULE_SET['person_count'] < self.RULE_SET['min_persons']:
                self.RULE_SET['person_count'] = self.RULE_SET['min_persons']
        clog(WARN, self.CAMERA, "New threshold for mob: "+str(self.RULE_SET['person_count']))
        return

class LeftLuggageRule(Rule):
    def __init__(self, interval):
        Rule.__init__(self,'Left Luggage Rule')
        self.RULE_SET = {
            'max_time':10
        }
        self.INTERVAL = interval
        self.POS_FRAMES = 0
        self.THRESHOLD = int(self.RULE_SET['max_time'] / interval)

    def _countLuggage(self, y_result):
        # Ladders are more readable than combined logic. Change my mind.
        count = 0
        for result in y_result:
            if result[0] == 'handbag':
                count += 1
            elif result[0] == 'backpack':
                count += 1
            elif result[0] == 'suitcase':
                count +=1
        return count

    def eval(self, y_result):
        count = self._countLuggage(y_result)
        clog(INFO, self.CAMERA, "Number of Luggage Objects: " + str(count))

        # If no luggage detected.
        if count == 0:
            self.POS_FRAMES = 0
            return False

        # If Stagnant Luggage.
        else:
            self.POS_FRAMES += 1
            if self.POS_FRAMES >= self.THRESHOLD:
                clog(ERROR, self.CAMERA, "Stagnant Luggage Detected.")
                # Write Callback code here.
                return True
            return False

    def train(self, y_result):
        # No Training. Static Rule.
        return

class ParkingCarsUtilityRule(Rule):
    def __init__(self, interval):
        Rule.__init__(self, "Parking cars counting utility.")
        self.RULE_SET = {
            'max_cars' : 15
        }
        self.CURRENT_CARS = 0

    def _countVehicles(self, y_result):
        # Count vehicles, if it finds illegal vehicles straight return false.
        #
        # Ladders are more readable than combined logic. Change my mind.
        count = 0
        for result in y_result:
            if result[0] == 'truck':
                return False
            if result[0] == 'bus':
                return False
            if result[0] == 'train':
                return False

            # The legal vehicles
            if result[0] == 'car':
                count += 1
            if result[0] == 'bicycle':
                count += 1
            if result[0] == 'motorbike':
                count += 1
        return count

    def eval(self, y_result):
        '''
        Two Triggering Rules:
            - If there are more cars than there should be.
            - If there is a goddamn truck in the hotel parking lot. That is not correct. No sir. Or a bus or a train too.
        '''
        count = self._countVehicles(y_result)
        if count is False:
            clog(ERROR, self.CAMERA, "Illegal Vehicle Detected.")
            return True
        elif count > self.RULE_SET['max_cars']:
            self.CURRENT_CARS = count
            clog(ERROR, self.CAMERA, "Vehicle Limit Exceeded.")
            return True

        return False

    def train(self, y_result):
        # No training. Static Rule.
        return

class AreaIntrusion(Rule):
    def __init__(self, interval):
        Rule.__init__(self, "Intrusion Detection Rule")
        self.RULE_SET = {
            'x_pos' : 400,
            'y_pos' : 400
        }

    def eval(self, y_result):
        # Laddersssss
        for result in y_result:
            if result[0] == 'person':
                clog(INFO, self.CAMERA, "Person Detected")
                if result[2][0] >= self.RULE_SET['x_pos']:
                    if result[2][0] >= self.RULE_SET['y_pos']:
                        clog(ERROR, self.CAMERA, "Intrusion detected.")
        return

    def train(self, y_result):
        # No training. Static rule.
        return