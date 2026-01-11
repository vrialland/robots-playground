"""
This module defines semantic names for the Eliobot board pins.

It provides a mapping between the raw hardware definitions
and meaningful variable names representing specific robot components (e.g., motors, LEDs, sensors).
"""

import board

BATTERY = board.BATTERY
BUTTON = board.IO0
BUZZER = board.IO17
LED = board.NEOPIXEL

# Obstacle sensors
OBSTACLE_SENSOR_FRONT_LEFT = board.IO4
OBSTACLE_SENSOR_FRONT = board.IO5
OBSTACLE_SENSOR_FRONT_RIGHT = board.IO6
OBSTACLE_SENSOR_REAR = board.IO7

# Line sensors pins
LINE_SENSOR_OUTER_LEFT = board.IO10
LINE_SENSOR_INNER_LEFT = board.IO11
LINE_SENSOR_CENTER = board.IO12
LINE_SENSOR_INNER_RIGHT = board.IO13
LINE_SENSOR_OUTER_RIGHT = board.IO14

# Motors
MOTOR_LEFT_FORWARD = board.IO38
MOTOR_LEFT_BACKWARD = board.IO36
MOTOR_RIGHT_FORWARD = board.IO37
MOTOR_RIGHT_BACKWARD = board.IO35
