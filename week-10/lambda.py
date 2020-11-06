# Author: Chris Ibraheem

names_list=['Frank Harrelson', 'Bob Charles', 'Bob Franklin', 'Bob Brody', 'Frank Charles', 'Bob Harrelson', \
'Mack Dobson', 'John Jones', 'Rob Franklin', 'Tom Simpson', 'Rob Harrelson', 'John Brody', \
'Frank Jones', 'John Harrelson','Frank Charles', 'Tom Charles', 'Frank Franklin', 'Frank Charles', \
'John Charles', 'John Franklin', 'Frank Dobson', 'Diane Jones', 'Bob Dobson', 'Tom Harrelson', \
'Rob Simpson', 'Tom Brody', 'Rob Harrelson', 'John Charles', 'Bob Dobson', 'Bob Brody']

# sort names by last name
'''
This first lambda function sorts the list names_list by the key which is defined through the lambda function using the name parameter 
which is assigned to the lastname by using the split()[-1] method.
    - split()[-1] returns the last item in the sequence
'''
names_list.sort(key=lambda name:name.split()[-1])
# print(names_list)

# create username by taking first five characters from last name and first two characters from first name
'''
This method below that is commented out uses three separate lambda functions to assign first the five characters from the last name, then the two characters from the last name,
then it concatenates the two and places it into the usernames list. I selected the specific characters by setting a range in the lambda function. Also, map iterates through all the items
so a loop is not necessary.
'''
# get_five_lastname = list(map(lambda user: user.split()[-1].lower()[:5], names_list))
# get_two_firstname = list(map(lambda user: user.split()[0].lower()[:2], names_list))
# usernames = list(map(lambda first, last: last+first, get_two_firstname, get_five_lastname))
# print(usernames)

'''
The lambda function below takes the other two lambda functions used previously for get_five_lastname and get_two_firstname and uses the functions themself as the input into the overarching lambda function that pushes the usernames into the usernames list.
'''
# usernames = list(map(lambda first, last: last+first, list(map(lambda user: user.split()[0].lower()[:2], names_list)), list(map(lambda user: user.split()[-1].lower()[:5], names_list))))

'''
In this final and most refined example, we use the methods of getting the first five characters of the last name and the first two characters of the last name directly into the argument of the
lambda function. We do this by iterating through every name in names_list and create a new string then add it to the usernames list. This is the most effecient and concise way.
'''
usernames = list(map(lambda name: name.split()[-1].lower()[:5] +  name.split()[0].lower()[:2], names_list))
# print(usernames)