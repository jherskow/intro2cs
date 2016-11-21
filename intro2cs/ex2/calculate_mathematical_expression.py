##########################################################################
# FILE : calculate_mathematical_expression
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: Functions that parse and solve Basic math expressions.
##########################################################################


def calculate_mathematical_expression(num1, num2, operator):
    """
    performs requested basic math operation on the two given numbers, and
    returns the result.
    """
    # series of IF/ELIF checks to determine operator
    if operator == "+":
        result = num1 + num2 # given operation in given order
    elif operator == "-":
        result = num1 - num2
    elif operator == "/":
        # prevent division by zero
        if num2 == 0:
            return None
        result = num1 / num2
    elif operator == "*":
        result = num1 * num2
    else:           # if operator given is not one of 4 basic operations
        return None
    return result


def calculate_from_string(expression):
    """
    parses a string 'num1 operator num2' into a math expression,
    and then returns the result
    """
    # parse expression to list
    parse = expression.split(' ')
    # extract expression from list, casting numbers to float
    num1 = float(parse[0])
    operator = parse[1]
    num2 = float(parse[2])
    # passing the parsed expression to the calculate function
    result = calculate_mathematical_expression(num1,num2,operator)
    return result
