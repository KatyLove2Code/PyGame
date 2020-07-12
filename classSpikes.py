import pygame
from pygame import *
from random import choice

PLATFORM_WIDTH = 30
SPIKE_SPEED = 1
spike_image = transform.scale(image.load("textures/spikes1.png"), (30, 30))


class Spikes(pygame.sprite.Sprite):
    def __init__(self, group, x, y):
        super().__init__(group[0], group[1])
        self.start_x = x
        self.start_y = y
        self.spike_status = choice([-1, 1])
        self.height = 30 if self.spike_status > 0 else 0
        self.image = spike_image.subsurface((0, 0, PLATFORM_WIDTH, self.height))
        self.rect = self.image.get_rect(x=x, y=y + 30 - self.height)
        self.delay = time.get_ticks()

    def update(self, hero):
        if sprite.collide_rect(self, hero):
            hero.damage()
        if self.spike_status < 0 and time.get_ticks() - self.delay >= 2000 or self.height != 0:
            self.animation()

    def animation(self):
        self.height -= SPIKE_SPEED if self.spike_status > 0 else -SPIKE_SPEED
        if self.height == 0 or self.height == 30:
            self.spike_status *= -1

        self.image = spike_image.subsurface((0, 0, PLATFORM_WIDTH, self.height))
        self.rect = self.image.get_rect(x=self.start_x, y=self.start_y + 30 - self.height)
        self.delay = time.get_ticks()


