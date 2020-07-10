from pygame import *
from random import choice
from random import randint as r

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30
ANIMATION_SLOWNESS = 20
LASER_ANIMATION_SLOWNESS = 10
RAY_SPEED = 10
RAY_WIDTH = 15

'''spritesheet = image.load("textures/terrex_0.png")
images = [
    transform.scale(spritesheet.subsurface((25, 10, 60, 65)), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(spritesheet.subsurface((75, 10, 60, 65)), (PLATFORM_WIDTH, PLATFORM_HEIGHT))

]'''

move_animation = [
    transform.scale(image.load('textures/moveglaz1.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/glazmove2.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/glazmove3.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/glazmove4.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
]

death_animation = [
    transform.scale(image.load('textures/glazdie1.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/glazdie2.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/glazdie3.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/glazdie4.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
]

damage_animation = transform.scale(image.load('textures/glazdamage.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT))

laser_animation = [
    transform.scale(image.load('textures/laser1.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/laser2.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/laser3.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(image.load('textures/laser4.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
]

laser_static = transform.scale(image.load('textures/laser1.png'), (PLATFORM_WIDTH, PLATFORM_HEIGHT))

ray_image = transform.scale(image.load('textures/laser.png'), (RAY_WIDTH, 3))


class Mob(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.direction = 0
        self.damage_status = False
        self.death_status = False
        self.counter = 0
        self.counter1 = 0
        self.counter2 = 0
        self.start_x = x
        self.start_y = y
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = self.image.get_rect(x=x, y=y)
        self.x_vel = choice([1, -1])
        self.health = 40  # Здоровье
        self.damage_timer = time.get_ticks()
        self.maxDistance = 34

    def update(self, hero):
        self.rect.x += self.x_vel
        if abs(self.start_x - self.rect.x) >= self.maxDistance:
            self.x_vel *= -1

        if sprite.collide_rect(self, hero):
            if time.get_ticks() - self.damage_timer >= 500 and not self.death_status:
                hero.health -= 20
                self.damage_timer = time.get_ticks()

        if self.health <= 0:
            self.death_status = True

        self.animation()

    def animation(self):
        if self.death_status:
            if self.x_vel > 0:
                self.direction = 1
            self.image = (transform.flip(death_animation[self.counter2 // ANIMATION_SLOWNESS], True, False) if self.direction else death_animation[self.counter2 // ANIMATION_SLOWNESS])
            self.counter2 += 1
            self.x_vel = 0

        elif self.damage_status:
            if self.x_vel < 0:
                self.image = damage_animation
            else:
                self.image = transform.flip(damage_animation, True, False)
            self.counter1 += 1

        else:
            if self.x_vel < 0:
                self.image = move_animation[self.counter // ANIMATION_SLOWNESS]
            else:
                self.image = transform.flip(move_animation[self.counter // ANIMATION_SLOWNESS], True, False)
            self.counter += 1

        if self.counter == len(move_animation) * ANIMATION_SLOWNESS - 1:
            self.counter = 0

        if self.counter1 == 10:
            self.counter1 = 0
            self.damage_status = False

        if self.counter2 == len(death_animation) * ANIMATION_SLOWNESS - 1:
            self.counter2 = 0
            self.death_status = False
            self.kill()


class Ray(sprite.Sprite):
    def __init__(self, groups, laser):
        super().__init__(groups[0], groups[1])
        self.image = Surface((7, 5))
        self.rect = self.image.get_rect()
        self.direction = laser.direction
        self.laser = laser
        if self.direction:
            self.rect.midright = laser.rect.midleft
        else:
            self.rect.midleft = laser.rect.midright

    def update(self, platform_group, hero):
        self.rect.x += -self.direction * RAY_SPEED
        if sprite.collide_rect(self, hero):
            hero.health -= 50
            self.kill()
        for p in platform_group:
            if sprite.collide_rect(self, p):
                self.kill()
        self.animation()

    def animation(self):
        self.image = ray_image


class Laser(sprite.Sprite):
    def __init__(self, groups, x, y, direction):
        super().__init__(groups)
        self.direction = direction
        self.start_x = x
        self.start_y = y
        self.image = (laser_static if direction else transform.flip(laser_static, True, False))
        self.rect = self.image.get_rect(x=x, y=y)
        self.y_vel = -1
        self.height = 90
        self.move_status = True
        self.count = 0
        self.shoot_timer = time.get_ticks()

    def update(self, hero, ray_group, all_sprites):
        if self.move_status:
            self.rect.y += self.y_vel
        if abs(self.rect.y - self.start_y) >= self.height:
            self.y_vel *= -1
        if -15 < self.rect.y - hero.rect.y < 35 and time.get_ticks() - self.shoot_timer >= 1500 and (self.rect.x - hero.rect.x < 300 and self.direction or hero.rect.x - self.rect.x < 300 and self.direction == 0):
            self.move_status = False
            self.shoot_timer = time.get_ticks()
        self.animation(ray_group, all_sprites)

    def animation(self, ray_group, all_sprites):
        if self.move_status:
            self.image = (laser_static if self.direction else transform.flip(laser_static, True, False))
        else:
            self.image = (laser_animation[self.count // LASER_ANIMATION_SLOWNESS] if self.direction else transform.flip(laser_animation[self.count // LASER_ANIMATION_SLOWNESS], True, False))
            self.count += 1
            if self.count == len(laser_animation) * LASER_ANIMATION_SLOWNESS - 1:
                self.count = 0
                self.move_status = True
                Ray((ray_group, all_sprites), self)
