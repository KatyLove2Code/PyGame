from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30

BULLET_SPEED = 20

bullet_picture = image.load("textures/bulletSilverSilver_outline.png")

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
        self.image = Surface((7, 5))
        self.rect = self.image.get_rect()
        self.direction = hero.direction
        self.hero = hero
        if self.direction:
            self.rect.midleft = hero.rect.midright
        else:
            self.rect.midright = hero.rect.midleft

    def update(self, enemy_group, platform_group, laser_group):
        self.rect.x += self.direction * BULLET_SPEED
        for e in enemy_group:
            if sprite.collide_rect(self, e):
                e.health -= 30
                e.damage_status = True
                self.kill()
        for ls in laser_group:
            if sprite.collide_rect(self, ls):
                ls.kill()
                self.kill()
        for p in platform_group:
            if sprite.collide_rect(self, p):
                self.kill()
        self.animation()

    def animation(self):
        if self.hero.direction:
            self.image = transform.scale(bullet_picture, (7, 5))
        else:
            self.image = transform.flip(bullet_picture, True, False)



