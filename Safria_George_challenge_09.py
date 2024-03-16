#Define main function
def main():
    word_frequency_dict = {} #Create empty dictionary
    #Open file in read mode
    with open("Word Frequency.txt", "r") as read_file:
        for words in read_file: #for loop to read each line in the file
            each_word = words.split() #create variable to split each word in the file
            for key in each_word: #for loop to iterate over each word 
                if key in word_frequency_dict: #using 'in' operator to determine if the key exists in the dictionary
                    word_frequency_dict[key] += 1 #IF statement will reference each key placed in the dictionary and add up the frequency of each word
                else:
                    word_frequency_dict[key] = 1 #if the key is not referneced more than once then its value will be 1
    print(f"\n       \t*****Word Frequency Table*****\n") #title of the table
    print(f"       *WORD*\t\t\t    *COUNT*") #formatting column headers of the table
    for key in word_frequency_dict: #for loop to iterate over all the keys in the dictionary
        print(f"{key:^20}\t {word_frequency_dict[key]:^30}") #formatting the keys and values in the dictionary for the table
#Call main function
if __name__ == '__main__':
    main()