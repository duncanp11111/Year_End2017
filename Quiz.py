correct = 0

answer = input("What is the colour of blood when oxygenated? \nAnswer: ")
if answer.lower() == "red":
	print("Correct!")
	correct = (correct + 1)
else:
	print("Incorrect")
print()

print("How many letters are in the word razzmatazz?")
print("a) 8 \nb) 11 \nc) 10 \nd) 9")
answer = input("Answer: ")
if answer.lower() == "c":
	print("Correct!")
	correct = (correct + 1)
else:
	print("Incorrect")
print()

answer = input("Elephants cannot jump. \nTrue or False? \nAnswer: ")
if answer.lower() == "true":
	print("Correct!")
	correct = (correct + 1)
else:
	print("Incorrect")
print()

answer = input("What 4 x 8 - 10? \nAnswer: ")
answer = int(answer)
if answer == 22:
	print("Correct!")
	correct = (correct + 1)
else: 
	print("Incorrect")
print()

print("Who was the King of Rock")
print("a) George Washington \nb) Michael Jackson \nc) Matty B Raps \nd) Elvis Presley")
answer = input("Answer: ")
if answer.lower() == "d":
	print("Correct")
	correct = (correct + 1)
else:
	print("Incorrect")
print()

print("Congratulations, you got " , correct , " answers right. \nThat is a score of " , round(correct * (100 / 5)) , " percent." , sep='')