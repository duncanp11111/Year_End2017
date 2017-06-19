import math
done = False
G = 0.0000000000667
Me = 5980000000000000000000000
Re = 6380000
while not done:
    print ("Welcome to the Gravitional Orbit Calculator.")
    print ("Please select what variable you would like to solve for and follow the further instructions.")
    print ("A. Orbital Velocity")
    print ("B. Orbital Radius")
    print ("C. Period")
    print ("D. Gravitaional Potential Energy")
    print ("E. Kinetic Energy")
    print ("F. Work")
    print ("Q. QUIT")
    begin = input("What do you need to solve for?: ")
    
    
    if begin.lower() == ("a"):
        print ("")
        print ("You selected Orbital Velocity")
        print ("For Orbital Velocity we will use the formula/n")
        print ("")
        print ("(GMm/r^2) = (mv^2/r)")
        print ("")
        print ("For this equation to work I need...")
        radius1 = input("Orbital Radius in metres: ")
        radius1 = float(radius1)
        ansa = float((G * Me)/radius1)
        print ("The velocity for stable orbit around Earth is", ansa, "m/s")
        print ("")
        
    elif begin.lower() == "b":
        print ("")
        print ("You selected Orbital Radius")
        print ("For Orbital Radius we will use the formula/n")
        print ("")
        print ("R + R(earth) = R(orb)")
        print ("")
        print ("For this equation to work I need...")
        alt1 = input("Altitude in metres: ")
        alt1 = float(alt1)
        ansb = float(Re + alt1)        
        print ("The Orbital Radius is", ansb, "m")
        print ("")
    
    elif begin.lower() == "c":
        print ("")
        print ("You selected Period")
        print ("For Period we will use the formula/n")
        print ("")
        print ("(GMm/r^2) = ((m4(pi)^2r)/T^2)")
        print ("")
        print ("For this equation to work I need...")
        orbr = input("Orbital Radius in metres: ")
        orbr = float(orbr)
        ansc = float(((4 * (3.14159265359**2) * (orbr**3))/(G * Me))**(1/2))        
        print ("The Period is", ansc, "seconds")     
        print ("")

    elif begin.lower() == "d":
        print ("")
        print ("You selected Orbital Potential Energy")
        print ("For Orbital Potential Energy we will use the formula/n")
        print ("")
        print ("PE = -GMm/r")
        print ("")
        print ("For this equation to work I need...")
        orbr2 = input("Orbital Radius in metres: ")
        mass = input("Mass in kg: ")
        orbr2 = float(orbr2)
        mass = float(mass)
        ansd = float((-1 * G * Me * mass)/(orbr2))        
        print ("The Orbital Potential Energy is", ansd, "J")     
        print ("")        
        
    elif begin.lower() == "e":
        print ("")
        print ("You selected Kinetic Energy")
        print ("For Kinetic Energy we will use the formula/n")
        print ("")
        print ("KE = 1/2mv^2")
        print ("")
        print ("For this equation to work I need...")
        velo = input("Velocity in metres per second: ")
        mass2 = input("Mass in kg: ")
        velo = float(velo)
        mass2 = float(mass2)
        anse = float((1/2) * mass2 * (velo**2))       
        print ("The Kinetic Energy is", anse, "J")     
        print ("")  
        
    elif begin.lower() == "f":
        print ("")
        print ("You selected Work")
        print ("For Work we will use the formula/n")
        print ("")
        print ("W = (change in)PE + (change in)KE")
        print ("")
        print ("For this equation to work I need...")
        veloorb = input("Orbital Velocity in metres per second: ")
        mass3 = input("Mass in kg: ")
        inirad = input("Initial Radius: ")
        finrad = input("Final Radius: ")
        inivelo = input("(If applicable enter value, if not enter 0) Initial Velocity: ")
        inirad = float(inirad)
        inivelo = float(inivelo)
        finrad = float(finrad)
        veloorb = float(veloorb)
        mass3 = float(mass3)
        ansKEf = float((1/2) * mass3 * (veloorb**2))
        ansKei = float((1/2) * mass3 * (inivelo**2))
        ansPEf = float(((-1) * G * Me * mass3)/finrad)
        ansPei = float(((-1) * G * Me * mass3)/inirad)
        ansf = float((ansKEf - ansKei) + (ansPEf - ansPei))
        print ("The Work is", ansf, "J")     
        print ("")          
    
    elif begin.lower() == ("q"):
        done = True
        
