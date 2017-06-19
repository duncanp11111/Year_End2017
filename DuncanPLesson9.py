import pygame
import random
 
# Initialize the game engine
pygame.init()
 
BLACK = [0, 0, 0]
COL = [100, 50, 99]
COL2 = [12, 98, 200]
COL3 =[200, 251, 9]
COL4 = [175, 140, 70]
COL5 = [12, 241, 132]
 
# Set the height and width of the screen
SIZE = [700, 500]
 
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Rectangle")
rect_x = 50
rect_y = 50
rect_x2 = 100
rect_y2 = 100
rect_x3 = 150
rect_y3 = 150
rect_x4 = 200
rect_y4 = 200
rect_x5 = 250
rect_y5 = 250
rect_y_change = 5
rect_x_change = 5
rect_y2_change = 5
rect_x2_change = 5
rect_y3_change = 5
rect_x3_change = 5
rect_y4_change = 5
rect_x4_change = 5
rect_y5_change = 5
rect_x5_change = 5

clock = pygame.time.Clock()
 
# Loop until the user clicks the close button.
done = False
while not done:
 
    for event in pygame.event.get():   # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True   # Flag that we are done so we exit this loop
 
    # Set the screen background

    screen.fill(BLACK)
 
    pygame.draw.rect(screen, COL, [rect_x, rect_y, 50, 50]) 
    rect_x += rect_x_change
    rect_y += rect_y_change    
    pygame.draw.rect(screen, COL2, [rect_x2, rect_y2, 50, 50]) 
    rect_x2 += rect_x2_change
    rect_y2 += rect_y2_change    
    pygame.draw.rect(screen, COL3, [rect_x3, rect_y3, 50, 50]) 
    rect_x3 += rect_x3_change
    rect_y3 += rect_y3_change    
    pygame.draw.rect(screen, COL4, [rect_x4, rect_y4, 50, 50]) 
    rect_x4 += rect_x4_change
    rect_y4 += rect_y4_change    
    pygame.draw.rect(screen, COL5, [rect_x5, rect_y5, 50, 50]) 
    rect_x5 += rect_x5_change
    rect_y5 += rect_y5_change        
    
    
    if rect_y > 450 or rect_y < 0:
        rect_y_change = rect_y_change * -1
    if rect_x > 650 or rect_x < 0:
        rect_x_change = rect_x_change * -1    
    if rect_y2 > 450 or rect_y2 < 0:
        rect_y2_change = rect_y2_change * -1
    if rect_x2 > 650 or rect_x2 < 0:
        rect_x2_change = rect_x2_change * -1    
    if rect_y3 > 450 or rect_y3 < 0:
        rect_y3_change = rect_y3_change * -1
    if rect_x3 > 650 or rect_x3 < 0:
        rect_x3_change = rect_x3_change * -1    
    if rect_y4 > 450 or rect_y4 < 0:
        rect_y4_change = rect_y4_change * -1
    if rect_x4 > 650 or rect_x4 < 0:
        rect_x4_change = rect_x4_change * -1    
    if rect_y5 > 450 or rect_y5 < 0:
        rect_y5_change = rect_y5_change * -1
    if rect_x5 > 650 or rect_x5 < 0:
        rect_x5_change = rect_x5_change * -1



pygame.quit()