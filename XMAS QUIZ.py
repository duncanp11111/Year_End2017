import random
import time
done = False
i = 0
rangset = random.sample(range(1, 9), 8)
print (rangset)
print ("To gain access to your gifts you must first answer a series of questions correctly")
print ()
print ()
while not done:
    num = (rangset[i])
    i+=1
    if num == 1:
      while not done:
        print ("What is the world's fastest land speed set by a bird?")
        print ("A. Austrailian Emu 31 MPH\nB. Antarctic Penguin 21 MPH\nC. African Ostrich 42 MPH\nD. Roadrunner 38 MPH")
        ans_1 = input("Answer:")
        if ans_1.lower() == "a":
          print ("Correct!")
          print ()
          break
        else:
          done = True
          print ("Unluckyyyyyyyyyyyy")
        print ()
        print ()
    elif num == 2:
      while not done:
        print ("How much older is The United States of America than Canada?")
        print ("A. 104\nB. 91\nC. Canada is actually older\nD. They're the same age")
        ans_2 = input("Answer:")
        if ans_2.lower() == "b":
          print ("Correct!")
          print ()
          break
        elif ans_2.lower() != "b":
          print ("Unluckyyyyyyyyyyyy")
          done = True
        print ()
        print ()
    elif num == 3:    
      while not done:
          print ("How many degrees of tilt is necessary for a bowling pin to tip over?")
          print ("A. 19\nB. 62\nC. 12.125\nD. 7.5")
          ans_2 = input("Answer:")
          if ans_2.lower() == "d":
            print ("Correct!")
            print ()
            break
          elif ans_2.lower() != "d":
            print ("Unluckyyyyyyyyyyyy")
            done = True
          print ()
          print ()
    elif num == 4:      
      while not done:
          print ("Which planet (in our solar system) is the only to rotate clockwise?")
          print ("A. Saturn\nB. Earth\nC. Mercury\nD. Venus")
          ans_2 = input("Answer:")
          if ans_2.lower() == "d":
            print ("Correct!")
            print ()
            break
          elif ans_2.lower() != "d":
            print ("Unluckyyyyyyyyyyyy")
            done = True
            print ()
            print ()
    elif num == 5:        
      while not done:
        print ("Which animal produces the most by-product?")
        print ("A. Cattle\nB. Pigs\nC. Chickens\nD. Fish")
        ans_2 = input("Answer:")
        if ans_2.lower() == "b":
          print ("Correct!")
          print ()
          break
        elif ans_2.lower() != "b":
          print ("Unluckyyyyyyyyyyyy")
          done = True
        print ()
        print ()
    elif num == 6:
      while not done:
        print ("What was Thomas Edison afraid of?")
        print ("A. The dark\nB. Snakes\nC. Spiders\nD. Death")
        ans_2 = input("Answer:")
        if ans_2.lower() == "a":
          print ("Correct!")
          print ()
          break
        elif ans_2.lower() != "a":
          print ("Unluckyyyyyyyyyyyy")
          done = True
        print ()
        print ()
    elif num == 7:    
      while not done:
        print ("How many times on average does a person laugh everyday?")
        print ("A. 10\nB. 9\nC. 5\nD. 2")
        ans_2 = input("Answer:")
        if ans_2.lower() == "c":
          print ("Correct!")
          print ()
          break
        elif ans_2.lower() != "c":
          print ("Unluckyyyyyyyyyyyy")
          done = True
        print ()
        print ()
    elif num == 8:    
      while not done:
        print ("How fast does a sneeze travel at?")
        print ("A. 600 MPH\nB. 9 MPH\nC. 5000 MPH\nD. 212.5 MPH")
        ans_2 = input("Answer:")
        if ans_2.lower() == "a":
          print ("Correct!")
          print ()
          break
        elif ans_2.lower() != "a":
          print ("Unluckyyyyyyyyyyyy")
          done = True
        print ()
        print ()
    