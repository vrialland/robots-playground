from elio import Buzzer, EyesMatrix, Motors
import analogio
import board
import pwmio
import time

# Tunes
# Imperial March (Tempo ~ 120 BPM, Beat = 0.5s)
IMPERIAL_MARCH = (
    (440, 0.5),  # A4
    (440, 0.5),  # A4
    (440, 0.5),  # A4
    (349.23, 0.35),  # F4
    (523.25, 0.15),  # C5
    (440, 0.5),  # A4
    (349.23, 0.35),  # F4
    (523.25, 0.15),  # C5
    (440, 1.0),  # A4
    (659.26, 0.5),  # E5
    (659.26, 0.5),  # E5
    (659.26, 0.5),  # E5
    (698.46, 0.35),  # F5
    (523.25, 0.15),  # C5
    (415.30, 0.5),  # G#4 (Ab4)
    (349.23, 0.35),  # F4
    (523.25, 0.15),  # C5
    (440, 1.0),  # A4
)

# Star Wars Main Theme (Tempo ~ 100 BPM, Beat = 0.6s)
STAR_WARS_THEME = (
    (392.00, 0.2),  # G4 (Triplet)
    (392.00, 0.2),  # G4
    (392.00, 0.2),  # G4
    (523.25, 1.2),  # C5 (Half)
    (783.99, 1.2),  # G5 (Half)
    (698.46, 0.2),  # F5 (Triplet)
    (659.26, 0.2),  # E5
    (587.33, 0.2),  # D5
    (1046.50, 1.2),  # C6 (Half)
    (783.99, 0.6),  # G5 (Quarter)
    (698.46, 0.2),  # F5 (Triplet)
    (659.26, 0.2),  # E5
    (587.33, 0.2),  # D5
    (1046.50, 1.2),  # C6 (Half)
    (783.99, 0.6),  # G5 (Quarter)
    (698.46, 0.2),  # F5 (Triplet)
    (659.26, 0.2),  # E5
    (698.46, 0.2),  # F5
    (587.33, 1.2),  # D5 (Half)
)

# Eyes
LIGHT_COLOR = (64, 64, 255)
DARK_COLOR = (128, 0, 0)

LIGHT_EYES = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
] * 2

DARK_EYES = [
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 1, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,

    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 1, 0, 0,
    0, 0, 0, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 1, 0,
    0, 1, 1, 1, 1, 1, 1, 0,
    0, 0, 1, 1, 1, 1, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,
]

STEPS = 12
VOLUME = 100

eyes_matrix = EyesMatrix(board.IO2)
buzzer = Buzzer(pwmio.PWMOut(board.IO17, variable_frequency=True))
AIN1 = pwmio.PWMOut(board.IO36)
AIN2 = pwmio.PWMOut(board.IO38)
BIN1 = pwmio.PWMOut(board.IO35)
BIN2 = pwmio.PWMOut(board.IO37)
battery_pin = analogio.AnalogIn(board.BATTERY)
motors = Motors(AIN1, AIN2, BIN1, BIN2, battery_pin)


def display_eyes(pattern, color):
    eyes_matrix.set_matrix_colors([color if value == 1 else 0 for value in pattern])


def fade_out(pattern, color, steps):
    r, g, b = color
    r_step = r // steps
    g_step = g // steps
    b_step = b // steps
    for i in range(steps):
        eyes_matrix.set_matrix_colors(
            [
                ((r - i * r_step), (g - i * g_step), (b - i * b_step))
                if value == 1
                else 0
                for value in pattern
            ]
        )
        time.sleep(0.15)
    eyes_matrix.set_matrix_colors([0] * 128)


def fade_in(pattern, color, steps):
    target_r, target_g, target_b = color
    r, g, b = 0, 0, 0
    r_step = target_r // steps
    g_step = target_g // steps
    b_step = target_b // steps
    for i in range(steps):
        eyes_matrix.set_matrix_colors(
            [
                ((r + i * r_step), (g + i * g_step), (b + i * b_step))
                if value == 1
                else 0
                for value in pattern
            ]
        )
        time.sleep(0.15)


def play_tune(tune, volume=VOLUME):
    for frequency, duration in tune:
        # Articulation: Play for 90% of duration, rest for 10%
        tone_duration = duration * 0.9
        pause_duration = duration * 0.1
        buzzer.play_tone(frequency, tone_duration, volume)
        time.sleep(pause_duration)


motors.move_forward()
display_eyes(LIGHT_EYES, LIGHT_COLOR)
play_tune(STAR_WARS_THEME)
motors.motor_stop()
fade_out(LIGHT_EYES, LIGHT_COLOR, STEPS)
time.sleep(1)
fade_in(DARK_EYES, DARK_COLOR, STEPS)
motors.move_forward()
display_eyes(DARK_EYES, DARK_COLOR)
play_tune(IMPERIAL_MARCH)
motors.motor_stop()
