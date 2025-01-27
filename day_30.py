from textblob import TextBlob

def analyze_sentiment(text):
    """Analyze the sentiment of a given text."""
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "Positive"
    elif sentiment_score < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return sentiment, sentiment_score

if __name__ == "__main__":
    text = input("Enter text to analyze sentiment: ")
    sentiment, score = analyze_sentiment(text)
    print(f"Sentiment: {sentiment}")
    print(f"Polarity Score: {score:.4f}")
