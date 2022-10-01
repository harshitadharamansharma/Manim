from manim import *
 
class line(Scene):
    def construct(self):
        #23.6.22
        #generate table 
        #add lines in the table
        #li = Line(LEFT, RIGHT).shift(DOWN,LEFT*5) #width=8
        #li1= Line(UP,DOWN).shift(DOWN*1.5,LEFT*3) # height=4


        """li = Line((-6,0,0),(6,0,0))
        li1 = Line((-4,2,0),(-4,-2,0))
        li2  = DashedLine((-3,2,0),(-3,-2,0))
        li3 = DashedLine((-2,2,0),(-2,-2,0))
        li4 = DashedLine((-1,2,0),(-1,-2 ,0))
        li5  = DashedLine((0,2,0),(0,-2,0))
        li6 = DashedLine((1,2,0),(1,-2,0))
        li7 = DashedLine((2,2,0),(2,-2 ,0))
        """


        """"""
        #text in the table
        texpass2 = Tex("Pass: ", font_size=60).shift(LEFT*5.5,UP*1)
        texiteration2 = Tex("Iteration: ", font_size=60).next_to(
            texpass2, DOWN, buff=1.5)


        li = Line((-6,0,0),(6,0,0))
        li1 = Line((-4,1.5,0),(-4,-1.5,0))
        li2  = DashedLine((-2.5,1.5,0),(-2.5,-1.5,0))
        li3 = DashedLine((-1,1.5,0),(-1,-1.5,0))
        li4 = DashedLine((0.5,1.5,0),(0.5,-1.5 ,0))
        li5  = DashedLine((2,1.5,0),(2,-1.5,0))
        li6 = DashedLine((3.5,1.5,0),(3.5,-1.5,0))
        li7 = DashedLine((5,1.5,0),(5,-1.5 ,0))
        

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
        
        

#____

        	
class DrawLine(Scene):
    def construct(self):
        START = (0,0,0)
        END =   (4,0,0)
        line = Line(START,END)
        self.play(Create(line))