from books import search_books
from llm import interpret_mood, rank_and_explain

def get_recommendations(mood_text):
    mood_result = interpret_mood(mood_text)
    wyniki = search_books(mood_result.search_query, limit=20)
    return wyniki

if __name__ == "__main__":
    rekomendacje = get_recommendations("coś lekkiego przed snem, max 30 min czytania")
    rekomendacje = rank_and_explain(rekomendacje, "coś lekkiego przed snem, max 30 min czytania")
    for r in rekomendacje:
        print(r.title, "-", r.reasoning)