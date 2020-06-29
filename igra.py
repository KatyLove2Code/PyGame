import pygame
from pygame import *
from classPlayer import Player  # импорт грока и файла
from classPlatform import *
from classSpikes import Spikes
from classCamera import Camera
from levels import levels

pygame.init()

# Объявляем переменные
W = 1920  # Ширина окна
H = 1080  # Высота окна
display = (W, H)
bg_color = "#000000"
platforms = []
spikes = []
fps = pygame.time.Clock()
x1, y1 = 0, 0

num_of_level=0 #0 -> первый уровень (n-1 -> n уровень)

all_sprites = pygame.sprite.Group()
player_group = pygame.sprite.Group()
platform_group = pygame.sprite.LayeredUpdates() #https://www.pygame.org/docs/ref/sprite.html#pygame.sprite.LayeredUpdates
spike_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
treasure_group = pygame.sprite.Group()
lever_group = pygame.sprite.Group()
deco_group = pygame.sprite.Group()


#pygame.time.set_timer(pygame.USEREVENT, 3000) #Событие будет генерироваться раз в 3 секунды

def draw_sprites(screen):
    all_sprites.draw(screen)

def draw_level(screen):
    x, y = 0, 0
    global x1, y1
    for row in levels[num_of_level]:
        for col in row:
            if col == "-":
                platform = Platform((platform_group, all_sprites), col, x, y)
                platforms.append(platform)
            elif col == "1":
                # platform = Platform((spike_group, all_sprites), col, x, y)
                spike = Spikes(("Spikes_CD.png", PLATFORM_WIDTH, PLATFORM_HEIGHT, False),
                               (spike_group, all_sprites), (x, y), 0)
                spikes.append(spike)
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
                x1, y1 = x, y
            x += PLATFORM_WIDTH  # блоки платформы ставятся на ширине блоков
        y += PLATFORM_HEIGHT  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля
    #Отрисовка уровня и создание платформ и спрайтов отдельной функцией или классом
    #ПРИ ПРОИГРЫШЕ МОЖНО УБИТЬ ОСТАВШХСЯ МОБОВ ВОИЗБЕЖАНИЕ ДУБЛИРОВАНИЯ
    #mob.kill() - убъёт спрайт во всех группах


def main():
    screen = pygame.display.set_mode(display, FULLSCREEN)
    pygame.display.set_caption("ultra_game")
    bg = Surface((W, H))  # Создание видимой поверхности для фона
    bg.fill(Color(bg_color))  # Заливаем поверхность
    draw_level(screen)
    hero = Player((player_group, all_sprites), x1, y1, [platform_group])  # создаем героя по x,y координатам
    camera = Camera((len(levels[0]), len(levels[num_of_level])), W, H)
    while 1:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                pygame.quit()
                quit()

            #if event.type == pygame.USEREVENT:
                #hero.damage()
        screen.fill(pygame.Color("black"))  # специально для обновления экрана
        #x = y = 0
        draw_sprites(screen)

        for i in spikes:
            i.update(hero, player_group)
        hero.update(platforms)  # передвижение
        camera.update(hero)
        for sprite in all_sprites:
            camera.apply(sprite)
        pygame.display.update()  # обновление и вывод всех изменений на экран

        fps.tick(60)


if __name__ == "__main__":
    main()
