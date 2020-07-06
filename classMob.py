from pygame import *

PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30


class Mob(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color("#F11032"))

        self.start_x = x  # Начальная позиция Х и Y
        self.start_y = y
        self.rect = self.image.get_rect(x=x, y=y)  # прямоугольный объект(герой)

        self.x_vel = 1  # скорость бега
        self.health = 40  # Здоровье
        # Запоминаем старовую точку отсчёта
        self.damage_timer = time.get_ticks()  # https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks
        self.maxDistance = 24

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
