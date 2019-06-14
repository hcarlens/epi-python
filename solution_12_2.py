""" Is an anonymous letter constructible? """

from collections import Counter

def is_constructible_pythonic(anonymous_letter, magazine):
    return (not Counter(anonymous_letter) - Counter(magazine))

def is_constructible(anonymous_letter, magazine):

    # count character frequencies as they occur in the letter
    char_frequency_for_letter = Counter(anonymous_letter)

    # iterate over the magazine until we either have enough letters
    # or get to the end of the magazine
    for c in magazine:
        if c in char_frequency_for_letter:
            char_frequency_for_letter[c] -= 1
            if char_frequency_for_letter[c] == 0:
                del char_frequency_for_letter[c]
            if not char_frequency_for_letter:
                # all characters have been matched
                return True
    
    return not char_frequency_for_letter

