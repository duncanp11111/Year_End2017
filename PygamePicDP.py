import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SKY = (122, 222, 255)
PI = 3.1415926
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Microsoft Park")
 
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
    pygame.draw.rect(screen, GREEN, [0 , 300, 700, 500]) 
    pygame.draw.line(screen, BLACK, [350, 300], [350, 500], 5)
    pygame.draw.ellipse(screen, BLACK, [300, 350, 100, 100], 5)
    pygame.draw.line(screen, BLACK, [0, 350], [50, 350], 5)
    pygame.draw.line(screen, BLACK, [0, 450], [50, 450], 5)
    pygame.draw.line(screen, BLACK, [50, 350], [50, 450], 5)
    pygame.draw.line(screen, BLACK, [0, 375], [25, 375], 5)
    pygame.draw.line(screen, BLACK, [0, 425], [25, 425], 5)
    pygame.draw.line(screen, BLACK, [25, 375], [25, 425], 5)
    pygame.draw.line(screen, BLACK, [700, 350], [650, 350], 5)
    pygame.draw.line(screen, BLACK, [700, 450], [650, 450], 5)
    pygame.draw.line(screen, BLACK, [650, 350], [650, 450], 5)
    pygame.draw.line(screen, BLACK, [700, 375], [675, 375], 5)
    pygame.draw.line(screen, BLACK, [700, 425], [675, 425], 5)
    pygame.draw.line(screen, BLACK, [675, 375], [675, 425], 5)
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen, SKY, [100, 0+y_offset], [0, 200+y_offset], 10)
        y_offset += 1
    pygame.draw.rect(screen, SKY, [0, 0, 100, 100])
    pygame.draw.rect(screen, SKY, [0, 50, 50, 150])
    pygame.draw.line(screen, BLACK, [100, 100], [700, 100], 10)
    pygame.draw.line(screen, BLACK, [100, 100], [100, 0], 10)
    pygame.draw.line(screen, BLACK, [100, 100], [0, 300], 10)
    pygame.draw.rect(screen, RED, [130, 10, 25, 25])
    pygame.draw.rect(screen, RED, [160, 10, 25, 25])
    pygame.draw.rect(screen, RED, [130, 40, 25, 25])
    pygame.draw.rect(screen, RED, [160, 40, 25, 25])
    font = pygame.font.SysFont('Arial', 50, True, False)
    text = font.render("Microsoft Park", True, RED)
    screen.blit(text, [200, 10])
    x_offset = 0
    while x_offset < 699:
        pygame.draw.circle(screen, BLACK, (20+x_offset, 285), 5, 5)
        pygame.draw.circle(screen, BLACK, (30+x_offset, 265), 5, 5)
        pygame.draw.circle(screen, BLACK, (40+x_offset, 245), 5, 5)
        pygame.draw.circle(screen, BLACK, (50+x_offset, 225), 5, 5)
        pygame.draw.circle(screen, BLACK, (60+x_offset, 205), 5, 5)
        pygame.draw.circle(screen, BLACK, (70+x_offset, 185), 5, 5)
        pygame.draw.circle(screen, BLACK, (80+x_offset, 165), 5, 5) 
        pygame.draw.circle(screen, BLACK, (90+x_offset, 145), 5, 5)
        pygame.draw.circle(screen, BLACK, (100+x_offset, 125), 5, 5)
        x_offset += 20
    pygame.draw.circle(screen, RED, (300, 350), 5, 5)    
    pygame.draw.circle(screen, RED, (450, 450), 5, 5)  
    pygame.draw.circle(screen, RED, (515, 320), 5, 5)  
    pygame.draw.circle(screen, RED, (680, 400), 5, 5)  
    pygame.draw.circle(screen, RED, (600, 450), 5, 5)  
    
    pygame.draw.circle(screen, BLUE, (20, 400), 5, 5)  
    pygame.draw.circle(screen, BLUE, (100, 315), 5, 5)  
    pygame.draw.circle(screen, BLUE, (200, 450), 5, 5)  
    pygame.draw.circle(screen, BLUE, (250, 375), 5, 5)  
    pygame.draw.circle(screen, BLUE, (350, 425), 5, 5)  
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()