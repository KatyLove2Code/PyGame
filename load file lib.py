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