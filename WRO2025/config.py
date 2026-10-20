from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from baseClass import BaseController
from ColorSen import ColorSen
from lineFollowClass import LineController
from constants import *
from AccOneEncoder import *
from PdCtrl import *

ev3 = EV3Brick()
left_motor = Motor(Port.A, positive_direction=Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.D, positive_direction=Direction.CLOCKWISE)
up_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
blocks_motor = Motor(Port.C, Direction.CLOCKWISE)
left_sensor = ColorSen(Port.S1)
right_sensor = ColorSen(Port.S4)
up_left_sensor = ColorSen(Port.S2)
up_right_sensor = ColorSen(Port.S3)
one_encoder = AccelerationProfile()

pd = PDController()
base = BaseController(left_motor=left_motor, right_motor=right_motor,
                      wheel_diameter=62, left_sensor=left_sensor,
                      right_sensor=right_sensor, axle_track=180, one_encoder=one_encoder)
base.settings(turn_rate=2250, straight_speed=1000,
              straight_acceleration=250, turn_acceleration=600)
line = LineController(base, left_sensor=left_sensor,
                      right_sensor=right_sensor, pd=pd, left_motor=left_motor, right_motor=right_motor)
if (DEBUG):
    stopwatch = StopWatch()
