import pygame
import random

#Define some colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)
move = 3
background_image = pygame.image.load("space.jpg").convert()
#CLASSES

#Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self, width0, height0, width, height):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)

        pygame.draw.ellipse(self.image, YELLOW, [width0, height0, width, height])
        
        self.rect = self.image.get_rect()
        
    def reset_pos(self):
        
        self.rect.x = random.randrange(0, screen_width)
        self.rect.y = random.randrange(0, screen_height)

#Asteroid class
class asteriod(pygame.sprite.Sprite):
    def __init__(self):
    
        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Load the image
        self.image = pygame.image.load("Asteroid.bmp").convert()
    
        # Set transparent color
        self.image.set_colorkey(BLACK)
        
        self.rect = self.image.get_rect() 
        
    def update(self):
        #Move bullet
        self.rect.x -= move
        self.rect.y -= move
        
#Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
    
        # Load the image
        self.image = pygame.image.load("Spaceship.bmp").convert()
    
        # Set transparent color
        self.image.set_colorkey(WHITE)
        
        self.rect = self.image.get_rect()  
    def update(self):
        #Update player position
        #Get the current mouse position
        pos = pygame.mouse.get_pos()
        
        #Set the player's x and y positions to the mouses coordinates
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        
#Create the window

#Initialize Pygame
pygame.init()

#Set perameters for the screen
screen_width = 700
screen_height = 400
screen = pygame.display.set_mode([screen_width, screen_height])

#Define Font
font = pygame.font.Font(None, 36)

#Instructions
display_instructions = True
instruction_page = 1
name = ""

#Instruction Loop
done = False
while not done and display_instructions:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.unicode.isalpha():
                name += event.unicode
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif event.key == pygame.K_RETURN:
                instruction_page += 1
                if instruction_page == 4:
                    display_instructions = False

    screen.fill(BLACK)    
    screen.blit(background_image, [0 , 0])
    
    if instruction_page == 1:
        """Draws title for the game"""
        text = font.render("Space Hopper", True, RED)
        screen.blit(text, [350, 200])
        
        text = font.render("Current High Score is: ", True, WHITE)
        screen.blit(text, [100, 250])
        
        """text = font.render()
        screen.blit(text, [310, 250])"""
        
    if instruction_page == 2:
        """Draws the instructions for page 1"""
        text = font.render("Instructions", True, WHITE)
        screen.blit(text, [10, 10])
        
        text = font.render("Enter your name: ", True, WHITE)
        screen.blit(text, [10, 40])     
        
        text = font.render(name, True, WHITE)
        screen.blit(text, [220, 40])
        
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 80])
        
        text = font.render("Page 1", True, WHITE)
        screen.blit(text, [10, 120])      
        
    if instruction_page == 3:
        """Draws the instructions for page 2"""
        text = font.render("This program throws asteroids towards you.\n Avoid the asteroids and collect all of the coins to progress through the levels.", True, WHITE)
        screen.blit(text, [10, 10])
        
        text = font.render("Hit enter to continue", True, WHITE)
        screen.blit(text, [10, 40])        
        
        text = font.render("During the game, hit enter to end the game.", True, WHITE)
        screen.blit(text, [10, 80])
        
        text = font.render("Page 2", True, WHITE)
        screen.blit(text, [10, 120])        

#Sprite lists

#all spirtes
all_sprites_list = pygame.sprite.Group()

#List of each coin
coin_list = pygame.sprite.Group()

#List of each asteroid
asteroid_list = pygame.sprite.Group()

#Create Sprites

for i in range(10):
    #Coin
    coin = Coin()
    
    #Set a random location for the coin
    coin.rect.x = random.randrange(screen_width)
    coin.rect.y = random.randrange(screen_height)
    
    #Add the coin to the coin list and the all sprites list
    coin_list.add(coin)
    all_sprites_list.add(coin)
    
for i in range(25):
    #Asteroid
    asteroid = Asteroid()
    
    #Set start position for asteroid
    asteroid.rect.x = (screen_width - random.randrange(screen_width))
    asteroid.rect.y = (screen_height - random.randrange(screen_height))
    
    #Add the asteroid to the asteroid list and the all sprites list
    coin_list.add(asteroid)
    all_sprites_list.add(asteroid)
    
#create player and add to all sprites list
player = Player()
all_sprites_list.add(player)

#Loop until closed
done = False

#Screen update speed 
clock = pygame.time.Clock()

#Set the score to 0
score = 0

#MAIN PROGRAM LOOP
while not done:
    #Process events
    for event in pygame.event.get():
        #in case of quit
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                
                file = open('highscores.txt', 'w')
                writescore = str(score) + "\n"
                file.write(writescore)
                writename = name + "\n"
                file.write(writename)
                file.close
    
    
    #Game logic
    
    #Call the update method
    all_sprites_list.update()
    
    #Calculate the mechanics for each Asteroid
    for asteroid in asteroid_list:
        
        #See if the player collided with an asteroid
        asteroid_hit_list = pygame.sprite.spritecollide(player, asteroid_list, True)
        
        #If the player hits an asteroid, end the game
        for asteroid in asteroid_hit_list:
            done = True
            print ("Game Over")
            print ("Your score is:", score)
            
    for coin in coin_list:
        
        #See if the player collided with a coin
        coin_hit_list = pygame.sprite.spritecollide(player, coin_list, True)
        
        #If the player hits a coin, delete coin and add one to the score
        for coin in coin_list:
            score += 1
            print (score)
            
            
        
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    