from manim import *

class PythagoreanTheoremProof(Scene):
    def construct(self):
        # Define side lengths for the right triangle
        a = 3
        b = 4
        c = np.sqrt(a**2 + b**2) # Hypotenuse, which will be 5

        # 1. Introduce the basic right triangle with labels
        # Create a right triangle with legs 'a' and 'b' and hypotenuse 'c'
        # Right angle at ORIGIN, leg 'a' along X-axis, leg 'b' along Y-axis
        triangle_points = [ORIGIN, RIGHT * a, UP * b]
        base_triangle = Polygon(*triangle_points, color=BLUE, fill_opacity=0.7)

        # Labels for sides
        line_a = Line(ORIGIN, RIGHT * a)
        line_b = Line(ORIGIN, UP * b)
        line_c = Line(RIGHT * a, UP * b)

        label_a = Text("a").next_to(line_a, DOWN, buff=SMALL_BUFF)
        label_b = Text("b").next_to(line_b, LEFT, buff=SMALL_BUFF)
        label_c = Text("c").next_to(line_c, RIGHT, buff=SMALL_BUFF)
        labels = VGroup(label_a, label_b, label_c)

        self.play(Create(base_triangle))
        self.play(Write(labels))
        self.wait(1)
        self.play(FadeOut(labels))

        # 2. First configuration: (a+b) square with c^2 in center and 4 triangles
        # Create the outer square frame with side length (a+b)
        s = a + b
        outer_square = Square(side_length=s).move_to(ORIGIN)
        outer_square.set_stroke(WHITE, width=2)

        # Transform the single triangle into the outer square frame
        # (Visually, we fade out the triangle and create the square)
        self.play(
            FadeOut(base_triangle),
            Create(outer_square)
        )

        # Define the four triangles that surround the central c^2 square
        # Each triangle has right angle at a corner of the outer_square.
        t1 = Polygon(outer_square.get_corner(DL) + RIGHT * b, outer_square.get_corner(DL), outer_square.get_corner(DL) + UP * a).set_color(BLUE).set_fill(BLUE, opacity=0.8)
        t2 = Polygon(outer_square.get_corner(DR) + UP * b, outer_square.get_corner(DR), outer_square.get_corner(DR) + LEFT * a).set_color(BLUE).set_fill(BLUE, opacity=0.8)
        t3 = Polygon(outer_square.get_corner(UR) + LEFT * b, outer_square.get_corner(UR), outer_square.get_corner(UR) + DOWN * a).set_color(BLUE).set_fill(BLUE, opacity=0.8)
        t4 = Polygon(outer_square.get_corner(UL) + DOWN * b, outer_square.get_corner(UL), outer_square.get_corner(UL) + RIGHT * a).set_color(BLUE).set_fill(BLUE, opacity=0.8)
        
        triangles_initial = VGroup(t1, t2, t3, t4)
        
        # Create the central square c^2
        square_c = Square(side_length=c).set_color(RED).set_fill(RED, opacity=0.8)

        self.play(
            FadeIn(triangles_initial),
            FadeIn(square_c)
        )

        area_c_text = Text("Area = c^2 + 4 * (1/2 * a * b)").to_edge(UP)
        self.play(Write(area_c_text))
        self.wait(2)
        self.play(FadeOut(area_c_text))

        # 3. Rearrangement: (a+b) square showing a^2 + b^2 + 2 * (a * b)
        # Animate the central c^2 square fading out
        self.play(FadeOut(square_c))

        # Define the target positions for the two squares a^2 and b^2
        square_a_target = Square(side_length=a).set_color(GREEN).set_fill(GREEN, opacity=0.8).align_to(outer_square, UL)
        square_b_target = Square(side_length=b).set_color(YELLOW).set_fill(YELLOW, opacity=0.8).align_to(outer_square, DR)

        # Define the target shapes for the four triangles to form two rectangles
        # These two rectangles represent the 2ab part of the (a+b)^2 expansion

        # Bottom-left rectangle (a x b) formed by t1 and t4
        bl_rect_corner = outer_square.get_corner(DL)
        t1_final = Polygon(bl_rect_corner, bl_rect_corner + RIGHT * a, bl_rect_corner + UP * b).set_color(BLUE).set_fill(BLUE, opacity=0.8)
        t4_final = Polygon(bl_rect_corner + RIGHT * a, bl_rect_corner + RIGHT * a + UP * b, bl_rect_corner + UP * b).set_color(BLUE).set_fill(BLUE, opacity=0.8)

        # Top-right rectangle (b x a) formed by t2 and t3
        tr_rect_corner = outer_square.get_corner(UL) + RIGHT * a
        t2_final = Polygon(tr_rect_corner, tr_rect_corner + RIGHT * b, tr_rect_corner + UP * a).set_color(BLUE).set_fill(BLUE, opacity=0.8)
        t3_final = Polygon(tr_rect_corner + RIGHT * b, tr_rect_corner + RIGHT * b + UP * a, tr_rect_corner + UP * a).set_color(BLUE).set_fill(BLUE, opacity=0.8)

        self.play(
            Transform(t1, t1_final),
            Transform(t4, t4_final),
            Transform(t2, t2_final),
            Transform(t3, t3_final),
            run_time=2
        )
        self.wait(1)

        # Fade in the a^2 and b^2 squares in the remaining space
        self.play(
            FadeIn(square_a_target),
            FadeIn(square_b_target)
        )

        area_ab_text = Text("Area = a^2 + b^2 + 2 * (a * b)").to_edge(UP)
        self.play(Write(area_ab_text))
        self.wait(2)

        # 4. Conclusion: Equating the areas
        conclusion_text = Text("Since the total area of the large square is the same, then:").to_edge(UP)
        self.play(Transform(area_ab_text, conclusion_text))
        self.wait(1)

        equation_initial = Text("c^2 + 2ab").shift(UP*0.8)
        equation_final = Text("= a^2 + b^2 + 2ab").next_to(equation_initial, RIGHT)

        self.play(Write(equation_initial))
        self.play(Write(equation_final))
        self.wait(1)

        # Visually "cancel out" the 2ab part from both sides
        cross_out_2ab_1 = Line(equation_initial[equation_initial.text.find("2ab"):].get_corner(UL) + 0.1 * UL, equation_initial[equation_initial.text.find("2ab"):].get_corner(DR) + 0.1 * DR, color=RED)
        cross_out_2ab_2 = Line(equation_final[equation_final.text.find("2ab"):].get_corner(UL) + 0.1 * UL, equation_final[equation_final.text.find("2ab"):].get_corner(DR) + 0.1 * DR, color=RED)
        
        self.play(Create(cross_out_2ab_1), Create(cross_out_2ab_2))
        self.wait(1)

        # Show the final Pythagorean theorem
        final_equation = Text("c^2 = a^2 + b^2").move_to(equation_initial)
        self.play(
            FadeOut(equation_initial, target_mode="line"), # Use target_mode to fade out parts covered by cross-out
            FadeOut(equation_final, target_mode="line"),
            FadeOut(cross_out_2ab_1),
            FadeOut(cross_out_2ab_2),
            Transform(conclusion_text, final_equation)
        )
        self.wait(3)