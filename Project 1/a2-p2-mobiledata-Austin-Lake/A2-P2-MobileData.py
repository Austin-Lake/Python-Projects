#Program 2 – Erehwon Mobile Data Plans
#Erewhon Mobile charges cellular customers a rate based on the total amount of data used by a customer 
# in the billing period. For simplicity, customers are charge based on which range their total data usage 
# falls within.
# Note, it is not a cumulative charge; your program will figure out which single range the usage falls into, 
# then calculate the cost based on that range’s cost. 

#Student #: 
#Student Name:

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Get user's data usage

    usage = float(input('Enter total usage in GB: '))

    # Use user's input in calculation to find total cost

    if usage <= .200:
        total_cost = 20
    elif usage > .200 and usage <= .500:
        total_cost = (usage * 1000) * .105
    elif usage > .500 and usage <= 1:
        total_cost = (usage * 1000) * .110
    elif usage > 1:
        total_cost = 118

    # Print user's total data cost to console

    print(f'Your total is ${total_cost}')

    # YOUR CODE ENDS HERE

main()