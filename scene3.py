

# text without LaTex ; Using Pango

from typing_extensions import Self
from manim import *


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello world", font_size=144)
        self.add(text)


class SingleLineColor(Scene):
    def construct(self):
        text = MarkupText(
            f'all in red <span fgcolor ="{BLUE}">And this is in Blue </span><span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        self.add(text)

# Pango


class ThanksCPS(Scene):
     def construct(self):
       # worda = MarkupText("Thank you very much") # fgcolor ="YELLOW", weight=BOLD, , font="sans-serif"
       # wordb = MarkupText("CYBER PHYSICAL SYSTEMS LAB") #  fgcolor ="GREEN",weight=BOLD, ,  font="sans-serif"

         # fgcolor ="YELLOW", weight=BOLD, , font="sans-serif"
         worda = MarkupText(
             f' <span fgcolor ="{YELLOW}">Thank you very much </span>')
         # fgcolor ="GREEN",weight=BOLD, ,  font="sans-serif"
         wordb = MarkupText(
             f' <span fgcolor ="{GREEN}">CYBER PHYSICAL SYSTEMS LAB </span>')

         self.add(worda)
         self.play(Transform(worda, wordb))
         self.wait(1)

     #       worda = MarkupText("<span fgcolor ="{YELLOW}"Thank you very much</span>", weight=BOLD, font="sans-serif")
     #       wordb = MarkupText("<span fgcolor ="{GREEN}"CYBER PHYSICAL SYSTEMS LAB</span>", weight=BOLD, font="sans-serif")
    # self.add(worda)
    # self.play(Transform(worda,wordb), Transform(wordb, worda),run_time=2)

     #   self.wait(1)
   # self.add(worda)
  #  self.play(Transform(worda,wordb))
   # self.wait(1)

    # worda = MarkupText("Thank you very much", fgcolor ="YELLOW", weight=BOLD, font="sans-serif")
    # wordb = MarkupText("CYBER PHYSICAL SYSTEMS LAB",  fgcolor ="GREEN",weight=BOLD, font="sans-serif")

  #  self.add(worda)
   # self.play(Transform(worda,wordb))
    # self.wait(1)


class ThanksCPS(Scene):
     def construct(self):
       # worda = MarkupText("Thank you very much") # fgcolor ="YELLOW", weight=BOLD, , font="sans-serif"
       # wordb = MarkupText("CYBER PHYSICAL SYSTEMS LAB") #  fgcolor ="GREEN",weight=BOLD, ,  font="sans-serif"

         # fgcolor ="YELLOW", weight=BOLD, , font="sans-serif"
         worda = MarkupText(
             f' <span fgcolor ="{YELLOW}">Thank you very much </span>')
         # fgcolor ="GREEN",weight=BOLD, ,  font="sans-serif"
         wordb = MarkupText(
             f' <span fgcolor ="{GREEN}">CYBER PHYSICAL SYSTEMS LAB </span>')

         self.add(worda)
         self.wait(4)
         self.play(Transform(worda, wordb))
         self.wait(1)


class FontsExample(Scene):
    def construct(self):
        ft = Text("Noto Sans", font="Noto Sans")
        self.add(ft)


class ThanksCPS2(Scene):
     def construct(self):

         # fgcolor ="YELLOW", weight=BOLD, , font="sans-serif"
         worda = MarkupText(
             f' <span fgcolor ="{YELLOW}">Thank you very much </span>')
         # fgcolor ="GREEN",weight=BOLD, ,  font="sans-serif"
         wordb = MarkupText(
             f' <span fgcolor ="{GREEN}">CYBER PHYSICAL SYSTEMS LAB </span>')

         #word1 = MarkupText("Thank you very much",  weight=BOLD, font="sans-serif", font_size = 56).to_edge(UR).set_color(YELLOW)  #fgcolor ="YELLOW",
        # word2 = MarkupText("CYBER PHYSICAL SYSTEMS LAB", weight=BOLD, font="sans-serif", font_size=64).next_to(self.mobjects[-1],DOWN).set_color(GREEN) #  fgcolor ="GREEN",

         # self.add(Text(f"Thank you very much",  weight=BOLD, font="sans-serif", font_size = 56).to_edge(UR).set_color(YELLOW))  #fgcolor ="YELLOW",
        # selfText("CYBER PHYSICAL SYSTEMS LAB", weight=BOLD, font="sans-serif", font_size=64).next_to(self.mobjects[-1],DOWN) #  fgcolor ="GREEN",

         self.add(worda)
         self.wait(4)
         self.play(Transform(worda,wordb),run_time=4)
         self.wait(1)

         self.remove(wordb)
         self.wait(1)
         
         self.add(wordb)
         self.play(Transform(wordb,worda),run_time=4)
         self.wait(1)

         """self.add(word1)
         self.wait(4)
         self.play(Transform(word1,word2),run_time=4)


         self.wait(4)
         self.play(Transform(word2,word1),run_time=4)

         self.wait(2)"""

