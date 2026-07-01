import os
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from generate_scene import generate_animation_video

os.makedirs("media",exist_ok = True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount(
    "/media",
    StaticFiles(directory="media"),
    name="media",
)

class GenerateRequest(BaseModel):
    prompt: str
    filename: str = "generated_scene"

@app.post("/generate")
def generate(request: GenerateRequest):
    try:
        video_path = generate_animation_video(
            request.prompt,
            request.filename,
        )
        return {
            "video_url" : "/" + video_path.replace("\\","/")
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e),
        )
    
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,
    )