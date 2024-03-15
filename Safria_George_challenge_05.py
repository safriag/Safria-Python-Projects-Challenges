#define the free fall distance function
def free_fall_distance(seconds):  #header  free_fall_distance accepts an argument in its parameter to calculate the distance traveled based on the inputted time
    for num in range(1,seconds+1):  #body  for loop with range of "seconds" so that it will print output for each second from users input
        secondswrite = num #assigning variable "num" to variable "secondswrite"
        distance = float(0.5*9.8*(secondswrite**2))  #formula for free fall distance 
        print(f"After {secondswrite} seconds, the object has traveled {distance:.2f} meters.") #prints output


if __name__ == "__main__":   #This file will run as the main program.
    print("\t\t ***** Free-Falling Distance Calculator *****")  #title/intro
    time = int(input(f"Please enter the time (in seconds) and I will tell you how far the object has traveled after each second: ")) #Asking for user input and then it will be assigned to the variable "time"
    result = free_fall_distance(time)  #passing an argument (time) to free_fall_distance and assigning it to the variable "result"