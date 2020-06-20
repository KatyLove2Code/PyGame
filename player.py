"""
крч, я не знаю, где ошибки, но он либо не ходит, либо не обновляет картинку
помогите пожалуйста
"""

from pygame import *

speed = 7
gg_wight=30
gg_height= 50
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
        self.rect = Rect(x, y, gg_wight, gg_height)  # прямоугольный объект(герой)
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # стою на земле или нет
        self.collide_with = collide_with  # группы, с которыми игрок может взаимодействовать

    def update(self, left, right, up):
        if up:
            if self.onGround:  # прыгаем только когда можем оттолкнуться от земли(потом сделаю двойной прыжок(как-хз пока что))
                self.yvel = -JUMP_POWER
                self.onGround = False

        if left is True:
            self.xvel = -speed  # Лево = x- n

        if right is True:
            self.xvel = speed  # Право = x + n

        if left is False and right is False:  # стоим, когда нет указаний идти
            self.xvel = 0
            if self.onGround is True:
                self.yvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        if sprite.spritecollideany(self, self.collide_with[0]) is not None:
            self.onGround = True
        else:
            self.onGround = False

        # self.onGround = False;  # Мы не знаем, когда мы на земле
        self.rect.y += self.yvel
        self.rect.x += self.xvel  # переносим свои положение на xvel

    '''def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))'''
