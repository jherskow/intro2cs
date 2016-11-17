##########################################################################
# FILE : largest_and_smallest.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: Returns the largest and smallest of 3 numbers.
# It's easier than trying to find a ruler.
##########################################################################

def largest_and_smallest(num1, num2, num3):
    """returns the largest number first and the smallest second"""
    if num1 >= num2:
        if num2 >= num3:  #1>=2>=3
            big = num1
            small = num3
        elif num1 >= num3:  #1>=3>=2
            big = num1
            small = num2
        else:               #3>=1>=2
            big = num3
            small = num2
    else:
        if num1 >= num3:     #2>=1>=3
            big = num2
            small = num3
        elif num2 >= num3:   #2>=3>=1
            big = num2
            small = num1
        else:               #3>=2>=1
            big = num3
            small = num1
    return big, small

print(largest_and_smallest(1,1,4))
