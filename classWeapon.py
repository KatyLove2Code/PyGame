from pygame import *

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30

BULLET_SPEED = 5

bullet_picture = transform.scale(image.load("textures/bulletSilverSilver_outline.png"), (7, 5))


class Bullet(sprite.Sprite):
    def __init__(self, groups, hero):
        super().__init__(groups[0], groups[1])
        self.direction = hero.direction
        if self.direction > 0:
            self.image = bullet_picture
            self.rect = self.image.get_rect()
            self.rect.midleft = hero.rect.midright
        else:
            self.image = transform.flip(bullet_picture, True, False)
            self.rect = self.image.get_rect()
            self.rect.midright = hero.rect.midleft

    def update(self, enemy_group, platform_group, laser_group):
        self.rect.x += self.direction * BULLET_SPEED
        for e in enemy_group:
            if sprite.collide_rect(self, e):
                e.health -= 20
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
        pass


