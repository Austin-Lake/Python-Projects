#Program 3 – Girl Guide Cookies
#Description:   The organizers of the annual Girl Guide cookie sale event want to raise 
#               the stakes on the number of cookies sold and are offering cool prizes to
#               those guides who go above and beyond in their sales efforts. The organizers
#               want a program to print the guide list and their prizes.

#Student #: W0420180
#Student Name: Austin Lake

import operator

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    """
    Design Overview:
    Ask user for number of girl guides,
    create a loop to ask user for input on each girl guide's name and cookies sold,
    store values into two lists for calculations,
    populate a dictionary with those two list to conduct further calculations
    """

    # Get the amount of guides from the user
    amount = int(input('Enter how many girl guides there are: '))

    # Initalize to empty lists to use in Calculation
    names = []
    cookies_sold = []

    # Create a for loop to interate through each guide to enter a name and amount of cookies sold, then populate both lists with data given
    for _ in range(amount):
        guide = input("Enter name of guide: ")
        cookies = int(input("Enter how many cookies guide sold: "))

        names.append(guide)
        cookies_sold.append(cookies)

    print('\n')

    print(names)

    print('\n')

    # Use a for loop to find the total cookies sold and then divide by number of guides to get average
    total_cookies = 0

    for cookies in cookies_sold:
        total_cookies += cookies
    
    average_cookies = total_cookies / len(names)

    print(f'Average Cookies sold: {round(average_cookies, 0)}')

    print('\n')

    # Create a dictionary and a for loop to populate key-value pairs of guide name and cookies sold to use in Calculation
    guides = {}

    for i in range(len(names)):
        guides[names[i]] = cookies_sold[i]

    # Sort dictionary from Higest - Lowest, use dictionary in calculation to find which prizes are won
    sorted_guides = sorted(guides.items(), key=operator.itemgetter(1), reverse=True)
    for guide, cookies in dict(sorted_guides).items():
        if (cookies == max(dict(sorted_guides).values())):
            prize = 'Girl Guide Jamboree'
        elif (cookies > round(average_cookies, 0)):
            prize = 'Badge' 
        elif (cookies >= 1):
            prize = 'Eat remaining cookies'
        else:
            prize = 'No prize'

        print(f'Guide {guide} sold {cookies} : Prize: {prize}')

    # YOUR CODE ENDS HERE

main()