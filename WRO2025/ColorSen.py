#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import ColorSensor  # type: ignore
from pybricks.parameters import Port, Direction, Color, Stop  # type: ignore
from constants import *


def rgb_to_hsv(rgb):
    r, g, b = rgb
    r_normalized = r / 255.0
    g_normalized = g / 255.0
    b_normalized = b / 255.0
    max_val = max(r_normalized, g_normalized, b_normalized)
    min_val = min(r_normalized, g_normalized, b_normalized)
    delta = max_val - min_val
    if delta == 0:
        h = 0
    elif max_val == r_normalized:
        h = 60 * (((g_normalized - b_normalized) / delta) % 6)
    elif max_val == g_normalized:
        h = 60 * (((b_normalized - r_normalized) / delta) + 2)
    elif max_val == b_normalized:
        h = 60 * (((r_normalized - g_normalized) / delta) + 4)
    s = 0 if max_val == 0 else (delta / max_val)
    v = max_val
    h = h if h >= 0 else h + 360
    s = s * 100
    v = v * 100
    return (h, s, v)


class ColorSen(ColorSensor):
    def reflection(self):
        ref = super().reflection()
        ref -= BLACK
        ref *= 100/(WHITE-BLACK)
        return ref

    def rawRef(self):
        return super().reflection()

    def hsv(self):
        return rgb_to_hsv(self.rgb())
