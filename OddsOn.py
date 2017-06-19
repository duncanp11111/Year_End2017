from random import randrange
import time 

print ("Welcome to Odds On!")
odds_on = input("what will you do if you lose?: ")
odds = int(input("What are your odds?: "))
print ("Your odds are 1 to", odds)
print ("Please select a number between 1 and", odds, "when the counter hits zero.")
print ("Ready?")
print ("3")
time.sleep(0.5)
print ("2")
time.sleep(0.5)
print ("1")
time.sleep(0.5)
usr_input = int(input("What is your number?:" ))
bot = randrange(1, (odds+1))
print ("Bot's number is", bot)
print ("Your number is", usr_input)
if bot == usr_input:
  print ("Now you have to", odds_on, ". GLHF!")
else:
  print ("Lucky!")
