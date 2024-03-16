#The Person class holds data about the person's contact information
class Person:
    #The __init__ method accepts arguments for the 'name', 'address', and 'phone_num'. It initializes the attributes with these values.
    def __init__(self, name, address, phone_num):
        self.name = name
        self.address = address
        self.phone_num = phone_num
    #setters/mutators
    def set_name(self, name):
        self.name = name
        
    def set_address(self, address):
        self.address = address
    
    def set_phone_num(self, phone_num):
        self.phone_num = phone_num
    #Getters/accessors
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def get_phone_num(self):
        return self.phone_num
#The Customer class represents the customer. It is a subclass of the Person class.
class Customer(Person): #Customer inherits from the Person class
    #The __init__ method accepts arguments for the customer's 'name', 'address', 'phone_num', 'custom_num', and 'mail_list'.
    def __init__(self,name, address, phone_num, custom_num, mail_list):
        #Calling the superclass's __init__ method and passing the required arguments.
        Person.__init__(self, name, address, phone_num)
        #Initializing the 'custom_num' and 'mail_list' attributes.
        self.custom_num = custom_num
        self.mail_list = mail_list
    
    def custom_ID(self): #Displaying the Customer's contact information and their customer number
        return f"\nCustomer Name: {self.name}\nAddress: {self.address}\nPhone Number: {self.phone_num}\nCustomer ID#: {self.custom_num}"
   
    def join_list(self, choice):
        #Using Boolean for the mail_list attribute to indicate whether the customer would like to join the mailing list or not
        self.mail_list = False
        if choice.lower() == "yes":
            self.mail_list = True
        else:
            self.mail_list = False
        return f"Mail List: {self.mail_list}"
    
#Define the main function    
def main():
    #Ask for user's input
    custom_name = input("Please enter your name: ")
    custom_adress = input("Please enter your address: ")
    custom_phone_num = input("Please enter your telephone number: ")
    custom_ID_num = input("Please enter your customer ID number: ")
    mail_list_choice = input("Would you like to join the mail list? (Enter 'Yes' or 'No'): ")
    #Creating an object called "customer_info" of the Customer class
    customer_info = Customer(custom_name, custom_adress, custom_phone_num, custom_ID_num, mail_list_choice)
    print(customer_info.custom_ID())
    print(customer_info.join_list(mail_list_choice))
#Call main function
if __name__ == "__main__":
    main()       