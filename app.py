import pygame
import game_config as gc
from animal import Animal

from pygame import display, event, image

pygame.init()

display.set_caption('Matching Pictures')

screen = display.set_mode((512, 512))

matched = image.load('Other_Assets/matched.png')

tiles = [Animal(i) for i in range(0,gc.NUM_TILES_TOTAL)]

running = True

while running: 
    current_event = event.get()

    for e in current_event:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False
    screen.fill((255,255,255))

    for tile in tiles:
        screen.blit(tile.image,(tile.row*gc.IMAGE_SIZE + gc.MARGIN,tile.col*gc.IMAGE_SIZE + gc.MARGIN))
    
    display.flip()

print ("Good Bye")