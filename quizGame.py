print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing != "yes" :
    quit()
print("Okay! Let's play :)")
score = 0
answer = input("What does the CPU stands for? ")
if answer.lower() == "central processing unit" :
    print('Correct!')
    score+=1
else :
    print("Incorrect!")
   
    
answer = input("What does the GPU stands for? ")
if answer.lower() == "graphics processing unit" :
    print('Correct!')
    score+=1
else :
    print("Incorrect!")
    
answer = input("What does the RAM stands for? ")
if answer.lower() == "random access memory" :
    print('Correct!')
    score+=1
else :
    print("Incorrect!")
    
answer = input("What does the PSU stands for? ")
if answer.lower()== "power supply" :
    print('Correct!')
    score+=1
else :
    print("Incorrect!")

print("You got " + str(score) + " questions correct!" )
print("You got " + str((score/4) * 100) + "%")
