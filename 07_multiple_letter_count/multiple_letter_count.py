def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    word_dic = {}
    for letter in phrase:
        if letter in word_dic:
            word_dic[letter] += 1
        else:
            word_dic[letter] = 1
    return word_dic