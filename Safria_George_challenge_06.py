import random  #imports random module into memory
#define main function
def main():
    while True: #This loop will continue to ask for users input and break after a valid input
        try:
            #try suite
            user_input = int(input("Please enter how many random numbers you want in your new file: ")) #Asks for user input
        except ValueError: #Exception handling for invalid input
            #handler
            print("ERROR: Input must be a valid number. Please try again.\n")
        else:
            #opening a file
            with open(r"D:\StudentTestCodeFiles\SafriaFile.txt","w") as new_file:
                for num in (range(1,user_input+1)): #for loop with range of user's input
                    num = random.randint(1,501)
                    new_file.write(f'{str(num)}\n') #writes to file
                print("A new file has been created with your random numbers.")
                break

#Calling the main function
if __name__ == "__main__":
    main()