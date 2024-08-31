def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = []

    new_phrase.append(phrase[0].upper())
    new_phrase.append(phrase[1:])

    return ''.join(new_phrase)