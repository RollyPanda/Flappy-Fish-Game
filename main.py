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
    for pipe in pipes[-4:]:
        pipe.centerx -= 5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes[-4:]:
        if pipe.bottom >= 1024:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)

def check_collision(pipes):
    for pipe in pipes[-4:]:
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

        fact_surface = game_font.render(f"Fact: {fact_text}", True, (255, 255, 255))
        fact_rect = fact_surface.get_rect(center = (288, 750))
        screen.blit(fact_surface, fact_rect)

        high_score_surface = game_font.render(f"High Score: {str(int(high_score))}", True, (255, 255, 255))
        high_score_rect = score_surface.get_rect(center = (288, 850))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    high_score = max(score, high_score)
    return high_score

# pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 3, buffer = 512)
pygame.init()
screen = pygame.display.set_mode((576, 1024))
clock = pygame.time.Clock()
game_font = pygame.font.Font("04B_19.ttf", 10)

# Game Variables
gravity = 0.25
bird_movement = 0
game_active = True
old_score = 0
score = 0
fact_text = random.choice(["Fresh water on earth is only 2.5 percent of the total water when 70 percent of the earth's surface is covered by water."
                            , "Around 70 percents of industrial waste is dumped to water.", "80 percent of the water pollution is caused due to domestic sewage.", 
                            "More than 6 billion pounds of garbage, mainly plastic end up in the oceans every year.",
                            "The contaminated water is the main cause of various diseases such as cholera and typhus.", 
                            "15 million children under the age of five years die every year from diseases caused by drinking contaminated water.",
                            "The nuclear crisis created by the tsunami of 2011, unleashed 11 million liters of radioactive water into the Pacific Ocean.", 
                            "The same tsunami debris created islands totaling 70 kilometers in length which float in the ocean.", 
                            " Asia has the highest number of contaminated rivers than any other continent, mainly of bacteria from human waste.",
                            "Almost two million tons of human waste are exposed daily to water.", "The Ganges river in India is considered the most polluted river in the world and contains dirt, garbage, dead animals and humans.",
                            "Underground Bangladeshi water is contaminated with arsenic, which is highly toxic, poisonous and carcinogenic.", 
                            "20 percent of groundwater in China which are used as drinking water contaminated with carcinogens.", 
                            "In America 40 percent of rivers and 46 percent of the lakes are polluted and unsuitable for swimming, fishing or any other activity."])
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

# flap_sound = pygame.mixer.Sound('sound/sfx_ocean-sounds.wav')
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
                # flap_sound.play()

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