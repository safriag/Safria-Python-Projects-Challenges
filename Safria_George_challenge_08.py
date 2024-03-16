#global variable lists for morse code and alphabet letters
morse_code = ('/' , '--..--', '.-.-.-', '..--..','-----', '.----','..---', '...--', '....-', '.....', '-....', '--...','---..', '----.', '.-','-...','-.-.', '-..', '.', '..-.', '--.', '....','..', '.---', '-.-','.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.-', '--..')
equivalent_char = [' ', ',', '.', '?', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# define alphabet_index
def alphabet_index(translate_input): #Accepts 'user_input' as an argument in the parameter 'translate_input'
    uppercase_input = translate_input.upper() #use case-insensitive comparison
    for char in uppercase_input: #for loop to test each character in user input
        letter_index = equivalent_char.index(char)#assign the index of each char found in 'equivalent_char' list to variable 'letter_index'
        morse_code_translate(letter_index) #Call 'morse_code_translate' and pass 'letter_index' as an argument
#define morse_code_translate
def morse_code_translate(morse_index): #Accepts 'letter_index' as an argument in the parameter 'morse_index'
    morse_translate = " " #create variable to translate user input to morse code and leave it blank
    morse_translate += morse_code[morse_index] #concatenating the 'morse_code' translation using the index from the function parameter to the blank variable
    print(morse_translate, end=" ") #print morse code translation and suppressing the print function's ending newline
#Call main function
if __name__ == "__main__":
    user_input = input(str("Please enter what you want me to translate in morse code: "))#Ask for user input and convert it to a string
    alphabet_index(user_input) #Call 'alphabet_index' and pass 'user_input' as an argument