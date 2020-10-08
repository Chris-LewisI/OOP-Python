# Take the following phrase: The only thing we have to fear is fear itself
# 1. Convert it to a list
# 2. Inspect each word in the list
#   - If the word in the list starts with a vowel (excluding y), then:
#       - add the letters "way" to the end of the word.
#       - EX: the word "and" would become "andway"
#   - If the word in the list does not start with a vowel (including y), then:
#       - take the first letter from the word and move it to the end of the word
#       - add to the end of the word, the letters "ay"
#       - EX: the word "money" would become "oneymay"
# 3. Append each modified word to a new list
# 4. convert the list to a string and print that string out 
#   - HINT: use join()

#initializing variables and lists
vowels = "a","e","i","o","u"
extra_vowel = "y"

phrase = "The only thing we have to fear is fear itself"
phrase_list = phrase.split()

new_phrase = []

hasVowel = False

#iterating through the phrase and the vowels
for i in phrase_list:
    for x in vowels:
        if i[0].lower() == x:
            i = i.lower() + "way"
            new_phrase.append(i)
            hasVowel = True
    if hasVowel == True:
        hasVowel = False
        continue
    #checking for "y"
    elif hasVowel == False and i[0] == extra_vowel:
        i = i[1:len(i)].lower() + i[0].lower() + "ay"
        new_phrase.append(i)
    else:
        i = i[1:len(i)].lower() + i[0].lower() + "ay"
        new_phrase.append(i)

new_phrase_string = " ".join(new_phrase)

print(f"{new_phrase_string[0].upper()}{new_phrase_string[1:len(new_phrase_string)]}")

# can use the capitalize method to make the first letter upper case but not taught in class yet I believe
# print(f"{new_phrase_string.capitalize()}")