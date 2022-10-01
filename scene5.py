# Text using LaTex 
# Tex

from manim import *

class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"\LaTeX", font_size=144)
        self.add(tex)



class MathTeXDemo(Scene):
    def construct(self):
        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xleftarrow{x^6y^8}$", font_size=96)

        self.add(VGroup(rtarrow0, rtarrow1).arrange(DOWN))

class AMSLaTeX(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        self.add(tex)

class AMSLaTeX2(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        ttex =Tex(r'$\mathtt{H} \looparrowleft$ \LaTex', font_size = 144, color=BLUE) #use oonly color not font_color
        self.add(Group(tex,ttex).arrange(DOWN,buff=1))
        
class AMSLaTeX3(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowleft$ \LaTeX', font_size=144)
        self.add(tex)


class AMSLaTeX4(Scene):
    def construct(self):
        tex = Tex(r'$\mathtt{H} \looparrowright$ \LaTeX', font_size=144)
        tex2 =Tex(r'$\mathtt{H} \looparrowleft$ \LaTex', font_size = 144) # font_color=BLUE
      #  self.add(Group(tex,tex2).arrange(DOWN,buff=1))
        self.add(tex)
#


 #20.6.20220       

class LaTeXAttributes(Scene):
    def construct(self):
        tex = Tex(r'Hello \LaTeX', color=BLUE, font_size=144)
        self.add(tex)


class AddPackageLatex(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(
            r"$\mathscr{H} \rightarrow \mathbb{H}$}",
            tex_template=myTemplate,
            font_size=144,
        )
        self.add(tex)       


class LaTeXSubstrings(Scene):
    def construct(self):
        tex = Tex('Hello', r'$\bigstar$', r'\LaTeX', font_size=144)
        tex.set_color_by_tex('o', RED)
        self.add(tex)



class IncorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

class CorrectLaTeXSubstringColoring(Scene):
    def construct(self):
        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        self.add(equation)

class IndexLabelsMathTex(Scene):
    def construct(self):
        text = MathTex(r"\binom{2n}{n+2}", font_size=96)

        # index the first (and only) term of the MathTex mob
        self.add(index_labels(text[0]))

        text[0][1:3].set_color(YELLOW)  #HOw so
        text[0][3:6].set_color(RED)
        self.add(text)


class LaTeXMathFonts(Scene):
    def construct(self):
        tex = Tex(
            r"$x^2 + y^2 = z^2$",
            tex_template=TexFontTemplates.french_cursive,
            font_size=144,
        )
        self.add(tex)

"""
class LaTeXTemplateLibrary(Scene):
    def construct(self):
        tex = Tex('Hello 你好 \\LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        self.add(tex)

"""

class LaTeXAlignEnvironment(Scene):
    def construct(self):
        tex = MathTex(r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', font_size=96)
        self.add(tex)
        
class Test(Scene):
    def construct(self):
        text = Text("something")
        self.play(Write(text))
        self.play(text.animate.to_edge(UP))