#The PlayerCharacter class holds data about the player's character
class PlayerCharacter:
    #The __init__ method initializes the attributes
    def __init__(self, health, armor_rating, attack_power):
        self.__health = health
        self.__armor_rating = armor_rating
        self.__attack_power = attack_power
    #The set_health method accepts an argument for the player's health
    def set_health(self, health):
        self.__health = health
    #The set_armor_rating method accepts an argument for the player's armor rating    
    def set_armor_rating(self, armor_rating):
        self.__armor_rating = armor_rating
    #The set_attack_power method accepts an argument for the player's attack power    
    def set_attack_power(self, attack_power):
        self.__attack_power = attack_power
    #The get_health method returns the player's health    
    def get_health(self):
        return self.__health
    #The get_armor_rating method returns the player's armor rating
    def get_armor_rating(self):
        return self.__armor_rating
    #The get_attack_power method returns the player's attack power
    def get_attack_power(self):
        return self.__attack_power
#Define the main function   
def main():
    #Using a while loop and exception handling so that the user's input is valid and doesn't go past 100 for health
    health_range = 0
    while 1 > health_range or 100 < health_range:
        try: 
            health_range = int(input("Please enter your value for Health ranging from 1-100: "))
            if health_range not in range(1,101):
                print("Please make sure your value is in the range of 1-100.")
        except Exception:
            print("Input must be a valid number. Please try again.")
    #Using a while loop and exception handling so that the user's input is valid and doesn't go past 20 for armor rating
    armor_range = 0
    while 1 > armor_range or 20 < armor_range:
        try:
            armor_range = int(input("Please enter your value for Armor Rating ranging from 1-20: "))
            if armor_range not in range(1,21):
                print("Please make sure your value is in the range of 1-20.")
        except Exception:
            print("Input must be a valid number. Please try again.")
    #Using a while loop and exception handling so that the user's input is valid and doesn't go past 20 for attack power      
    power_range = 0
    while 1 > power_range or 20 < power_range:
        try:     
            power_range = int(input("Please enter the value for Attack Power ranging from 1-20: "))
            if power_range not in range(1,21):
                print("Please make sure your value is in the range of 1-20.")
        except Exception:
            print("Input must be a valid number. Please try again.")
    #Creating an object called "Wizard" of the PlayerCharacter class
    wizard = PlayerCharacter(health_range, armor_range, power_range)
    #Displaying the Wizard's attributes
    print("\nHere are the Wizard's attributes: ")
    print(f"Health: {wizard.get_health()}")
    print(f"Armor Rating: {wizard.get_armor_rating()}")
    print(f"Attack Power: {wizard.get_attack_power()}")
#Call main function
if __name__ == "__main__":
    main()