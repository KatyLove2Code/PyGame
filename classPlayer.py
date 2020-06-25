"""
крч, я не знаю, где ошибки, но он либо не ходит, либо не обновляет картинку
помогите пожалуйста
"""

from pygame import *

speed = 7
gg_wight = 30
gg_height = 50
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.5  # величина гравитации


class Player(sprite.Sprite):
    def __init__(self, groups, x, y, collide_with):
        super().__init__(groups[0], groups[1])
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
        self.collide_with = collide_with  # группы, с которыми игрок может взаимодействовать
        self.health = 120 #Здоровье

    def update(self):
        keys = key.get_pressed()
        self.image.fill(Color(COLOR))
        draw.rect(self.image, (255, 0, 0), (0,0, self.health//4, 5))

        # ДВИЖЕНИЕ ПО ГОРИЗОНТАЛИ
        if keys[K_LEFT]:
            self.xvel = -speed  # Лево = x- n

        elif keys[K_RIGHT]:
            self.xvel = speed  # Право = x + n

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

        # self.onGround = False;  # Мы не знаем, когда мы на земле
        self.rect.y += self.yvel
        self.rect.x += self.xvel  # переносим свои положение на xvel


    # ПРОВЕРКА СТОЛКНОВЕНИЙ
    def check_collide(self, platforms):

        # if sprite.spritecollideany(self, self.collide_with[0]) is not None: #Столкнулся с чем-то, нужно проверить с чем или кем(мобы)
        #
        #       if len(platforms.get_sprites_at(self.rect.midbottom)) != 0:  #если середина низа пересекается с платформой, то на земле
        #           self.onGround = True
        #       else:
        #           self.onGround = False        #
        #
        # else:  #мы падаем
        #      self.onGround = False
        #
        # КОД НЕ АКТУАЛЕН, НИЖЕ РАСШИРЕННАЯ ПРОВЕРКА
        self.onGround = False #По умолчанию считаем, что падает, пока не докажет обратное
         #Проверяем столкновения с платформами
        for p in platforms:
            playerRange = set(range(self.rect.left, self.rect.right))
            platformRange = set(range(p.rect.left, p.rect.right))
            intersect = playerRange & platformRange ##https://pythonworld.ru/tipy-dannyx-v-python/mnozhestva-set-i-frozenset.html
            if self.rect.bottom == p.rect.top and len(intersect) != 0:
                self.onGround = True

            elif p.rect.bottom > self.rect.bottom > p.rect.top and len(intersect) != 0:

                self.rect.bottom = p.rect.top
                self.onGround = True


        print(self.onGround)

    def damage(self):
        self.health -= 40




if __name__ == "__main__":
    pass



"""
for p in platforms:
    if player.rect.bottom == p.rect.top or player.colliderect(p):
        #игрок не падает

"""
