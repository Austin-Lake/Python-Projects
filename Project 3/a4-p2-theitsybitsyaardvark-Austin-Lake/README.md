Design and develop a program that presents the user with a “Mad Libs” type game, where a random choice of words are read from a file, then interjected into a story read from another file.

Your solution should demonstrate an understanding of how to apply file I/O, string manipulation, list and looping concepts.

Two files are provided:
•	the_story_file.txt – Text file that contains an incomplete story, broken over four lines of text.
•	the_choices_file.csv – A CSV file containing different series of word types. Each line has a particular format, where the descriptor is the first item, followed by 5 word choices of a certain type (ie. Noun or adjective). 
•	The format of each line in this file is the following:
<phrase describing the word type for this line>,<word choice A>,<word choice B>,<word choice C>,<word choice D>,<word choice E>
In other words, each line of the choices file will contain 6 elements: the first is a phrase describing the word type, which will be displayed in the prompt, the 2nd through 6th contain the different word choices. The word choice text in the Choices file should not contain the letters/numbers used to identify each answer to the user when the program is running.

Examples of word choices file format: 
•	an adjective,hot,cold,big,small,angry
•	a verb ending in ‘ing’,running,walking,bouncing,throwing,eating
When the program is run, the user will be asked to choose a word of each type for each line of the choice file in turn. The first element in each line will be used in the on-screen prompt, while the five choices will be listed as a multiple choice list, preceded by either letters or numbers. Only valid answers (a,b,c,d or 1,2,3,4) should be accepted as valid answers before proceeding to the next word choice. If an invalid answer choice is entered, a message indicating an invalid choice should be displayed, and the user should be prompted to enter a new choice.
When the program has prompted the user to choose one word from each line, the program will read the “story” from the second file and replace the numbered placeholders (ex. _1_, _2_, etc.) with an all-uppercase version of the user-selected word choices. The completed story will be printed on screen.
Note that a single line of text from the “story” file may contain multiple placeholders.

Your solution must contain examples demonstrating your understanding of appropriate use of functions and core assignment concepts (file I/O, 2-d lists).
