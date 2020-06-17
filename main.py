import pygame

maindisplay = pygame.display.set_mode((800, 600))

game = True

while game:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            game = False
            
    maindisplay.fill((0, 134, 38))
    pygame.display.update()
pygame.quit()
    
