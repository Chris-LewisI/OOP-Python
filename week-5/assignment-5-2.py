print("Press 'Enter' to close program\n")
while True:
    user_input = input("Date (YYYY-MM-DD): \n")
    if user_input == '':
        break
    else:
        date_tuple = user_input.split('-')

        months = "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", 'November', "December"
        monthDays = 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31

        days_and_months = (months, monthDays)

        year = int(date_tuple[0])
        month = int(date_tuple[1])
        day = int(date_tuple[2])

        if year >= 0:
            if day < 1 or day <= int(days_and_months[1][month-1]):
                if month > 0 and month < 13:
                    print(f"{months[month-1]} {day}, {year}")
                else:
                    print("Month must be equal to or between 1 and 12.")
            else:
                print("Days must be within month's parameters.")
        else:
            print('Year cannot be negative.')
        print("\n")