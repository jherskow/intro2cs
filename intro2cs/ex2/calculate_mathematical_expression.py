##########################################################################
# FILE : calculate_mathematical_expression
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION: Performs requested basic math operation on two numbers.
##########################################################################

def calculate_mathematical_expression(num1,num2,operator):
    """performs requested basic math operation on two numbers"""
    if (operator == "+"):
        result = num1 + num2
    else if (operator == "-"):
        result = num1 - num2
    else if (operator == "/"):
        if (num2 == 0):
            return None
        result = num1 / num2
    else if (operator == "*"):
        result = num1 * num2
    else
        return None
    return result

