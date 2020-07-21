from pygame import *
from constants import *

PORTAL = USEREVENT+1


class Platform(sprite.Sprite):
    def __init__(self, groups, plat_type, x, y):
        super().__init__(groups[0], groups[1])
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = self.image.get_rect().move(x, y)

        if plat_type == PLATFORM:
            self.image = image.load("textures/block.png")

        elif plat_type == MOBS:
            self.color = Color("#011032")

        elif plat_type == TREASURE:
            self.color = Color("#555353")

        elif plat_type == LEVER:
            self.color = Color("#125364")
        else:
            self.color = (255, 0, 255)


portal = transform.scale(image.load("textures/portal2.png"), (PLATFORM_WIDTH, PLATFORM_HEIGHT) )


class Portal(sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        self.image = portal
        self.rect = self.image.get_rect().move(x, y)
        self.color = (255, 255, 0)
        self.group = groups[1]

    def update(self):
        if len(sprite.spritecollide(self, self.group, False)) > 1:
            event.post(event.Event(PORTAL))
