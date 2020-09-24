# author: CHRIS IBRAHEEM
# OOP Assignment 4: Take the average of the values from the user until they input 0
# When the user enters 0 to end the numbers entered by the user, 
# that last 0 is NOT to be included in the average calculation.

print(f"Enter 0 or Ctrl + C to end the program and show average of values...\n")

#initialize variables
amountOfElements = 0
prevSum = 0
avg = 0

#set loop to while true so that it loops until the user ends it
while True:
    #take user input
    userInput = float(input(f"Value {amountOfElements + 1}: "))

    #if user inputs 0 then program prints the final average, breaks, and ends
    if userInput == 0:
        print(f"Final Average: {avg}")
        break;

    #if user enters a number then the average will be taken and will include the previous numbers they input
    else:
        amountOfElements += 1
        avg = (userInput + prevSum) / amountOfElements
        prevSum = userInput + prevSum
