import pygame
from pygame import *
from classPlayer import Player
from classPlatform import *
from classSpikes import Spikes
from levels import levels
from classMob import Mob, Laser
from constants import *

pygame.init()
display = (WIN_WIDTH, WIN_HEIGHT)
surf = pygame.Surface((1000, 800))
fps = pygame. time.Clock()
x1, y1 = 0, 0
current_bullets = 10

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
laser_group = pygame.sprite.Group()
ray_group = pygame.sprite.Group()

background = image.load("textures/background.png")


def draw_level(screen):
    x, y = 0, 0
    global x1, y1
    for row in levels[num_of_level]:
        for col in row:
            if col == PLATFORM:
                Platform((platform_group, all_sprites), col, x, y)

            elif col == SPIKES:
                Spikes((spike_group, all_sprites), x, y)

            elif col == MOBS:
                Mob((enemy_group, all_sprites), x, y)

            elif col == TREASURE:
                Platform((treasure_group, all_sprites), col, x, y)

            elif col == LASER_RIGHT:
                Laser((laser_group, all_sprites), x, y, 0)

            elif col == LASER_LEFT:
                Laser((laser_group, all_sprites), x, y, 1)

            elif col == LEVER:
                Platform((lever_group, all_sprites), col, x, y)

            elif col == PORTALS:
                Portal((portal_group, all_sprites), x, y)

            elif col == HERO:
                x1, y1 = x, y
            x += PLATFORM_WIDTH
        y += PLATFORM_HEIGHT
        x = 0


def start_level(screen):
    screen.fill(pygame.Color("black"))  # специально для обновления экрана
    draw_level(screen)


def restart_level(hero, screen):
    for s in all_sprites:
        if s != hero:
            s.kill()
    start_level(screen)
    hero.death(x1, y1)
    global current_bullets
    current_bullets = 20


def main():
    global current_bullets
    disable_keyboard = False
    death_delay = 0
    current_bullets = 20
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

                if e.type == pygame.KEYDOWN and e.key == pygame.K_n:
                    hero.explosion(enemy_group)

                if e.type == pygame.KEYDOWN and e.key == pygame.K_b:
                    if current_bullets:
                        hero.shoot_animation_status = True
                    current_bullets -= (1 if current_bullets > 0 else 0)

        if hero.health <= 0:
            disable_keyboard = True
            if death_delay == 30:
                disable_keyboard = False
                restart_level(hero, screen)
                current_bullets = 10
                death_delay = 0
            death_delay += 1

        screen.fill(pygame.Color("black"))  # специально для обновления экрана
        screen.blit(surf, (460, 140))
        surf.blit(background, (0, 0))
        spike_group.update(hero)
        hero.update(platform_group, weapon_group, all_sprites)  # передвижение
        portal_group.update()
        enemy_group.update(hero)
        weapon_group.update(enemy_group, platform_group, laser_group)
        laser_group.update(hero, ray_group, all_sprites)
        ray_group.update(platform_group, hero)
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
