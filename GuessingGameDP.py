from random import randrange
done = False
number = randrange(1,101)
while not done:
    guess = int(input("Enter a guess: "))
    if guess!= range (1, 101):
        print ("Invalid input!")
        done = True
    elif guess > number:
        print("Too high")
    elif number > guess:
        print("Too low")
    else:
        print("You got it!")
        done = True
