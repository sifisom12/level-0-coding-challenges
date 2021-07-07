def vowel_printout(given_string):
    vowels = ("a", "e", "i", "o", "u")    

    for letter in given_string.lower():
        if letter in vowels:
            vowel_output = letter[0]
            print(vowel_output, end= ", ")
      
vowel_printout("Infectious")







