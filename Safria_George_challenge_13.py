#This program will determine if a password is valid using regular expressions.
import re
#Create regex object
pattern = r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[@#$%*!])[A-Za-z0-9@#$%*!]{8,}$"
#Ask for user input
user_password = input("Please enter your new password. It must be at least 8 characters, contain at least 1 digit, 1 uppercase letter, and 1 special character(@#$%*!): ")
#IF statement to check if user_password matches the requirements from regex object
if re.match (pattern, user_password):
    print("That is a valid password.")
else:
    print("That is not a valid password.")