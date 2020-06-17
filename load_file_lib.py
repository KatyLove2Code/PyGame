import pygame
import os


def load_image(name, color_key=None):
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert_alpha()

    if color_key is not None:
        if color_key is -1:
            color_key = image.get_at((0, 0))
        image.set_colorkey(color_key)
    return image


def load_sound(filename):
    filename = "data/" + filename
    sound = pygame.mixer.Sound(filename)
    return sound


def load_music(filename):
    filename = "data/" + filename
    music = pygame.mixer.music.load(filename)
    return music


def rot_center(image, rect, angle):
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def mirror_center(image, rect, x_tr, y_tr):
    mirr_image = pygame.transform.flip(image, x_tr, y_tr)
    mirr_rect = mirr_image.get_rect(center=rect.center)
    return mirr_image, mirr_rect


def scales_and_mirrors(image, scale_x, scale_y, mirror_flag, mirror_x=None, mirror_y=None):
    if mirror_flag is False:
        return pygame.transform.scale(load_image(image), (scale_x, scale_y))
    else:
        return pygame.transform.scale(mirror_center(load_image(image), load_image(image).get_rect(),
                                                    mirror_x, mirror_y)[0], (scale_x, scale_y))


def scales_and_rots(image, scale_x, scale_y, angle):
    return pygame.transform.scale(rot_center(load_image(image), load_image(image).get_rect(), angle)[0],
                                  (scale_x, scale_y))


def terminate():
    pygame.quit()
    sys.exit()
