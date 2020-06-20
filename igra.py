"""
крч, я не знаю, где ошибки, но он либо не ходит, либо не обновляет картинку
помогите пожалуйста
"""
import pygame
from pygame import *
from player import Player  # импорт грока и файла
from scratch_29 import Platform
pygame.init()


# Объявляем переменные
wight = 800  # Ширина окна (это пишется, как "width", друг мой)
height = 640  # Высота окна
display = (wight, height)
bg_color = "#000000"
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#ffffff"
fps=pygame.time.Clock()
player_group = pygame.sprite.Group()  # умоляю, пользуйтесь спрайт группами!
platform_group = pygame.sprite.Group()
spike_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
lever_group = pygame.sprite.Group()
level = [
       "-------------------------",
       "-                       -",
       "-         ----          -",
       "-                       -",
       "-            --         -",
       "-                       -",
       "--                      -",
       "-          ----         -",
       "-                   --- -",
       "-                       -",
       "-                       -",
       "-      ---              -",
       "-                       -",
       "-   -----------         -",
       "-                       -",
       "-                -      -",
       "-          ----     --  -",
       "-                       -",
       "-                       -",
       "-------------------------"]

level_2 = ["----------------------------------------------------------------",
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"---0000000000000000000000000500000000000000000000000000000000---",
"---0000000000000000000000000000000000000000000000000000000030---",
"---0---------------200000000000000-00000000000--0000000000------",
"---00000000-0000000--000000000-000-0-000000000000-------00000---",
"---00000000-0000000000--000010-1-1-1-0000000-0000000000000000---",
"----0000000-020202020000000------------000000-000000000000000---",
"---01010100-----------00--00000000000000-0000-0000000-----00----",
"---0------00000000000000-000000000000000000000-00-00000000000---",
"---000000000000000000000-00010101001010-00000000000-0000000-----",
"---002000000000000001100000-------------00000000-000000000000---",
"---0------------------000-000000000000000000000-0000000000------",
"---0000000000000000000000-00002000200000000001-0000000--00000---",
"---0000000000000000000010-----------------000-000000000000000---",
"-------------------------0000000000000000000-00000000000-1000---",
"---000000000000000000000000000000000000000-----------------00---",
"---000000000000000000000000000000000000000000000000000000000----",
"---0000000000000000000010000000000000000000000020002000200000---",
"---00000000000000000000-000100000000---00-----------------------",
"---000------------00000000----------0000000000000000000000000---",
"----0000000000000-0-0000-000000000000000000000000000000000000---",
"-----000000000000-0000000000000000000001000000000000000000000---",
"------00000000000-0000000-0000000000000-0---00000000000000000---",
"---00000100000000-000-000000000--------0000-00000000000001000---",
"---000----1000000-00000000-0000000000000000-----0-0--0-----00---",
"---000--------001-000000000000000010000010000000000000000000----",
"---000000000000---0-0000000-1010-0-0000--00000000000000000000---",
"---000000000000---0000000000---00000--000000000000000000000-----",
"---0000000--------000000000000000000--000-0000001010010000------",
"---0000000--------000-00--000000------0000000----------00-------",
"---000------------11111111100000------1000-000000000000110000---",
"----------------------------------------------------------------",
"----------------------------------------------------------------",
"----------------------------------------------------------------"]


def draw_sprites(screen):
    player_group.draw(screen)
    platform_group.draw(screen)
    spike_group.draw(screen)
    enemy_group.draw(screen)
    treasure_group.draw(screen)
    lever_group.draw(screen)


def main():
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("utra_game")
    bg = Surface((wight, height))  # Создание видимой поверхности для фона
    bg.fill(Color(bg_color))  # Заливаем поверхность
    hero = Player(player_group, 55, 55)  # создаем героя по x,y координатам
    left = right = up = False  # по умолчанию стоим

    # bg = pygame.Surface((wight, height))
    # bg.fill(pygame.Color(bg_color))
    x = y = 0
    for row in level_2:
        for col in row:
            if col == "-":
                platform = Platform(platform_group, col, x, y)
                # создаем блок, заливаем его цветом и рисеум его
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "1":
                platform = Platform(spike_group, col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "2":
                platform = Platform(enemy_group, col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "3":
                platform = Platform(treasure_group, col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "5":
                platform = Platform(lever_group, col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    while 1:  # Основной цикл программы
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                pygame.quit()
                quit()
            if event.type == KEYDOWN and event.key == K_LEFT:
                left = True
            if event.type == KEYDOWN and event.key == K_RIGHT:
                right = True
            if event.type == KEYDOWN and event.key == K_SPACE:
                up = True

            if event.type == KEYUP and event.key == K_SPACE:
                up = False
            if event.type == KEYUP and event.key == K_RIGHT:
                right = False
            if event.type == KEYUP and event.key == K_LEFT:
                left = False

        screen.fill(pygame.Color("black"))  # специально для обновления экрана
        x = y = 0
        for row in level_2:
            for col in row:
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(pygame.Color(PLATFORM_COLOR))
                    screen.blit(pf, (x, y))
                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля
        draw_sprites(screen)
        hero.update(left, right, up)  # передвижение
        pygame.display.flip()  # обновление и вывод всех изменений на экран

        fps.tick(60)


if __name__ == "__main__":
    main()