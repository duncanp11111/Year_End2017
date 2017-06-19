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

# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 10
y_coord = 10

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Animation")
 
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
 
    # --- Game logic should go here
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
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    def draw_car(screen, x, y):
        pygame.draw.rect(screen, BLACK, [x, y, 100, 30])
        pygame.draw.ellipse(screen, BLACK, [x, y+30, 25, 25], 10)
        pygame.draw.ellipse(screen, BLACK, [x+75, y+30, 25, 25], 10)
        pygame.draw.line(screen, GREEN, (x, y+20), (x+100, y+20), 5) 
        pygame.draw.line(screen, GREY, (x+95, y), (x+80, y-20), 5)     
    draw_car(screen, x_coord, y_coord)

        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()