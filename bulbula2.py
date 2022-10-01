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

                texpass = Tex("Pass :", font_size=50).shift(UR*3)
                texiteration = Tex("Iteration :", font_size=40).next_to(texpass, DOWN, buff=0.5)

             #   self.play(Write(texpass))
             #  self.play(Write(texiteration))
                
               # texpassno = Tex("123456", font_size=50).next_to(texpass, RIGHT)
                #texiterno = Tex("123456",font_size =40).next_to(texiteration, RIGHT)

             #  self.play(Write(texpassno[0]))
             #  self.play(Write(texiterno[0])) 

                # now you know how to add integer so make it integer and increement after everypass and loop
                intpassno1 = Integer(number=1).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
                intpassno2 = Integer(number=2).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
                intpassno3 = Integer(number=3).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
                intpassno4 = Integer(number=4).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
                intpassno5 = Integer(number=5).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
                intpassno6 = Integer(number=6).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
                intpassno7 = Integer(number=7).set_color(YELLOW).scale(2).next_to(texpass, RIGHT)
               
                intiterno1 = Integer(number=1).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)
                intiterno2 = Integer(number=2).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)
                intiterno3 = Integer(number=3).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)
                intiterno4 = Integer(number=4).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)
                intiterno5 = Integer(number=5).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)
                intiterno6 = Integer(number=6).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)
                intiterno7 = Integer(number=7).set_color(YELLOW).scale(1).next_to(texiteration, RIGHT)

              


                numa = Text("4") #6
                numb = Text("7").shift(3*LEFT) #3
                numc = Text("14").shift(2*LEFT) #4
                numd = Text("21").shift(1*LEFT) #5
                nume = Text("28").shift(5*LEFT)  #1
                numf = Text("47").shift(4*LEFT)  #2

                grnum = VGroup(numa, numb,numc, numd, nume, numf)

                # FINAL POSITION OGF THE NUMBERS ---> 6TH ONE THE RIGHTMOST WILL BE REMOVED FIRST 
                
                numa2 = Text("4") #1
                numb2 = Text("7").shift(1*RIGHT) #2
                numc2 = Text("14").shift(2*RIGHT) #3
                numd2 = Text("21").shift(3*RIGHT) #4
                nume2 = Text("28").shift(4*RIGHT)  #5
                numf2 = Text("47").shift(5*RIGHT)  #6

                
                
                
                
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
                
                gr2 = (circlea,circleb,circlec,circled,circlee,circlef)

                #grouping 2 groups :- grnum and gr and adding in gr for animation 

                gr+=grnum
        
                self.play(FadeIn(gr, shift = DOWN, scale=0.66))

                # gr-=grnum
                #group removed
               
                self.wait(2)
                self.play(gr.animate.shift(UP*2.75),run_time=4)
                
                #self.add(grnum.shift(UP*2.75))

                
                #add text 
                self.play(Write(texpass))
                self.play(Write(texiteration))

                
                self.play(Create(rect))
                self.wait(2)

                #add integer value
                #self.play(Write(texpassno[0]))
                #self.play(Write(texiterno[0])) 

                self.play(Create(intpassno1))#next_to(texpass, RIGHT)
                self.play(Create(intiterno1))#next_to(texiteration, RIGHT)

               
               
                self.play(rect.animate.shift(RIGHT))
                
                    #transform iteration value
                self.play(Transform(intiterno1,intiterno2))

                self.wait(2)
                
            

                #intpassno = intpassno.increment_value(1.0) 
              # intiterno = intiterno.increment_value(1.0) 
              
               # for i in range(1,7) :
                # self.play(Create(intpassno))#next_to(texpass, RIGHT)
                   #self.play(Create(intiterno.number+=i))#next_to(texiteration, RIGHT)
                    #   self.play(Create(intiterno.increment_value(1.0)))#next_to(texiteration, RIGHT)



                self.play(rect.animate.shift(RIGHT))
                
                    #transform iteration value
                self.play(Transform(intiterno1,intiterno3))
                
                self.wait(2)
                
                self.play(rect.animate.shift(RIGHT))
                
                    #transform iteration value
                self.play(Transform(intiterno1,intiterno4))

                
                self.wait(2)
                
                self.play(rect.animate.shift(RIGHT))
                
                    #transform iteration value
                self.play(Transform(intiterno1,intiterno5))

                self.wait(2)
                
                self.play(Transform(rect,rect2))
                
                    #transform iteration value
                self.play(Transform(intiterno1,intiterno6))

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
               #circlef+=numf2

              
                self.play(FadeOut(numf))
                self.play(Transform(squaref,circlef))
                self.play(FadeIn(numf2))

                self.play(FadeOut(nume))
                self.play(Transform(squaree,circlee))
                self.play(FadeIn(nume2))

                self.play(FadeOut(numd))
                self.play(Transform(squared,circled))
                self.play(FadeIn(numd2))

                self.play(FadeOut(numc))
                self.play(Transform(squarec,circlec))
                self.play(FadeIn(numc2))

                self.play(FadeOut(numb))
                self.play(Transform(squareb,circleb))
                self.play(FadeIn(numb2))

                self.play(FadeOut(numa))
                self.play(Transform(squarea,circlea))
                self.play(FadeIn(numa2))

                #gr2 = (circlea,circleb,circlec,circled,circlee,circlef)

                #self.play(gr2.animate.     -----------> scale up and keep in the mid, final sorted array, add sound add text iteration wise

                self.wait(4)
                
                #self.add(gr2)
                #self.play(gr2.animate.shift(DOWN),run_time=2)

                
                
                #do special animation circle by circle

                #self.play(gr2.lag_ratio=0.1,run_time=1.5).shift(DOWN*2)
                #for gr2 in 
           






 
            #no. of pass 
            # and no. of iterations in each pass
            