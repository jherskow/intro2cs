###########################################################################
# FILE : ex7.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex7 2016-2017
# DESCRIPTION: C
###########################################################################

# ============ LINEAR RECURSION ===========================================


def print_to_n(n):
    """Prints integers 1 up to n including"""
    # See PEP 257 for spec of one-liner docstring
    if n != 1:
        print_to_n(n - 1)
    print(n)
    pass


def print_reversed(n):
    """Prints integers n down to 1 including"""
    if n != 1:
        print(n)
        print_reversed(n-1)
    else:
        print(n)
    pass


def has_divisor_smaller_than(n, i):
    """returns true if n has a divisor d : d>1 """
    if i <= 2:
        return False
    elif n % (i-1) == 0:
        return True
    else:
        return has_divisor_smaller_than(n, i - 1)


def is_prime(n):
    """returns bool of prime-ness of int n"""
    return has_divisor_smaller_than(n, n)


def list_divisors_leq(n, x):
    """Returns an ordered list of natural divisors of natural int n,
    less than or equal to x, and excluding zero."""
    if x == 1:
        list = [x]
        return list
    else:
        if n % x == 0:
            list = [x]
            return list + list_divisors_leq(n, x - 1)
        else:
            return list_divisors_leq(n, x - 1)


def divisors(n):
    """Returns an ordered list of natural divisors of natural int n,
        less than or equal to n, and excluding zero."""
    return list_divisors_leq(n, n)


def fact(n):
    """ returns factorial of natural n"""
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def exp_n_x(n, x):
    """ """
    # This function makes use of the exponential sum formula:
    # http://mathworld.wolfram.com/ExponentialSumFunction.html
    if n != 0:
        return (x**n)/(fact(n)) + exp_n_x(n-1, x)
    else:
        return 1


# ============ NON-LINEAR RECURSION =======================================
