import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (66, 89, 244)



def draw_clouds(screen, x, y):
    pygame.draw.circle(screen, WHITE, (x+25, y), 25)
    pygame.draw.circle(screen, WHITE, (x, y), 35)
    pygame.draw.circle(screen, WHITE, (x-25, y), 30)
    
def draw_car(screen, x, y):
    pygame.draw.circle(screen, BLACK, (x+90, y+50), 20)
    pygame.draw.circle(screen, BLACK, (x+10, y+50), 20)
    pygame.draw.rect(screen, RED, (x, y, 100, 30))
    pygame.draw.line(screen, RED, (x+99, y), (x+69, y-30), 4)
    
pygame.init() 

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Chapter 8 assignment") 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x_speed = 0
y_speed = 0
x_coord = 10
y_coord = 10
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        
        elif event.type == pygame.KEYDOWN:   
            if event.key == pygame.K_LEFT:
                x_speed = -3
            elif event.key == pygame.K_RIGHT:
                x_speed = 3
            elif event.key == pygame.K_UP:
                y_speed = -3
            elif event.key == pygame.K_DOWN:
                y_speed = 3
            
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_speed = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                y_speed = 0
                


    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed    
    # --- Game logic should go here
    if x_coord > 650:
        x_coord = 650
    elif x_coord < 0:
        x_coord = 0
    if y_coord > 475:
        y_coord = 475
    elif y_coord < 0:
        y_coord = 0
    
    
    
    
    
    pos = pygame.mouse.get_pos()
    x_mouse = pos[0]
    y_mouse = pos[1]    
        
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    pygame.draw.rect(screen, GREEN, (0, 0, 700, 500))    
    pygame.draw.rect(screen, BLUE, (0, 0, 700, 350))    
    draw_clouds(screen, x_mouse, y_mouse )
    draw_car(screen, x_coord, y_coord)
    #-----------------
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()