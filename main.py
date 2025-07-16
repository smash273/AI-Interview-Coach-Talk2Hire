from fastapi import FastAPI
from pydantic import BaseModel
from feedbackllm import run_feedback_pipeline  
import uvicorn

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
if__name__=="main":
    uvicorn.run(app,host="0.0.0.0",port=8000)
