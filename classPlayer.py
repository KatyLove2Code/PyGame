from pygame import *

SPEED = 7
gg_wight = 25
gg_height = 50
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.5  # величина гравитации


class Player(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.xvel = 0  # скорость бега
        self.startX = x  # Начальная позиция Х и Y
        self.startY = y
        self.image = Surface((gg_wight, gg_height))
        self.image.fill(Color(COLOR))
        self.rect = self.image.get_rect()  # прямоугольный объект(герой)
        self.rect.x = self.startX
        self.rect.y = self.startY
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # стою на земле или нет
        self.health = 12000 #Здоровье
        #Запоминаем старовую точку отсчёта
        self.damage_timer = time.get_ticks() #https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks

    def update(self, platform_group):
        keys = key.get_pressed()
        self.image.fill(Color(COLOR))
        draw.rect(self.image, (255, 0, 0), (0,0, self.health // 4, 5))
        # ДВИЖЕНИЕ ПО ГОРИЗОНТАЛИ
        if keys[K_LEFT]:
            self.xvel = -SPEED  # Лево = x- n

        elif keys[K_RIGHT]:
            self.xvel = SPEED  # Право = x + n

        else:  # стоим, когда нет указаний идти
            self.xvel = 0

        # ПРЫЖОК
        if keys[K_SPACE]:
            if self.onGround:  # прыгаем только когда можем оттолкнуться от земли(потом сделаю двойной прыжок(как-хз пока что))
                self.yvel = -JUMP_POWER
                self.onGround = False

        # ГРАВИТАЦИЯ
        if not self.onGround:
            self.yvel += GRAVITY #Если не на земле, то действует гравитация
        else:
            self.yvel = 0

        self.onGround = False  # Мы не знаем, когда мы на земле
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platform_group)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platform_group)

        # self.rect.y += self.yvel
        # self.rect.y += self.yvel
        # self.collide(self.xvel, self.yvel, platforms)


    # ПРОВЕРКА СТОЛКНОВЕНИЙ
    def collide(self, xvel, yvel, platform_group):
        for p in platform_group:
            if sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                elif xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево


                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # и становится на что-то твердое
                    self.yvel = 0                 # и энергия падения пропадает

                elif yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадает

    def damage(self):
        if time.get_ticks() - self.damage_timer >= 1000: #Если с момента последнего урона прошло больше 1 секнды (1000 млс)
            self.health -= 40
            self.damage_timer = time.get_ticks()

    def smert(self, startX, startY ):
        self.rect.x = startX
        self.rect.y = startY
        self.health = 120
        self.yvel = 0
        self.xvel = 0
        self.onGround = False

if __name__ == "__main__":
    pass
