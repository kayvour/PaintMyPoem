from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def detect_emotion(poem_text):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(poem_text)

    # {
    #   'neg': 0.2,     # % of text that feels negative
    #   'neu': 0.6,     # % of text that is neutral
    #   'pos': 0.2,     # % of text that feels positive
    #   'compound': 0.0 # final score combining all above (-1 to +1)
    # }

    if scores["compound"] >= 0.5:
        return "happy"
    elif scores["compound"] <= -0.5:
        return "sad"
    else:
        return "neutral"
