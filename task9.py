def vowel_chars(str):
    vowels = [] #we make it a list because tupple cannot be appended
    str = str.lower()
    list_of_vowels = ["a","e","i","o","u"]
    for character in str:
        if character in list_of_vowels:
            vowels.append(character)
    return vowels

print("Vowels:", sorted(set(vowel_chars("Umuzi")))) #To remove duplicates from list
