import pygame, sys, random

def draw_floor():
    """ draws two floor images one after the other to show a continuous animation"""
    screen.blit(floor_surface,(floor_x_pos,800))
    screen.blit(floor_surface,(floor_x_pos+576,800))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700,random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700,random_pipe_pos-300))
    return bottom_pipe,top_pipe

def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -= 5 # moves the pipes to left by -5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1008: # if pipe is bottom pipe
            screen.blit(pipe_surface, pipe)
        else: # if pipe is top pipe flip it
            flip_pipe = pygame.transform.flip(pipe_surface, False,True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe): # checks if bird hits pipes
            return False
    if bird_rect.top <= -100 or bird_rect.bottom >= 900: # checks if bird is too high or low
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird,-bird_movement*3,1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100,bird_rect.centery))
    return new_bird,new_bird_rect

pygame.init()

# Game Varibles
display_size = (576,1024)
display_size = (567,1008)
gravity = 0.25 
bird_movement = 0
game_active = True

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
bird_downflap= pygame.transform.scale2x(pygame.image.load('assets/sprites/bluebird-downflap.png').convert_alpha())
bird_midflap= pygame.transform.scale2x(pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha())
bird_upflap= pygame.transform.scale2x(pygame.image.load('assets/sprites/bluebird-upflap.png').convert_alpha())
bird_frames = [bird_downflap,bird_midflap,bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100,504))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

#bird_surface = pygame.image.load('assets/sprites/bluebird-midflap.png').convert_alpha()
#bird_surface = pygame.transform.scale2x(bird_surface)

# load pipe image
pipe_surface = pygame.image.load('assets/sprites/pipe-green.png')
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200) # trigger SPAWNPIPE every 1.2 secounds
pipe_height = [400,600,700]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN: # Any key pressed down
            if event.key == pygame.K_SPACE and game_active: # Space = Jump
                bird_movement = 0 # remove gravity so that the -12 can lead to a jump
                bird_movement -= 12
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100,504)
                bird_movement = 0

        if event.type == SPAWNPIPE: # to spawn pipes
            pipe_list.extend(create_pipe())

        if event.type == BIRDFLAP:
            if bird_index < 2:
                bird_index += 1
            else:
                bird_index = 0
                
            bird_surface,bird_rect = bird_animation()

    screen.blit(bg_surface,(0,0)) # background images to screen
    
    if game_active:
        # bird logic
        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect) # bird image to center of screen
        game_active = check_collision(pipe_list) # check collisions with pipes

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
