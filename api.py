from fastapi import FastAPI
from main import get_recommendations
from llm import rank_and_explain
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

class MoodRequest(BaseModel):
    mood: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Book Matcher API is running"}

@app.post("/recommend")
def recommend(request: MoodRequest):
    candidates = get_recommendations(request.mood)
    recommendations = rank_and_explain(candidates, request.mood)
    return recommendations