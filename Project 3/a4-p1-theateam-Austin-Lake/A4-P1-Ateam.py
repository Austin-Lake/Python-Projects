#Program 1 – The A-Team
#Description: Design and write a program that reads the text from a provided text file into a list, displays the 
# text on-screen, makes some alterations to the text and outputs the changed text to the screen, then saves the 
# altered text as a new file. 

#Student #: W0420180 
#Student Name: Austin Lake

import random

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Get both file paths to Original and Altered text files
    file = "C:/Users/Austi/OneDrive/Documents/School/IT Programming/Programming/Assignment 4/a4-p1-theateam-Austin-Lake/ateam_Original.txt"
    new_file = "C:/Users/Austi/OneDrive/Documents/School/IT Programming/Programming/Assignment 4/a4-p1-theateam-Austin-Lake/ateam_Altered.txt"

    # Open Original file make alterations to each line, store each line into a list, and return that list
    lines = OpenFile(file)

    # Open Altered file and write each line of the altered list into it
    WriteToFile(new_file, lines)

    # YOUR CODE ENDS HERE

def OpenFile(file) -> list:

    with open(file, 'r') as a_file:

        print(a_file.read())
        lines = []
        a_file.seek(0)
        random_line = random.randrange(1, len(a_file.readlines()))
        a_file.seek(0)

        for index, line in enumerate(a_file.readlines(), start=1):
            if len(line) > 20 and index != random_line:
                print(f'{index}. {line.lower()}')
                lines.append(f'{index}. {line.lower()}')
            elif len(line) <= 20 and index != random_line:
                print(f'{index}. {line.upper()}')
                lines.append(f'{index}. {line.upper()}')
        
        return lines


def WriteToFile(file, a_list):
    
    with open(file, 'w') as a_file:

        for i in range(len(a_list)):
            a_file.write(a_list[i])
            
            
main()