
from pybricks.tools import wait, StopWatch  # type: ignore
from config import *
from pybricks.tools import wait, StopWatch  # type: ignore
from constants import *


def preflight_checks():
    if (DEBUG):
        stopwatch.reset()
    voltage = ev3.battery.voltage()
    print("The voltage is :", voltage)
    if voltage < 8000:
        if (DEBUG):
            ev3.speaker.beep(frequency=200, duration=1000)
        if (DEBUG):
            print("Low battery.")
        from sys import exit
        exit()
    ev3.speaker.beep(frequency=600, duration=300)


def wait_for_button_press():
    print("Waiting for the button:")
    while not ev3.buttons.pressed():
        wait(10)
    while ev3.buttons.pressed():
        wait(10)
    wait(500)
    stopwatch.reset()


def printCalibrateColor():
    global BLACK, WHITE
    print("Black:")
    wait_for_button_press()
    black = (left_sensor.rawRef() + right_sensor.rawRef())/2
    BLACK = black
    print(black)
    print("White:")
    wait_for_button_press()
    white = (left_sensor.rawRef() + right_sensor.rawRef())/2
    WHITE = white
    print(white)
    print("Finished calibrate")


def finish(infint: bool = False):
    if (DEBUG):
        print(stopwatch.time()//1000)
    if (DEBUG):
        print("finished!")
    ev3.screen.draw_text(10, 10, stopwatch.time()//1000,
                         text_color=Color.BLACK, background_color=None)
    wait(6000 if not infint else 999999999)


def test_calabrtion():
    while True:
        print((left_sensor.reflection() + right_sensor.reflection()))


def printValues(sensor):
    while True:
        h, s, v = sensor.hsv()
        wait(200)
        print(h)
        print(s)
        print(v)
        print("______________________________")


def getMising():
    global COLORS, WH
    first_four = COLORS[:4]
    cnt = [0, 0, 0, 0]
    for i, x in enumerate(first_four):
        if x != 0:
            cnt[x-1] += 1
            if cnt[x-1] > 1:
                COLORS[i] = 0
    existing_numbers = {x for x in first_four if x != 0}
    missing_numbers = [x for x in range(1, 5) if x not in existing_numbers]
    missing_index = 0
    res = []
    for i, num in enumerate(COLORS):
        if i < 4 and num == 0:
            res.append(missing_numbers[missing_index])
            missing_index += 1
        else:
            res.append(num)
    COLORS[:] = res
    print(COLORS)
# right_motor.reset_angle(0)
# right_motor.run_angle(speed=700, rotation_angle=565)
# wait(10)
# print(right_motor.angle())
# left_motor.reset_angle(0)
# wait_for_button_press()
# left_motor.run_angle(speed=700, rotation_angle=565)
# wait(10)
# print(left_motor.angle())
