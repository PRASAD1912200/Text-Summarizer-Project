from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Text Summarizer API")

@app.get("/")
def root():
    return {"message": "Text Summarizer API is running"}

@app.post("/summarize")
def summarize(text: str):
    # TODO: Implement text summarization logic
    return {"summary": "Summarization not implemented yet", "original_length": len(text)}