from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Define side lengths for a 3-4-5 right triangle
        a_len = 3
        b_len = 4
        c_len = np.sqrt(a_len**2 + b_len**2) # Should be 5

        # Colors for visual distinction
        COLOR_A = BLUE
        COLOR_B = RED
        COLOR_C = GREEN
        COLOR_TRIANGLE_FILL = WHITE
        COLOR_PROOF_TRIANGLE = ORANGE
        COLOR_LARGE_SQUARE = YELLOW
        COLOR_TEXT = YELLOW_A

        # --- Part 1: Introduction of the right triangle and squares ---

        # 1. Create the right triangle (right angle at origin)
        p_right_angle = ORIGIN + LEFT * 4.5 + DOWN * 1.5 # Shift for better placement
        p_a = p_right_angle + UP * a_len
        p_b = p_right_angle + RIGHT * b_len

        triangle = Polygon(p_right_angle, p_a, p_b, color=COLOR_TRIANGLE_FILL, fill_opacity=0.6, stroke_width=2)

        side_a_line = Line(p_right_angle, p_a).set_color(COLOR_A)
        side_b_line = Line(p_right_angle, p_b).set_color(COLOR_B)
        side_c_line = Line(p_a, p_b).set_color(COLOR_C)

        # Labels for sides a, b, c
        label_a = Text("a").scale(0.6).next_to(side_a_line, LEFT, buff=0.1).set_color(COLOR_A)
        label_b = Text("b").scale(0.6).next_to(side_b_line, DOWN, buff=0.1).set_color(COLOR_B)
        label_c = Text("c").scale(0.6).next_to(side_c_line, UP + RIGHT, buff=0.1).set_color(COLOR_C)

        # Title
        title = Text("Pythagorean Theorem").scale(1).to_edge(UP).set_color(COLOR_TEXT)
        intro_text = Text("A Visual Proof").scale(0.7).next_to(title, DOWN).set_color(WHITE)

        self.play(Write(title), Write(intro_text))
        self.wait(1)
        self.play(Create(triangle), Create(side_a_line), Create(side_b_line), Create(side_c_line))
        self.play(Write(label_a), Write(label_b), Write(label_c))
        self.wait(1)

        # 2. Create squares on each side
        # Square on side a
        sq_a_points = [p_right_angle, p_a, p_a + LEFT * a_len, p_right_angle + LEFT * a_len]
        square_a = Polygon(*sq_a_points, color=COLOR_A, fill_opacity=0.5, stroke_width=2)
        label_sq_a = Text("a²").scale(0.6).move_to(square_a).set_color(COLOR_A)

        # Square on side b
        sq_b_points = [p_right_angle, p_b, p_b + DOWN * b_len, p_right_angle + DOWN * b_len]
        square_b = Polygon(*sq_b_points, color=COLOR_B, fill_opacity=0.5, stroke_width=2)
        label_sq_b = Text("b²").scale(0.6).move_to(square_b).set_color(COLOR_B)

        # Square on side c (hypotenuse)
        # Vector along hypotenuse
        hyp_vector = p_b - p_a
        # Perpendicular vector for the square side
        perp_hyp_vector = rotate_vector(hyp_vector, -PI / 2) # Rotate "outwards" from triangle
        sq_c_points = [p_a, p_b, p_b + perp_hyp_vector, p_a + perp_hyp_vector]
        square_c = Polygon(*sq_c_points, color=COLOR_C, fill_opacity=0.5, stroke_width=2)
        label_sq_c = Text("c²").scale(0.6).move_to(square_c).set_color(COLOR_C)

        self.play(Create(square_a), Create(square_b), Create(square_c))
        self.play(Write(label_sq_a), Write(label_sq_b), Write(label_sq_c))
        self.wait(2)

        # Group all initial objects for later recall
        initial_scene_group = VGroup(
            triangle, side_a_line, side_b_line, side_c_line,
            label_a, label_b, label_c,
            square_a, square_b, square_c,
            label_sq_a, label_sq_b, label_sq_c
        )

        # --- Part 2: Geometric Proof using a larger square (Euclid's proof variant) ---

        self.play(FadeOut(initial_scene_group, shift=DOWN*2), FadeOut(title), FadeOut(intro_text))
        self.wait(0.5)

        proof_intro_text = Text("Consider a large square with side length (a + b)").scale(0.7).to_edge(UP).set_color(COLOR_TEXT)
        self.play(Write(proof_intro_text))
        self.wait(1)

        # Define total side length for the large square
        S_len = a_len + b_len # 3 + 4 = 7

        # Create the large square, centered
        large_square = Square(side_length=S_len, color=COLOR_LARGE_SQUARE, fill_opacity=0.1, stroke_width=2)
        self.play(Create(large_square))
        self.wait(1)

        # Label the side length of the large square
        label_large_side = Text(f"Side = {a_len}+{b_len} = {S_len}").scale(0.6).next_to(large_square, DOWN, buff=0.5)
        self.play(Write(label_large_side))
        self.wait(1)

        # Vertices of the large square
        P1 = large_square.get_corner(DOWN + LEFT)
        P2 = large_square.get_corner(DOWN + RIGHT)
        P3 = large_square.get_corner(UP + RIGHT)
        P4 = large_square.get_corner(UP + LEFT)

        # Create 4 copies of the right triangle and place them in the corners of the large square
        # Triangle 1 (bottom-left corner)
        t1 = Polygon(P1, P1 + RIGHT * b_len, P1 + UP * a_len, color=COLOR_PROOF_TRIANGLE, fill_opacity=0.8, stroke_width=2)
        # Triangle 2 (bottom-right corner)
        t2 = Polygon(P2, P2 + LEFT * a_len, P2 + UP * b_len, color=COLOR_PROOF_TRIANGLE, fill_opacity=0.8, stroke_width=2)
        # Triangle 3 (top-right corner)
        t3 = Polygon(P3, P3 + DOWN * a_len, P3 + LEFT * b_len, color=COLOR_PROOF_TRIANGLE, fill_opacity=0.8, stroke_width=2)
        # Triangle 4 (top-left corner)
        t4 = Polygon(P4, P4 + RIGHT * a_len, P4 + DOWN * b_len, color=COLOR_PROOF_TRIANGLE, fill_opacity=0.8, stroke_width=2)

        self.play(Create(t1), Create(t2), Create(t3), Create(t4))
        self.wait(2)

        # The inner space forms a square with side 'c'
        sq_c_inner_coords = [
            t1.get_vertices()[1], # Vertex (b,0) of tri1
            t2.get_vertices()[2], # Vertex (0,b) of tri2 after rotation
            t3.get_vertices()[1], # Vertex (b,0) of tri3 after rotation
            t4.get_vertices()[2], # Vertex (0,b) of tri4 after rotation
        ]
        square_c_inner = Polygon(*sq_c_inner_coords, color=COLOR_C, fill_opacity=0.7, stroke_width=2)
        label_c_inner = Text("Area = c²").scale(0.6).move_to(square_c_inner).set_color(COLOR_C)

        self.play(Create(square_c_inner), Write(label_c_inner))
        self.wait(2)

        # Explanatory text for areas
        equation1 = Text(f"Area of large square = ({a_len} + {b_len})²").scale(0.6).next_to(proof_intro_text, DOWN, buff=0.5).set_color(WHITE)
        self.play(Write(equation1))
        self.wait(2)

        equation2 = Text(f"Area of large square = 4 × (Area of one triangle) + Area of inner square").scale(0.6).next_to(equation1, DOWN).set_color(WHITE)
        self.play(Write(equation2))
        self.wait(2)

        area_triangle = 0.5 * a_len * b_len
        equation3 = Text(f"({a_len} + {b_len})² = 4 × (1/2 × {a_len} × {b_len}) + c²").scale(0.6).next_to(equation2, DOWN).set_color(WHITE)
        self.play(Write(equation3))
        self.wait(2)

        equation4 = Text(f"({a_len} + {b_len})² = 2 × {a_len} × {b_len} + c²").scale(0.6).next_to(equation3, DOWN).set_color(WHITE)
        self.play(Write(equation4))
        self.wait(2)

        equation5 = Text(f"{a_len}² + 2×{a_len}×{b_len} + {b_len}² = 2×{a_len}×{b_len} + c²").scale(0.6).next_to(equation4, DOWN).set_color(WHITE)
        self.play(Write(equation5))
        self.wait(2)

        equation6 = Text(f"{a_len}² + {b_len}² = c²").scale(0.8).next_to(equation5, DOWN, buff=0.5).set_color(COLOR_TEXT)
        self.play(Write(equation6))
        self.wait(3)

        # --- Part 3: Conclusion ---
        self.play(
            FadeOut(VGroup(
                large_square, label_large_side, t1, t2, t3, t4, square_c_inner, label_c_inner,
                proof_intro_text, equation1, equation2, equation3, equation4, equation5, equation6
            ))
        )
        self.wait(0.5)

        final_theorem_text = Text("Thus, for any right triangle:").scale(0.8).to_edge(UP).set_color(WHITE)
        final_theorem_equation = Text("a² + b² = c²").scale(1.2).set_color(COLOR_TEXT)
        qed_text = Text("Q.E.D.").scale(0.7).next_to(final_theorem_equation, DOWN).set_color(WHITE)

        self.play(FadeIn(final_theorem_text))
        self.play(Write(final_theorem_equation))
        self.play(FadeIn(initial_scene_group)) # Bring back the original setup
        self.play(initial_scene_group.animate.shift(DOWN*0.5 + LEFT*0.5).scale(0.7)) # Adjust position to fit
        self.play(Write(qed_text))

        self.wait(3)