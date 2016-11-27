##########################################################################
# FILE : bmi.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A non-biased solution to "Do i look fat?"
##########################################################################


def is_normal_bmi(weight, height):
    """
    Returns true if weight(kg)/height(m)^2 is between 18.5 and 24.9.
    Otherwise returns false.
    """
    weight = float(weight)
    height = float(height)
    bmi = float(weight/(height**2))
    if 18.5 <= bmi <= 24.9:
        return True
    else:
        return False
