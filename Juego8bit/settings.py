import pygame
import random

# Configuraciones generales del juego
res = (720, 720)
c1 = random.randint(125, 255)
c2 = random.randint(0, 255)
c3 = random.randint(0, 255)

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

color_list = [red, green, blue]
startl = (169, 169, 169)
startd = (100, 100, 100)

lead_x = 40
lead_y = 360
speed = 15
count = 0
