from run import run_file
from manim import Scene, Text, MathTex, WHITE, UP, DOWN, Arrow, VDict, Write

class PIntersection(Scene):
    """
    Display the P-Intersection operation
    """

    def setup(self):
        self.setup_equations()
        self.setup_arrows()

    def create_title(self):
        title = Text("P-Intersection", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

    def create_first_eq(self):
        terms = [
            ("first_term", MathTex(r"p(50)")),
            ("op", MathTex(r"\div")),
            ("second_term", MathTex(r"p(10)"))
        ]
        return VDict(terms).arrange(buff=0.5)

    def create_second_eq(self):
        terms = [
            ("first_term", MathTex(r"\{(2,1),(5,2)\}")),
            ("op", MathTex(r"\cap_{p}")),
            ("second_term", MathTex(r"\{(2,1),(5,1)\}"))
        ]
        return VDict(terms).arrange(buff=0.5)

    def setup_equations(self):
        eq_list = [
            ("first_eq", self.create_first_eq()),
            ("second_eq", self.create_second_eq()),
            ("third_eq", MathTex(r"\{(5,1)\}"))
        ]
        self.equations = VDict(eq_list).arrange(direction=DOWN, buff=1.5)

    def setup_arrows(self):
        self.arrows = [
            Arrow(start=self.equations["first_eq"]["first_term"].get_bottom(
            ), end=self.equations["second_eq"]["first_term"].get_top()),
            Arrow(start=self.equations["first_eq"]["second_term"].get_bottom(
            ), end=self.equations["second_eq"]["second_term"].get_top()),
            Arrow(start=self.equations["second_eq"]["first_term"].get_bottom(
            ), end=self.equations["third_eq"].get_top()),
            Arrow(start=self.equations["second_eq"]["second_term"].get_bottom(
            ), end=self.equations["third_eq"].get_top())
        ]

    def animate(self, index: int, wait: int = 2):
        animation_items = []
        # index 0
        animation_items.append([
            Write(self.equations["first_eq"])
        ])
        # index 1
        animation_items.append([
            Write(self.arrows[0]),
            Write(self.arrows[1]),
            Write(self.equations["second_eq"])
        ])
        # index 2
        animation_items.append([
            Write(self.arrows[2]),
            Write(self.arrows[3]),
            Write(self.equations["third_eq"])
        ])
        self.play(*animation_items[index])
        self.wait(wait)

    def construct(self):
        self.create_title()
        self.animate(0)
        self.animate(1)
        self.animate(2)
        self.clear()


if __name__ == "__main__":
    run_file("p_intersection.py")
