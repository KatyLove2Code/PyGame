"""
крч, я не знаю, где ошибки, но он либо не ходит, либо не обновляет картинку
помогите пожалуйста
"""
import pygame
from pygame import *
from classPlayer import Player  # импорт грока и файла
from classPlatform import *
from classCamera import Camera
from levels import level_2, level

pygame.init()

# Объявляем переменные
W = 800  # Ширина окна
H = 640  # Высота окна
display = (W, H)
bg_color = "#000000"

fps = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()  # умоляю, пользуйтесь спрайт группами!
platform_group = pygame.sprite.LayeredUpdates() #https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.LayeredUpdates
spike_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
lever_group = pygame.sprite.Group()
deco_group = pygame.sprite.Group() #


#pygame.time.set_timer(pygame.USEREVENT, 3000) #Событие будет генерироваться раз в 3 секунды

def draw_sprites(screen):
    all_sprites.draw(screen)

def draw_level(number_of_level):
    pass
    #Отрисовка уровня и создание платформ и спрайтов отдельной функцией или классом
    #ПРИ ПРОИГРЫШЕ МОЖНО УБИТЬ ОСТАВШХСЯ МОБОВ ВОИЗБЕЖАНИЕ ДУБЛИРОВАНИЯ
    #mob.kill() - убъёт спрайт во всех группах


def main():
    screen = pygame.display.set_mode(display)
    pygame.display.set_caption("ultra_game")
    bg = Surface((W, H))  # Создание видимой поверхности для фона
    bg.fill(Color(bg_color))  # Заливаем поверхность
    left = right = up = False  # по умолчанию стоим
    # bg = pygame.Surface((wight, height))
    # bg.fill(pygame.Color(bg_color))
    x = y = 0
    for row in level_2:
        for col in row:
            if col == "-":
                platform = Platform((platform_group, all_sprites), col, x, y)
                # создаем блок, заливаем его цветом и рисеум его
                """
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))"""
            elif col == "1":
                platform = Platform((spike_group, all_sprites), col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "2":
                platform = Platform((enemy_group, all_sprites), col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "3":
                platform = Platform((treasure_group, all_sprites), col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "5":
                platform = Platform((lever_group, all_sprites), col, x, y)
                pf = pygame.Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
                pf.fill(pygame.Color(PLATFORM_COLOR))
                screen.blit(pf, (x, y))
            elif col == "x":
                hero = Player((player_group, all_sprites), x, y, [platform_group])  # создаем героя по x,y координатам
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    camera = Camera((len(level_2[0]), len(level_2)), W, H)
    while 1:  # Основной цикл программы
        for event in pygame.event.get():  # Обрабатываем события
            if event.type == QUIT:
                pygame.quit()
                quit()

            #if event.type == pygame.USEREVENT:
                #hero.damage()
        screen.fill(pygame.Color("black"))  # специально для обновления экрана
        x = y = 0
        draw_sprites(screen)

        hero.check_collide(platform_group)
        hero.update()  # передвижение
        camera.update(hero)
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.update()  # обновление и вывод всех изменений на экран

        fps.tick(60)


if __name__ == "__main__":
    main()
