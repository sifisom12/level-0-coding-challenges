# Task 0.9

def vowel_printout(given_string):
    vowels = ("a", "e", "i", "o", "u")    

    for letter in given_string.lower():
        if letter in vowels:
            print(letter)

vowel_printout("Incredible")


