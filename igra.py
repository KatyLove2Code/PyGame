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
    for row in level:
        for col in row:
            if col == "-":
                platform = Platform(platform_group, x, y)
                # создаем блок, заливаем его цветом и рисеум его
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
        for row in level:
            for col in row:
                if col == "-":
                    # создаем блок, заливаем его цветом и рисеум его
                    pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                    pf.fill(pygame.Color(PLATFORM_COLOR))
                    screen.blit(pf, (x, y))
                x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
            y += PLATFORM_HEIGHT  # то же самое и с высотой
            x = 0  # на каждой новой строчке начинаем с нуля
        player_group.draw(screen)
        platform_group.draw(screen)
        hero.update(left, right, up)  # передвижение
        pygame.display.flip()  # обновление и вывод всех изменений на экран

        fps.tick(60)


if __name__ == "__main__":
    main()