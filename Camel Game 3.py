import random
#intorduction comments
print ("Welcome to Camel!")
print ("You have stolen a camel to cross the desert ahead of you")
print ("The natives want their camel back")
print ("Survive the trek and outrun the natives")

#variable definitions
miles_travelled = "MT"
thirst = "T"
camel_tiredness = "CT"
CT = 0
added_camel_tiredness = "ACT"
ACT = random.randrange (1, 4)
T = 0
MT = 0
full_speed = "FS"
FS = random.randrange (10, 21)
mod_speed = "MS"
MS = random.randrange (5, 13)
native_travel = "NT"
travel_natives = "TNN" 
TNN = random.randrange (7, 15)
NT = -20
if NT < 0:
    NT * -1
drinks_initial = "DI"
DI = 3


#text loop
done = False
while not done:
    print ("A. Drink from canteen")
    print ("B. Progress at a moderate speed")
    print ("C. Progress at full speed")
    print ("D. Stop for night")
    print ("E. Status check")
    print ("Q. Quit")
    usr_choice = input ("Your Choice: ")
    if usr_choice.upper() == "Q":
        done = True
        print ("Thank you for playing!")
        #status output
    elif usr_choice.upper() == "E":
            print ("Miles travelled:", MT)
            print ("Drinks remaining in canteen:", DI)
            print ("The natives are", NT, "miles behind you")
        
        #Night update of stats
    elif usr_choice.upper() == "D":
            CT = 0
            print ("Camel is happy and rested")
            NT =+ TNN
            print ("Natives are", NT, "miles behind you")
        
        #Full speed stat update
    elif usr_choice.upper() == "C":
            print ("Camel tiredness is now", CT + ACT)
            print ("You have now travelled", MT + FS, "miles")
            NT =+ TNN
            print ("The natives are now", MT-NT, "behind you")
            T =+ 1
            print ("Your camel has a thirst value of", T)
            
        #Moderate speed stat update
    elif usr_choice.upper() == "B":
            CT =+ 1
            print ("Camel tiredness is now", CT)
            MT =+ MS
            print ("You have now travelled", MT, "miles")
            NT =+ TNN
            print ("The natives are now", MT-NT, "behind you")
            T =+ 1
            print ("Your camel has a thirst value of", T)    
    


    
#Drink stat update
