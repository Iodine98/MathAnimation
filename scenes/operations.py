from run import run_file
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
        operation_texts = [
            "1. P-Union",
            "2. P-Intersection",
            "3. Scaling"
        ]
        operation_texts = [Text(text).set_color(WHITE) for text in operation_texts]
        return VGroup(*operation_texts) \
            .arrange(direction=DOWN, aligned_edge=LEFT) \
            .scale(0.7) \
            .next_to(ORIGIN,DR)\
            .set_opacity(0.5)
    def animate_over_list(self, list_of_operations):
        for obj in list_of_operations.submobjects:
            obj.set_opacity(1)
            self.add(list_of_operations)
            self.wait()
            obj.set_opacity(0.5)

    def construct(self):
        self.set_title()
        ops = self.create_list_of_operations()
        self.animate_over_list(list_of_operations=ops)
        ops[-1].set_opacity(1)
        self.wait(3)

if __name__ == '__main__':
    run_file("operations.py")
