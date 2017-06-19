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
PI = 3.1415926
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Game #1")
 
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
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [100,400,100,100], 2)    
    # Draw an ellipse, using a rectangle as the outside boundaries
    pygame.draw.ellipse(screen, BLACK, [400,400,100,100], 2)
    pygame.draw.line(screen, BLACK, [100, 400], [500, 400], 5)
    pygame.draw.arc(screen, GREEN, [100,300,200,200],  PI/2,     PI, 5)
    pygame.draw.line(screen, GREEN, [200, 300], [500, 300], 5)
    pygame.draw.line(screen, GREEN, [500, 300], [500, 400], 5)
    pygame.draw.line(screen, GREEN, [500, 300], [525, 275], 5)
    pygame.draw.line(screen, GREEN, [525, 275], [525, 375], 5)
    pygame.draw.line(screen, GREEN, [525, 375], [500, 400], 5)
    pygame.draw.line(screen, GREEN, [125, 375], [100, 400], 5)
    pygame.draw.arc(screen, GREEN, [125,275,200,200],  PI/2,     PI, 5)
    pygame.draw.line(screen, GREEN, [125, 375], [525, 375], 5)
    pygame.draw.line(screen, GREEN, [225, 275], [525, 275], 5)
    pygame.draw.line(screen, GREEN, [200, 300], [225, 275], 5)
    pygame.draw.line(screen, BLACK, [200, 300], [225, 250], 5)
    pygame.draw.line(screen, BLACK, [225, 275], [250, 225], 5)
    pygame.draw.line(screen, BLACK, [225, 250], [250, 225], 5)
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()