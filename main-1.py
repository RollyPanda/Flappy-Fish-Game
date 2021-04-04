import pygame, sys, random

def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 900))
    screen.blit(floor_surface, (floor_x_pos + 576, 900))

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop = (700, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom = (700, random_pipe_pos - 300))
    return bottom_pipe, top_pipe

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            death_sound.play()
            return False
    
    if bird_rect.top <= -100 or bird_rect.bottom >= 900:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center = (100, bird_rect.centery))
    return new_bird, new_bird_rect

def score_display(game_state):
    if game_state == 'main_game':
        score_surface = game_font.render(f"{int(score)}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)
    elif game_state == 'game_over':
        score_surface = game_font.render(f"Score: {int(score)}", True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (288, 100))
        screen.blit(score_surface, score_rect)

        high_score_surface = game_font.render(f"High Score: {str(int(high_score))}", True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center = (288, 850))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    high_score = max(score, high_score)
    return high_score

def frame_animation():
    new_frame = end_frames[frame_index]
    new_frame_rect = new_frame.get_rect(center = (100, frame_rect.centery))
    return new_frame, new_frame_rect

# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.ttf", 40)

# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
old_score = 0
score = 0
high_score = 0


# bg_surface original is assets/background-day.png
bg_surface = pygame.image.load('assets/background-sea-2.png').convert()
bg_surface = pygame.transform.scale2x(bg_surface)

floor_surface = pygame.image.load('assets/base-seaweed.png').convert_alpha()
floor_surface = pygame.transform.scale2x(floor_surface)
floor_x_pos = 0

# bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-downflap.png'))
# bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png'))
# bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/bluebird-upflap.png'))
bird_downflap = pygame.transform.scale2x(pygame.image.load('assets/fish-1.png')).convert_alpha()
bird_midflap = pygame.transform.scale2x(pygame.image.load('assets/fish-2.png')).convert_alpha()
bird_upflap = pygame.transform.scale2x(pygame.image.load('assets/fish-3.png')).convert_alpha()
bird_frames = [bird_downflap, bird_midflap, bird_upflap]
bird_index = 0
bird_surface = bird_frames[bird_index]
bird_rect = bird_surface.get_rect(center = (100, 512))

BIRDFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BIRDFLAP, 200)

# bird_surface original is assets/bluebird-midflap.png
# bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert_alpha()
# bird_surface = pygame.transform.scale2x(bird_surface)
# bird_rect = bird_surface.get_rect(center = (100, 512))

# pipe_surface original is assets/pipe-green.png
pipe_surface = pygame.image.load('assets/garbage.png').convert_alpha()
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [400, 600, 800] 

