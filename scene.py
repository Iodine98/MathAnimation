from manim import *

class PSets(Scene):
    def intro(self):
        text = Text("Let me introduce you to the world of P-sets...", font_size=48)
        self.play(Write(text))
        self.wait()
        self.clear()

    def p_function(self):
        title = Text("P-Union", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))

        tex1_0 = MathTex("p(50) = ")
        tex1_1 = MathTex("p(5)")
        tex1_op = MathTex("\cup_{p}")
        tex1_2 = MathTex("p(10)")
        first_line_eq = VGroup(tex1_0, tex1_1, tex1_op, tex1_2).set_x(0).arrange()

        tex2_1 = MathTex("\{(5,1)\}")
        tex2_op = MathTex("\cup_{p}")
        tex2_2 = MathTex("\{(2,1), (5,1)\}")
        second_line_eq = VGroup(tex2_1, tex2_op, tex2_2).set_x(0).arrange()

        
        second_line_eq = VGroup(tex2_1, tex2_op, tex2_2).set_x(0).arrange()
        third_line_eq = MathTex("\{(2,1), (5,2)\}")


        vertical_group_1 = VGroup(first_line_eq, second_line_eq).arrange(direction=DOWN, aligned_edge=LEFT, buff=2.0)
        left_arrow = Arrow(vertical_group_1[0][1].get_bottom(), second_line_eq[0].get_top())
        right_arrow = Arrow(vertical_group_1[0][3].get_bottom(), second_line_eq[2].get_top())

        vertical_group_2 = VGroup(first_line_eq, third_line_eq).arrange(direction=DOWN, aligned_edge=LEFT, buff=2.0)
        self.add(vertical_group_1, left_arrow, right_arrow)
        self.wait(2)
        self.play(Transform(vertical_group_1, vertical_group_2))
        self.wait(2)
        self.clear()


    
    def operations(self):
        title = Text("P-Set operations", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))
        t1 = Text("1. P-Union").set_color(WHITE)
        t2 = Text("2. P-Intersection").set_color(WHITE)
        t3 = Text("3. Subset").set_color(WHITE)
        x = VGroup(t1, t2, t3).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR)
        x.set_opacity(0.5)
        for obj in x.submobjects:    
            obj.set_opacity(1)
            self.add(x)
            self.wait()
            obj.set_opacity(0.5)
        self.clear()

    def construct(self):
        # self.intro()
        # self.next_section("Operations")
        # self.operations()
        # self.next_section("formula")
        self.p_function()
        
