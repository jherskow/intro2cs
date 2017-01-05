"""########################################################################
# FILE : helpers.py
# WRITER : Joshua Herskowitz , jherskow , 321658379
# WRITER : Rachel Zilberberg, rachelz , 314421876                          # FILE : helpers.py
# EXERCISE : intro2cs ex9 2016-2017
# DESCRIPTION:
#######################################################################"""
import math
import random

# ============ helper functions ===========================================

# ===== constants =====
HALF_CIRCLE = 180
PI = math.pi
CIRCLE = 360


# ===== Space_objects methods =========

def deg_to_radian(degs):
    """converts degrees to radians"""
    return (degs * PI) / HALF_CIRCLE


def random_heading():
    """returns a random int in given range"""
    return random.randint(1, CIRCLE)


