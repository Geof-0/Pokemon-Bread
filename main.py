# main game logic here
# other files just import

import pokemon
import pokemon_battle
import pygame

pygame.init()


#frames setup
clock = pygame.time.Clock()
fps = 75

#screen setup
screen = pygame.display.set_mode((300, 200))
pygame.display.set_caption("Title_holder")


#main_loop

running = True
    
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.display.update()
    clock.tick(fps)

pygame.quit

