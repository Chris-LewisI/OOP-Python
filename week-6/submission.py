# Assignment 1
myList = [15, 70, 15, 38, 49, 98, 62, 89, 2, 21, 40, 74, 36, 36, 65, 1, 55, 16, 24, 56]
myList.sort()
counter = -1 
for x in myList:
    counter = counter + 1
print(f"Lowest Value: {myList[0]}\nHighest Value: {myList[counter]}")



# Assignment 2
myList = [-2, 1, -2, 7, -8, -5, 5, 10, -6, 7, 0]
for x in myList:
    if x < 0:
        print(f"{x} is negative.")
    elif x > 0:
        print(f"{x} is positive.")
    else:
        print(f"{x} is zero.")



# Assignment 3
myList = []
for x in range(1, 51, 2):
    myList.append(x)
for x in myList:
    print(f"{x}")



# Assignment 4
vowels = "a","e","i","o","u"
extra_vowel = "y"

phrase = "The only thing we have to fear is fear itself"
phrase_list = phrase.split()

new_phrase = []

hasVowel = False

for i in phrase_list:
    for x in vowels:
        if i[0].lower() == x:
            i = i.lower() + "way"
            new_phrase.append(i)
            hasVowel = True
    if hasVowel == True:
        hasVowel = False
        continue
    elif hasVowel == False and i[0] == extra_vowel:
        i = i[1:len(i)].lower() + i[0].lower() + "ay"
        new_phrase.append(i)
    else:
        i = i[1:len(i)].lower() + i[0].lower() + "ay"
        new_phrase.append(i)

new_phrase_string = " ".join(new_phrase)

print(f"{new_phrase_string[0].upper()}{new_phrase_string[1:len(new_phrase_string)]}")