# Using the following list, do the following:
# 1. Sort it in ascending order
# 2. In a print statement, referencing the list and its index numbers, print the lowest value and the highest value.
# [15, 70, 15, 38, 49, 98, 62, 89, 2, 21, 40, 74, 36, 36, 65, 1, 55, 16, 24, 56]

#Put list in list variable
myList = [15, 70, 15, 38, 49, 98, 62, 89, 2, 21, 40, 74, 36, 36, 65, 1, 55, 16, 24, 56]

#Sort list
myList.sort()

#find the index of the last value
counter = -1 
for x in myList:
    counter = counter + 1

#Print the first and last value in the list
print(f"Lowest Value: {myList[0]}\nHighest Value: {myList[counter]}")