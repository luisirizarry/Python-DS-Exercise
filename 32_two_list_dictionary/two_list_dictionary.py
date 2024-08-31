def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """
    result_dict = {}
    
    num_keys = len(keys)
    num_values = len(values)
    min_length = min(num_keys, num_values)
    
    for i in range(min_length):
        result_dict[keys[i]] = values[i]

    if num_keys > num_values:
        for i in range(num_values, num_keys):
            result_dict[keys[i]] = None
    
    return result_dict
    
    