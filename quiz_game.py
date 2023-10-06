print(" welcome to my computer quiz!")
playing=input("Do you want to play? ")

if playing.lower() !="yes":
    quit()
    
print("Okay! Let's play:)")
score=0
#1

answer =input("what does CPU stand for? ")
if answer.lower()=="central processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect")
#2
  
answer =input("what does GPU stand for? ")
if answer.lower()=="graphics processing unit":
    print("Correct!")
    score +=1

else:
    print("Incorrect")
#3    
 
answer =input("what does RAM stand for? ")
if answer.lower()=="random access memory":
    print("Correct!")
    score +=1

else:
    print("Incorrect")
 #4   
  
answer =input("what does PSU stand for? ")
if answer.lower()=="power supply":
    print("Correct!")
    score +=1

else:
    print("Incorrect")
    
    
print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score/4) * 100) + "%.")

    
