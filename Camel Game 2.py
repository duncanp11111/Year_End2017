import random
#intorduction comments
print ("Welcome to Camel!")
print ("You have stolen a camel to cross the desert ahead of you")
print ("The natives want their camel back")
print ("Survive the trek and outrun the natives")

#Set Up of Variables
miles_travelled = 0
thirst = 0
camel_tiredness = 0
natives = 20
initial_amount_of_drinks = 3

#Variables
MT = miles_travelled
T = thirst
CT = camel_tiredness
N = natives
D = initial_amount_of_drinks



#Loop
done = False
while not done:
    print ()
    print ("A. Drink from canteen")
    print ("B. Progress at a moderate speed")
    print ("C. Progress at full speed")
    print ("D. Stop for night")
    print ("E. Status check")
    print ("Q. Quit")
    usr_choice = input ("Your Choice: ")
    print()
    
    #Choice Variables
    added_camel_tiredness = random.randrange (1 , 4)
    ACT = added_camel_tiredness
    moderate_speed = random.randrange (5 , 13)
    MS = moderate_speed
    native_travel = random.randrange (7 , 15)
    NT = native_travel

        
    #quit
    if usr_choice.upper() == "Q":
        print ("Thank you for playing!")
        done = True
    
    #status
    elif usr_choice.upper() == "E":
        print ("Miles travelled:", MT)
        print ("Drinks remaining in canteen:", D)
        print ("The natives are", N, "miles behind you")
    
    #Night update of stats
    elif usr_choice.upper() == "D":
        CT = 0
        print ("Camel is happy and rested")
        N -= NT
        print ("Natives are", N, "miles behind you")
        
    #Full speed stat update
    elif usr_choice.upper() == "C":
        full_speed = random.randrange (10 , 21)
        FS = full_speed        
        NDF = (FS - NT)        
        CT += ACT
        MT += FS
        N += NDF
        T += 1
        print ("Camel tiredness is now", CT)
        print ("You have now travelled", MT, "miles")
        print ("The natives are now", N, "miles behind you")
        print ("Your thirst value is", T)
        
    #Moderate speed stat update
    elif usr_choice.upper() == "B":
        mod_speed = random.randrange (5 , 13)
        MS = mod_speed
        native_difference_mod = (MS - NT)
        NDM = native_difference_mod
        CT += 1
        MT += MS
        N += NDM
        T += 1
        print ("Camel tiredness is now", CT)
        print ("You have now travelled", MT, "miles")
        print ("The natives are now", N, "miles behind you")
        print ("Your thirst value is", T)
        
    #Drink stat update
    elif usr_choice.upper() == "A":
        T *= 0
        CT = 1
        print ("Camel tiredness is now", CT)
        print ("You have now travelled", MT, "miles")
        print ("The natives are now", N, "behind you")
        print ("Your thirst value is", T)
        
    if CT >= 8:
        print ("Your camel has died")
        done = True
    elif CT >= 5:
        print ("Your camel is tired")
        
    if T >= 8:
        print ("You died of thirst")
        done = True
    elif T >= 4:
        print ("You're thirsty")
        
    if N <= 0:
        print ("You were killed!")
        done = True
    elif N <= 15:
        print ("The natives are getting close!")
        
    if MT >= 200:
        print ("You won!")
        done = True
    
    if random.randrange (1 , 21) == 17:
        T = 0
        CT = 0
        print ("You found an oasis! Your camel is rested and you are no longer thirsty!")
        