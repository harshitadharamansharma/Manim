from turtle import left, right
from manim import *

class Createcircle(Scene):
     def construct(self):
         circle = Circle() #create a circle
         circle.set_fill(PINK, opacity=0.5) # set the color and transparency
         self.play(Create(circle)) #show the circle on screen

         #mp4 video as output ; -p for auto play after pql

class SquareToCircle(Scene):
    def construct (self):
        circle = Circle() #create a circle
        circle.set_fill(PINK, opacity=0.5) #set color andd transparency

        square = Square() #create a square
        square.rotate(PI/4) # rotate a certain amount
        
        self.play(Create(square)) #animate the creation of the square        
        self.play(Transform(square,circle)) #interpolate the Square into the circle      
        self.play(FadeOut(square)) #fade out animation


class SquareToCirclE(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)  # ye bina animate ke self.play mein nhi hai toh jab .animater lagaoge toh direct self.play ke andar // kar skte ho ke andr 
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

# positioning Mobjects

class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen
                   #create is a predefined animation  
        # next_to is a Mobject method for positioning Mobjects.

#Using .animate syntax to animate methods

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square  ; you can also try flip() instead of rotate(PI / 4)
        self.play(ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class DifferentRotations2(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * RIGHT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

class DifferentRotations3(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * RIGHT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * LEFT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()

""""this is 
multiline comment in newwsdfsdfer versiodfsfshnds of python
fksdghksdfh"""

""" self.play are sections of the final video which gets created and each section contains atleast 1 animation ____.animate.___
when we create new broad files  
and tries to....
ok .....
so 
 here in line 60   self.play(ReplacementTransform(square, circle)
 ReplacementTransform(square, circle) is a predefined animation 
 and similarly in line 20, 21, 22
  self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))

create, transfoem , fadeout all these are predefines animations"""

class Df(Scene):
    def construct(self):
        self.next_section()
        self.add(Circle())
            # now we wait 1sec and have an animation to satisfy the section
        self.wait()
        self.next_section()


"""class Dff(Scene):
    def construct(self):
    # play the first animations...
    # you don't need a section in the very beginning as it gets created automatically
   # self.next_section("bh")
    # play more animations...
    self.next_section("this is an optional name that doesn't have to be unique")
    # play even more animations...
    self.next_section("this is a section without any animations, it will be removed")
"""


