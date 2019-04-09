import random
def num_vowels(string):
    vowels = "aeiou"
    initial=0
    for vowel_count in string:
        if vowel_count in vowels:
            initial = initial + 1
    return initital
