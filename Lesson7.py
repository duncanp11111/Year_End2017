x = [1,2]
print (x)
print (x[0])
my_list = [1,2,3,4]
for item in my_list:
    print (item)
    
my_list = [1,2,3,4,5]
for item in my_list:
    print(item)
my_list = ["Spoon", "Fork", "Knife"]
for item in my_list:
    print(item)
my_list = [101, 20, 10, 50, 60]
for i in range(len(my_list)):
    print(my_list[i])
my_list = [2, 4, 5, 6]
print(my_list)
my_list.append(9)
print(my_list)
x = "This is a sample string"
#x = "0123456789"
 
print("x=", x)
 
# Accessing a single character
print("x[0]=", x[0])
print("x[1]=", x[1])
 
# Accessing from the right side
print("x[-1]=", x[-1])
 
# Access 0-5
print("x[:6]=", x[:6])
# Access 6
print("x[6:]=", x[6:])
# Access 6-8
#months = "JanFebMarAprMayJunJulAugSepOctNovDec" 
#while not done:
    #n = int(input("Enter a month number: ")) 
    #print(months[(n * 3 - 3):n * 3])
plain_text = "ISISISISISISISIS"
 
encrypted_text = ""
for c in plain_text:
    x = ord(c)
    x = x + 1
    c2 = chr(x)
    encrypted_text = encrypted_text + c2
print(encrypted_text)    