from manim import *
import numpy as np

class FourierSeriesDecomposition(Scene):
    def construct(self):
        # --- Configuration ---
        AXES_CONFIG = {
            "x_range": [-PI, PI, PI / 2],
            "y_range": [-1.5, 1.5, 0.5],
            "x_length": 10,
            "y_length": 6,
            "axis_config": {"font_size": 24},
            "tips": False
        }

        # --- Axes and Plotting Area ---
        axes = Axes(**AXES_CONFIG)
        labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        self.play(Create(axes), Write(labels), run_time=1.5)
        self.wait(0.5)

        # --- Target Square Wave ---
        # Define the square wave function for plotting
        # np.sign handles the discontinuities well for our purpose
        def square_wave_func(x):
            return np.sign(x)

        square_wave_graph = axes.plot(square_wave_func, color=YELLOW_A, stroke_width=4)
        
        intro_text = Text(
            "Target: A Square Wave",
            font_size=38
        ).to_edge(UP).shift(LEFT * 1.5)

        self.play(Create(square_wave_graph), Write(intro_text), run_time=2)
        self.wait(2)

        # --- Introduce Fourier Concept ---
        fourier_concept_text = Text(
            "Complex periodic functions can be approximated\nby sums of sine waves (harmonics).",
            font_size=36
        ).to_edge(UP).shift(LEFT * 1.5)

        self.play(ReplacementTransform(intro_text, fourier_concept_text))
        self.wait(3)

        self.play(FadeOut(fourier_concept_text, shift=UP))

        # --- Fourier Series Logic ---
        # Fourier series for square wave f(x) = -1 for x in (-PI, 0) and f(x) = 1 for x in (0, PI)
        # is (4/PI) * sum_{n=1,3,5,...} (1/n) * sin(nx)

        # Initialize current approximation function and graph
        current_sum_function = lambda x: 0
        fourier_approx_graph = axes.plot(current_sum_function, color=BLUE_B, stroke_width=3)
        self.play(Create(fourier_approx_graph))

        # Initialize text for current harmonic and mathematical expression
        harmonic_label = Text("Starting Fourier Approximation...", font_size=32).to_edge(UP).shift(LEFT * 1.5)
        self.play(Write(harmonic_label))

        math_expression = Text("f(x) = 0", font_size=28).to_edge(DOWN).set_x(0)
        self.play(Write(math_expression))
        self.wait(1)

        # List to store individual terms for the sum string
        fourier_term_strings = []
        
        # Loop to add odd harmonics
        # We will go up to the 15th harmonic to show good convergence
        odd_harmonics = [1, 3, 5, 7, 9, 11, 13, 15] 
        
        # This will hold the coefficients and functions for current sum
        current_terms = [] 

        for i, n in enumerate(odd_harmonics):
            # Update harmonic label
            new_harmonic_label = Text(f"Adding the {n}th Harmonic (n={n}):", font_size=32).to_edge(UP).shift(LEFT * 1.5)
            self.play(Transform(harmonic_label, new_harmonic_label))

            # Add current term to our list for calculation
            current_terms.append((1 / n, n)) # (coefficient, harmonic_number)

            # Update the approximation function
            def update_sum_function(x, terms):
                s = 0
                for coeff, h_num in terms:
                    s += coeff * np.sin(h_num * x)
                return (4 / np.pi) * s
            
            # Create a new function that encapsulates the current terms
            new_sum_function = lambda x: update_sum_function(x, current_terms)

            # Create the new graph
            new_fourier_approx_graph = axes.plot(new_sum_function, color=BLUE_B, stroke_width=3)

            # Update the mathematical expression string
            fourier_term_strings.append(f"(1/{n})sin({n}x)")
            
            # Limit the number of displayed terms for readability
            displayed_terms = fourier_term_strings[:]
            if len(displayed_terms) > 4: # If more than 4 terms, show first 3 and ellipsis
                displayed_terms = displayed_terms[:3] + ["..."]

            full_expression_str = "f(x) = (4/pi) * (" + " + ".join(displayed_terms) + ")"
            
            new_math_expression = Text(
                full_expression_str, 
                font_size=28
            ).to_edge(DOWN).set_x(0)
            
            # Animate the update
            self.play(
                Transform(fourier_approx_graph, new_fourier_approx_graph),
                Transform(math_expression, new_math_expression),
                run_time=1.5
            )
            self.wait(1.5)
        
        # --- Final cleanup and message ---
        final_message = Text(
            "The approximation converges to the square wave\nas more harmonics are added.",
            font_size=36
        ).to_edge(UP).shift(LEFT * 1.5)

        self.play(Transform(harmonic_label, final_message))
        self.wait(3)

        self.play(
            FadeOut(harmonic_label),
            FadeOut(math_expression),
            FadeOut(fourier_approx_graph),
            FadeOut(square_wave_graph),
            FadeOut(axes),
            FadeOut(labels)
        )
        self.wait(1)