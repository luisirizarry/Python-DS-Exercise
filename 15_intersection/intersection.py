def intersection(l1, l2):
    """Return intersection of two lists as a new list::
    
        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]
        
        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]
        
        >>> intersection([1, 2, 3], [3, 4])
        [3]
        
        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """
    temp_set_1 = set(l1)
    temp_set_2 = set(l2)
    final_lst = []

    for ele in temp_set_1 & temp_set_2:
        final_lst.append(ele)
    
    return final_lst