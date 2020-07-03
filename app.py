import pygame

from pygame import display, event, image

pygame.init()

display.set_caption('Matching Pictures')

screen = display.set_mode((512, 512))

matched = image.load('Other_Assets/matched.png')
screen.blit(matched, (0,0))
display.flip()

running = True

while running: 
    current_event = event.get()

    for e in current_event:
        if e.type == pygame.QUIT:
            running = False
    
print ("Good Bye")