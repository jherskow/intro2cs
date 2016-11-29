##########################################################################
# FILE : ex3.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex3 2016-2017
# DESCRIPTION:
##########################################################################


def create_list():
    """
    saves user string inputs to a list, until "" is entered
    :return: list of inputs in direct order
    """
    list_of_inputs = []
    input_counter = 0
    while True:
        user_input = input()
        if user_input != "":
            list_of_inputs.append(user_input)
            input_counter += 1
        else:
            return list_of_inputs


def concat_list(str_lst):
    """
    concatenates a list of strings into a continuous string, without spaces
    :param str_lst: list of strings
    :return: continuous string
    """
    concat_str = ""
    for string in str_lst:
        concat_str = concat_str + string
    return concat_str


def average(num_list):
    """
    calculates the float average of a list of floats/ints
    :param num_list: list of ints and/or floats
    :return: average (float)
    """
    total, divisor = 0.0, 0.0
    for num in num_list:
        total += num
        divisor += 1
    if divisor == 0:
        return None
    return total / divisor


def cyclic(lst1, lst2):
    """
    Evaluates whether 2 same-length lists are cyclic permutations of each
     other.
    :param lst1: any list
    :param lst2: any list
    :return: Boolean value
    """
    #  Ensure lists are same length
    if len(lst1) != len(lst2):
        return False
    k_length = len(lst1)
    # Iterate over possible shifts (same as list length)
    for shift in range(k_length):
        # Set flag to default value
        same = True
        # Compare each member to its shifted equivalent
        for i in range(k_length):
            if lst1[i] != lst2[(i+shift) % k_length]:
                # Invalidate this iteration
                same = False
        # If no discrepancies were detected in this shift
        # Then there is an equivalent shifted permutation
        if same is True:
            return True
    return False
#DEBUG
# print(cyclic(create_list(),create_list()))


def histogram(n, num_list):
    """
    creates 0-indexed histogram of all numbers between 0 and n-1 in a list
    :param n: 1 more than the greatest number desired in the histogram
    :param num_list: list of numbers
    :return: a list where [0] corresponds to the 0-count and so on.
    """
    histogram_list = []
    for num_index in range(n):
        num_count = 0
        for num in num_list:
            if float(num) == num_index:
                num_count += 1
        histogram_list.append(num_count)
    return histogram_list
#DEBUG
# x = create_list()
# print(histogram(4, x))

def prime_factors(n):
    """
    Displays the prime factors of a positive integer
    :param n: any positive integer
    :return: list of prime factors, from least to greatest
    """
    factors = []
    FIRST_PRIME = 2
    # Since any non-prime number is a multiple of some prime, it is sufficient to check divisibility by all numbers
    # going up. For example, if x is divisible by 4, it will first be divisible by 2.
    for x in range(FIRST_PRIME, n):
        while n%x == 0 :
            factors.append(x)
            n = n/x
    return factors

print(prime_factors(int(input())))


def cartesian(lst1, lst2):
    """
    Returns the cartesian product of two sets
    :param lst1: a set
    :param lst2: another set
    :return: list of (x,y) where x is in set 1 and y is in set 2
    """
    product = []
    for x in lst1:
        for y in lst2:
            product.append([x,y])
    return product
# DEBUG
# print(cartesian(create_list(),create_list()))

def pairs(n, num_list):
    """
    This Function
    :param n:
    :param num_list:
    :return:
    """
    # The ex3 pdf explicitly states that the order is not  significant for the pairs,
    # But the pdf also states that the program must return *all* pairs.
    # So the program will return both permutations of a pair, in accordance with a binary relation.
    sum_pairs = []
    permutations = cartesian(num_list, num_list)
    # print(permutations) #debug
    for pair in permutations:
        if int(pair[0]) + int(pair[1]) == n:
            sum_pairs.append(pair)
    return sum_pairs
# DEBUG
# print(pairs(6, create_list()))

