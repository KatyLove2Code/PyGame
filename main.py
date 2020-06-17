import pygame
import os
import sys
import ctypes
import random

pygame.init()
pygame.mixer.init()

FPS = 60

user32 = ctypes.windll.user32
print(user32.GetSystemMetrics(0), user32.GetSystemMetrics(1))
size = WIDTH, HEIGHT = int(user32.GetSystemMetrics(0) - user32.GetSystemMetrics(0) * 0.052), \
                       int(user32.GetSystemMetrics(1) - user32.GetSystemMetrics(1) * 0.092)

maindisplay = pygame.display.set_mode(size)
clock = pygame.time.Clock()

game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            
    maindisplay.fill((0, 134, 38))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
