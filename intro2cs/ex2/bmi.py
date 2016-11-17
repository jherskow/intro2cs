##########################################################################
# FILE : bmi.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex2 2016-2017
# DESCRIPTION: A non-biased solution to "Do i look fat?"
##########################################################################

def is_normal_bmi(weight,height):
    """
    Returns true if weight(kg)/height(m) is between 18.5 and 24.9.
    Otherwise returns false.
    """

    bmi = float(weight/height)
    if bmi <= 24.9 and bmi >= 18.5
        return True
    else
        return False
