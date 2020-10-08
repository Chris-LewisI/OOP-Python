# Create a new list using the range function, appending the values from the range function's output into the list.
# The range function must:
# 1. Start at 1
# 2. Stop at 50
# 3. Skip every other number
# Hint: Use either a for loop or a list comprehension

#initialize list
myList = []

#create range function to go from 1-50 and skip every other number
for x in range(1, 51, 2):
    #append it to the list initialized above
    myList.append(x) #this results in all the outputs being odd

#print out the list
for x in myList:
    print(f"{x}")