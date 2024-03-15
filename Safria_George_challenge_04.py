print("\n\t\t*****Welcome to my Escape Room Simulator*****")
ask = (input("Do you want to play a game? "))
correct = int(0)
questions = int(0)
while(ask.lower() == "yes"):
    print("Please answer the first riddle.")
    first_rid = input("What can you hold in your right hand, but never in your left hand? " )
    questions += 1
    if (first_rid.lower() == "your left hand"):
        correct += 1
    else: 
        print(f"You were asked 1/5 riddles and you answered {correct} questions correctly.")
        break
    ask = input("Would you like to answer another riddle? ")
    if (ask.lower() != "yes"):
        break
    second_rid = input("What gets wet while drying? ")
    questions += 1
    if (second_rid.lower() == "a towel" ):
        correct += 1
    else:
        print(f"You were asked 2/5 riddles and you answered {correct} questions correctly.")
        break
    ask = input("Would you like to answer another riddle? ")
    if (ask.lower() != "yes"):
        break
    third_rid = input("What kind of band never plays music? ")
    questions += 1
    if (third_rid.lower() == "a rubber band"):
        correct += 1
    else:
        print(f"You were asked 3/5 questions and you answered {correct} questions correctly.")
        break
    ask = input("Would you like to answer another riddle? ")
    if (ask.lower() != "yes"):
        break
    fourth_rid = input("What is the end of everything? ")
    questions += 1
    if (fourth_rid.lower() == "g"):
        correct += 1
    else:
        print(f"You were asked 4/5 questions and you answered {correct} questions correctly.")
        break
    ask = input("Would you like to answer another riddle? ")
    if (ask.lower() != "yes"):
        break
    fifth_rid = input("When is a door no longer a door? ")
    questions += 1
    if (fifth_rid.lower() == "when it is ajar"):
        correct += 1
    print(f"You were asked 5/5 questions and answered {correct} questions correctly.")
    break

if (ask.lower() != "yes"):
    print(f"You were asked {questions}/5 riddles and you answered {correct} questions correctly.")