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
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.xvel = 0  # скорость бега
        self.startX = x  # Начальная позиция Х и Y
        self.startY = y
        self.image = Surface((gg_wight, gg_height))
        self.image.fill(Color(COLOR))
        self.rect = Rect(x, y, gg_wight, gg_height)  # прямоугольный объект(герой)
        self.yvel = 0  # скорость вертикального перемещения
        self.onGround = False  # стою на земле или нет

    def update(self, left, right, up):
        if up:
            if self.onGround:  # прыгаем только когда можем оттолкнуться от земли(потом сделаю двойной прыжок(как-хз пока что))
                self.yvel = -JUMP_POWER

        if left==True:
            self.xvel -= speed  # Лево = x- n

        if right==True:
            self.xvel += speed # Право = x + n

        if  (left==False and right==False):  # стоим, когда нет указаний идти
            self.xvel = 0

        if not self.onGround:
            self.yvel += GRAVITY

        self.onGround = False;  # Мы не знаем, когда мы на земле
        self.rect.y += self.yvel
        self.rect.x += self.xvel  # переносим свои положение на xvel

    def draw(self, screen):  # Выводим себя на экран
        screen.blit(self.image, (self.rect.x, self.rect.y))
