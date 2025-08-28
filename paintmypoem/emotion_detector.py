from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(poem_text: str) -> str:
    """Detect emotion from poem text using VADER sentiment analysis.
    Returns emotion keys that match visual_mapper expectations.
    Args:
        poem_text (str): Input poem text.
    Returns:
        str: Detected emotion (e.g., 'joy', 'sadness').
    """
    if not poem_text or not isinstance(poem_text, str):
        raise ValueError("Invalid poem text")
    scores = analyzer.polarity_scores(poem_text)
    compound = scores["compound"]
    positive = scores["pos"]
    negative = scores["neg"]
    if compound >= 0.6:
        if "love" in poem_text.lower() or "heart" in poem_text.lower() or "dear" in poem_text.lower():
            return "love"
        else:
            return "joy"
    elif compound >= 0.2:
        return "joy"
    elif compound <= -0.6:
        if "angry" in poem_text.lower() or "rage" in poem_text.lower() or "mad" in poem_text.lower():
            return "anger"
        elif "scared" in poem_text.lower() or "afraid" in poem_text.lower() or "fear" in poem_text.lower():
            return "fear"
        else:
            return "sadness"
    elif compound <= -0.2:
        return "sadness"
    else:
        return "neutral"

def get_emotion_intensity(poem_text: str) -> float:
    """Get the intensity of the detected emotion (0.0 to 1.0).
    Useful for adjusting visual effects.
    Args:
        poem_text (str): Input poem text.
    Returns:
        float: Emotion intensity.
    """
    if not poem_text or not isinstance(poem_text, str):
        raise ValueError("Invalid poem text")
    scores = analyzer.polarity_scores(poem_text)
    return abs(scores["compound"])

def analyze_poem_mood(poem_text: str) -> dict:
    """Comprehensive poem analysis returning emotion, intensity, and keywords.
    Args:
        poem_text (str): Input poem text.
    Returns:
        dict: Keys 'emotion', 'intensity', 'mood_keywords', 'raw_scores'.
    """
    if not poem_text or not isinstance(poem_text, str):
        raise ValueError("Invalid poem text")
    emotion = detect_emotion(poem_text)
    intensity = get_emotion_intensity(poem_text)
    mood_keywords = {
        "joy": ["happy", "bright", "sun", "smile", "laugh", "dance", "celebration"],
        "love": ["love", "heart", "dear", "beloved", "kiss", "embrace", "romance"],
        "sadness": ["sad", "cry", "tear", "lonely", "dark", "rain", "sorrow"],
        "anger": ["angry", "rage", "mad", "fury", "storm", "fire", "hate"],
        "fear": ["fear", "scared", "afraid", "dark", "shadow", "nightmare", "worry"],
        "neutral": []
    }
    found_keywords = [kw for kw in mood_keywords.get(emotion, []) if kw in poem_text.lower()]
    return {
        "emotion": emotion,
        "intensity": intensity,
        "mood_keywords": found_keywords,
        "raw_scores": analyzer.polarity_scores(poem_text)
    }

def get_recommended_background_type(emotion: str) -> str:
    """Get recommended background type based on detected emotion.
    This integrates with the BackgroundManager system.
    Args:
        emotion (str): Detected emotion.
    Returns:
        str: Recommended background type.
    """
    emotion_backgrounds = {
        "joy": ["sunset", "sky", "mountains"],
        "happy": ["sunset", "sky", "mountains"],
        "sadness": ["ocean", "forest", "mountains"],
        "sad": ["ocean", "forest", "mountains"],
        "anger": ["mountains", "sunset", "forest"],
        "fear": ["forest", "mountains", "ocean"],
        "love": ["sunset", "sky", "ocean"],
        "neutral": ["sky", "forest", "ocean", "mountains"]
    }
    import random
    recommended = emotion_backgrounds.get(emotion, ["sky", "forest", "ocean"])
    return random.choice(recommended)
    