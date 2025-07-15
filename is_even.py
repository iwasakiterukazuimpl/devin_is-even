def is_even(n):
    """
    Check if a given integer is even.
    
    An integer is even if it is divisible by 2 with no remainder.
    Zero is considered even.
    
    Args:
        n (int): The integer to check
        
    Returns:
        bool: True if n is even, False if n is odd
        
    Examples:
        >>> is_even(2)
        True
        >>> is_even(3)
        False
        >>> is_even(0)
        True
        >>> is_even(-2)
        True
    """
    return n % 2 == 0
