def factorial( n ):
    """Function to calculate factorial. The function will return -1 for n < 0. 
    Args:
        n: whole number
    Returns:
        Factorial of n
    """
    if n < 0:
        return -1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial = factorial * i
        return factorial

def combination( n, r ):
    """Function to calculate combination. The function will return -1 for n < 0, r < 0, or r > n. 
    Args:
        n: whole number, total number of items
        r: whole number, total number of items in the set
    Returns:
        Combination of n and r
    """
    if n < 0 or r < 0 or r > n:
        return -1
    a = factorial(n)
    b = factorial(n-r)
    c = factorial(r)
    return a/(b*c)