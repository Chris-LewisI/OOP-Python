# Using the following list, do the following:
# 1. Iterate through each element in the list
# 2. Print out whether the element is positive or negative or zero on a new line for each element.

#create list
myList = [-2, 1, -2, 7, -8, -5, 5, 10, -6, 7, 0]

#create loop to iterate through list
for x in myList:
    #check negative values
    if x < 0:
        print(f"{x} is negative.")
    #check positive values
    elif x > 0:
        print(f"{x} is positive.")
    #if neither negative nor positive then it is 0
    else:
        print(f"{x} is zero.")