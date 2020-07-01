import pygame
from pygame import *
from classPlayer import Player  # импорт грока и файла
from classPlatform import *
from classSpikes import Spikes
from classCamera import Camera
from levels import levels
from classMob import Mob

pygame.init()

# Объявляем переменные
W = 1920  # Ширина окна
H = 1080  # Высота окна
display = (W, H)
bg_color = "#000000"
spikes = []
fps = pygame.time.Clock()
x1, y1 = 0, 0

num_of_level = 0  # 0 -> первый уровень (n-1 -> n уровень)

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.LayeredUpdates()  # https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.LayeredUpdates
spike_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
lever_group = pygame.sprite.Group()
portal_group = pygame.sprite.Group()


# deco_group = pygame.sprite.Group()


def draw_level(screen):
    x, y = 0, 0
    global x1, y1
    for row in levels[num_of_level]:
        for col in row:
            if col == "-":
                Platform((platform_group, all_sprites), col, x, y)

            elif col == "1":
                Spikes(("Spikes_CD.png", PLATFORM_WIDTH, PLATFORM_HEIGHT, False),
                       (spike_group, all_sprites), (x, y), 0)
            elif col == "2":
                Mob((enemy_group, all_sprites),  x, y)

            elif col == "3":
                Platform((treasure_group, all_sprites), col, x, y)

            elif col == "5":
                Platform((lever_group, all_sprites), col, x, y)

            elif col == "6":
                Portal((portal_group, all_sprites), x, y)


            elif col == "x":
                x1, y1 = x, y
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    # Отрисовка уровня и создание платформ и спрайтов отдельной функцией или классом
    # ПРИ ПРОИГРЫШЕ МОЖНО УБИТЬ ОСТАВШХСЯ МОБОВ ВОИЗБЕЖАНИЕ ДУБЛИРОВАНИЯ
    # mob.kill() - убъёт спрайт во всех группах


def startLevel(screen):
    screen.fill(pygame.Color("black"))  # специально для обновления экрана
    draw_level(screen)


def restartLevel(hero, screen):
    for s in all_sprites:
        if s != hero:
            s.kill()
    print("Sprites left: ", len(all_sprites.sprites()))
    startLevel(screen)
    hero.smert(x1, y1)
    camera = Camera((len(levels[0]), len(levels[num_of_level])), W, H)
    return camera


def main():
    screen = pygame.display.set_mode(display, FULLSCREEN)
    pygame.display.set_caption("ultra_game")
    global num_of_level
    camera = Camera((len(levels[0]), len(levels[num_of_level])), W, H)
    startLevel(screen)
    hero = Player((player_group, all_sprites), x1, y1)  # создаем героя по x,y координатам

    game = True
    while game:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                game = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                game = False

            if e.type == PORTAL:
                num_of_level+=1
                camera = restartLevel(hero, screen)

        if hero.health <= 0:
            camera = restartLevel(hero, screen)

        screen.fill(pygame.Color("black"))  # специально для обновления экрана
        all_sprites.draw(screen)
        spike_group.update(hero, player_group)
        hero.update(platform_group)  # передвижение
        camera.update(hero)
        portal_group.update()
        enemy_group.update()
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.update()  # обновление и вывод всех изменений на экран

        fps.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
