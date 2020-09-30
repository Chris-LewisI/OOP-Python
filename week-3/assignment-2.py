# Author: Chris Ibraheem

while True:
    # Take user input to check
    user_letter = input("Input Letter: ")
    if user_letter:
        user_letter_lower = user_letter.lower()

        # Testing if user input is a vowel
        # also accounting for capital letters
        if user_letter_lower in ("aeiou"):
            print(f"{user_letter} is a vowel.")

        #Testing if user input is "y"
        elif user_letter == "y" or user_letter == "Y":
            print(f"somtimes {user_letter} is a vowel.")

        # If all above tests fail then the users input is a consonant
        else:
            print(f"{user_letter} is a consonant!")
    else:
        break