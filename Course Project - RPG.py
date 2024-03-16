import random
#The Humanoids class holds data for the Humanoids attributes
class Humanoids:
    #Initializing attributes
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.height = height
        self.weight = weight
        self.hair_color = hair_color
        self.eye_color = eye_color
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
    #Setters
    def set_height(self, height):
        self.height = height
        
    def set_weight(self, weight):
        self.weight = weight
        
    def set_hair_color(self, hair_color):
        self.hair_color = hair_color
        
    def set_eye_color(self, eye_color):
        self.eye_color = eye_color
        
    def set_strength(self, strength):
        self.strength = strength
        
    def set_dexterity(self, dexterity):
        self.dexterity = dexterity
        
    def set_constitution(self, constitution):
        self.constitution = constitution
        
    def set_intelligence(self, intelligence):
        self.intelligence = intelligence
        
    def set_wisdom(self, wisdom):
        self.wisdom = wisdom
        
    def set_charisma(self, charisma):
        self.charisma = charisma
    #Getters    
    def get_height(self):
        return (self.height) 
    
    def get_weight(self):
        return (self.weight)
    
    def get_hair_color(self):
        return (self.hair_color)
    
    def get_eye_color(self):
        return (self.eye_color)
    
    def get_strength(self):
        return self.strength
    
    def get_dexterity(self):
        return self.dexterity 
    
    def get_constitution(self):
        return self.constitution 
    
    def get_intelligence(self):
        return self.intelligence 
    
    def get_wisdom(self):
        return self.wisdom 
    
    def get_charisma(self):
        return self.charisma 
#The Humans class represents the human race and is a subclass of the Humanoids class. 
class Humans(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, extra_attr):
        #Calling the superclass's __init__ method and passing the required arguments.
        Humanoids.__init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.extra_attr = extra_attr
    #Define human_details function
    def human_details(self):
        return f"\nHeight: {self.height}ft\nWeight: {self.weight}lbs\nHair Color: {self.hair_color}\nEye Color: {self.eye_color}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"
    #Define add_attr function
    def add_attr(self):
        pick_attribute = input("\nAs a Human, you may add +2 bonus points to a single attribute of your choosing. (Enter one of these: strength, dexterity, constitution, intelligence, wisdom, charisma): ")
        if pick_attribute == "strength":
            self.strength += 2
        elif pick_attribute == "dexterity":
            self.dexterity +=2
        elif pick_attribute == "constitution":
            self.constitution +=2
        elif pick_attribute == "intelligence":
            self.intelligence +=2
        elif pick_attribute == "wisdom":
            self.wisdom +=2
        elif pick_attribute == "charisma":
            self.charisma +=2
        return f"\nYour character's final attributes are:\n\nHeight: {self.height}ft\nWeight: {self.weight}lbs\nHair Color: {self.hair_color}\nEye Color: {self.eye_color}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}"
#The Elves class represents the elf race and is a subclass of the Humanoids class.
class Elves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, sleep):
        #Calling the superclass's __init__ method and passing the required arguments.
        Humanoids.__init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.sleep = sleep
    #Define sleep_resistance function
    def sleep_resistance(self):
        print("\nAs an Elf, you will have 100% Resistance to sleep, and you will receive 2 points to you Dexterity and Charisma scores.")
        self.dexterity +=2
        self.charisma +=2
        return f"\nYour character's final attributes are:\nHeight: {self.height}ft\nWeight: {self.weight}lbs\nHair Color: {self.hair_color}\nEye Color: {self.eye_color}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\nSleep Resistance: {self.sleep}%"
#The Dwarves class represents the dwarf race and is a subclass of the Humanoids class.  
class Dwarves(Humanoids):
    def __init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma, magic):
        #Calling the superclass's __init__ method and passing the required arguments.
        Humanoids.__init__(self, height, weight, hair_color, eye_color, strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.magic = magic
    #Define magic_resistance function
    def magic_resistance(self):
        print("\nAs a Dwarf, you will have 20% resistance to magic, and you will receive 2 points to your Strength and Constitution scores. However, 2 points will be deducted from your Charisma score. ")
        self.strength += 2
        self.constitution += 2
        self.charisma -= 2
        return f"\nYour character's final attributes are:\nHeight: {self.height}ft\nWeight: {self.weight}lbs\nHair Color: {self.hair_color}\nEye Color: {self.eye_color}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nConstitution: {self.constitution}\nIntelligence: {self.intelligence}\nWisdom: {self.wisdom}\nCharisma: {self.charisma}\nMagic Resistance: {self.magic}%"
#Define characterCreation function
def characterCreation():
    #Introduction for the game and ask user to choose race
    intro = print("\nWelcome to Falls of Eternity. This is a simple RPG simulator written in Python. You may choose from the following playable races:\n\n1. Human\n2. Elf\n3. Dwarf\n")
    user_race = 0
    #Excpetion handling for if user does not choose a valid option for race
    while 1 > user_race or 3 < user_race:
        try:
            user_race = int(input("Which race have you chosen for your starting character? "))
            if user_race not in range(1,4):
                print("Please make sure you input 1, 2, or 3 when choosing the race of your character.")
        except ValueError:
            print("Input must be a valid number. Please try again.")
    #Ask user for hair and eye color
    user_hair = input("Please enter the hair color for your character: ")
    user_eye = input("Please enter the eye color for your character: ")
    #Exception handling if user input is invalid and chooses a height outside of asked range
    user_height = 0
    while 3 > user_height or 7 < user_height:
        try:
            user_height = int(input("Please enter the height of your character from 3-7ft: "))
            if user_height not in range(3,8):
                print("Please make sure the value for your character's height is in the range of 3-7ft.")
        except ValueError:
            print("Input must be a valid number. Please try again.")
    #Exception handling if user input is invalid and chooses weight outside of asked range
    user_weight = 0
    while 60 > user_weight or 300 < user_weight:
        try:
            user_weight = int(input("Please enter the weight for your character from 60-300lbs: "))
            if user_weight not in range(60,301):
                print("Please make sure the value for your character's weight is in the range of 60-300lbs. ")
        except ValueError:
            print("Input must be a valid number. Please try again.")
    #Rolling random score for attributes
    user_stren = random.randint(1,18)
    user_dex = random.randint(1,18)
    user_cons = random.randint(1,18)
    user_intell = random.randint(1,18)
    user_wis = random.randint(1,18)
    user_char = random.randint(1,18)
    extra_attribute = 0
    elf_sleep = 100
    dwarf_magic = 20
    #IF statements for classes based on user's input for race
    if user_race == 1:
        human_info = Humans(user_height, user_weight, user_hair, user_eye, user_stren, user_dex, user_cons, user_intell, user_wis, user_char, extra_attribute)
        print("\nYour character has the following attributes: ")
        print(human_info.human_details())
        print(human_info.add_attr())
    elif user_race == 2:
        elf_info = Elves(user_height, user_weight, user_hair, user_eye, user_stren, user_dex, user_cons, user_intell, user_wis, user_char, elf_sleep)
        print(elf_info.sleep_resistance())
    elif user_race == 3:
        dwarf_info = Dwarves(user_height, user_weight, user_hair, user_eye, user_stren, user_dex, user_cons, user_intell, user_wis, user_char, dwarf_magic)
        print(dwarf_info.magic_resistance())
#Define main function and call characterCreation function
def main():
    characterCreation()
#Call main
if __name__ == "__main__":
    main()