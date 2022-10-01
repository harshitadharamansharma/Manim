from manim import *

class SurroundingRectExample(Scene):
    def construct(self):
        title = Title("A Quote from Newton")
        quote = Text(
            "If I have seen further than others, \n"
            "it is by standing upon the shoulders of giants.",
            color=BLUE,
        ).scale(0.75)
        box = SurroundingRectangle(quote, color=YELLOW, buff=MED_LARGE_BUFF)

        t2 = Tex(r"Hello World").scale(1.5)
        box2 = SurroundingRectangle(t2, corner_radius=0.2)
        mobjects = VGroup(VGroup(box, quote), VGroup(t2, box2)).arrange(DOWN)
        self.add(title, mobjects)




class MovingFrameBox(Scene):
    def construct(self):
        text=MathTex(
            "\\frac{d}{dx}f(x)g(x)=","f(x)\\frac{d}{dx}g(x)","+",
            "g(x)\\frac{d}{dx}f(x)"
        )
        self.play(Write(text))
        framebox1 = SurroundingRectangle(text[1], buff = .1)
        framebox2 = SurroundingRectangle(text[3], buff = .1)
        self.play(
            Create(framebox1),
        )
        self.wait()
        self.play(
            ReplacementTransform(framebox1,framebox2),
        )
        self.wait()