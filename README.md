# Manim AI Animation Generator

## Overview

This project generates Manim animations from natural language prompts using Google's Gemini API.

The workflow is:

1. Accept a text prompt.
2. Send the prompt to Gemini.
3. Generate valid Manim Python code.
4. Extract the generated code.
5. Save it as a Python file.
6. Render it using Manim.
7. Serve the generated video through a FastAPI backend.

The repository also contains the analysis reports completed as part of the earlier assignments.

---

## Project Structure

```text
.
├── prompts/
│   ├── pythagoras_prompt.txt
│   ├── fourier_prompt.txt
│   └── ...
│
├── media/
│   └── videos/
│
├── generate_scene.py
├── main.py
├── requirements.txt
├── .env.example
├── README.md
├── Week1_Task_Analysis.md
├── Week2_Task2.md
└── .gitignore
```

---

## Assignment Reports

- **Week1_Task_Analysis.md** – Critical evaluation of the AI-generated Pythagorean Theorem and Fourier Series animations.
- **Week2_Task2.md** – Project Feedback and Suggestions.

---

## Requirements

- Python 3.10+
- Manim Community Edition
- FFmpeg
- Google Gemini API key

---

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Quasar4606/manim-genai-assignment.git
cd manim-genai-assignment
```

### 2. Create a virtual environment

#### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

```text
GEMINI_API_KEY=YOUR_API_KEY_HERE
```

A sample `.env.example` file is included in the repository.

---

# Running the Generator (CLI)

Run

```bash
python3 generate_scene.py
```

The program will ask for:

- Prompt file path
- Output filename

Example

```text
Enter prompt file path:
prompts/circle.txt

Enter filename:
circle
```

The generator will:

1. Read the prompt file.
2. Generate Manim code using Gemini.
3. Save the generated Python file.
4. Render the animation using Manim.
5. Print the path of the generated video.

The generated video is saved under:

```text
media/videos/
```

---

# Running the FastAPI Backend

Start the backend using either of the following methods.

### Method 1 (Recommended)

```bash
python3 main.py
```

### Method 2

```bash
uvicorn main:app --reload
```

Once the server starts, open

```text
http://127.0.0.1:8000/docs
```

to access the interactive Swagger UI.

---

# API

## POST `/generate`

Generates and renders a Manim animation.

### Request

```json
{
    "prompt": "Draw a blue circle.",
    "filename": "circle"
}
```

The `filename` field specifies the name of the generated Python file and the corresponding Manim output directory.

### Response

```json
{
    "video_url": "/media/videos/circle/480p15/BlueCircle.mp4"
}
```

The returned URL can be opened directly in a browser while the server is running.

---

# Workflow

```text
Prompt
   │
   ▼
Gemini API
   │
   ▼
Generate Manim Code
   │
   ▼
Extract Python Code
   │
   ▼
Save Python File
   │
   ▼
Extract Scene Class
   │
   ▼
Render Animation (Manim)
   │
   ▼
Generate MP4
   │
   ▼
Serve Video through FastAPI
```

---

# Features

- Natural language to Manim animation generation
- Prompt engineering for reliable code generation
- Automatic extraction of Python code from LLM responses
- Automatic Scene class detection
- Automatic Manim rendering
- FastAPI backend
- Static file serving
- CORS enabled
- Interactive Swagger documentation
- Error handling for common failure cases

---

# Error Handling

The project handles:

- Missing Gemini API key
- Empty prompts
- Empty Gemini responses
- Missing Scene class
- Manim rendering failures
- Missing output video

Errors are returned through FastAPI using appropriate `HTTPException` responses.

---

# Technologies Used

- Python
- FastAPI
- Google Gemini API
- Manim Community Edition
- Pydantic
- python-dotenv
- Uvicorn

---

# Notes

- `uvicorn main:app --reload` should only be used during development.
- The `.env` file is intentionally excluded from version control.
- Generated videos are served through FastAPI using `StaticFiles`.
- Do not commit your API key; only commit `.env.example`.