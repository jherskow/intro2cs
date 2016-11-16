##########################################################################
# FILE : calculate_mathematical_expression
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex1 2016-2017
# DESCRIPTION: Performs requested basic math operation on two numbers.
##########################################################################

def calculate_mathematical_expression(num1,num2,operator):
    """
    performs requested basic math operation on the two given numbers, and
    returns the result.
    """
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

def calculate_from_string(expression): # ("num1 operator num2") (spaces incl)
    """
    parses a string 'num1 operator num2' into a math expression,
    and then returns the result
    """
    parse = expression.split(' ')
    num1 = float(parse[0])
    operator = parse[1]
    num2 = float(parse[2])
    return (calculate_mathematical_expression(num1,num2,operator))


