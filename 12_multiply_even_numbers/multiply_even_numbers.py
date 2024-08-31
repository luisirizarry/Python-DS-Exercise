def multiply_even_numbers(nums):
    """Multiply the even numbers.
    
        >>> multiply_even_numbers([2, 3, 4, 5, 6])
        48
        
        >>> multiply_even_numbers([3, 4, 5])
        4
        
    If there are no even numbers, return 1.
    
        >>> multiply_even_numbers([1, 3, 5])
        1
    """
    even_nums = []
    for num in nums:
        if num % 2 == 0:
            even_nums.append(num)
    
    if even_nums:
        new_num = 1
        for num in even_nums:
            new_num *= num
        return new_num
    
    else:
        return 1