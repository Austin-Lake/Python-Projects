#Program 3 – Auto Insurance
#Write a program that computes monthly insurance according to the provided schedule. 

#Student #:     
#Student Name:  

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # Get user input for calculation
    gender = input("What is your gender Male(m) / Female(f): ")
    age = float(input("What is your age: "))
    cost = float(input("What is the cost of the car: "))

    # Use user's input in calculation to find monthly rate
    if gender.lower() == 'm' or gender.lower() == 'male':
        if age >= 15 and age < 25:
            cost = (cost * .25) / 12
        elif age >= 25 and age < 40:
            cost = (cost * .17) / 12
        elif age >= 40 and age < 70:
            cost = (cost * .10) / 12
    elif gender.lower() == 'f' or gender.lower() == 'female':
        if age >= 15 and age < 25:
            cost = (cost * .20) / 12
        elif age >= 25 and age < 40:
            cost = (cost * .15) / 12
        elif age >= 40 and age < 70:
            cost = (cost * .10) / 12

    # Print output of calculation 
    print(f"Your monthly insurance rate is ${round(cost, 2)}")

    # YOUR CODE ENDS HERE

main()