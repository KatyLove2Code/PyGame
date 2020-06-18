import pygame
from load_file_lib import load_image, scales_and_mirrors

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
FPS = 60

spike_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()


class Spikes(pygame.sprite.Sprite):
    def __init__(self, image_tuple, coords, spike_speed=0):
        super().__init__(spike_group, all_sprites)
        self.image = scales_and_mirrors(image_tuple[0], image_tuple[1], image_tuple[2], image_tuple[3])
        self.rect = self.image.get_rect().move(coords)
        self.init_coord = coords
        self.spike_speed = spike_speed
        self.spikes_out = True
        self.spike_counter = spike_speed
        self.spike_anim_timer = 0

    def retract(self):
        self.rect.y += int(self.rect.width / 3)
        self.spike_anim_timer += 1
        if self.spike_anim_timer == 3 and self.rect.y != self.init_coord[1] + self.rect.width:
            self.rect.y = self.init_coord[1] + self.rect.width
            self.spikes_out = False
        elif self.spike_anim_timer == 3:
            self.spikes_out = False

    def pop_out(self):
        self.rect.y -= int(self.rect.width / 3)
        self.spike_anim_timer += 1
        if self.spike_anim_timer == 3 and self.rect.y != self.init_coord[1]:
            self.rect.y = self.init_coord[1]
            self.spikes_out = True
        elif self.spike_anim_timer == 3:
            self.spikes_out = True

    def update(self):
        if self.spike_speed > 0:
            if self.spike_counter > 0:
                self.spike_counter -= 1
            else:
                if self.spikes_out is True:
                    self.retract()
                else:
                    self.pop_out()
                if self.spike_anim_timer == 3:
                    self.spike_counter = self.spike_speed
                    self.spike_anim_timer = 0


def run_cycle():
    spike = Spikes(("Spikes_CD.png", 50, 50, False), (150, 150), 150)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill(pygame.Color(0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), (120, 200, 250, 140))
        spike.update()
        spike_group.draw(screen)
        pygame.display.flip()
        clock.tick(FPS)


run_cycle()
