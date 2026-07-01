import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if api_key is None:
    raise RuntimeError("GEMINI_API_KEY not found in .env")

client = genai.Client(api_key = api_key)

def ask_ai_for_manim_code(user_prompt):
    system_instruction = (
       "You are an expert in Python and the Manim animation library. "
        "When given a request, generate ONLY valid Python code using Manim. "
        "CRITICAL FONT RULES: You must NEVER use Tex() or MathTex(). "
        "You must ONLY use the standard Text() class for all text. "
        "Do not include any explanations or additional text. "
        "Just output the raw code block."
    )
    
    full_prompt = f"{system_instruction}\n\nUser Request: {user_prompt}"

    print("\nSending prompt to Gemini, please wait...")

    response = client.models.generate_content(
        model = 'gemini-2.5-flash',
        contents= full_prompt,
    )

    return response.text

def extract_python_code(raw_text):
    backticks = chr(96) * 3
    pattern = rf"{backticks}(?:python)?\n(.*?)\n{backticks}"
    match = re.search(pattern, raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()

def generate_animation_video(prompt : str,filename : str = "generated_scene") -> str:
    if prompt.strip() == "":
        raise ValueError("Prompt cannot be empty.")
    try:
        raw_response = ask_ai_for_manim_code(prompt)
        cleaned_code = extract_python_code(raw_response)
        output_filename = f"{filename}.py"
        with open(output_filename, "w") as f:
            f.write(cleaned_code)
        print(f"Generated code saved to {output_filename}")
        return output_filename
    except Exception as e:
        raise RuntimeError(f"Animation generation failed: {e}")

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Welcome to the AI Animation Generator!")
    print("Enter a prompt file path, or type 'quit' to exit.")
    print("="*50)
    while True:
        prompt_file = input("\nEnter prompt file path: ").strip()
        if prompt_file.lower() in ["quit", "exit"]:
            print("Shutting down. Goodbye!")
            break
        try:
            with open(prompt_file, "r") as f:
                user_request = f.read()
        except FileNotFoundError:
            print("Prompt file not found.")
            continue
        if(user_request.strip() == ""):
            continue
        while True:
            filename = input("\nEnter filename (without .py): ").strip()
            if filename != "":
                break
            print("Filename cannot be empty.")
        try:
            generated_file = generate_animation_video(user_request,filename)
            print(f"Success! Saved as -> {generated_file}")
        except Exception as e:
            print(e)