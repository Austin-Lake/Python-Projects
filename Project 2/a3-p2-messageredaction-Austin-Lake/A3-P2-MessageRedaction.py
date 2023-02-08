#Program 2 – Message Redaction
#Description:   Design and write a program that counts and removes all desired letters from 
#               any user-entered sentence or phrase.

#Student #: W0420180    
#Student Name: Austin Lake

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    '''
    Design Overview:
    Take a user entered string and a list of characters,
    loop through the string and replace all occurences of each character in the list with an underscore
    '''

    # Get a string from the user
    user_string = input("Enter a sentence: ")

    # Check to see if user wants to quit
    if (user_string.lower() == 'quit'):
        quit()

    # Create a list storing all the characters to replace
    letters = ['a', 'e', 'o', 't', 'u', 'p']

    # Loop through each letter in the string
    # and if the letter is in the list of characters replace it with an _ and a +1 to the count
    count = 0
    
    for letter in user_string.lower():
        if letter in letters:
            user_string = user_string.replace(letter, '_', 1)
            count += 1

    # Print the modified string
    print(f'{user_string} - Letters removed: {count}')

    # Rerun function
    main()
    # YOUR CODE ENDS HERE

main()