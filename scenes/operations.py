from manim import Text, WHITE, UP, DOWN, LEFT, ORIGIN, DR, VGroup, Scene

class Operations(Scene):
    """
    Display the P-Set operations
    """

    def set_title(self):
        title = Text("P-Set operations", color=WHITE)
        title.scale(0.75)
        self.add(title.to_edge(UP))  

    def create_list_of_operations(self):
        text_one = Text("1. P-Union").set_color(WHITE)
        text_two = Text("2. P-Intersection").set_color(WHITE)
        text_three = Text("3. Subset").set_color(WHITE)
        return VGroup(text_one, text_two, text_three).arrange(direction=DOWN, aligned_edge=LEFT).scale(0.7).next_to(ORIGIN,DR).set_opacity(0.5)

    def animate_over_list(self, list_of_operations):
        for obj in list_of_operations.submobjects:    
            obj.set_opacity(1)
            self.add(list_of_operations)
            self.wait()
            obj.set_opacity(0.5)  

    def construct(self):
        self.set_title()
        self.animate_over_list(list_of_operations=self.create_list_of_operations())
        self.clear()

