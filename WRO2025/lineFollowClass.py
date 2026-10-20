from pybricks.hubs import EV3Brick  # type: ignore
from pybricks.ev3devices import Motor, ColorSensor, GyroSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from pybricks.tools import wait, StopWatch  # type: ignore
from pybricks.robotics import DriveBase  # type: ignore
from baseClass import BaseController
import time
import ColorSen
from constants import *
from PdCtrl import *


class LineController:
    def __init__(self, robotBase: BaseController,
                 left_sensor: ColorSen,
                 right_sensor: ColorSen,
                 left_motor: Motor,
                 right_motor: Motor,
                 pd: PDController,
                 ):
        self.robotBase = robotBase
        self.left_sensor = left_sensor
        self.right_sensor = right_sensor
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.pd = pd

    def correct(self, duration=0.6, speed=50):
        kp, kd = 0.2, 1.3
        self.pd.config(kp, kd, speed)
        err = (BLACK+WHITE)/2
        speed = abs(speed)
        start_time = time.time()
        while (time.time() - start_time) < duration:
            e1 = self.left_sensor.reflection()-err
            e2 = self.right_sensor.reflection()-err
            pwrL, pwrR = self.pd.compute(e1, e2)
            pwrL = max(min(pwrL, 100), -100)
            pwrR = max(min(pwrR, 100), -100)
            self.robotBase.stop()
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.robotBase.stop()
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def line_until_method(self, method, speed=70):
        kp, kd = KP70, KD70
        if speed == 100:
            kp, kd = KP100, KD100
        self.pd.config(kp, kd, speed)
        err = (BLACK+WHITE)/2
        speed = abs(speed)
        while not method():
            e1 = self.left_sensor.reflection()-err
            e2 = self.right_sensor.reflection()-err
            pwrL, pwrR = self.pd.compute(e1, e2)
            pwrL = max(min(pwrL, 100), -100)
            pwrR = max(min(pwrR, 100), -100)
            self.robotBase.stop()
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.robotBase.stop()
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def line_until_method_white(self, method, speed=60):
        kp, kd = KP70, KD70
        if speed == 100:
            kp, kd = KP100, KD100
        self.pd.config(kp, kd, speed)
        err = 170
        speed = abs(speed)
        while not method():
            e1 = err-self.left_sensor.reflection()
            e2 = err-self.right_sensor.reflection()
            pwrL, pwrR = self.pd.compute(e1, e2)
            pwrL = max(min(pwrL, 100), -100)
            pwrR = max(min(pwrR, 100), -100)
            self.robotBase.stop()
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.robotBase.stop()
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def follow_one_until_left_gray(self, speed, kp=0.3, kd=1.2):
        self.pd.config(kp, kd, speed)
        speed = abs(speed)
        target = (BLACK + WHITE) / 2
        self.robotBase.stop()
        while self.left_sensor.reflection() > 90:
            error = target-self.right_sensor.reflection()
            pwrL, pwrR = self.pd.compute_single(error)
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def follow_one_until_left_gray_ditance(self, distance_cm, speed, kp=0.3, kd=1.2):
        self.pd.config(kp, kd, speed)
        speed = abs(speed)
        self.robotBase.stop()
        captured_angles = self.robotBase.capture_motor_angles()
        distance_degrees = (
            distance_cm / self.robotBase.wheel_circumference) * 360
        target = (BLACK + WHITE) / 2
        while self.robotBase.get_avg_motor_deg(captured_angles) < distance_degrees:
            error = target-self.right_sensor.reflection()
            pwrL, pwrR = self.pd.compute_single(error)
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.left_motor.hold()
        self.right_motor.hold()
        return

    def turn_to_line(self, dis=1, angle=80):
        if (dis == 1):
            self.robotBase.turn(angle)
            self.robotBase.turn_until_method(
                lambda: self.right_sensor.reflection() < 30, 200)
        else:
            self.robotBase.turn(angle)
            self.robotBase.turn_until_method(
                lambda: self.right_sensor.reflection() < 30, -200)
        # self.correct(duration=0.5)

    def followUntilSensor(self, dis=-1, speed=100):
        kp, kd = KP70, KD70
        if abs(speed) == 100:
            kp, kd = KP100, KD100
        sensor = self.left_sensor
        if (dis == 1):
            sensor = self.right_sensor
        self.pd.config(kp, kd, speed)
        err = (BLACK+WHITE)/2
        # speed = abs(speed)
        self.robotBase.stop()
        while sensor.reflection() > 9:
            e1 = self.left_sensor.reflection()-err
            e2 = self.right_sensor.reflection()-err
            pwrL, pwrR = self.pd.compute(e1, e2)
            pwrL = max(min(pwrL, 100), -100)
            pwrR = max(min(pwrR, 100), -100)
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.left_motor.stop()
        self.right_motor.stop()

    def follow_cm(self, distance_cm, speed: int = 70):
        kp, kd = KP70, KD70
        if abs(speed) == 100:
            kp, kd = KP100, KD100
        distance_cm = abs(distance_cm)
        self.pd.config(kp, kd, speed)
        err = (BLACK+WHITE)/2
        speed = abs(speed)
        self.robotBase.stop()
        captured_angles = self.robotBase.capture_motor_angles()
        distance_degrees = (
            distance_cm / self.robotBase.wheel_circumference) * 360
        while self.robotBase.get_avg_motor_deg(captured_angles) < distance_degrees:
            e1 = self.left_sensor.reflection()-err
            e2 = self.right_sensor.reflection()-err
            pwrL, pwrR = self.pd.compute(e1, e2)
            pwrL = max(min(pwrL, 100), -100)
            pwrR = max(min(pwrR, 100), -100)
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.left_motor.hold()
        self.right_motor.hold()

    def follow_cm_acc(self, distance_cm, speed: int = 70, accel_ratio=0.3):
        kp, kd = KP70, KD70
        if speed == 100:
            kp, kd = KP100, KD100
        distance_cm = abs(distance_cm)
        speed = abs(speed)
        self.pd.config(kp, kd, 50)
        err = (BLACK + WHITE) / 2
        self.robotBase.stop()
        captured_angles = self.robotBase.capture_motor_angles()
        distance_degrees = (
            distance_cm / self.robotBase.wheel_circumference) * 360
        accel_cm = distance_cm * accel_ratio
        decel_cm = distance_cm * (1 - accel_ratio)
        while True:
            traveled_deg = self.robotBase.get_avg_motor_deg(captured_angles)
            traveled_cm = (traveled_deg / 360) * \
                self.robotBase.wheel_circumference
            if traveled_cm >= distance_cm:
                break
            if traveled_cm < accel_cm:
                current_speed = int(speed * (traveled_cm / accel_cm))
            elif traveled_cm > decel_cm:
                remain_cm = distance_cm - traveled_cm
                current_speed = int(
                    speed * (remain_cm / (distance_cm - decel_cm)))
            else:
                current_speed = speed
            current_speed = max(50, current_speed)
            self.pd.pwr = current_speed
            e1 = self.left_sensor.reflection() - err
            e2 = self.right_sensor.reflection() - err
            pwrL, pwrR = self.pd.compute(e1, e2)
            pwrL = max(min(pwrL, 100), -100)
            pwrR = max(min(pwrR, 100), -100)
            self.left_motor.dc(pwrL)
            self.right_motor.dc(pwrR)
        self.left_motor.hold()
        self.right_motor.hold()

