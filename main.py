# main game logic here
# other files just import

import pokemon
import pokemon_battle
import pygame


pygame.init()

#frames_setup    <-- percy what the hell is this, no space between the # and the comment? get better at commenting brochacho

size=[500,500]
clock = pygame.time.Clock()
fps = 75

#screen_setup    <-- percy what the hell is this, no space between the # and the comment? get better at commenting brochacho

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Title_holder")

#movement    <-- percy what the hell is this, no space between the # and the comment? get better at commenting brochacho

chr_x = 50
chr_y = 50
width = 40
height = 40
vel = 3

#main_loop    <-- percy what the hell is this, no space between the # and the comment? get better at commenting brochacho

running = True
    
while running:

    pygame.time.delay(10)


    for event in pygame.event.get():


        if event.type == pygame.QUIT:
            running = False


    #keyboard_presses    <-- percy what the hell is this, no space between the # and the comment? get better at commenting brochacho

    keys = pygame.key.get_pressed()

        #keyboard_movement_checks    <-- percy what the hell is this, no space between the # and the comment? get better at commenting brochacho
        
    if keys[pygame.K_w] and chr_y > 0:
        chr_y -= vel

    if keys[pygame.K_a] and chr_x > 0:
        chr_x -= vel

    if keys[pygame.K_s] and chr_y < screen_height - height:
        chr_y += vel

    if keys[pygame.K_d] and chr_x < screen_width - width:
        chr_x += vel


    screen.fill((0,0,0))
    pygame.draw.rect(screen, (255, 0, 0), (chr_x, chr_y, width, height))
    pygame.display.update()
    clock.tick(fps)


pygame.quit
