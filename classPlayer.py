import pygame
from pygame import *
#from classWeapon import Weapon

SPEED = 7
gg_wight = 25
gg_height = 50
COLOR = "#888888"
JUMP_POWER = 10
GRAVITY = 0.5  # величина гравитации
at_wight = 90
at_height = 140
COLOR_AT = "#efa94a"

images = [
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right1.png"), (gg_wight, gg_height)),

    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right2.png"), (gg_wight, gg_height)),

    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height)),
    transform.scale(image.load("textures/right3.png"), (gg_wight, gg_height))
]
died_image = transform.scale(image.load("textures/died.png"), (gg_wight, 20))
stand_image = transform.scale(image.load("textures/stand.png"), (gg_wight, gg_height))
shoot_image = transform.scale(image.load("textures/shoot_right.png"), (gg_wight, gg_height))


class Player(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.shoot_animation_status = False
        self.direction = 1
        self.y_max = 2000  # такое число взято от балды, оно просто должно быть больше нач. коорд. по y перса
        self.x_vel = 0  # скорость бега
        self.start_x = x  # Начальная позиция Х и Y
        self.start_y = y
        # self.image_r = Surface((gg_wight, gg_height)) #картинка идущего направо
        # self.image_r.fill(Color(COLOR))
        self.images = images
        self.count_animation = 0  # счётчик для списка картинок героя
        self.count_shoot_animation = 0
        self.image = self.images[self.count_animation]  # текущая картинка
        self.rect = self.image.get_rect(x=x, y=y)  # прямоугольный объект(герой)
        # self.rect.x = self.start_x
        # self.rect.y = self.start_y
        self.y_vel = 0  # скорость вертикального перемещения
        self.onGround = False  # стою на земле или нет
        self.health = 120  # Здоровье
        # Запоминаем старовую точку отсчёта
        self.damage_timer = time.get_ticks()  # https://www.pygame.org/docs/ref/time.html#pygame.time.get_ticks
        self.doubleJump = False
        self.doubleJump_timer = time.get_ticks()
        #self.weapon = Weapon(groups[1], self)
        self.attack = False

    def update(self, platform_group):
        keys = key.get_pressed()
        self.y_max = min(self.y_max,
                         self.rect.y)  # пока он не приземлится выщитываем наивысшую точку в которой он находился
        # ДВИЖЕНИЕ ПО ГОРИЗОНТАЛИ
        if keys[K_LEFT]:
            self.x_vel = -SPEED  # Лево = x- n
            self.direction = -1

        elif keys[K_RIGHT]:
            self.x_vel = SPEED  # Право = x + n
            self.direction = 1

        else:  # стоим, когда нет указаний идти
            self.x_vel = 0

        # ГРАВИТАЦИЯ
        if not self.onGround:
            self.y_vel += GRAVITY  # Если не на земле, то действует гравитация
        else:
            if self.rect.y - self.y_max > 240:  # получает по роже если спрыгнул на блок ниже высоты в 8 блоков, дамаг и порог его получения будут балансироваться...
                self.health -= 20
            self.y_max = 2000  # опаааааааааааа... вот он и на земле, значит ищем наивысшую точку по-новой
            self.y_vel = 0
            self.doubleJump = False

        self.animation()
        self.onGround = False  # Мы не знаем, когда мы на земле
        self.rect.y += self.y_vel
        self.collide(0, self.y_vel, platform_group)
        self.rect.x += self.x_vel
        self.collide(self.x_vel, 0, platform_group)

        # АТАКА
        #self.weapon.update()

    def jump(self):
        if self.onGround or not self.doubleJump:  # прыгаем только когда можем оттолкнуться от земли, не использовали двойной прыжок и с момента прыжка прошло пол секунды

            if self.y_vel not in [0, 0.5]:  # Если уже находится в прыжке, 0.5 проскакивает иногда если он стоит
                self.doubleJump = True

            self.y_vel = -JUMP_POWER
            self.onGround = False

    def animation(self):
        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)
        if self.shoot_animation_status:
            if self.direction > 0:
                self.image = shoot_image
            else:
                self.image = transform.flip(shoot_image, True, False)
        elif self.health <= 0:
            self.x_vel = 0
            self.image = died_image
        elif self.x_vel > 0:
            self.image = self.images[self.count_animation]
        elif self.x_vel < 0:
            self.image = transform.flip(self.images[self.count_animation], True, False)
        else:
            self.image = stand_image

        if self.count_animation != len(self.images) - 1:
            self.count_animation += 1
        else:
            self.count_animation = 0
        self.count_shoot_animation += 1
        if self.count_shoot_animation == 50:
            self.count_shoot_animation = 0
            self.shoot_animation_status = False

    # ПРОВЕРКА СТОЛКНОВЕНИЙ
    def collide(self, x_vel, y_vel, platform_group):
        for p in platform_group:
            if sprite.collide_rect(self, p):  # если есть пересечение платформы с игроком

                if x_vel > 0:  # если движется вправо
                    self.rect.right = p.rect.left  # то не движется вправо

                elif x_vel < 0:  # если движется влево
                    self.rect.left = p.rect.right  # то не движется влево

                if y_vel > 0:  # если падает вниз
                    self.rect.bottom = p.rect.top  # то не падает вниз
                    self.onGround = True  # и становится на что-то твердое
                    self.y_vel = 0  # и энергия падения пропадает

                elif y_vel < 0:  # если движется вверх
                    self.rect.top = p.rect.bottom  # то не движется вверх
                    self.y_vel = 0  # и энергия прыжка пропадает

    def damage(self):
        if time.get_ticks() - self.damage_timer >= 500:  # Если с момента последнего урона прошло больше 0.5 секнды (500 млс)
            self.health -= 40
            self.damage_timer = time.get_ticks()

    def death(self, start_x, start_y):
        self.rect.x = start_x
        self.rect.y = start_y
        self.health = 120
        self.y_vel = 0
        self.x_vel = 0
        self.onGround = False

    def explosion(self, enemy_group):
        """запускается нажатием кнопки "c"
        создать спрайт с центром в центре спрайтя игрока, который в каждую сторону на блок от игроа отходит
        проверить на столкновение этого спрайта с мобом
        запустить анимацию
        если сталкивается то удалить моба
        удалить спрайт"""
        for e in enemy_group:
            if self.rect.x-100 < e.rect.x and self.rect.x+100 < e.rect.x and self.rect.y-100 < e.rect.y and self.rect.y+100 < e.rect.y:
                e.kill()


if __name__ == "__main__":
    pass
