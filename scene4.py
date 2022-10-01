from manim import *

class BasicMarkupExample(Scene):
    def construct(self):
        text1 = MarkupText("<b>foo</b> <i>bar</i> <b><i>foobar</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

  
class SlantsExample(Scene):
    def construct(self):
        a = Text("Italic", slant=ITALIC)
        self.add(a)      


class DifferentWeight(Scene):
    def construct (self):
        import manimpango

        g = VGroup()
        weight_list = dict  (
            sorted (
            {
                weight :  manimpango.Weight(weight).value
                for weight in manimpango.Weight

            }.items(),
            key=lambda x: x[1],
           )  
        )

        for weight in weight_list:
            g += Text ( weight.name, weight=weight.name, font="Open Sans")
        self.add(g.arrange(DOWN).scale(0.5))




class SimpleColor(Scene):
    def construct(self):
        col = Text("RED COLOR", color=RED)
        self.add(col)

class Textt2cExample(Scene):
    def construct(self):
        t2cindices = Text('Hello', t2c={'[1:-1]': BLUE}).move_to(LEFT)  # ttthiiss ids similar to string slicing
        t2cwords = Text('World',t2c={'rl':RED}).next_to(t2cindices, RIGHT)
        self.add(t2cindices, t2cwords)
#it is Text not MarkupText

class GradientExample(Scene):
    def construct(self):
        t = Text("Hello", gradient =(RED, BLUE,GREEN,YELLOW ),font_size=96, weight = 'BOLD')
        self.add(t)


class GradientExample1(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, BLUE, GREEN), font_size=96)
        self.add(t)

class GradientExample2(Scene):
    def construct(self):
        t = Text("Hello", gradient=(RED, GREEN), font_size=96)
        self.add(t)

class t2gexample(Scene):
    def construct (self):
        t2gindices =Text ( 'CYBER', 
        t2g = { '[1:-1]' : (RED, GREEN),
        },  ).move_to(LEFT)
        t2gwords = Text(
            'WORLD',
            t2g={'WORLD':(YELLOW,BLUE),
            },
        ).next_to(t2gindices,RIGHT)
        self.add(t2gindices, t2gwords)

class LineSpacing(Scene):
    def construct(self):
        a= Text("Hello\nWorld", line_spacing=1)
        b= Text("Hello\nCPS", line_spacing=4)

        self.add(Group(a,b).arrange(LEFT, buff=5))

class DisableLigature(Scene):
    def construct(self):
        li = Text("fl ligature",font_size=96)
        nli = Text("fl ligature", disable_ligatures=True, font_size=96)
        self.add(Group(li, nli).arrange(DOWN, buff=.8))

class IterateColor(Scene):
    def construct(self):
        text = Text("Colors", font_size=96, disable_ligatures=False)
        for letter in text:
            letter.set_color(random_bright_color())
        self.add(text)


class MarkupTest(Scene):
    def construct(self):
        text = MarkupText(
            f'<span underline="double" underline_color="green">double green underline</span> in red text<span fgcolor="{YELLOW}"> except this</span>',
            color=RED,
            font_size=34
        )
        self.add(text)