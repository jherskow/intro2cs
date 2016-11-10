##############################################################################
# This is an example script which suggests an example for proper
#   documentation. The purpose of good documentation is to make the code
#   readable to anyone, without requiring particular knowledge of the problem
#   being solved.
# The point here is really to think of another programmer which has never read
#   the code and now needs to either use it or modify it and make his life as
#   easy as possible.
# The two main guidelines here are :
#       1. Each function gets its own documentation.
#       2. Parts in the code which are not trivial and require additional
#           explanations, get inline documentation.
##############################################################################


def differentiate(a, b, c):
    """
    Differentiate a polynomial of the form (a*x^2 + b*x + c)
    :param a: The coefficient of x^2 (x squared)
    :param b: The coefficient of x
    :param c: The free coefficient
    :return: 3 parameters, representing the (a, b, c) coefficients of the
    derived polynomial.
    """
    # Here, not everybody which reads my implementation may know how to
    #   compute derivative so it might not be clear to them why is the
    #   result I return is such.
    #   Hence, it is a good place to add a documentation of how the
    #   derivative it is calculated, and a link to an online resource would
    #   be very useful. Following is the actual comment:

    # The derivative of (a*x^2 + b*x + c) is (2*a*x + b). More formally,
    # d/dx (a*x^2 + b*x + c) = 0*x^2 + 2*a*x + b
    # For relevant documentation, see :
    #   http://www.freemathhelp.com/derivative-of-polynomial.html
    a_result = 0
    b_result = 2*a
    c_result = b
    return a_result, b_result, c_result


def derivative_in_point(a, b, c, x):
    """
    Calculate the value of the derivative of the given polynomial
    (a*x^2 + b*x + c) at a specific point (x).
    :param a: The coefficient of x^2 (x squared)
    :param b: The coefficient of x
    :param c: The free coefficient
    :param x: The point in which the derivative should be calculated.
    :return: The value of the derivative of the polynomial at x.
    """
    d_a, d_b, d_c = differentiate(a, b, c)  # here 'd_' stands for "derived"
    # Some documentation on calculating derivative at a specific point :
    #   http://oregonstate.edu/instruct/mth251/cq/Stage5/Lesson/diffPoint.html
    return d_a*x**2 + d_b*x + d_c

poly_a = 2
poly_b = 3
poly_c = 5
evaluation_point = 1
print('The derivative of [' +
      str(poly_a) + 'x^2 + ' +
      str(poly_b) + 'x + ' +
      str(poly_c) +
      '] at x = [' + str(evaluation_point) + ']' +
      ' is: ' +
      str(derivative_in_point(2, 3, 4, 1)))
