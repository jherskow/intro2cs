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
        has = False
    elif n % (i-1) == 0:
        has = True
    else:
        has = has_divisor_smaller_than(n, i - 1)
    return has


def is_prime(n):
    """returns bool of prime-ness of int n"""
    return has_divisor_smaller_than(n, n)


def divisors(n):
    pass


def exp_n_x(n, x):
    pass

# ============ NON-LINEAR RECURSION =======================================
