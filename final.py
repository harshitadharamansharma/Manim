from manim import *
# from manimlib.imports import *
import numpy as np

class graphx(GraphScene):
    CONFIG={
        "x_min": -4,
        "x_max": 4,
        "y_min": -2,
        "y_max": 2,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        # "graph_origin": 0.5 * DOWN + 0 * LEFT,
    }

    # Defining graph functions 
    def show_function_graph(self): 
        self.setup_axes(animate=True)
        # Math function
        def func(x):
            return x

        graph=self.get_graph(func,x_min=-1,x_max=1)
        self.play(ShowCreation(graph))

#haha constructor
    def construct(self):
        self.show_function_graph()

