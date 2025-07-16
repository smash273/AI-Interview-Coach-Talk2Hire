from fastapi import FastAPI
from pydantic import BaseModel
from feedbackllm import run_feedback_pipeline  # assuming feedbackllm.py is in same folder

app = FastAPI()

class FeedbackRequest(BaseModel):
    question: str
    answer: str
    tone: str
    emotion: str

@app.post("/generate-feedback")
def generate(data: FeedbackRequest):
    run_feedback_pipeline(data.question, data.answer, data.tone, data.emotion)
    return {"status": "Feedback generated"}
