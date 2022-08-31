from manim import Scene, Text, Write

class Intro(Scene):
    """
    Display the video's intro
    """
    def construct(self):
        text = Text("Let me introduce you to the world of P-sets...", font_size=48)
        self.play(Write(text))
        self.wait()
        self.clear()
