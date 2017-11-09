### Solution for C-1.14 (counts the number of vowels in a given string)

def vowelCounter(string):
    vowelsArray = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    vowelCount = 0
    for letter in string:
        if letter in vowelsArray:
            vowelCount+=1
    return vowelCount

#print(vowelCounter(""))
