"""
место под описание ошибок
"""

from pygame import *

WIN_WIDTH = 1920
WIN_HEIGHT = 1080
BACKGROUND_COLOR = "#FFFFFF"
PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30
PLATFORM_COLOR = "#CD5700"
bg = Surface((WIN_WIDTH, WIN_HEIGHT))
Rect = bg.get_rect()

SPIKES = "1"  # шипы
MOBS = "2"  # мобы
TREASURE = "3"  # сокровище
LEVER = "5"  # рычаг который триггерится при соприкосновении с игроком и убивающий то скопление из 4 мобов слева снизу от него


class Platform(sprite.Sprite):
    def __init__(self, groups, plat_type, x, y):
        super().__init__(groups[0], groups[1])
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = self.image.get_rect().move(x, y)

        if plat_type == "-":
            self.color = Color("#123456")

        # elif plat_type == SPIKES:
        #     pass
        #     color = Color("#FFFFFF")

        elif plat_type == MOBS:
            self.color = Color("#011032")

        elif plat_type == TREASURE:
            self.color = Color("#555353")

        elif plat_type == LEVER:
            self.color = Color("#125364")
        else:
            self.color = (255, 0, 255)  # Если попался случайно не тот символ, то он подкрасится

        # self.image = image.load("textures/block.jpg")
        self.image.fill(self.color)
