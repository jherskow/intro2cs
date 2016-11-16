##########################################################################
# FILE : calculate_mathematical_expression
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION: Performs requested basic math operation on two numbers.
##########################################################################

def calculate_mathematical_expression(num1,num2,operator):
    """performs requested basic math operation on two numbers"""

    if operator == "+":      #series of IF/ELIF checks to determine operator
        result = num1 + num2 #do requested operation in requested order
    elif operator == "-":    #as before
        result = num1 - num2 #as before
    elif operator == "/":
        if num2 == 0:   #prevents division by zero
            return None
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    else:               # operator given is not one of 4 basic operations
        return None
    return result

