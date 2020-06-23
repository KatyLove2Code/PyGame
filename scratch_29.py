"""
место под описание ошибок
"""

from pygame import *
SPIKES = "1" #шипы
MOBS = '2'
TRIGGER = '5'
TREASURE = '3'
PLATFORM_COLOR = "#ffffff"
PLATFORM_WIDTH = 30
PLATFORM_HEIGHT = 30
class Platform(sprite.Sprite):
    def __init__(self, groups, plat_type, x, y):
        super().__init__(groups[0], groups[1])
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        if plat_type == "-":
            self.image.fill(Color("#123456"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == SPIKES:
            self.image.fill(Color("#654321"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == "2":
            self.image.fill(Color("#011032"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == "3":
            self.image.fill(Color("#555353"))
            self.rect = self.image.get_rect().move(x, y)
        elif plat_type == "5":
            self.image.fill(Color("#125364"))
            self.rect = self.image.get_rect().move(x, y)

#1 - шипы
#2 - мобы
#5 - рычаг который триггерится при соприкосновении с игроком и убивающий то скопление из 4 мобов слева снизу от него
#3 - 'сокровище', типо бонуса
