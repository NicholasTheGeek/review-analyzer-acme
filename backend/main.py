from fastapi import FastAPI, Form
import requests
import re

app = FastAPI()

def query_ollama(prompt: str):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False}
        )
        response.raise_for_status()
        return response.json()["response"].strip()
    except requests.exceptions.RequestException as e:
        return f"Error querying Ollama: {e}"
    except KeyError:
        return "Error: Malformed response from Ollama"

def clean_response(text: str):
    return re.sub(r"^(The main (issue|topic|point) is|Topic:|Issue:|Main topic:)\s*", "", text.strip(), flags=re.I)

@app.post("/analyze/")
def analyze_review(text: str = Form(...)):
    sentiment_prompt = f"What is the sentiment (Positive, Neutral, Negative) of this review? Only answer with one word: Positive, Neutral or Negative.\n\n{text}"
    topic_prompt = f"What is the main issue/topic discussed in this review? Answer in 2-5 words max.\n\n{text}"
    summary_prompt = f"Summarize the review in one short sentence:\n\n{text}"
    
    sentiment = query_ollama(sentiment_prompt).capitalize()
    topic = clean_response(query_ollama(topic_prompt))
    summary = query_ollama(summary_prompt)

    return {
        "sentiment": sentiment if sentiment in ["Positive", "Neutral", "Negative"] else "Neutral",
        "topic": topic,
        "summary": summary
    }
