import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

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

    print("Sending prompt to Gemini, please wait...")

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

if __name__ == "__main__":
    print("\n" + "="*50)
    print("Welcome to the AI Animation Generator!")
    print("Type your idea, or type 'quit' to exit.")
    print("="*50)
    while True:
        user_request = input("\nEnter your animation idea: ")
        if user_request.lower() in ["quit","exit"]:
            print("Shutting down. Goodbye!")
            break
        if(user_request.strip() == ""):
            continue
        result = ask_ai_for_manim_code(user_request)
        cleaned_code = extract_python_code(result)
        while True:
            filename = input("\nEnter filename (without .py): ").strip()
            if filename != "":
                break
            print("Filename cannot be empty.")
        output_filename = f"{filename}.py"
        with open(output_filename,"w") as f:
            f.write(cleaned_code)
        print(f"Success! Saved as -> {output_filename}")