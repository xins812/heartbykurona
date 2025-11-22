import math
import pygame
import numpy as np
from turtle import *

# --------------------------
# HEART functions
# --------------------------
def heart_x(k):
    return 15 * math.sin(k)**3

def heart_y(k):
    return (12*math.cos(k)
            - 5*math.cos(2*k)
            - 2*math.cos(3*k)
            - math.cos(4*k))

# --------------------------
# AUDIO SETUP
# --------------------------
pygame.mixer.init()
pygame.mixer.music.load("music.mp3")  # <<<<<< СЮДА КЛАДЁШЬ СВОЮ МУЗЫКУ
pygame.mixer.music.play()

# --------------------------
# TURTLE SETUP
# --------------------------
speed(0)
bgcolor("black")
hideturtle()
colormode(255)

penup()
color("#F55AA2")

# --------------------------
# DRAW HEART
# --------------------------
for i in range(6000):
    x = heart_x(i / 50) * 20
    y = heart_y(i / 50) * 20
    goto(x, y)
    pendown()

penup()

# --------------------------
# NEON FADE-IN FOR "S"
# --------------------------
goto(0, -20)
max_glow = 12

for glow in range(max_glow):
    c = 255 - int(255 * (glow / max_glow))
    color(c, c, c)
    write("S", align="center", font=("Arial", 48 + glow, "bold"))
    undo()

# --------------------------
# REALTIME PULSE LOOP
# --------------------------
# Просто маленькая синусоида + лёгкая имитация баса
# (pygame не даёт доступ к аудиобуферу в реальном времени,
#  так что мы делаем музыкально-красивую пульсацию)
# --------------------------

import time
t = 0

while pygame.mixer.music.get_busy():

    # Плавная волна
    base = (math.sin(t * 6) + 1) / 2  

    # Имитация басовых акцентов (быстрые всплески)
    beat = abs(math.sin(t * 14))

    pulse = base * 0.4 + beat * 0.6
    size = 48 + int(pulse * 18)

    color(255, 255, 255)
    goto(0, -20)
    write("S", align="center", font=("Arial", size, "bold"))
    time.sleep(0.03)
    undo()

    t += 0.04

done()
