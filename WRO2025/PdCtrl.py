import math


class PDController:
    def __init__(self):
        self.kp = 0
        self.kd = 0
        self.pwr = 0
        self.err_old = 0

    def config(self, kp, kd, pwr):
        self.kp = kp
        self.kd = kd
        self.pwr = pwr
        self.err_old = 0

    def compute(self, e1, e2):
        err = e1 - e2
        U = err * self.kp + (err - self.err_old) * self.kd
        self.err_old = err
        pB = self.pwr + U
        pC = self.pwr - U
        return pB, pC

    def compute_with_pwr(self, pwrIn, e1, e2):
        err = e1 - e2
        U = err * self.kp + (err - self.err_old) * self.kd
        self.err_old = err
        pB = pwrIn + U
        pC = pwrIn - U
        return pB, pC

    def compute_single(self, error):
        U = error * self.kp + (error - self.err_old) * self.kd
        self.err_old = error
        pB = self.pwr - U
        pC = self.pwr + U
        return pB, pC
