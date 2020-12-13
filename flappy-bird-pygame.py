import pygame, sys

def draw_floor():
    """ draws two floor images one after the other to show a continuous animation"""
    screen.blit(floor_surface,(floor_x_pos,800))
    screen.blit(floor_surface,(floor_x_pos+576,800))

pygame.init()

# Game Varibles
display_size = (576,1024)
display_size = (567,1008)
gravity = 0.25 
bird_movement = 0

# start screen and clock
screen = pygame.display.set_mode(display_size)
clock = pygame.time.Clock()

# load background image 
bg_surface = pygame.image.load('assets/sprites/background-day.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

# load floor image
floor_surface = pygame.image.load('assets/sprites/base.png').convert()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0  # sets floor postion

# load bird image
bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert()
bird_surface = pygame.transform.scale2x(bird_surface)
bird_rect = bird_surface.get_rect(center = (100,504))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # Any key pressed down
            if event.key == pygame.K_SPACE: # Space = Jump
                bird_movement = 0 # remove gravity so that the -12 can lead to a jump
                bird_movement -= 12
            
    screen.blit(bg_surface,(0,0)) # background images to screen
    
    # bird logic
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect) # bird image to center of screen

    # floor logic - make the floor seem moving by adding a image of the floor to the right as the floor moves to the left
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    
    pygame.display.update() #updates the screen
    clock.tick(120) # 120 frames per secounds
