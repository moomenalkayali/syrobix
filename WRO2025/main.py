#!/usr/bin/env pybricks-micropython
from re import M
from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from pybricks.media.ev3dev import SoundFile  # type: ignore
from ColorSen import rgb_to_hsv
from Utils import *
from config import *
from mainFunctions import *
import time


#======================================#
# Our Mission Plan:
# wait_for_button_press()
putRockets()#done
battary()#done
theater()
breaker()  
TakingBlocks()

