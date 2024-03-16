#define StoredPasswords
def StoredPasswords(checkPass):#accepts 'user_pass' as an argument in the parameter 'checkPass'
    #Store 50 most common passwords in tuple
    common_password = ('123456', '123456789', '12345', 'qwerty', 'password', '12345678', '111111', '123123', '1234567890', '1234567', 'qwerty123', '000000', '1q2w3e', 'aa12345678', 'abc123', 'password1', '1234', 'qwertyuiop', '123321', 'password123', '1q2w3e4r5t', 'iloveyou', '654321', '666666', '987654321', '123', '123456a', 'qwe123', '1q2w3e4r', '7777777', '1qaz2wsx', '123qwe', 'zxcvbnm', '121212', 'asdasd', 'a123456', '555555', 'dragon', '112233', '123123123', 'monkey', '11111111', 'qazwsx', '159753', 'asdfghjkl', '222222', '1234qwer', 'qwerty1', '123654', '123abc')
    found = "Your password is too common. Please consider changing it."
    notFound = "You have a strong password."
    if checkPass in common_password: #IF statement to detect if user input is a common password
        return found, common_password.index(checkPass), True #returns variable back to the call function (getUserPass), and indicates which index the common password is found in the tuple
    else:
        return notFound
#define getUserPass
def getUserPass():
    user_name = input("Please enter your username: ")
    user_pass = input("Please enter your password: ")
    result = StoredPasswords(user_pass) #Call StoredPasswords and pass 'user_pass' as an argument; and store it in a variable to get the returned value
    print(result)
#Call getUserPass from main function
if __name__ == "__main__":
    getUserPass()