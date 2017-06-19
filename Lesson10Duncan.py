"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame

 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREY = (211, 211, 211)
RED = (255, 0, 0)
GREEN2 = (0, 100, 0)
GREY2 = (139, 137, 137)
PINK = (255,171,244)
BROWN = (89,71,0)
YELLOW = (255,204,0)
CYAN = (0, 255, 255)
PURPLE = (160, 32, 240)
ORANGE = (255, 140, 0)
DARKGREY = (100, 100, 100)


#DEF DRAWINGS
def draw_house(COL, x, y):
    pygame.draw.rect(screen,COL,(x,y-100,200,100))
    pygame.draw.rect(screen,BROWN,(x+80,y-60,40,60))
    pygame.draw.circle(screen,YELLOW,(x+112,y-30),4)
    pygame.draw.polygon(screen, (125,125,125), ((x,y-100),(x+100,y-170),(x+200,y-100) ) )  
def draw_back(screen, x, y, change):
    pygame.draw.rect(screen, GREY2, [x, y+200, x+1400, y+75])
    pygame.draw.rect(screen, GREY2, [x, y+500, x+1400, y+75]) 
    pygame.draw.rect(screen, GREY2, [x+700, y, x+100, y+400])
    pygame.draw.rect(screen, GREY2, [x+650, y+600, x+100, y+800]) 
    pygame.draw.circle(screen, GREY2, (x+700, y+550), 200)
    pygame.draw.circle(screen, BLACK, (x+700, y+550), 50)
    pygame.draw.rect(screen, DARKGREY, [x, y+575, x+400, y+500])
    for i in range(3):
        for i in range(3):
            pygame.draw.line(screen, WHITE, (x, y+1000), (x, y+950), 5)
            x += change
        x = 1
        y -= (375/2)
def draw_car(screen, x, y):
    pygame.draw.rect(screen, BLACK, [x, y, 100, 30])
    pygame.draw.rect(screen, BLACK, [x+100, y+10, 10, 8])
    pygame.draw.line(screen, BLACK, (x+100, y+5), (x+130, y+25), 10)
    pygame.draw.line(screen, BLACK, (x+100, y+25), (x+130, y+24), 10)
    pygame.draw.ellipse(screen, BLACK, [x, y+30, 25, 25], 10)
    pygame.draw.ellipse(screen, BLACK, [x+75, y+30, 25, 25], 10)
    pygame.draw.line(screen, GREEN, (x, y+20), (x+119, y+20), 5) 
    pygame.draw.line(screen, GREY, (x+95, y), (x+80, y-20), 5)
def draw_car2(screen, x, y):
    pygame.draw.rect(screen, BLACK, [x, y, 100, 30])
    pygame.draw.rect(screen, BLACK, [x-10, y+10, 10, 8])
    pygame.draw.line(screen, BLACK, (x, y+5), (x-30, y+25), 10)
    pygame.draw.line(screen, BLACK, (x, y+24), (x-30, y+24), 10)
    pygame.draw.ellipse(screen, BLACK, [x, y+30, 25, 25], 10)
    pygame.draw.ellipse(screen, BLACK, [x+75, y+30, 25, 25], 10)
    pygame.draw.line(screen, RED, (x-20, y+20), (x+99, y+20), 5) 
    pygame.draw.line(screen, GREY, (x+5, y), (x+20, y-20), 5)
    

# Speed in pixels per frame
x_speed = 0
y_speed = 0
x2 = 0
y2 = 0

# Current position
x_coord = 10
y_coord = 10


pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1200, 1000)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Animation")

xpos = 0
ypos = 0
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
    pos = pygame.mouse.get_pos()
    x1 = pos[0]
    y1 = pos[1]     
    pygame.mouse.set_visible(0)
    
    if event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
        if event.key == pygame.K_LEFT:
            x_speed = -20
        elif event.key == pygame.K_RIGHT:
            x_speed = 20
        elif event.key == pygame.K_UP:
            y_speed = -20
        elif event.key == pygame.K_DOWN:
            y_speed = 20     
            
            
    # User let up on a key
    elif event.type == pygame.KEYUP:
        # If it is an arrow key, reset vector back to zero
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            x_speed = 0
        elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
            y_speed = 0

# Move the object according to the speed vector.
    x_coord += x_speed
    y_coord += y_speed
    x1 += x2
    y1 += y2
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    # --- Drawing code should go here
  
    
    if y_coord > 950:
        y_coord = 950
    elif y1 > 950:
        y1 = 50    
    elif y_coord < 20:
        y_coord = 20
    elif y1 < 20:
        y1 = 20 
    if x1 > 1100:
        x1 = 1100
    elif x_coord < 0:
        x_coord = 0
    elif x_coord > 1100:
        x_coord = 1100    
    elif x1 < 0:
        x1 = 0
   
    screen.fill(GREEN2)
    draw_back(screen, 0, 0, 199)
    draw_house(PINK, 50, 500)
    draw_house(RED, 300, 500)
    draw_house(GREEN, 950, 500)
    draw_house(CYAN, 50, 200)
    draw_house(PURPLE, 300, 200)
    draw_house(ORANGE, 950, 200)               
               
    draw_car(screen, x_coord, y_coord)
    draw_car2(screen, x1, y1)
    

        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()