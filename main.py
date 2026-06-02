from fastapi import FastAPI
from fastapi.responses import FileResponse
import uvicorn

app = FastAPI()

# This route serves your HTML portfolio when someone visits the main URL
@app.get("/", response_class=FileResponse)
async def read_index():
    return "index.html"

if __name__ == "__main__":
    # Run this file with: python main.py
    uvicorn.run(app, host="0.0.0.0", port=8000)