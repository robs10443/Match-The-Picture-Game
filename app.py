import pygame
import game_config as gc
from animal import Animal

from pygame import display, event, image

pygame.init()

display.set_caption('Matching Pictures')

screen = display.set_mode((512, 512))

def find_index(x,y):
    row = x // gc.IMAGE_SIZE
    col = y // gc.IMAGE_SIZE
    return row*gc.NUM_TILES_SIDE + col


def display_message(msg,color,x,y,size):
    font = pygame.font.SysFont(None,size)
    screen_text = font.render(msg,True,color)
    screen.blit(screen_text,(x,y))
    return screen_text.get_rect()

running_starting_window = True

screen.fill((255,255,255))

while running_starting_window:
    current_event = event.get()
    x = gc.SCREEN_SIZE // 2 - 60
    y = gc.SCREEN_SIZE // 2 - 10
    left_top_x,left_top_y,right_bottom_x,right_bottom_y = display_message('START',(7,252,3),x,y,60)
    for e in current_event:
        if e.type == pygame.QUIT:
            exit()
            running_starting_window = False
        
        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            display_message('START',(7,252,3),x,y,60)
            if mouse_x >= x and mouse_y >= y and mouse_x <= x + right_bottom_x and mouse_y <= y + right_bottom_y :
                running_starting_window = False
    display.flip()

matched = image.load('Other_Assets/matched.png')

tiles = [Animal(i) for i in range(0,gc.NUM_TILES_TOTAL)]

screen.fill((255,255,255))

for tile in tiles:
    screen.blit(tile.image,(tile.row*gc.IMAGE_SIZE + gc.MARGIN,tile.col*gc.IMAGE_SIZE + gc.MARGIN))

display.flip()

pygame.time.wait(2000)

current_image_index = []

flag_for_delay = False

num_of_skips = 0

running = True

while running: 
    current_event = event.get()

    for e in current_event:
        if e.type == pygame.QUIT:
            running = False
        
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            index = find_index(mouse_x,mouse_y)
            if index not in current_image_index:
                current_image_index.append(index)
            if len(current_image_index) > 2:
                current_image_index = current_image_index[1:]


    screen.fill((255,255,255))

    for i,tile in enumerate(tiles):
        if tile.skip == False:
            if i in current_image_index:
                screen.blit(tile.image,(tile.row*gc.IMAGE_SIZE + gc.MARGIN,tile.col*gc.IMAGE_SIZE + gc.MARGIN))
            else:
                screen.blit(tile.box,(tile.row*gc.IMAGE_SIZE + gc.MARGIN,tile.col*gc.IMAGE_SIZE + gc.MARGIN))
    
    if (len(current_image_index) == 2):
        if (tiles[current_image_index[0]].name == tiles[current_image_index[1]].name):
            tiles[current_image_index[0]].skip = True
            tiles[current_image_index[1]].skip = True
            current_image_index = []
            display.flip()
            pygame.time.wait(500)
            num_of_skips += 2
            flag_for_delay = True
            screen.blit(matched,(0,0))

    display.flip()
    if flag_for_delay == True:
        pygame.time.wait(100)
        flag_for_delay = False
    
    if num_of_skips == gc.NUM_TILES_TOTAL:
        running = False


print ("Good Bye")