from manim import *

class DrawCircle(Scene):
    def construct(self):
        circle = Circle()
        self.play(Create(circle))
        self.wait()