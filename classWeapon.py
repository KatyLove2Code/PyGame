from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30

BULLET_SPEED = 15


'''class Weapon(sprite.Sprite):
    def __init__(self, groups, hero):
        super().__init__(groups)
        self.image = image.load('data/sword.png')
        self.image.set_colorkey((255, 255, 255))
        self.hero = hero
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.bottomleft = self.hero.rect.center'''


class Bullet(sprite.Sprite):
    def __init__(self, groups, hero):
        super().__init__(groups[0], groups[1])
        self.image = Surface((5, 3))
        self.rect = self.image.get_rect()
        self.direction = hero.direction
        if self.direction:
            self.rect.midleft = hero.rect.midright
        else:
            self.rect.midright = hero.rect.midleft

    def update(self, enemy_group, platform_group):
        self.rect.x += self.direction * BULLET_SPEED
        for e in enemy_group:
            if sprite.collide_rect(self, e):
                e.kill()
                self.kill()
        for p in platform_group:
            if sprite.collide_rect(self, p):
                self.kill()



