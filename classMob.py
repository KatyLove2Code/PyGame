from pygame import *
from random import choice
from constants import *
from random import randint as r


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
        self.count = 1
        self.is_alive = True
        if self.direction:
            self.rect = self.image.get_rect(midright=laser.rect.midleft)
        else:
            self.rect = self.image.get_rect(midleft=laser.rect.midright)

    def update(self, platform_group, hero):
        self.animation()
        if self.is_alive:
            if self.direction:
                self.rect = self.image.get_rect(midright=(self.laser.rect.midleft[0] + 13, self.laser.rect.midleft[1]))
            else:
                self.rect = self.image.get_rect(midleft=(self.laser.rect.midright[0] - 13, self.laser.rect.midright[1]))
            if sprite.collide_rect(self, hero):
                hero.damage()
                self.is_alive = False
            else:
                for p in platform_group:
                    if sprite.collide_rect(self, p):
                        if self.direction:
                            self.image = transform.scale(ray_image, (self.laser.start_x - p.rect.midright[0] + PLATFORM_WIDTH // 2, 3))
                        else:
                            self.image = transform.scale(ray_image, (p.rect.midleft[0] - self.laser.start_x - PLATFORM_WIDTH // 2, 3))
                        self.is_alive = False
            if self.direction:
                self.rect = self.image.get_rect(midright=(self.laser.rect.midleft[0] + 13, self.laser.rect.midleft[1]))
            else:
                self.rect = self.image.get_rect(midleft=(self.laser.rect.midright[0] - 13, self.laser.rect.midright[1]))

    def animation(self):
        if not self.is_alive:
            self.kill()
            self.laser.move_status = True
        elif self.direction:
            self.image = transform.scale(ray_image, (self.count * RAY_SPEED, 3))
        else:
            self.image = transform.scale(ray_image, (self.count * RAY_SPEED, 3))
        self.count += 1


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
        self.in_range = False

    def update(self, hero, ray_group, all_sprites):
        if self.move_status:
            self.rect.y += self.y_vel
        if abs(self.rect.y - self.start_y) >= self.height:
            self.y_vel *= -1
        if -15 < self.rect.y - hero.rect.y < 35 and time.get_ticks() - self.shoot_timer >= 500 and (hero.rect.x < self.rect.x and self.rect.x - hero.rect.x < RAY_DISTANCE * PLATFORM_WIDTH and self.direction or hero.rect.x - self.rect.x < RAY_DISTANCE * PLATFORM_WIDTH and self.direction == 0 and hero.rect.x > self.rect.x):
            self.move_status = False
            self.shoot_timer = time.get_ticks()
        if not self.move_status and not ray_group:
            self.animation(ray_group, all_sprites)

    def animation(self, ray_group, all_sprites):
        self.image = (laser_animation[self.count // LASER_ANIMATION_SLOWNESS] if self.direction else transform.flip(laser_animation[self.count // LASER_ANIMATION_SLOWNESS], True, False))
        self.count += 1
        if self.count == len(laser_animation) * LASER_ANIMATION_SLOWNESS - 1:
            self.count = 0
            self.move_status = False
            Ray((ray_group, all_sprites), self)
            self.image = (laser_static if self.direction else transform.flip(laser_static, True, False))