game_over_surface = pygame.transform.scale2x(pygame.image.load('assets/message.png').convert_alpha())
game_over_rect = game_over_surface.get_rect(center = (288, 512))
if True: 
    end_frame_1 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-1.png')).convert_alpha()
    end_frame_2 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-2.png')).convert_alpha()
    end_frame_3 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-3.png')).convert_alpha()
    end_frame_4 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-4.png')).convert_alpha()
    end_frame_5 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-5.png')).convert_alpha()
    end_frame_6 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-6.png')).convert_alpha()
    end_frame_7 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-7.png')).convert_alpha()
    end_frame_8 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-8.png')).convert_alpha()
    end_frame_9 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-9-1.png')).convert_alpha()
    end_frame_10 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-10.png')).convert_alpha()
    end_frame_11 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-11.png')).convert_alpha()
    end_frame_12 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-12.png')).convert_alpha()
    end_frame_13 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-14.png')).convert_alpha()
    end_frame_14 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-14.png')).convert_alpha()
    end_frame_15 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-15.png')).convert_alpha()
    end_frame_16 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-16.png')).convert_alpha()
    end_frame_17 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-17.png')).convert_alpha()
    end_frame_18 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-18.png')).convert_alpha()
    end_frame_19 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-19.png')).convert_alpha()
    end_frame_20 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-20.png')).convert_alpha()
    end_frame_21 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-21.png')).convert_alpha()
    end_frame_22 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-22.png')).convert_alpha()
    end_frame_23 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-23.png')).convert_alpha()
    end_frame_24 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-24.png')).convert_alpha()
    end_frame_25 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-25.png')).convert_alpha()
    end_frame_26 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-26.png')).convert_alpha()
    end_frame_27 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-27.png')).convert_alpha()
    end_frame_28 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-28.png')).convert_alpha()
    end_frame_29 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-29.png')).convert_alpha()
    end_frame_30 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-30.png')).convert_alpha()
    end_frame_31 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-31.png')).convert_alpha()
    end_frame_32 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-32.png')).convert_alpha()
    end_frame_33 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-33.png')).convert_alpha()
    end_frame_34 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-34.png')).convert_alpha()
    end_frame_35 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-35.png')).convert_alpha()
    end_frame_36 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-36.png')).convert_alpha()
    end_frame_37 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-37.png')).convert_alpha()
    end_frame_38 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-38.png')).convert_alpha()
    end_frame_39 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-39.png')).convert_alpha()
    end_frame_40 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-40.png')).convert_alpha()
    end_frame_41 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-41.png')).convert_alpha()
    end_frame_42 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-42.png')).convert_alpha()
    end_frame_43 = pygame.transform.scale2x(pygame.image.load('flappy_fish_end_frames/frame-43.png')).convert_alpha()

end_frames = [end_frame_1, end_frame_2, end_frame_3, end_frame_4, end_frame_5, end_frame_6, end_frame_7, end_frame_8, 
              end_frame_9, end_frame_10, end_frame_11, end_frame_12, end_frame_13, end_frame_14, end_frame_15, end_frame_16, 
              end_frame_17, end_frame_18, end_frame_19, end_frame_20, end_frame_21, end_frame_22, end_frame_23, end_frame_24, 
              end_frame_25, end_frame_26, end_frame_27, end_frame_28, end_frame_29, end_frame_30, end_frame_31, end_frame_32, 
              end_frame_33, end_frame_34, end_frame_35, end_frame_36, end_frame_37, end_frame_38, end_frame_39, end_frame_40, 
              end_frame_41, end_frame_42, end_frame_43]
SPAWNFRAME = pygame.USEREVENT
frame_index = 0
pygame.time.set_timer(SPAWNFRAME, 100)
frame_surface = end_frames[frame_index]
frame_rect = frame_surface.get_rect(center = (288, 512))

flap_sound = pygame.mixer.Sound('sound/sfx_ocean-sounds.wav')
death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
score_sound = pygame.mixer.Sound('sound/sfx_point.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key in [pygame.K_SPACE, pygame.K_UP] and game_active:
                bird_movement = 0
                # bird_movement here original is 12, but the smaller it is, the easier the game is
                bird_movement -= 7
                flap_sound.play()

            if event.key in [pygame.K_SPACE, pygame.K_UP] and not game_active:
                game_active = True
                pipe_list.clear()
                bird_rect.center = (100, 512)
                bird_movement = 0
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())
        if event.type == BIRDFLAP:
            if bird_index < len(bird_frames)-1:
                bird_index += 1
            else:
                bird_index = 0
            bird_surface, bird_rect = bird_animation()
    screen.blit(bg_surface, (0, 0))

    if game_active:
        # Bird

        bird_movement += gravity
        rotated_bird = rotate_bird(bird_surface)
        bird_rect.centery += bird_movement
        screen.blit(rotated_bird,bird_rect)
        game_active = check_collision(pipe_list)

        # Pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)
    
        score = len(pipe_list) / 2
        score_display('main_game')
        if old_score != score:
            score_sound.play()
            old_score = score

        if score >= 10:
            frame_surface, frame_rect = frame_animation()

    else:
        screen.blit(game_over_surface,game_over_rect)
        high_score = update_score(score, high_score)
        score_display('game_over')

    # Floor

    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -576:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)