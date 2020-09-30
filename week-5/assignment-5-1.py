lName= input('What is your last name? \n')
fName= input('What is your first name? \n')
streetNum= input('What is your street number? \n')
streetName= input('What is your street name? \n')
apartment= input('What is your apartment number? \n')
city= input('What is your city? \n')
state= input('What is your state? \n').upper()
zipcode= input('What is your zipcode? \n')

# brute method (tedious way)
userInfo = lName, fName, streetNum, streetName, apartment, city, state, zipcode
print(f"{userInfo[0]}, {userInfo[1]}")
print(f"{userInfo[2]} {userInfo[3]}")
print(f"{userInfo[4]}")
print(f"{userInfo[5]}, {userInfo[6]}, {userInfo[7]}")

# collection method
# in order to remove the single quotes and parantheses that appear in the output I would have to use methods beyond the scope of what we have learned!
userInfo2 = (lName, fName), (streetNum, streetName), apartment, (city, state, zipcode)
for item in userInfo2:
    print(f"{item}\n") 