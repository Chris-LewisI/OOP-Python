year = int(input("Input Year: "))

if year < 0:
    print(f"Year must be greater than 0")
else:
    remainder = year % 12
    if remainder == 0:
        print(f"Monkey")
    elif remainder == 1:
        print(f"Rooster")
    elif remainder == 2:
        print(f"Dog")
    elif remainder == 3:
        print(f"Pig")
    elif remainder == 4:
        print(f"Rat")
    elif remainder == 5:
        print(f"Ox")
    elif remainder == 6:
        print(f"Tiger")
    elif remainder == 7:
        print(f"Hare")
    elif remainder == 8:
        print(f"Dragon")
    elif remainder == 9:
        print(f"Snake")
    elif remainder == 10:
        print(f"Horse")
    elif remainder == 11:
        print(f"Sheep")
    else:
        print(f"error")
