import os
from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


class MoodInterpretation(BaseModel):
    search_query: str
    themes: list[str]
    pace: str
    max_pages: int

class BookRecommendation(BaseModel):
    title: str
    reasoning: str
    author: str

class RecommendationList(BaseModel):
    recommendations: list[BookRecommendation]

def rank_and_explain(candidates, mood_text):
    candidate_lines = []
    for c in candidates:
        desc = c['description']
        if desc is None:
            desc = "No description available"
        line = f"- {c['title']} by {c['author']}: {desc[:200]}" 
        candidate_lines.append(line)
    
    candidates_text = "\n".join(candidate_lines)
    
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=(
            f"A reader's mood: '{mood_text}'. "
            f"Here are candidate books:\n{candidates_text}\n\n"
            "Pick the 3-5 best matches for this mood. For each, give a short "
            "(1-2 sentence) reasoning explaining why it fits this specific mood."
        ),
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": RecommendationList.model_json_schema()
        },
        timeout=60
    )
    result = RecommendationList.model_validate_json(interaction.output_text)
    return result.recommendations

def interpret_mood(mood_text):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=(
            f"A reader describes their current mood as: '{mood_text}'. "
            "Suggest a concrete, searchable book genre or a comparable well-known "
            "book title for the search_query field (examples: 'cozy mystery', "
            "'contemporary fiction', 'light fantasy'). Avoid abstract mood words "
            "like 'relaxing' or 'cozy' as the search_query itself — those belong "
            "in the themes field instead."
        ),
        response_format={
            "type": "text",
            "mime_type": "application/json",
            "schema": MoodInterpretation.model_json_schema()
        },
            timeout=60
    )

    result = MoodInterpretation.model_validate_json(interaction.output_text)
    return result

