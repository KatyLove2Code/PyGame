from pygame import *
from random import choice
from random import randint as r

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30

spritesheet = image.load("textures/terrex_0.png")
images = [
    transform.scale(spritesheet.subsurface((25, 10, 60, 65)), (PLATFORM_WIDTH, PLATFORM_HEIGHT)),
    transform.scale(spritesheet.subsurface((75, 10, 60, 65)), (PLATFORM_WIDTH, PLATFORM_HEIGHT))

]


class Mob(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        # self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        # self.image.fill(Color("#F11032"))

        self.images = images
        self.countanimation = 0
        self.image = self.images[self.countanimation]

        self.start_x = x  # Начальная позиция Х и Y
        self.start_y = y
        self.rect = self.image.get_rect(x=x, y=y)  # прямоугольный объект(герой)

        self.x_vel = 1 * choice([-1, 1])  # скорость бега
        self.health = 40  # Здоровье
        # Запоминаем старовую точку отсчёта
        self.damage_timer = time.get_ticks()  # https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks
        self.maxDistance = 24
        self.rect.x += r(0, self.maxDistance)

    def update(self, hero):

        self.rect.x += self.x_vel

        if abs(self.start_x - self.rect.x) >= self.maxDistance:
            self.x_vel *= -1
        if sprite.collide_rect(self, hero):
            print('hero collide')
            print(hero.weapon)
            # hero.health -= 10
            # self.kill()
        keys = key.get_pressed()
        if keys[K_c]:
            if sprite.collide_rect(self, hero.weapon):
                self.kill()
                print("Collide")

    # def animation(self):
