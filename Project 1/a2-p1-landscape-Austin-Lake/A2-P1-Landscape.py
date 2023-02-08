#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Get user input to use in calculation

    address = input('Enter address: ')
    length = float(input('Enter length of property in ft: '))
    width = float(input('Enter height of property in ft: '))
    grass_type = input('What type of grass would you like - Fescue(f), Bentgrass(b), Campus(c): ')
    trees = float(input('How many trees do you want: '))

    # Set local variables in calculation

    total = 0 
    base_charge = 1000
    size = length * width

    # Start adding all calculations into total amount

    total += base_charge

    if size > 5000:
        total += 500

    if grass_type.lower() == 'f':
        total += 0.05 * size
    elif grass_type.lower() == 'b':
        total += 0.02 * size
    elif grass_type.lower() == 'c':
        total += 0.01 * size

    total += trees * 100

    # Print address and total amount

    print(f'The total cost for property: {address} is ${round(total, 2)}')

    # YOUR CODE ENDS HERE

main()