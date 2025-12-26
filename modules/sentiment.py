positive_words = {"good", "great", "excellent", "happy", "satisfied", "love"}
negative_words = {"bad", "poor", "delay", "late", "worst", "angry", "issue"}
neutral_words = {"ok", "fine", "average"}

def analyze_sentiment(message):
    msg = message.lower()
    score = 0

    for word in positive_words:
        if word in msg:
            score += 1
    for word in negative_words:
        if word in msg:
            score -= 1

    if score > 0:
        return 1, "Positive"
    elif score < 0:
        return -1, "Negative"
    else:
        return 0, "Neutral"

