
def word_check(string):

    count_vowel = 0
    count_consonants = 0
    count_blank = 0

    vowels = "AaEeIiOoUu"
    nums_chars_space = "~@#$%^&*()123456789 0"

    for i in range(0, len(string)):
        if string[i] in vowels:
            count_vowel += 1
        elif string[i] in nums_chars_space:
            pass
        else:
            count_consonants += 1

    print(count_vowel)
    print(count_consonants)

    ratio = count_vowel/count_consonants
    ratio_limit = round(ratio,2)

    return f'The ratio of the vowel and the consonants is {ratio_limit}'
