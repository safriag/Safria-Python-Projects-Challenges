print("\n\t\t*****Welcome to my Escape Room Simulator*****")
print("\n\t\t     Please answer the first question.\n")
correct = int(0)
incorrect = int(0)
first_rid = input("What can you hold in your right hand, but never in your left hand? ")
second_rid = input("What gets wet while drying? ")
third_rid = input("What kind of band never plays music? ")
fourth_rid = input("What is the end of everything? ")
fifth_rid = input("When is a door no longer a door? ")
if (first_rid.lower() == "your left hand" ): 
    correct = 1 + correct
else:
   incorrect = 1 + incorrect
    
if(second_rid.lower() == "a towel"):
    correct = 1 + correct
else:
    incorrect = 1 + incorrect
    
if (third_rid.lower() == "a rubber band"):
    correct = 1 + correct
else:
    incorrect = 1 + incorrect
           
if (fourth_rid.lower() == "g"):
    correct = 1 + correct
else:
    incorrect = 1 + incorrect
                
if (fifth_rid.lower() =="when it is ajar"):
    correct = 1 + correct
else:
    incorrect = 1 + incorrect

if (correct >= 3):
    escaped = "Congratulations, you escaped the room of many riddles."
    print(escaped)
elif (incorrect >= 3):
    noescape = "Unfortunately, you did not escape the room of many riddles."
    print(noescape)