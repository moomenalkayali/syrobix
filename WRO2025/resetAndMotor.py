from config import *
from Utils import *


# def downClaw(duty=100):
#     up_motor.run_until_stalled(1000, then=Stop.HOLD, duty_limit=duty)


def upClaw():
    up_motor.run_time(speed=100,time=1000,then=Stop.HOLD)
    wait(50)
    blocks_motor.run_time(speed=120,time=800, then=Stop.HOLD)
    wait(50)
    up_motor.run_time(speed=-100,time=1000,then=Stop.HOLD)

def upClawTwo():
    up_motor.run_time(speed=100,time=2000,then=Stop.HOLD)
    wait(500)
    blocks_motor.run_time(speed=-120,time=1000, then=Stop.HOLD)
    wait(500)
    up_motor.run_time(speed=100,time=1000,then=Stop.HOLD)
    wait(500)
    blocks_motor.run_time(speed=120,time=1000, then=Stop.HOLD)
    wait(500)
    up_motor.run_time(speed=-100,time=4000,then=Stop.HOLD)

def downMotorRight(waitA=True):
    base.sync_acc(10)
    blocks_motor.run_time(speed=800, time=650, then=Stop.COAST, wait=waitA)


def downMotorLeft(waitA=True, timeA=600):
    base.sync_acc(10)
    blocks_motor.run_time(speed=-800, time=timeA, then=Stop.COAST, wait=waitA)


def downMotorResetTakesBolts(angle=120, waitA=True):
    blocks_motor.run_angle(speed=-600, rotation_angle=angle,
                         then=Stop.HOLD, wait=waitA)


def upMotorResetWithTrueOrFalse(speed=1000, bool=True):
    up_motor.run_time(speed=speed, time=600, wait=bool)


def downMotorResetTrueOrFalse(speed=1000, bool=True):
    blocks_motor.run_time(speed=speed, time=900, wait=bool)


def upMotorFirstGearToUp(waitA=True, speed=1000):
    up_motor.run_angle(rotation_angle=230, speed=-
                       speed, then=Stop.HOLD, wait=waitA)
    wait(10)


def upMotorSecondGearToUp(speed):
    up_motor.run_angle(rotation_angle=115, speed=-speed, then=Stop.HOLD)
    wait(10)


def upMotorSecondGearToDown(speed):
    up_motor.run_angle(rotation_angle=120, speed=speed, then=Stop.HOLD)
    wait(10)


def upMotorThirdGearToDown(waitA=True, angle=150, speed=1000):
    up_motor.run_angle(rotation_angle=angle, speed=speed,
                       then=Stop.HOLD, wait=waitA)
    wait(10)


def downMotorMoveAngle(angle, speed=-1000, waitA=True):
    blocks_motor.run_angle(rotation_angle=angle, speed=speed,
                         then=Stop.HOLD, wait=waitA)
