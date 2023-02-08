#Program 1 – Timesheet
#Description:   Design and write a program that accepts the number of hours worked on 
#               each of five work days from the user, then displays different 
#               information calculated about those entries as output. 

#Student #: W0420180  
#Student Name: Austin Lake

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    ''' 
    Design Overview: 
    Ask user for all fives inputs,
    store inputs along with appropriate day into a dictionary,
    use the dictionary to manipulate the key - value pairs in separate caluclations.
    '''

    # Gets all five work days from user
    monday = float(input("Enter hours worked for Monday: "))
    tuesday = float(input("Enter hours worked for Tuesday: "))
    wednesday = float(input("Enter hours worked for Wednesday: "))
    thursday = float(input("Enter hours worked for Thursday: "))
    friday = float(input("Enter hours worked for Friday: "))

    # Create a dictionary to store day and hours worked
    a_dict = {monday : 'Monday', tuesday : 'Tuesday', wednesday : 'Wednesday', thursday : 'Thursday', friday : 'Friday'}

    print('\n')
    
    # Sort from Highest - Lowest and print to console in order
    for hours, day in sorted(a_dict.items(), reverse=True):
        print(f'{day} : {hours} hours')

    print('\n')

    # Get total hours and daily average by sorting through each key item in dictionary
    # and adding them together to get total hours and then dividing them by 5 to get daily average
    total_hours = 0

    for hours in a_dict.keys():
        total_hours += hours    

    print(f'Total hours worked: {total_hours}')
    print(f'Daily Average worked: {total_hours / 5}')

    print('\n')

    # Sort through keys and values in dictionary to find all days with less than 7 hours worked,
    # store the values from those keys into a list, then print list to console
    
    a_list = []

    for hours, day in a_dict.items():
        if hours < 7.0:
            a_list.append(day)
    
    print(a_list)
    # YOUR CODE ENDS HERE

main()