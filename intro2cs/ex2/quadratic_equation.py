##########################################################################
# FILE : quadratic_equation.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A simple quadratic solver.
##########################################################################

def quadratic_equation(a,b,c):
    """
    Returns list all x solutions for ax^2 +bx +c. = 0
    a,b,c are all given as inputs.
    """
    #This function makes use of the quadratic formula, and the quadratic
    #discriminant and its properties. See:
    #https://www.wikiwand.com/en/Quadratic_function#/Exact_roots

    x=[None,None]    #assign default values for x
    discriminant = (b**2 - 4*a*c)
    if discriminant >= 0:    #if x has at least one solution
        x[0]= (-b + discriminant**(1/2) ) / (2*a) #assign first solution
        #add second solution if non-zero discriminant
        if discriminant != 0:
            x[1]= (-b - discriminant**(1/2) ) / (2*a) #second
    #if discriminant is negative, x will be empty.
    return x

print(quadratic_equation(1,-2,34.5))