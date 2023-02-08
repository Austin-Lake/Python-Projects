#TECH CHECK 4 - Dungeon Attack!!
#Description:   Write a program that asks the user to enter a hit point total between 1-200, prints a snarky 
#               error message on wrong entry while prompting again, and then attacks the user with monsters stored in 
#               a monsters.csv file until the user’s character is dead (i.e. 0 hit points) while reporting the 
#               results of each attack. An even snarkier message gets printed when the user’s character has died.


#Student #:     
#Student Name:  

import csv

    
def AskInput():

    user_input = 0

    while user_input < 1 or user_input > 200:
        user_input = int(input("Enter a value between 1-200: "))

    return user_input

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    hit_points = 400
    print(f"You have {hit_points} Hit points")

    # Open File
    with open("c:/Users/Austi/OneDrive/Documents/School/IT Programming/Programming/Assignment 3/tc4-dungeonattack-Austin-Lake/Monsters.csv", "r") as csv_file:
    # Read in csv file
        csv_reader = csv.reader(csv_file)

        a_list = []
        for row in csv_reader:
            a_list.append(row)

    while hit_points > 0:

        user_input = AskInput()
        
        if user_input <= 200 and user_input > 160:
            print(f'{a_list[0][0]} attacks with {a_list[0][1]} and deals {a_list[0][2]} damage')
            hit_points = max(hit_points - int(a_list[0][2]), 0)
        elif user_input <= 160 and user_input > 120:
            print(f'{a_list[2][0]} attacks with {a_list[2][1]} and deals {a_list[2][2]} damage')
            hit_points = max(hit_points - int(a_list[2][2]), 0)

        if hit_points == 0:
            print("You lost, HAHAHAHA")
        
        print(f"You now have {hit_points} Hit points")

    # YOUR CODE ENDS HERE


main()