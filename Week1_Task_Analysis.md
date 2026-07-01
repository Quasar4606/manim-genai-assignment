# Week 1 Task Analysis

## Overview

The objective of the first assignment was to evaluate the ability of Google's Gemini API to generate Manim animations for mathematical concepts. Rather than only checking whether the generated code executed successfully, the focus was on critically analyzing the resulting animations, identifying their shortcomings, and suggesting improvements.

Two mathematical visualizations were generated and evaluated:

1. Visual Proof of the Pythagorean Theorem
2. Fourier Series Decomposition

---

# Question 1 – Visual Proof of the Pythagorean Theorem

## Prompt Used

Located in:

```text
prompts/pythagoras_prompt.txt
```

## Running the Scene

```bash
manim -pql pythagoras.py PythagoreanTheorem
```

## Output

```text
videos/PythagoreanTheorem.mp4
```

---

## Critical Analysis

### 1. Inward-Facing Hypotenuse Square

#### Issue

The square constructed on the hypotenuse is drawn inward instead of outward, causing it to overlap the original right triangle.

#### Impact

This makes the initial construction visually confusing and obscures the triangle itself.

#### Suggested Improvement

Construct the square externally so that it clearly represents the square on the hypotenuse.

---

### 2. Detached Hypotenuse Label

#### Issue

The label **c** is positioned too far away from the hypotenuse and remains visible after the diagram disappears.

#### Impact

The relationship between the label and the corresponding side becomes unclear, and the ending appears unfinished.

#### Suggested Improvement

Place the label near the midpoint of the hypotenuse and fade it out together with the rest of the diagram.

---

### 3. Diagram and Equation Overlap

#### Issue

As the proof progresses, the equations begin overlapping the geometric construction.

#### Impact

The animation becomes cluttered and difficult to follow.

#### Suggested Improvement

Use a split-screen layout by placing the geometric construction on one side and the algebraic derivation on the other.

---

### 4. Numerical Instead of Symbolic Proof

#### Issue

The animation substitutes the values 3 and 4 into the proof even though the theorem is meant to hold for all right triangles.

#### Impact

This changes the proof into a numerical example rather than a general mathematical argument.

#### Suggested Improvement

Retain symbolic variables throughout the derivation.

---

### 5. Mathematical Formatting

#### Issue

All equations are displayed using plain text.

#### Impact

The notation looks less professional than properly typeset mathematics.

#### Suggested Improvement

Use mathematical typesetting where permitted by the assignment constraints.

---

# Question 2 – Fourier Series Decomposition

## Prompt Used

Located in:

```text
prompts/fourier_prompt.txt
```

## Running the Scene

```bash
manim -pql fourier_series.py FourierSeriesDecomposition
```

## Output

```text
videos/FourierSeriesDecomposition.mp4
```

---

## Critical Analysis

### 1. Missing Harmonic Visualization

#### Issue

The animation directly shows the cumulative approximation without displaying the individual harmonics.

#### Impact

The viewer cannot understand how the Fourier approximation is built from successive sine waves.

#### Suggested Improvement

Animate each harmonic independently before adding it to the cumulative approximation.

---

### 2. Incorrect Square Wave Geometry

#### Issue

The target square wave is drawn using slanted transitions instead of vertical discontinuities.

#### Impact

This misrepresents the mathematical definition of a square wave.

#### Suggested Improvement

Construct the waveform using explicit horizontal and vertical line segments.

---

### 3. Mathematical Formatting

#### Issue

The Fourier equations are rendered as plain text.

#### Impact

The notation resembles source code more than mathematical expressions.

#### Suggested Improvement

Use proper mathematical formatting where allowed.

---

### 4. Text Transition Artifacts

#### Issue

Some text transformations stretch and distort the characters during animation.

#### Impact

These artifacts reduce the overall visual quality.

#### Suggested Improvement

Replace direct text transformations with fade-based transitions.

---

### 5. Incorrect Ordinal Labels

#### Issue

Labels such as **1th Harmonic** and **3th Harmonic** are displayed.

#### Impact

These grammatical errors reduce the professionalism of the animation.

#### Suggested Improvement

Generate the correct ordinal suffixes (1st, 2nd, 3rd, etc.).

---

# Overall Findings

Gemini was able to generate complete Manim scenes with minimal human intervention and generally captured the intended mathematical concepts. However, several issues related to geometry, layout, mathematical notation, and animation quality were present.

The evaluation showed that while modern LLMs can significantly accelerate animation development, human review is still essential to ensure mathematical correctness, visual clarity, and educational effectiveness.