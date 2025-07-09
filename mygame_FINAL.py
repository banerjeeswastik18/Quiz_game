import random
#=============================================================suffling the question order======================================
order=[1,2,3,4,5,6,7,8,9,10]
random.shuffle(order)
#==================================================================func. Q1===============================================
def Q1():
    ch=0
    print("QUESTION:")
    print("Which is the second planet from the sun?")
    print()
    print("A:Pluto   B:Earth   C:Venus   D:Mercury")
    print()
    a1=input("Enter Your Answer:")
    if a1=="c"  or a1=="C":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- C:Venus")
        print()
        lost()
        return ch
#=======================================================================func. Q2===================================================
def Q2():
    ch=0
    print("QUESTION:")
    print("Phobos and Diemos are the moons of which planet in our solar system?")
    print()
    print("A:Mars   B:Neptune   C:Venus   D:Jupiter")
    print()
    a2=input("Enter Your Answer:")
    if a2=="a"  or a2=="A":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch 
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- A:Mars")
        print()
        lost()
        return ch 
#===================================================================================func. Q3=======================================   
def Q3():
    ch=0
    print("QUESTION")
    print("How many planets in our solar system have rings?")
    print()
    print("A:1   B:6   C:0   D:4")
    print()
    a3=input("Enter Your Answer:")
    if a3=="d"  or a3=="D":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- D:4")
        print()
        lost()
        return ch
#=========================================================================================func. Q4=================================    
def Q4():
    ch=0
    print("QUESTION")
    print("Which is the fastest rotating planet in our solar system?")
    print()
    print("A:Earth   B:Mars   C:Jupiter   D:Uranus")
    print()
    a4=input("Enter Your Answer:")
    if a4=="c"  or a4=="C":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- C:Jupiter")
        print()
        lost()
        return ch
#========================================================================================func. Q5=====================================
def Q5():
    ch=0
    print("QUESTION")
    print("How many stars make up Orion’s Belt?")
    print()
    print("A:5   B:3   C:7   D:0")
    print()
    a5=input("Enter Your Answer:")
    if a5=="b"  or a5=="B":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- B:3")
        print()
        lost()
        return ch 
#===========================================================================================func. Q6===================================    
def Q6():
    ch=0
    print("QUESTION")
    print("Which is the only planet in our solar system to rotate clockwise?")
    print()
    print("A:Venus   B:Earth   C:Neptune   D:Jupiter")
    print()
    a6=input("Enter Your Answer:")
    if a6=="a"  or a6=="A":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- A:Venus")
        print()
        lost()
        return ch
#==============================================================================func. Q7===============================================    
def Q7():
    ch=0
    print("QUESTION")
    print("What is the name of the galaxy that contains the Earth?")
    print()
    print("A:Milky Way   B:Andromeda   C:Virgo A.   D:Cygnus A.")
    print()
    a7=input("Enter Your Answer:")
    if a7=="a"  or a7=="A":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- A:Milky Way")
        print()
        lost()
        return ch
#===================================================================================func.Q8==========================================    
def Q8():
    ch=0
    print("QUESTION")
    print("The Asteroid Belt lies between the orbits of which two planets in our solar system?")
    print()
    print("A:Earth & Mars   B:Mars & Jupiter   C:Uranus & Neptune   D:Mercury & Venus")
    print()
    a8=input("Enter Your Answer:")
    if a8=="b"  or a8=="B":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- B:Mars & Jupiter")
        print()
        lost()
        return ch
#=======================================================================================func.Q9=======================================
def Q9():
    ch=0
    print("QUESTION")
    print("Which planet in our solar system takes the shortest time to orbit the sun?")
    print()
    print("A:Earth   B:Mars   C:Uranus   D:Mercury")
    print()
    a9=input("Enter Your Answer:")
    if a9=="d"  or a9=="D":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- D:Mercury")
        print()
        lost()
        return ch
#==============================================================================================func. Q10===============================    
def Q10():
    ch=0
    print("QUESTION")
    print("Which planets do not have a natural satellite?")
    print()
    print("A:Earth & Mars   B:Mars & Jupiter   C:Uranus & Neptune   D:Mercury & Venus")
    print()
    a10=input("Enter Your Answer:")
    if a10=="d"  or a10=="D":
        ch=1
        print("YOUR ANSWER IS CORRECT!")
        print()
        return ch
    else:
        print("YOUR ANSWER IS INCORRECT!")
        print()
        print("CORRECT ANSWER IS- D:Mercury & Venus")
        print()
        lost()
        return ch

#========================================================================================func. lost===================================
def lost():
    print("XXXXXXXXXXXXXXXXXXXX   YOU LOST   XXXXXXXXXXXXXXXXXXXX")
    start()
#=====================================================================================func. question manager==========================
def QM(x):
    if x==1:
        c=Q1()
    elif x==2:
        c=Q2()
    elif x==3:
        c=Q3()
    elif x==4:
        c=Q4()
    elif x==5:
        c=Q5()
    elif x==6:
        c=Q6()
    elif x==7:
        c=Q7()
    elif x==8:
        c=Q8()
    elif x==9:
        c=Q9()
    elif x==10:
        c=Q10() 
#=======================================================================================func. start===================================
def start():
    print("DO YOU WANT TO START THE QUIZ ?")
    a=input("y/n:    ")
    if a=="y"or a=="Y":
        i=0
        while i<(len(order)):
            val=QM(order[i])
            i+=1
        print("!!!!!!!!!!!!!!!!!!!!   YOU WON   !!!!!!!!!!!!!!!!!!!!")
        start()
    else:
        print("=================================   GOODBYE   ===================================")
        quit()

start()                             #==========================================game start==========================================