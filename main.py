import pygame

maindisplay = pygame.display.set_mode((800, 600))

game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            
    maindisplay.fill((0, 134, 38))
    pygame.draw.rect(maindisplay, (255, 0, 0), (20, 120, 40, 150))
    pygame.display.update()

pygame.quit()
