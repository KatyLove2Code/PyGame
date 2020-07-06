from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30





class Weapon(sprite.Sprite):
    def __init__(self, groups, hero):
        super().__init__(groups)
        self.image = image.load('data/sword.png')
        self.image.set_colorkey((255, 255, 255))
        self.hero = hero
        self.rect = self.image.get_rect()


    def update(self):
        self.rect.bottomleft = self.hero.rect.center






