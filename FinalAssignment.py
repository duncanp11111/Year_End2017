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

#CLASSES

#Coin Class
class Coin(pygame.sprite.Sprite):
    def __init__(self, color):
        
        # Call the parent class (Sprite) constructor
        super().__init__()
        
        self.image = pygame.Surface([(10, 10), 5])
        self.image.fill(color)
        
        self.rect = self.image.get_rect()

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
    coin = Coin(YELLOW)
    
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
    
    #Game logic
    
    #Call the update method
    all_sprites_list.update()
    
    #Calculate the mechanics for each Asteroid
    for asteroid in asteroid_list:
        
        #See if the player collided withg an asteroid
        asteroid_hit_list = pygame.sprite.spritecollide(player, asteroid_list, True)
        
        #If the player hits an asteroid, end the game
        for asteroid in asteroid_hit_list:
            done = True
            print ("Game Over")
            print ("Your score is:", score)
            
        
           
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    