from run import run_file
from manim import Text, WHITE, UP, DOWN, VGroup, Scene, MathTex, Arrow, Transform


class PUnion(Scene):
    """
    Display the P-Union operation
    """

    def setup(self):
        first_line_eq = self.create_first_eq()
        second_line_eq = self.create_second_eq()
        third_line_eq = MathTex(r"p(50) = \{(2,1), (5,2)\}")
        self.vertical_group_1 = self.create_vertical_group_one(
            first_line_eq, second_line_eq)
        self.vertical_group_2 = self.create_vertical_group_two(
            first_line_eq, third_line_eq)

    def create_title(self):
        title = Text("P-Union", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

    def create_first_eq(self):
        tex1_0 = MathTex(r"p(50) = ")
        tex1_1 = MathTex(r"p(5)")
        tex1_op = MathTex(r"\cup_{p}")
        tex1_2 = MathTex(r"p(10)")
        return VGroup(tex1_0, tex1_1, tex1_op, tex1_2).set_x(0).arrange()

    def create_second_eq(self):
        tex2_0 = MathTex(r"p(50) = ")
        tex2_1 = MathTex(r"\{(5,1)\}")
        tex2_op = MathTex(r"\cup_{p}")
        tex2_2 = MathTex(r"\{(2,1), (5,1)\}")
        return VGroup(tex2_0, tex2_1, tex2_op, tex2_2).set_x(0).arrange()

    def create_vertical_group_one(self, eq_one, eq_two):
        vertical_group = VGroup(eq_one, eq_two).arrange(
            direction=DOWN, buff=2.0)
        left_arrow = Arrow(
            vertical_group[0][1].get_bottom(), eq_two[1].get_top())
        right_arrow = Arrow(
            vertical_group[0][3].get_bottom(), eq_two[3].get_top())
        return vertical_group + left_arrow + right_arrow

    def create_vertical_group_two(self, eq_one, eq_two):
        vertical_group = VGroup(eq_one, eq_two).arrange(
            direction=DOWN, buff=2.0)
        center_arrow = Arrow(
            vertical_group[0].get_bottom(), vertical_group[1].get_top())
        return vertical_group + center_arrow

    def construct(self):
        self.create_title()
        self.add(self.vertical_group_1)
        self.wait(2)
        self.play(Transform(self.vertical_group_1, self.vertical_group_2))
        self.wait(3)
        self.clear()


if __name__ == '__main__':
    run_file("p_union.py")
