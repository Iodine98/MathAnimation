from run import run_file
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

if __name__ == '__main__':
    run_file("intro.py")
