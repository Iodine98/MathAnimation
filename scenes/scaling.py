from run import run_file
from manim import Scene, MathTex, VGroup, Arrow, Write

if __name__ == '__main__':
    run_file(__file__)


class Scaling(Scene):
    """
    Display the equation property
    """

    def make_equation(self, equation_as_str: str):
        terms = equation_as_str.split()
        return VGroup(*[MathTex(term) for term in terms]).arrange(buff=1.0)

    def setup(self):
        self.to_prove = MathTex(r"2 \cdot p(50) = p(100)")
        self.equations = [
            self.make_equation(r"2 \cdot p(50) = p(2) \cdot p(50)"),
            self.make_equation(
                r"2 \cdot \{(2,1),(5,2)\} = \{(2,1)\} \cup_{p} \{(2,1),(5,2)\}"),
            self.make_equation(
                r"\{(2,1)\} \cup_{p} \{\{(2,1),(5,2)\} \equiv \{(2,1)\} \cup_{p} \{(2,1),(5,2)\}")
        ]
        self.arrows = [
            [Arrow(self.equations[0][i].get_bottom(), self.equations[1]
                   [i].get_top()) for i in range(0, 7, 2)],
            [Arrow(self.equations[1][i].get_bottom(), self.equations[1][i].get_top())
             for i in range(0, 7, 2)]
        ]
        self.to_animate = VGroup(self.to_prove, self.equations[0], *self.arrows[0], *self.arrows[1])

    def construct(self):
        self.play(Write(self.to_animate))
