def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    index = 0
    new_list = []

    for ele in lst:
        if index % 2 == 0:
            new_list.append(ele)
        index += 1

    return new_list