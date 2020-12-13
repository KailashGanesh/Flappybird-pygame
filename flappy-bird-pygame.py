import pygame, sys

def draw_floor():
    """ draws two floor images one after the other to show a continuous animation"""
    screen.blit(floor_surface,(floor_x_pos,800))
    screen.blit(floor_surface,(floor_x_pos+576,800))

def create_pipe():
    new_pipe = pipe_surface.get_rect(midtop = (283,504))
    return new_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5 # moves the pipes to left by -5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_surface, pipe)

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

# load pipe image
pipe_surface = pygame.image.load('assets/sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) # trigger SPAWNPIPE every 1.2 secounds

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # Any key pressed down
            if event.key == pygame.K_SPACE: # Space = Jump
                bird_movement = 0 # remove gravity so that the -12 can lead to a jump
                bird_movement -= 12
        if event.type == SPAWNPIPE: # to spawn pipes
            pipe_list.append(create_pipe())
            print(pipe_list)

    screen.blit(bg_surface,(0,0)) # background images to screen
    
    # bird logic
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface,bird_rect) # bird image to center of screen

    # pipes logic
    pipe_list = move_pipe(pipe_list)
    draw_pipes(pipe_list)

    # floor logic - make the floor seem moving by adding a image of the floor to the right as the floor moves to the left
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0
    
    pygame.display.update() #updates the screen
    clock.tick(120) # 120 frames per secounds
