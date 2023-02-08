#Program 2 – The Itsy Bitsy Aardvark
#Description: Design and develop a program that presents the user with a “Mad Libs” type game, where a random 
# choice of words are read from a file, then interjected into a story read from another file.

#Student #: W0420180
#Student Name: Austin Lake

import csv

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Path to files
    csv_file = "C:/Users/Austi/OneDrive/Documents/School/IT Programming/Programming/Assignment 4/a4-p2-theitsybitsyaardvark-Austin-Lake/the_choices_file.csv"
    story_file = "C:/Users/Austi/OneDrive/Documents/School/IT Programming/Programming/Assignment 4/a4-p2-theitsybitsyaardvark-Austin-Lake/the_story_file.txt"
    
    # Populates two list with every line of data in the csv file
    first_words, other_words = PopulateLists(csv_file)
    
    # Returns a dictionary of users choices
    choices = AskInput(first_words, other_words)

    # Replaces all occurences of each word in each line of the story file with user choices
    ReplaceWords(story_file, choices)

    # YOUR CODE ENDS HERE

def PopulateLists(csv_file) -> list:

    with open (csv_file, 'r+') as a_file:
        csv_reader = csv.reader(a_file)
        
        first_words = []
        other_words = []

        for line in csv_reader:
            first_word = line[0]
            first_words.append(first_word)
            line.remove(first_word)

            other_words.append(line)

        return first_words, other_words

def AskInput(first_words, other_words):

    a_dict = {}
    another_dict = {}

    for x in range(len(first_words)):
        for y, word in enumerate(other_words[x], start=1):
            print(f'{y} : {word}')
            another_dict[y] = word
        
        user_value = 0
        while user_value not in another_dict.keys():
            try:
                user_value = int(input(f"{first_words[x]}, Choose a number: "))
            except:
                print("Key does not exist try again")
            
        a_dict[x] = another_dict[user_value]

        print('\n')
        
    return a_dict

def ReplaceWords(file, choices):

    with open(file, 'r') as a_file:
        
        for line in a_file.readlines():
            new_line = line.replace('_1_', 
            str(choices[0]).upper()).replace('_2_', str(choices[1]).upper()).replace('_3_', 
            str(choices[2]).upper()).replace('_4_', str(choices[3]).upper()).replace('_5_',
            str(choices[4]).upper()).replace('_6_', str(choices[5]).upper()).replace('_7_', str(choices[6]).upper())
            print(new_line)

            
main()