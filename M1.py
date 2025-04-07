from manim import *

class HighlightLines(Scene):
    def construct(self):
        # Define points
        C = LEFT + UP
        B = RIGHT + UP
        A = ORIGIN
        Q = 0.5 * LEFT + 0.5 * UP
        P = 0.5 * RIGHT + 0.5 * UP

        # Create triangles
        triangle1 = Polygon(A, B, C, color=BLUE, fill_opacity=0.1)
        triangle2 = Polygon(Q, P, A, color=GREEN, fill_opacity=0.1)

        # "Blur" effect: make the triangles very transparent and gray
        triangle1.set_fill(GRAY, opacity=0.05).set_stroke(GRAY, opacity=0.2)
        triangle2.set_fill(GRAY, opacity=0.05).set_stroke(GRAY, opacity=0.2)

        # Highlight lines PQ and BC
        line_PQ = Line(P, Q, color=YELLOW, stroke_width=4)
        line_BC = Line(B, C, color=RED, stroke_width=4)

        # Labels (optional)
        label_C = Text("C", font_size=10).move_to(C + UP * 0.2).rotate(PI)
        label_B = Text("B", font_size=10).move_to(B + UP * 0.2).rotate(PI)
        label_A = Text("A", font_size=10).move_to(A + DOWN * 0.3).rotate(PI)
        label_Q = Text("Q", font_size=10).move_to(Q + LEFT * 0.2).rotate(PI)
        label_P = Text("P", font_size=10).move_to(P + RIGHT * 0.2).rotate(PI)

        # Group and rotate all
        all_shapes = VGroup(triangle1, triangle2, line_PQ, line_BC, label_A, label_B, label_C, label_P, label_Q)
        all_shapes.rotate(PI)

        # Animate
        self.play(Create(triangle1), Create(triangle2))
        self.play(Create(line_PQ), Create(line_BC))
        self.play(Write(label_A), Write(label_B), Write(label_C), Write(label_P), Write(label_Q))
        self.wait(10)