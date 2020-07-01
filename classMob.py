from pygame import *
PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30

class Mob(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image.fill(Color("#F11032"))


        self.startX = x  # Начальная позиция Х и Y
        self.startY = y
        self.rect = self.image.get_rect(x = x, y = y) # прямоугольный объект(герой)

        self.xvel = 0.01  # скорость бега
        self.health = 40 #Здоровье
        #Запоминаем старовую точку отсчёта
        self.damage_timer = time.get_ticks() #https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks
        self.maxDistance = 24


    def update(self, *args):
        print(abs(self.startX - self.rect.x))
        print(self.startX )
        print(self.rect.x)
        print()

        # self.rect.x += self.xvel
        #
        #
        # if abs(self.startX - self.rect.x) >= self.maxDistance:
        #     print(abs(self.startX - self.rect.x))
        #
        #     self.xvel *= -1
        #     print(self.xvel)


