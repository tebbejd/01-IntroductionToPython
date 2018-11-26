"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher,
         Aaron Wilkin, their colleagues, and Jacob Tebbe.
"""
########################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#   You should have RUN the  m5e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
#
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

fred = rg.SimpleTurtle('turtle')
fred.pen = rg.Pen('green', 2)
fred.speed = 10

for k in range(15):
    fred.draw_circle(k * 10)
    fred.pen_up()
    fred.right(90)
    fred.forward(k * 10)
    fred.pen_down()

george = rg.SimpleTurtle('turtle')
george.pen = rg.Pen('red', 3)
george.speed = 5

george.pen_up()
george.go_to(rg.Point(275, 175))
george.pen_down()

window.tracer(25)

for k in range(20):
    george.draw_regular_polygon(5,55)
    george.pen_up()
    george.left(45)
    george.forward(10)
    george.pen_down()

window.close_on_mouse_click()