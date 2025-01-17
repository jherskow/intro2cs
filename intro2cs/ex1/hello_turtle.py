##########################################################################
# FILE : hello_turtle.py
# WRITER : Josuha Herskowitz , jherskow , 321658379
# EXERCISE : intro2cs ex0 2016-2017
# DESCRIPTION: A set of functions that use turtle graphics to draw
# petals, stems, and pre-configured combinations of them (flowers).
##########################################################################
import turtle


def intro_test():
    """This is only a test method for printing hello"""
    print("hello")


def draw_petal():
    """draws one petal of a flower, returning to starting point"""
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)
    turtle.forward(30)
    turtle.left(45)
    turtle.forward(30)
    turtle.left(135)


def draw_flower():
    """draws a flower by rotating the turtle between petals and then
                draws a stem"""
    turtle.right(45)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(90)
    draw_petal()
    turtle.right(135)
    turtle.forward(150) # draws the stem


def draw_flower_advanced():
    """draws a flower, and then moves turtle from the bottom of the stem
                to a point 150 to the right of the flower's centre"""
    draw_flower()
    turtle.left(90)
    turtle.up()        #Raise pen for movement
    turtle.forward(150)
    turtle.left(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.down()      #lower pen for drawing


def draw_flower_bed():
    """Draws 3 equally spaced flowers, first moving turtle to screen left to
                center the image."""
    turtle.up()
    turtle.left(180)
    turtle.forward(200)
    turtle.right(180)
    turtle.down()
    for x in range(3):
        draw_flower_advanced()
