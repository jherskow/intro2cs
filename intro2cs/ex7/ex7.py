###########################################################################
# FILE : ex7.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex7 2016-2017
# DESCRIPTION: C
###########################################################################
EMPTY_STRING = ''

# ============ LINEAR RECURSION ===========================================


def print_to_n(n):
    """
    Prints integers 1 up to n including
    :param n: natural int
    """
    if n <= 0:
        return
    elif n != 1:
        print_to_n(n - 1)
    print(n)
    return


def print_reversed(n):
    """
    Prints integers n down to 1 including
    :param n: natural int
    """
    if n <= 0:
        pass
    elif n != 1:
        print(n)
        print_reversed(n-1)
    else:
        print(n)
    pass


def has_divisor_smaller_than(n, i):
    """
    returns true if n has a divisor d : d>1
    :param n: natural int
    :param i: natural int
    :return: bool
    """
    if i <= 2:
        return False
    elif n % (i-1) == 0:
        return True
    else:
        return has_divisor_smaller_than(n, i - 1)


def is_prime(n):
    """
    Returns bool of prime-ness of int n
    :param n: natural int
    :return: bool
    """
    if n <= 0:
        return False
    return not has_divisor_smaller_than(n, n)


def list_divisors_leq(n, x):
    """
    Returns an ordered list of natural divisors of natural int n,
    less than or equal to x, and excluding zero.
    :param n: natural int
    :param x: natural int
    :return: list
    """
    if x <= 0:
        return []
    elif x == 1:
        return [x]
    else:
        if n % x == 0:
            return list_divisors_leq(n, x - 1) + [x]
        else:
            return list_divisors_leq(n, x - 1)


def divisors(n):
    """
    Returns an ordered list of natural divisors of natural int n,
    less than or equal to n, and excluding zero.
    :param n: natural int
    :return: list
    """
    if n < 0:
        n = abs(n)
    return list_divisors_leq(n, n)


def fact(n):
    """
    returns factorial of natural n
    :param n: natural int
    :return: int sum
    """
    if n == 0:
        return 1
    else:
        return n * fact(n-1)


def exp_n_x(n, x):
    """
    Returns the exponential sum of n and x
    :param n: natural int
    :param x: real number
    :return: float sum
    """
    # This function makes use of the exponential sum formula:
    # http://mathworld.wolfram.com/ExponentialSumFunction.html
    if n != 0:
        return (x**n)/(fact(n)) + exp_n_x(n-1, x)
    else:
        return 1


# ============ NON-LINEAR RECURSION =======================================


def play_hanoi(hanoi, n, src, dest, temp):
    """
    :param hanoi:
    :param n:
    :param src:
    :param dest:
    :param temp:
    :return:
    """
    if n <= 1:
        pass
    if n > 1:
        play_hanoi(hanoi, n-1, src, temp, dest)
    hanoi.move(src, dest)
    if n > 1:
        play_hanoi(hanoi, n - 1, temp, dest, src)


def binary_permutations(n):
    """a"""
    if n != 0:
        list = binary_permutations(n - 1)
    new_list = []
    if n == 0:
        return [EMPTY_STRING]
    else:
        for str in list:
            new_list.append(str + '0')
            new_list.append(str + '1')
        return new_list


def print_binary_sequences(n):
    """a"""
    list = binary_permutations(n)
    for permutation in list:
        print(permutation)
    pass


def make_sequences(char_list, n):
    """a"""
    if n != 0:
        list = make_sequences(char_list, n - 1)
    new_list = []
    if n == 0:
        return [EMPTY_STRING]
    else:
        for str in list:
            for char in char_list:
                new_list.append(str + char)
        return new_list


def print_sequences(char_list, n):
    """a"""
    list = make_sequences(char_list, n)
    for sequence in list:
        print(sequence)
    pass


def no_repetition_sequences_list(char_list, n):
    """a"""
    return_list = []
    if n > 0:
        for letter in char_list:
            new_char_list = []
            # Create new list without that letter
            for char in char_list:
                new_char_list += char
            new_char_list.remove(letter)
            # Recursion: create n-1 length suffixes, without the letter
            add_list = no_repetition_sequences_list(new_char_list, n - 1)
            # add each combination of letter and legal suffixes
            for word in add_list:
                return_list.append(letter + word)
        # return permutations
        return return_list
    elif n == 0:
        return [EMPTY_STRING]
    else:
        return None


def print_no_repetition_sequences(char_list, n):
    """a"""
    list = no_repetition_sequences_list(char_list, n)
    for sequence in list:
        print(sequence)
    pass
'''
ls = ['a', 'b', 'c', 'd', 'e','f','g','h','i','j','k']
print_no_repetition_sequences(ls, 2)
print(list_divisors_leq(24,24))
print(has_divisor_smaller_than(6,6))
print(is_prime(5))
print_to_n(0)
print_reversed(0)
'''

