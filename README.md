# Manim AI Animation Generation and Critical Evaluation

## Overview

This project explores the use of Google's Gemini API to automatically generate Manim animations for mathematical concepts. The objective is to evaluate the quality of AI-generated animation code, identify its strengths and weaknesses, and critically assess the resulting visualizations.

The assignment consists of two tasks:

1. Visual Proof of the Pythagorean Theorem
2. Fourier Series Decomposition Visualization

---

## Repository Structure

```text
.
├── prompts/
│   ├── pythagoras_prompt.txt
│   └── fourier_prompt.txt
│
├── videos/
│   ├── PythagoreanTheorem.mp4
│   └── FourierSeriesDecomposition.mp4
│
├── generate_scene.py
├── pythagoras.py
├── fourier_series.py
├── README.md
├── .gitignore
└── .env
```

---

## Setup Instructions

### macOS / Linux

Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

### Windows

Create a virtual environment:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file:

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

---

## Running the Generator

Generate Manim code from a prompt file:

```bash
python3 generate_scene.py
```

The program will:

1. Read a prompt file.
2. Send the prompt to Gemini.
3. Generate Manim code.
4. Save the generated code to a Python file.

---

# Question 1 – Visual Proof of the Pythagorean Theorem

## Prompt Used

Located in:

```text
prompts/pythagoras_prompt.txt
```

## Running the Scene

### macOS / Linux

```bash
manim -pql pythagoras.py PythagoreanTheorem
```

### Windows

```powershell
manim -pql pythagoras.py PythagoreanTheorem
```

## Output

Output video:

```text
videos/PythagoreanTheorem.mp4
```

---

## Critical Analysis: Pythagorean Theorem Animation

### 1. Inward-Facing Hypotenuse Square (Geometric Overlap)

**Issue**

At the 0:08 mark, the square representing the area of the hypotenuse (c²) is drawn facing the wrong direction. Instead of building outward, it projects inward, heavily overlapping the original right-angled triangle.

**Impact**

This obscures the base shape and creates a confusing visual right at the start of the proof.

**Corrective Action**

The green hypotenuse square should be constructed outward and away from the triangle.

---

### 2. Floating and Detached Hypotenuse Label

**Issue**

The label "c" appears far away from the hypotenuse and remains visible at the end of the animation after the diagram disappears.

**Impact**

This weakens the visual connection between the label and the side it represents and makes the ending appear unfinished.

**Corrective Action**

Anchor the label near the midpoint of the hypotenuse and fade it out with the rest of the diagram.

---

### 3. Severe Text-on-Diagram Overlap

**Issue**

The algebraic derivation eventually overlaps the geometric proof diagram.

**Impact**

The animation becomes cluttered and difficult to follow.

**Corrective Action**

Use a split-screen layout with geometry on one side and equations on the other.

---

### 4. Loss of Mathematical Abstraction

**Issue**

The proof substitutes specific values (3 and 4) despite claiming the result applies to all right triangles.

**Impact**

The proof becomes a numerical demonstration rather than a general proof.

**Corrective Action**

Maintain symbolic variables throughout the derivation.

---

### 5. Poor Typographic Formatting for Mathematics

**Issue**

All equations are displayed using plain text.

**Impact**

The mathematical notation appears less polished than professionally typeset mathematics.

**Corrective Action**

Use mathematical typesetting where assignment requirements permit.

---

# Question 2 – Fourier Series Decomposition

## Prompt Used

Located in:

```text
prompts/fourier_prompt.txt
```

## Running the Scene

### macOS / Linux

```bash
manim -pql fourier_series.py FourierSeriesDecomposition
```

### Windows

```powershell
manim -pql fourier_series.py FourierSeriesDecomposition
```

## Output

Output video:

```text
videos/FourierSeriesDecomposition.mp4
```

---

## Critical Analysis: Fourier Series Decomposition

### 1. Missing Individual Harmonics (Instruction Failure)

**Issue**

The animation only displays the target square wave and the cumulative Fourier approximation. Individual harmonics are never shown independently.

**Impact**

The viewer cannot observe the individual building blocks that create the approximation, reducing educational value.

**Corrective Action**

Display each harmonic separately in a unique colour before adding it to the cumulative approximation.

---

### 2. Slanted Target Square Wave (Geometric Inaccuracy)

**Issue**

The target square wave is rendered with slanted transitions instead of perfectly vertical discontinuities.

**Impact**

This incorrectly suggests continuity and misrepresents the true mathematical structure of a square wave.

**Corrective Action**

Construct the square wave using explicit horizontal and vertical line segments.

---

### 3. Poor Typographic Formatting of Equations

**Issue**

The displayed Fourier expressions are rendered as plain text strings.

**Impact**

The equations appear closer to source code than formal mathematical notation.

**Corrective Action**

Use proper mathematical typesetting when allowed.

---

### 4. Garbled Text Transitions (Visual Glitching)

**Issue**

Several text transformations cause letters to stretch and overlap during transitions.

**Impact**

The animation appears visually unpolished and distracts from the mathematical content.

**Corrective Action**

Replace direct text transformations with fade transitions.

---

### 5. Incorrect Ordinal Suffixes (Grammar Error)

**Issue**

Labels such as "1th Harmonic" and "3th Harmonic" are displayed.

**Impact**

These grammatical errors reduce the professional quality of the animation.

**Corrective Action**

Implement proper ordinal suffix logic (1st, 2nd, 3rd, etc.).

---

## Overall Findings

This project demonstrated both the strengths and limitations of AI-generated code.

Gemini was able to generate complete Manim scenes with minimal human intervention and successfully capture the underlying mathematical concepts. However, the generated animations contained several implementation, layout, formatting, and presentation issues that required critical review.

The experiments showed that prompt engineering significantly influences output quality, but human verification remains necessary to ensure correctness, readability, and educational effectiveness.
