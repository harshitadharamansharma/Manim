from multiprocessing.connection import wait
from tkinter import W
from manim import *

   
class BubbleSort(Scene):
    def construct(self):
                squarea = Square(color=WHITE).scale(0.5).shift(5*LEFT)
                squareb = Square(color=WHITE).scale(0.5).shift(4*LEFT)
                squarec = Square(color=WHITE).scale(0.5).shift(3*LEFT)
                squared = Square(color=WHITE).scale(0.5).shift(2*LEFT)
                squaree = Square(color=WHITE).scale(0.5).shift(1*LEFT)
                squaref = Square(color=WHITE).scale(0.5)

                circlea = Circle(color=YELLOW).scale(0.5)
                circleb = Circle(color=YELLOW).scale(0.5).shift(1*RIGHT)
                circlec = Circle(color=YELLOW).scale(0.5).shift(2*RIGHT)
                circled = Circle(color=YELLOW).scale(0.5).shift(3*RIGHT)
                circlee = Circle(color=YELLOW).scale(0.5).shift(4*RIGHT)
                circlef = Circle(color=YELLOW).scale(0.5).shift(5*RIGHT)

                
                numa = Text("4") #6
                numb = Text("7").shift(3*LEFT) #3
                numc = Text("14").shift(2*LEFT) #4
                numd = Text("21").shift(1*LEFT) #5
                nume = Text("28").shift(5*LEFT)  #1
                numf = Text("47").shift(4*LEFT)  #2

                grnum = VGroup(numa, numb,numc, numd, nume, numf)

                #before bubble sort = 28, 47,7,14,21,4
                #loop 6 times 
                # 28, >47,7,14,21,4
                #after iteration 1 = ^28, 7, 14, 21, 4,  |  47
                #after iteration 2 = 7, 14, 21,4, | 28 , 47
                #after iteration 3 = 7, 14, 4, | 21, 28, 47  
                #after iteration 4 = 7, 4,| 14, 21, 28, 47
                #after iteration 5 = 7,| 4, 14, 21, 28, 47
                #after iteration 6 = | 7, 4, 14, 21, 28, 47
                #  14 ,7, 18, 21, 47, 28
                # after iteration 1 = 7,14,18,21,28,47
                
                rect = Rectangle(width=2,height=2).set_color(RED).shift(4.5*LEFT, UP*2.75)

        
                rect2 = Rectangle(width=2,height=2).set_color(GREEN).shift(UP*2.75)
                
           
               
                gr = VGroup(squarea , squareb, squarec,squared,squaree,squaref)
                
                #gr2 = (circlea,circleb,circlec,circled,circlee,circlef)

                #grouping 2 groups :- grnum and gr and adding in gr for animation 

                gr+=grnum
        
                self.play(FadeIn(gr, shift = DOWN, scale=0.66))

                # gr-=grnum
                #group removed
               
                self.wait(2)
                self.play(gr.animate.shift(UP*2.75),run_time=4)
                
                #self.add(grnum.shift(UP*2.75))
                
                self.play(Create(rect))
                self.wait(2)

                self.play(rect.animate.shift(RIGHT))
                self.wait(2)
                
                self.play(rect.animate.shift(RIGHT))
                self.wait(2)
                
                self.play(rect.animate.shift(RIGHT))
                self.wait(2)
                
                self.play(rect.animate.shift(RIGHT))
                self.wait(2)
                
                self.play(Transform(rect,rect2))
                self.wait(2)

                self.play(FadeOut(rect))

                self.play(squaref.animate.set_fill(GREEN, opacity=0.5))



                """

                framebox1 = SurroundingRectangle(grnum[1],grnum[2])
                #framebox2 = SurroundingRectangle(squareb,squarec, buff = .1)
                #framebox3 = SurroundingRectangle(squarec,squared, buff = .1)
                #framebox4 = SurroundingRectangle(squared,squaree, buff = .1)
                #framebox5 = SurroundingRectangle(squaree,squaref, buff = .1)

                self.play(
                Create(framebox1),
                 )

                self.play(
                Transform(framebox1,framebox2),
                )
               """
                self.wait()

                self.play(Transform(squaref,circlef))
                self.play(Transform(squaree,circlee))
                self.play(Transform(squared,circled))
                self.play(Transform(squarec,circlec))
                self.play(Transform(squareb,circleb))
                self.play(Transform(squarea,circlea))

                gr2 = (circlea,circleb,circlec,circled,circlee,circlef)

                #self.play(gr2.animate.     -----------> scale up and keep in the mid, final sorted array, add sound add text iteration wise

                self.wait(4)
                
                #self.add(gr2)
                #self.play(gr2.animate.shift(DOWN),run_time=2)

                
                
                #do special animation circle by circle

                #self.play(gr2.lag_ratio=0.1,run_time=1.5).shift(DOWN*2)
                #for gr2 in 
           






 
            