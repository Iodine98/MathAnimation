from run import run_file
from manim import Scene, MathTex, VGroup, Arrow, Write, DOWN, Tex

if __name__ == '__main__':
    run_file(__file__)


class Scaling(Scene):
    """
    Display the equation property
    """

    def make_equation(self, equation_as_str: str):
        terms = equation_as_str.split()
        return VGroup(*[MathTex(term) for term in terms]).arrange()

    def order_animation(self):
        order = [self.equations[0]]
        for j in range(0, 7):
            for i in range(1, len(self.equations)):
                order.append(self.equations[i][j])
                if i-1 < len(self.arrows) and j % 2 == 0:
                    order.append(self.arrows[i-1][j])
        return order

    def setup(self):
        self.equations = VGroup(*[
            Tex(r"To prove: $2 \cdot p(50) = p(100)$"),
            self.make_equation(r"2 \cdot p(50) = p(2) \cdot p(50)"),
            self.make_equation(
                r"p(2) \cdot \{(2,1),(5,2)\} = \{(2,1)\} \cup_{p} \{(2,1),(5,2)\}"),
            self.make_equation(
                r"\{(2,1)\} \cup_{p} \{\{(2,1),(5,2)\} \equiv \{(2,1)\} \cup_{p} \{(2,1),(5,2)\}")
        ]).arrange(DOWN, buff=1.0)
        self.arrows = [
            [Arrow(self.equations[1][i].get_bottom(), self.equations[2]
                   [i].get_top()) for i in range(0, 7)],
            [Arrow(self.equations[2][i].get_bottom(), self.equations[3][i].get_top())
             for i in range(0, 7)]
        ]
        self.to_animate = self.order_animation()

    def construct(self):
        for index, element in enumerate(self.to_animate):
            self.play(Write(element))
            if index == 0:
                self.wait(5)
        self.wait(5)
