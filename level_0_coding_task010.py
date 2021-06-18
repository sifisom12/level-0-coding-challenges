#Task 0.10

def common_letters(string1, string2):
    for letter1 in range(len(string1)):
        for letter2 in range(len(string2)):
            if string1[letter1] == string2[letter2]:
                print (letter1, letter2)

common_letters("Sifiso", "Sizwe")

