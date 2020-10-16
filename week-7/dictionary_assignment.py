# Author: Chris Ibraheem
# Dictionaries!
# In this exercise, your task is to ask the user to input an integer between 0 and 999 and return a string containing the English words for that num. For example, if the value of 142 is entered, then the code should print out "one hundred forty two".
# Use one or more dictionaries to implement the solution rather than large if/elif/else constructs. 
# You can use if statements, just not as the only method to solve this challenge.

print("Enter anything other than an integer to end the program.\n")

# creating first dictionary these numbers cannot be concatenated to be made but can be concatenated to other strings to make larger numbers
num_dictionary = {0:'', 1:'One', 2:'Two', 3: 'Three', 4:'Four', 5:'Five', \
6:'Six', 7:'Seven', 8:'Eight', 9:'Nine', 10:'Ten', \
11:'Eleven', 12:'Twelve', 13:'Thirteen', 14:'Fourteen', 15:'Fifteen', \
16:'Sixteen', 17:'Seventeen', 18:'Eighteen', 19:'Nineteen'}

# creating second dictionary these numbers also cannot be concatenated to be made but can be concatenated to other strings to make larger numbers
num_dictionary2 = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy', 8:'Eighty', 9:'Ninety'}

# loop will run until variable other than int is input. 
while True:
    user_num = int(input('Enter Integer between 0-999:'))
    
    # if(s), elif(s), else(s) used to find size of value and manage concatenation accordingly.
    if user_num == 0:
        print("Zero")
    elif 0 < user_num < 20:
        print(f"{num_dictionary[user_num]}")
    elif 20 <= user_num < 100:
        tens = int(user_num / 10)
        remainder = user_num % 10
        print(f"{num_dictionary2[tens]} {num_dictionary[remainder]}")
    elif 100 <= user_num < 1000:
        hundreds = int(user_num / 100)
        remainder = user_num % 100
        if remainder == 0:
            print(f'{num_dictionary[hundreds]} Hundred')
        elif remainder < 20:
            print(f'{num_dictionary[hundreds]} Hundred {num_dictionary[remainder]}')
        elif remainder > 19:
            remainder2 = (remainder % 10)
            remainder = int(remainder/10)
            print(f'{num_dictionary[hundreds]} Hundred {num_dictionary2[remainder]} {num_dictionary[remainder2]}')