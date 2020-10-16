# Author: Chris Ibraheem
# The following code below will use the random module to create a list of values from 1 to 10.
# Using the code below to create a random list of values, do the following:
# Count the number of times each number (1-10) appears in the list that was created. Print out a formatted string that lists the number and the count for that number Use a set object to remove the duplicates from the list. Confirm the set successfully removed the duplicates by printing out the length of the set.

# imports random library so that it can create a list with random variables
import random
random.seed(1)
list_of_numbers=[random.randint(1,10) for i in range(100)]

# counting and printing the amount of occurrences for each of the numbers 1 - 10 
for x in range(1,11):
    counter = 0
    for y in list_of_numbers:
        if x == y:
            counter = counter + 1
    print(f"{x}:\t{counter}")

# create a set to remove duplicates and display it to verify
set_of_numbers = set(list_of_numbers)
print(f"Set Of Numbers: {set_of_numbers}")