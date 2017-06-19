"""Ask whether to encrypt, decrypt or quit
if the answer is encrupt:
    ask for message to encrypt and key to encrypt it with
    store message as a string
    store key as an integer
    convert to lowercase
    convert lowercase to unicode numbers
    add the key amount to the unicode numbers making sure the code 
    does not convert special characters 
    by using if statements limiting the code to the lowercase alphabet
    convert the new unicode to lowercase letters
    iterate and store in a new list
    print that list
if the answer is decrypt:
    ask for message to decrypt and key to decrypt with
    store message as a string
    store key as an integer
    convert to lowercase
    convert lowercase to unicode numbers
    minus the key amount to the unicode numbers making sure the code 
    does not convert special characters 
    by using if statements limiting the code to the lowercase alphabet
    convert the new unicode to lowercase letters
    iterate and store in a new list
    print that list
if answer is quit
terminate program"""
    
done = False

def encrypt():
    encryption = ""
    enc = input("What phrase would you like to encrypt?: ")
    key = int(input("What key or shift would you like to use?: "))
    enc = enc.lower()
    for char in enc:
        x = ord(char)
        if x >= 97:
            x += key
            while x > 122:
                x = (x - 122 + 96)
        x = chr (x)
        encryption += x
    print (encryption)

def decrypt():
    enc2 = input("What phrase would you like to decrypt?: ")
    key2 = int(input("What key or shift would you like to use?: "))  
    enc2 = enc2.lower()
    decryption = ""
    for char in enc2:
        x = ord(char)
        if x >= 97:
            x -= key2
            while x < 97:
                x = (x - 97 + 123)
        x = chr (x)
        decryption += x
    print (decryption)        

while not done:
    print ("Welcome to the Encryption Machine.")
    print ("Please select an option from the list below.")
    print ("A. Encrypt.")
    print ("B. Decrypt.")
    print ("Q. Quit.")
    begin = input(": ")
    
    if begin.lower() == "a":
        try: 
            encrypt()
        except:
            print ("Invalid Key")
            continue
        
    elif begin.lower() == "b":
        try: 
            decrypt()   
        except:
            print ("Invalid Key")
            continue
        
    elif begin.lower() == "q":
        done = True 