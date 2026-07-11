# Frontend

This folder contains the frontend for the Manim AI Animation Generator. It provides a simple web interface where users can enter a prompt, generate a Manim animation, and watch the rendered video directly in the browser.

## Prerequisites

Before running the frontend, make sure the FastAPI backend from the project root is running.

Start the backend using either of the following:

```bash
uvicorn main:app --reload
```

or

```bash
python3 main.py
```

The backend will run at:

```
http://127.0.0.1:8000
```

## Running the Frontend

Navigate to the `frontend` directory:

```bash
cd frontend
```

Start a simple HTTP server:

```bash
python3 -m http.server 5500
```

Then open the following URL in your browser:

```
http://localhost:5500
```

## Using the Application

1. Enter an animation prompt.
2. (Optional) Enter an output filename. If left blank, `generated_scene` will be used.
3. Click **Generate!**
4. Wait for the animation to be generated.
5. Once rendering is complete, the generated video will appear on the page and can be played directly in the browser.

## Error Handling

The frontend displays appropriate messages for common errors, including:

- Empty prompt input
- Backend rendering errors
- Server connection failures

During generation, the **Generate!** button is temporarily disabled to prevent multiple simultaneous requests.