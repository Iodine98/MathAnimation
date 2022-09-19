import math
from run import run_file
from prime_set import PrimeSet
from manim import NumberPlane, Text, Dot, VGroup, DOWN, Scene, DrawBorderThenFill

ROWS = 2
COLS = 4
LOWER_BOUND = 2
INCREMENT = 1
UPPER_BOUND = LOWER_BOUND + ROWS * COLS * INCREMENT
Y_UPPER_BOUND = int(math.log(UPPER_BOUND) / math.log(2)) + 1

if __name__ == '__main__':
    run_file(__file__)


class PrimePlane:
    """
    Setup to create number planes with prime numbers
    """

    def __init__(self, number_input: int, x_upper_bound = None, y_upper_bound = None):
        self.prime_set_obj = PrimeSet(number=number_input)
        self.prime_set = self.prime_set_obj.prime_set
        x_upper_bound = max(self.prime_set.keys()) + 1 if x_upper_bound is None else x_upper_bound
        y_upper_bound = max(self.prime_set.values()) + 1 if y_upper_bound is None else y_upper_bound
        self.numberplane = NumberPlane(
            x_range=[0., x_upper_bound, INCREMENT],
            x_length=2,
            y_length=2,
            y_range=[0., y_upper_bound, 1.])
        self.label = Text(str(self.prime_set_obj), font_size=24)
        self.dots_mapping = {(base, exp): Dot(point=self.numberplane.c2p(float(base), float(exp), 0))
                             for base, exp in self.prime_set.items()}
        self.dots = self.dots_mapping.values()



class Lattice(Scene):
    """
    Display the lattice scene
    """

    def setup(self):
        self.prime_planes = []
        for i in range(LOWER_BOUND, UPPER_BOUND, INCREMENT):
            prime_plane = PrimePlane(i, x_upper_bound=UPPER_BOUND, y_upper_bound=Y_UPPER_BOUND)
            self.prime_planes.append(prime_plane)

    def construct(self):
        plane_graphs = [(prime_plane, VGroup())
                        for prime_plane in self.prime_planes]
        grid_group = VGroup()
        for plane, graph in plane_graphs:
            group = VGroup()
            graph.add(plane.numberplane, *plane.dots)
            group.add(graph, plane.label).arrange(DOWN, buff=1.0)
            grid_group.add(group)
        grid_group.arrange_in_grid(rows=ROWS, cols=COLS)
        self.play(DrawBorderThenFill(grid_group))
        self.wait(5)
