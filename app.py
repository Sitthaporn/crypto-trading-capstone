from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="Capstone FastAPI App")

# Serve static files (optional but good practice)
app.mount("/static", StaticFiles(directory="."), name="static")


@app.get("/", response_class=HTMLResponse)
async def root():
    """
    Serve index.html
    """
    file_path = "index.html"
    if not os.path.exists(file_path):
        return HTMLResponse(
            content="<h1>index.html not found</h1>",
            status_code=404
        )

    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/health")
async def health_check():
    return {"status": "ok"}
