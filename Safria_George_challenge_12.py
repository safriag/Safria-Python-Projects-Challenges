#The sum_of_nums function uses recursion to calculate the sum of numbers of its argument
def sum_of_nums(n):
    #base case
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #recursive case
    else:
        return sum_of_nums(n-1) + n #recursive call
#define main function
def main():
    #Ask user for number
    num = int(input("Please enter the number you would like me to sum up: "))
    #Get the sum of numbers
    result = sum_of_nums(num)
    #Display the sum of numbers
    print(result)
#Call main function
if __name__ == "__main__":
    main()