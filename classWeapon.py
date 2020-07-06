from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30





class Weapon(sprite.Sprite):
    def __init__(self, groups, hero):
        super().__init__(groups)
        self.image = Surface((25, 5))
        self.hero = hero
        self.rect = self.image.get_rect().move(self.hero.rect.x, self.hero.rect.y)
        self.image.fill((0,0,255))

    def update(self):
        self.rect.x = self.hero.rect.centerx
        self.rect.y = self.hero.rect.centery





