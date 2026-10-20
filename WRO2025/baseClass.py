from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
import math
from config import *


class BaseController(DriveBase):
    def __init__(self, left_motor: Motor,
                 right_motor: Motor,
                 wheel_diameter: float,
                 axle_track: float,
                 left_sensor: ColorSen,
                 right_sensor: ColorSen,
                 one_encoder: AccelerationProfile,
                 ):
        self.wheel_circumference = math.pi * wheel_diameter * 0.1
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.one_encoder = one_encoder
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        super().__init__(left_motor, right_motor, wheel_diameter, axle_track)

    def start_tank_dc(self, leftSpeed: int, rightSpeed: int):
        super().stop()
        self.left_motor.dc(leftSpeed)
        self.right_motor.dc(rightSpeed)
        return

    def start_tank(self, leftSpeed: int, rightSpeed: int):
        super().stop()
        self.left_motor.run(leftSpeed)
        self.right_motor.run(rightSpeed)
        return

    def stop_and_hold(self):
        super().stop()
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def reset_angles(self):
        self.stop()
        self.left_motor.reset_angle(0)
        self.right_motor.reset_angle(0)
        return

    def get_avg_motor_deg(self, captured_motor_angles):
        return int((abs(int(self.right_motor.angle()) - captured_motor_angles[1]) +
                    abs(int(self.left_motor.angle()) - captured_motor_angles[0])) / 2)

    def capture_motor_angles(self):
        return [int(self.left_motor.angle()), int(self.right_motor.angle())]

    def move_mm(self, distance_in_mm: float, speed: int):
        self.start_tank(speed, speed)
        captured_angles = self.capture_motor_angles()
        distance_in_degrees = abs(
            (distance_in_mm / self.wheel_circumference) * 36)
        while self.get_avg_motor_deg(captured_angles) < distance_in_degrees:
            pass
        self.stop_and_hold()
        return

    def turn(self, angle, acc=900):
        self.stop()
        self.settings(turn_acceleration=acc)
        super().turn(angle)
        return

    def sync_acc(self, distance_in_mm: float, acc=1000):
        self.stop()
        self.settings(straight_acceleration=acc)
        self.straight(distance_in_mm)
        return

    def turn_until_method(self, function, speed=60):
        self.start_tank(speed, -speed)
        while (not function()):
            pass
        self.stop_and_hold()
        return

    def turnWithOneMotor(self, motor, min, max, acc, dec, tot):
        self.one_encoder.config(minPwr_in=min, maxPwr_in=max,
                                accelDist_in=acc, decelDist_in=dec, totalDist_in=tot)
        motor.reset_angle(0)
        wait(10)
        while True:
            position = motor.angle()
            power, done = self.one_encoder.compute(position)
            if done:
                motor.hold()
                wait(10)
                break
            motor.run(power*10)
            wait(10)

    def resetOnWall(self, speed=-500, time=700):
        super().stop()
        self.left_motor.run_time(speed=speed, time=time, wait=False)
        self.right_motor.run_time(speed=speed, time=time, wait=True)
        self.stop_and_hold()

    def move_until_black(self, speed=600):
        self.stop()
        while self.left_sensor.reflection()+self.right_sensor.reflection() > 15:
            self.left_motor.run(speed=speed)
            self.right_motor.run(speed=speed)
        self.left_motor.stop()
        self.right_motor.stop()
        return
     

    def move_until_black_right(self, speed=600):
        self.stop()
        while self.right_sensor.reflection() > 20:
            self.left_motor.run(speed=speed)
            self.right_motor.run(speed=speed)
        self.left_motor.hold()
        self.right_motor.hold()
        return
