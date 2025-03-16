from fastapi import FastAPI
from pydantic import BaseModel
from textblob import TextBlob

# Initialize FastAPI app
app = FastAPI()

class PostInput(BaseModel):
    text: str  # Input post text

@app.post("/analyze/")
def analyze_post(post: PostInput):
    """
    Receives a post and determines if it should be approved.
    Returns True if Positive or Neutral, False if Negative.
    """
    analysis = TextBlob(post.text)
    sentiment_score = analysis.sentiment.polarity  # Polarity ranges from -1 to 1

    print(f"Sentiment Score: {sentiment_score}")  # Debugging output

    return {"approved": sentiment_score >= 0}  # Approve if Neutral (0) or Positive (>0), otherwise forward

# Run the API server with: uvicorn sentiment_api:app --host 0.0.0.0 --port 8000 --reload

