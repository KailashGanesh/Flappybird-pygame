import pygame, sys

pygame.init()
display_size = (576,1024)
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.update() #updates the screen
    clock.tick(120) # 120 frames per secounds
