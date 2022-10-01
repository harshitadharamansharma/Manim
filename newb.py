from multiprocessing.connection import wait
from tkinter import W
from turtle import width
from manim import *

class BubbleSort(Scene):
    def construct(self):
        square1 =[
        Square(color=WHITE).scale(0.5).shift(5*LEFT),
        Square(color=WHITE).scale(0.5).shift(4*LEFT),
        Square(color=WHITE).scale(0.5).shift(3*LEFT),
        Square(color=WHITE).scale(0.5).shift(2*LEFT),
        Square(color=WHITE).scale(0.5).shift(1*LEFT),
        Square(color=WHITE).scale(0.5)
        ]

        circle1=[
        Circle(color=YELLOW).scale(0.5).shift(3*DOWN),
        Circle(color=YELLOW).scale(0.5).shift(1*RIGHT,3*DOWN),
        Circle(color=YELLOW).scale(0.5).shift(2*RIGHT,3*DOWN),
        Circle(color=YELLOW).scale(0.5).shift(3*RIGHT,3*DOWN),
        Circle(color=YELLOW).scale(0.5).shift(4*RIGHT,3*DOWN),
        Circle(color=YELLOW).scale(0.5).shift(5*RIGHT,3*DOWN)
        ]


        texpass = Tex("Pass: ", font_size=50).shift(UR*3)
        texiteration = Tex("Iteration: ", font_size=40).next_to(
            texpass, DOWN, buff=0.5)
        rem = Tex("Remarks: ",)

     
     
        # now you know how to add integer so make it integer and increement after everypass and loop
        intpassno = [

        Integer(number=1).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),
        Integer(number=2).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),
        Integer(number=3).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),
        Integer(number=4).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),
        Integer(number=5).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),
        Integer(number=6).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),
        Integer(number=7).set_color(
            YELLOW).scale(2).next_to(texpass, RIGHT),

        ]



        intiterno = [

        Integer(number=1).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=2).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=3).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=4).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=5).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=6).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT)

        ]

        intitern = [
      
        Integer(number=1).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=2).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=3).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=4).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=5).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT),
        Integer(number=6).set_color(
            YELLOW).scale(1).next_to(texiteration, RIGHT)
        ]


        # now let's make it integers
        """numa = Text("4")  # 6
        numb = Text("7").shift(3*LEFT)  # 3
        numc = Text("14").shift(2*LEFT)  # 4
        numd = Text("21").shift(1*LEFT)  # 5
        nume = Text("28").shift(5*LEFT)  # 1
        numf = Text("47").shift(4*LEFT)  # 2
        """
        num =[
        Integer(number=4),  # 6
        Integer(number=7).shift(3*LEFT),  # 3
        Integer(number=14).shift(2*LEFT),  # 4
        Integer(number=21).shift(1*LEFT),  # 5
        Integer(number=28).shift(5*LEFT),  # 1
        Integer(number=47).shift(4*LEFT),  # 2
        ]
        #grnum = VGroup(numa, numb, numc, numd, nume, numf)

        # group number with each boxes
        """
                squarea+=numa
                squareb+=numb
                squarec+=numc
                squared+=numd
                squaree+=nume
                squaref+=numf
                """

        """
                numa=numa+squarea
                numb+=squareb
                numc+=squarec
                numd+=squared
                nume+=squaree
                numf+=squaref
                """


        # FINAL POSITION OGF THE NUMBERS ---> 6TH ONE THE RIGHTMOST WILL BE REMOVED FIRST
        # now let's make it integers
        """ numa2 = Text("4").shift(3*DOWN)  # 1
        numb2 = Text("7").shift(1*RIGHT,3*DOWN)  # 2
        numc2 = Text("14").shift(2*RIGHT,3*DOWN)  # 3
        numd2 = Text("21").shift(3*RIGHT,3*DOWN)  # 4
        nume2 = Text("28").shift(4*RIGHT,3*DOWN)  # 5
        numf2 = Text("47").shift(5*RIGHT,3*DOWN)  # 6
        """

        num2 = [
        Integer(number=4).shift(3*DOWN),  # 1
        Integer(number=7).shift(1*RIGHT,3*DOWN),  # 2
        Integer(number=14).shift(2*RIGHT,3*DOWN),  # 3
        Integer(number=21).shift(3*RIGHT,3*DOWN),  # 4
        Integer(number=28).shift(4*RIGHT,3*DOWN),  # 5
        Integer(number=47).shift(5*RIGHT,3*DOWN)  # 6
        ]

        #Make a python list or dictionary
        """num2 = {
            "numa2" = "Integer(number=4).shift(3*DOWN)"  # 1
            "numb2" = Integer(number=7).shift(1*RIGHT, 3*DOWN)  # 2
            "numc2" = Integer(number=14).shift(2*RIGHT, 3*DOWN)  # 3
            "numd2" = Integer(number=21).shift(3*RIGHT, 3*DOWN)  # 4
            "nume2" = Integer(number=28).shift(4*RIGHT, 3*DOWN)  # 5
            "numf2" = Integer(number=47).shift(5*RIGHT, 3*DOWN)  # 6
        }"""


        # before bubble sort = 28, 47,7,14,21,4
        # loop 6 times
        # 28, >47,7,14,21,4
        # after iteration 1 = ^28, 7, 14, 21, 4,  |  47
        # after iteration 2 = 7, 14, 21,4, | 28 , 47
        # after iteration 3 = 7, 14, 4, | 21, 28, 47
        # after iteration 4 = 7, 4,| 14, 21, 28, 47
        # after iteration 5 = 7,| 4, 14, 21, 28, 47
        # after iteration 6 = | 7, 4, 14, 21, 28, 47
        #  14 ,7, 18, 21, 47, 28
        # after iteration 1 = 7,14,18,21,28,47

        
        rect = Rectangle(width=2, height=2).set_color(
           RED).shift(4.5*LEFT, UP*2.75)

        rect2 = [
        Rectangle(width=2, height=2).set_color(GREEN).shift(UP*2.75),
        Rectangle(width=2, height=2).set_color(GREEN).shift(LEFT,UP*2.75),
        Rectangle(width=2, height=2).set_color(GREEN).shift(2*LEFT,UP*2.75),
        Rectangle(width=2, height=2).set_color(GREEN).shift(3*LEFT,UP*2.75),
        Rectangle(width=2, height=2).set_color(GREEN).shift(4*LEFT,UP*2.75),
        Rectangle(width=2, height=2).set_color(GREEN).shift(5*LEFT,UP*2.75)
        ]




        #for 2nd pass
        rectb = Rectangle(width=2, height=2).set_color(
           RED).shift(4.5*LEFT, UP*2.75)

        #rectb2 = 

        #for 3rd pass
        rectc = Rectangle(width=2, height=2).set_color(
           RED).shift(4.5*LEFT, UP*2.75)

        
        #rectc2 = 

        #for 4th pass
        rectd = Rectangle(width=2, height=2).set_color(
           RED).shift(4.5*LEFT, UP*2.75)

        #rectd2 = 

        #for 5th pass
        recte = Rectangle(width=2, height=2).set_color(
           RED).shift(4.5*LEFT, UP*2.75)

        #recte2 = 

        #for 6th pass
        rectf = Rectangle(width=2, height=2).set_color(
           RED).shift(4.5*LEFT, UP*2.75)

        #rectf2 = 

        #combine all the rectagles / squares ; kindfo matrx or applyb color chaqnge in theshift or make green as a different one.  

        ##gr = VGroup(squarea , squareb, squarec, squared, squaree,squaref)

       #need?  gr2 = VGroup(circlea, circleb, circlec,circled,circlee,circlef)

        # grouping 2 groups :- grnum and gr and adding in gr for animation

        gr += grnum

        self.play(FadeIn(gr, shift=DOWN, scale=0.66))

        # gr-=grnum
        # group removed

        self.wait(2)
        self.play(gr.animate.shift(UP*2.75), run_time=4)

        
        
        # self.add(grnum.shift(UP*2.75))

        # ungoup
        # gr-=grnum

        # add text
        self.play(Write(texpass))
        self.play(Write(texiteration))

        self.play(Create(rect))
        self.wait(2)

        # add integer value
        # self.play(Write(texpassno[0]))
        # self.play(Write(texiterno[0]))
        
        #TRANSFORM intiterno6 to intiterno1
        #Transform(intiterno6,intiterno1)
        self.play(Create(intpassno1))  # next_to(texpass, RIGHT)
        self.play(Create(intiterno1))  # next_to(texiteration, RIGHT)

        """ # call swapanim
        vgrp = VGroup(numa, numb)
        self.play(ApplyFunction(swapanim, vgrp))
        """
        #self.play(Swap(nume,numf))


         #text in the table
        texpass2 = Tex("Pass: ", font_size=60).shift(LEFT*5.5,UP*1)
        texiteration2 = Tex("Iteration: ", font_size=60).next_to(
            texpass2, DOWN, buff=1.5)



        
        finalintiner1 = Integer(number=1).set_color(
            YELLOW).scale(1).next_to(texiteration2, RIGHT)
        finalintiner2 = Integer(number=2).set_color(
            YELLOW).scale(1).next_to(texiteration2, 2*RIGHT)
        finalintiner3 = Integer(number=3).set_color(
            YELLOW).scale(1).next_to(texiteration2, 3*RIGHT)
        finalintiner4 = Integer(number=4).set_color(
            YELLOW).scale(1).next_to(texiteration2, 4*RIGHT)
        finalintiner5 = Integer(number=5).set_color(
            YELLOW).scale(1).next_to(texiteration2, 5*RIGHT)
        finalintiner6 = Integer(number=6).set_color(
            YELLOW).scale(1).next_to(texiteration2, 6*RIGHT)



        #make dictionary of all the lines
        li = Line((-6,0,0),(6,0,0))
        li1 = Line((-4,1.5,0),(-4,-1.5,0))
        li2  = DashedLine((-2.5,1.5,0),(-2.5,-1.5,0))
        li3 = DashedLine((-1,1.5,0),(-1,-1.5,0))
        li4 = DashedLine((0.5,1.5,0),(0.5,-1.5 ,0))
        li5  = DashedLine((2,1.5,0),(2,-1.5,0))
        li6 = DashedLine((3.5,1.5,0),(3.5,-1.5,0))
        li7 = DashedLine((5,1.5,0),(5,-1.5 ,0))
        
        """Lines={
        "li" : "Line((-6,0,0),(6,0,0))",
        "li1" :"Line((-4,1.5,0),(-4,-1.5,0))",
        "li2" :  "DashedLine((-2.5,1.5,0),(-2.5,-1.5,0))",
        "li3" : "DashedLine((-1,1.5,0),(-1,-1.5,0))",
        "li4" : "DashedLine((0.5,1.5,0),(0.5,-1.5 ,0))",
        "li5" :  "DashedLine((2,1.5,0),(2,-1.5,0))",
        "li6" : "DashedLine((3.5,1.5,0),(3.5,-1.5,0))",
        "li7" : "DashedLine((5,1.5,0),(5,-1.5 ,0))",
        }"""
    
    


        self.play(Create(li))

        self.play(Write(texpass2))
        self.play(Write(texiteration2))

        self.play(Create(li1))
        self.play(Create(li2))
        self.play(Create(li3))
        self.play(Create(li4))
        self.play(Create(li5))
        self.play(Create(li6))
        self.play(Create(li7))
        
        #wiggle effecgt for pass onesince 47>28 hence no change
        self.wait(2)
        self.play(Wiggle(numf)) #,run_time(0.4)
        self.play(Wiggle(nume)) #,run_time(0.4)
        
        
       
       # self.play(numa.become(numb))
        #self.play(numb.become(numa))
  
        
        self.play(rect.animate.shift(RIGHT))

          # transform iteration value
        self.play(Transform(intiterno1, intiterno2))
        self.play(Swap(numf,numb))
        self.wait(2)


        #intpassno = intpassno.increment_value(1.0)
      # intiterno = intiterno.increment_value(1.0)

       # for i in range(1,7) :
        # self.play(Create(intpassno))#next_to(texpass, RIGHT)
         # self.play(Create(intiterno.number+=i))#next_to(texiteration, RIGHT)
          #   self.play(Create(intiterno.increment_value(1.0)))#next_to(texiteration, RIGHT)

        self.play(rect.animate.shift(RIGHT))

          # transform iteration value
        self.play(Transform(intiterno1, intiterno3))
        self.play(Swap(numf,numc))
        self.wait(2)

        self.play(rect.animate.shift(RIGHT))

          # transform iteration value
        self.play(Transform(intiterno1, intiterno4))
        self.play(Swap(numf,numd))
        self.wait(2)

        self.play(rect.animate.shift(RIGHT))

          # transform iteration value
        self.play(Transform(intiterno1, intiterno5))
        self.play(Swap(numf,numa))
        self.wait(2)

        self.play(Transform(rect, rect2))

          # transform iteration value
        self.play(Transform(intiterno1, intiterno6))
        
        #self.play(Swap(numf,numa))
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

       # squaref+=numf
       # circlef+=numf2

        self.play(FadeOut(numf))
        self.play(Transform(squaref, circlef))
        self.play(FadeIn(numf2))

        """ #change color:
        self.play(intpassno1.animate.next_to(texpass2,RIGHT*1.5))
        self.play(intiterno6.animate.scale(0.5))

        """
        
        
        
        
        #now shiftcopy pass_no to the table 

        self.play(intpassno1.animate.next_to(texpass2,RIGHT*5.5))
        self.play(intiterno1.animate.next_to(intpassno1,DOWN*5))

        

        #2nd pass
        
        self.play(Create(rectb))
        self.wait(2)


         # transform iteration value
        self.play(Transform(intitern1, intitern2))
        self.play(Swap(nume,numb))
        self.wait(2)

        self.play(rectb.animate.shift(RIGHT))

         # transform iteration value
        self.play(Transform(intitern1, intitern3))
        self.play(Swap(nume,numc))
        self.wait(2)

        self.play(rectb.animate.shift(RIGHT))

         # transform iteration value
        self.play(Transform(intitern1, intitern4))
        self.play(Swap(nume,numd))
        self.wait(2)

        self.play(rectb.animate.shift(RIGHT))

         # transform iteration value
        self.play(Transform(intitern1, intitern5))
        self.play(Swap(nume,numa))
        self.wait(2)

        self.remove()

        self.play(rectb.animate.shift(0.5*RIGHT))
        #self.play(rectb.animate.shift(RIGHT))


        self.play(Transform(rectb, rectb2))

        self.play(squaree.animate.set_fill(GREEN, opacity=0.5))

        self.play(FadeOut(nume))
        self.play(Transform(squaree, circlee))
        self.play(FadeIn(nume2))
        
        self.play(Transform(intitern5,finalintiner5))
      #---
        
        self.play(FadeOut(numd))
        self.play(Transform(squared, circled))
        self.play(FadeIn(numd2))

        self.play(FadeOut(numc))
        self.play(Transform(squarec, circlec))
        self.play(FadeIn(numc2))

        self.play(FadeOut(numb))
        self.play(Transform(squareb, circleb))
        self.play(FadeIn(numb2))

        self.play(FadeOut(numa))
        self.play(Transform(squarea, circlea))
        self.play(FadeIn(numa2))

        #gr2 = (circlea,circleb,circlec,circled,circlee,circlef)

        # self.play(gr2.animate.     -----------> scale up and keep in the mid, final sorted array, add sound add text iteration wise

        self.wait(4)

        # self.add(gr2)
        # self.play(gr2.animate.shift(DOWN),run_time=2)

        # do special animation circle by circle

        # self.play(gr2.lag_ratio=0.1,run_time=1.5).shift(DOWN*2)
        # for gr2 in


    # no. of pass
    # and no. of iterations in each pass
        """
        #23.6.22
        #generate table 
        #add lines in the table
        li = Line(width=8).shift(DOWN,LEFT*5)
        li1= Line(height=4).shift(DOWN*1.5,LEFT*3)
        
        self.play(Create(li))
        self.play(Create(li1))
        """