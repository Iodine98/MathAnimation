from math import factorial
from run import run_file
from prime_set import PrimeSet
from manim import *


if __name__ == '__main__':
    run_file(__file__)

NUMBER_INPUT = factorial(20)


class LatticeGeneric(Scene):
    """
    Display the lattice scene
    """

    def setup(self):
        self.prime_set = PrimeSet(number=NUMBER_INPUT).prime_set
        x_range = [0., max(self.prime_set.keys()) + 1, 1.]
        y_range = [0., max(self.prime_set.values()) + 5, 1.]
        self.numberplane = NumberPlane(
            x_range=x_range, x_length = 10, y_length = 7, y_range=y_range).to_edge(DOWN)
        self.x_label = self.numberplane.get_x_axis_label("base", buff=0.5)
        self.y_label = self.numberplane.get_y_axis_label("exponent", buff=1., direction=UP)
        self.dots_mapping = {(base, exp): Dot(point=self.numberplane.c2p(float(base), float(exp), 0))
                             for base, exp in self.prime_set.items()}
        self.dots = self.dots_mapping.values()
        self.dots_text = [Text(str(key), font_size=24).next_to(self.dots_mapping[key], UP)
                          for key in self.dots_mapping.keys()]

    def construct(self):
        graph = VGroup()
        graph.add(self.numberplane, *self.dots, *self.dots_text, self.x_label, self.y_label)
        self.play(Create(graph))
        self.wait(5)
