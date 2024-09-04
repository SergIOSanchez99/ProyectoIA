# Aquí podrías poner funciones auxiliares o constantes
import pygame

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
startl = (169, 169, 169)
startd = (100, 100, 100)

def render_text(screen, font, text, color, position):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, position)
