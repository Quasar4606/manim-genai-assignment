const promptInput = document.getElementById("prompt-input");
const filenameInput = document.getElementById("filename-input");
const generateButton = document.getElementById("generate-btn");
const statusText = document.getElementById("status-text");
const videoPlayer = document.getElementById("video-player");

async function generateAnimation() {
    try{
        const prompt = promptInput.value.trim();
        const filename = filenameInput.value.trim() || "generated_scene";
        if (prompt === "") {
            statusText.textContent = "Please enter a prompt.";
            videoPlayer.style.display = "none";
            return;
        }
        statusText.textContent = "Generating animation...";
        generateButton.disabled = true;
        videoPlayer.style.display = "none";
        const response = await fetch(
            "http://127.0.0.1:8000/generate",
            {
                method: "POST",
                headers: {
                    "Content-Type" : "application/json",
                },
                body: JSON.stringify({
                    prompt: prompt,
                    filename: filename,
                }),
            }
        );
        if(!response.ok){
            const error = await response.json();
            statusText.textContent = error.detail;
            return;
        }
        const data = await response.json();
        statusText.textContent = "Animation generated successfully!";
        videoPlayer.src = "http://127.0.0.1:8000" + data.video_url;
        videoPlayer.style.display = "block";
        videoPlayer.load();
        videoPlayer.scrollIntoView({
            behavior: "smooth"
        });
    }
    catch(error){
        statusText.textContent = "Failed to connect to server.";
        console.error(error);
    }
    finally{
        generateButton.disabled = false;
    }
}

generateButton.addEventListener("click", generateAnimation);