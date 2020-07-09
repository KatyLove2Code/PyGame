import pygame
from pygame import *
from classPlayer import Player, images  # импорт грока и файла
from classPlatform import *
from classSpikes import Spikes
from levels import levels
from classMob import Mob
from classWeapon import Bullet

pygame.init()

# Объявляем переменные
W = 1920  # Ширина окна
H = 1080  # Высота окна
display = (W, H)
surf = pygame.Surface((1000, 800))
bg_color = "#000000"
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
weapon_group = pygame.sprite.Group()

background = image.load("textures/background.png")


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
                Mob((enemy_group, all_sprites), x, y)

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


def start_level(screen):
    screen.fill(pygame.Color("black"))  # специально для обновления экрана
    draw_level(screen)


def restart_level(hero, screen):
    for s in all_sprites:
        if s != hero:
            s.kill()
    start_level(screen)
    hero.death(x1, y1)


def main():
    disable_keyboard = False
    death_delay = 0
    current_bullets = 10
    screen = pygame.display.set_mode(display, FULLSCREEN)
    pygame.display.set_caption("ultra_game")
    global num_of_level
    start_level(screen)
    hero = Player((player_group, all_sprites), x1, y1)  # создаем героя по x,y координатам
    game = True
    while game:  # Основной цикл программы
        for e in pygame.event.get():  # Обрабатываем события
            if e.type == QUIT:
                game = False

            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                game = False

            if not disable_keyboard:
                if e.type == PORTAL:
                    num_of_level += 1
                    restart_level(hero, screen)

                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    hero.jump()

<<<<<<< Updated upstream
            if e.type == pygame.KEYDOWN and e.key == pygame.K_n:
                hero.explosion(enemy_group)

            if e.type == pygame.KEYDOWN and e.key == pygame.K_b:
                hero.shoot_animation_status = True
                if current_bullets:
                    Bullet((weapon_group, all_sprites), hero)
                current_bullets -= (1 if current_bullets > 0 else 0)
=======
                if e.type == pygame.KEYDOWN and e.key == pygame.K_b:
                    hero.shoot_animation_status = True
                    if current_bullets:
                        Bullet((weapon_group, all_sprites), hero)
                    current_bullets -= (1 if current_bullets > 0 else 0)
>>>>>>> Stashed changes

        if hero.health <= 0:
            disable_keyboard = True
            if death_delay == 50:
                disable_keyboard = False
                restart_level(hero, screen)
                current_bullets = 10
                death_delay = 0
            death_delay += 1

        screen.fill(pygame.Color("black"))  # специально для обновления экрана
        screen.blit(surf, (460, 140))
        #
        surf.blit(background, (0, 0))

        spike_group.update(hero, player_group)
        hero.update(platform_group)  # передвижение
        portal_group.update()
        enemy_group.update(hero)
        for b in weapon_group:
            b.update(enemy_group, platform_group)
        for e in all_sprites:
            surf.blit(e.image, (
                e.rect.x - (0 if hero.rect.x < 500 else 900 if hero.rect.x > 1400 else hero.rect.x - 500),
                e.rect.y - (0 if hero.rect.y < 400 else 280 if hero.rect.y > 680 else hero.rect.y - 400)))
        draw.rect(screen, (200, 0, 0), (460, 125, (hero.health * 8.34 if hero.health > 0 else 0), 15)) #Шкала XP
        pygame.display.update()  # обновление и вывод всех изменений на экран
        fps.tick(60)
    pygame.quit()
    quit()


if __name__ == "__main__":
    main()
