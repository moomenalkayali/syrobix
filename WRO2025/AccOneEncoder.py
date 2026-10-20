import math
class AccelerationProfile:
    def __init__(self):
        self.minPwr = 0
        self.maxPwr = 0
        self.accelDist = 0
        self.decelDist = 0
        self.totalDist = 0
        self.isNEG = False
    def config(self, minPwr_in, maxPwr_in, accelDist_in, decelDist_in, totalDist_in):
        self.minPwr = abs(minPwr_in)
        self.maxPwr = abs(maxPwr_in)
        self.accelDist = accelDist_in
        self.decelDist = decelDist_in
        self.totalDist = totalDist_in
        self.isNEG = minPwr_in < 0
    def compute(self, currEnc):
        currEnc = abs(currEnc)
        if currEnc >= self.totalDist:
            return 0, True
        if currEnc > self.totalDist / 2:
            if self.decelDist == 0:
                pwr = self.maxPwr
            else:
                pwr = ((self.maxPwr - self.minPwr) / self.decelDist ** 2) * (currEnc - self.totalDist) ** 2 + self.minPwr
        else:
            if self.accelDist == 0:
                pwr = self.maxPwr
            else:
                pwr = ((self.maxPwr - self.minPwr) / self.accelDist ** 2) * currEnc ** 2 + self.minPwr
        pwr = max(min(pwr, self.maxPwr), self.minPwr)
        if self.isNEG:
            pwr = -pwr
        return pwr, False