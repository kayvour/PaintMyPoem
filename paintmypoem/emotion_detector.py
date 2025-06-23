from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def detect_emotion(poem_text):
    """
    Detect emotion from poem text using VADER sentiment analysis.
    Returns emotion keys that match visual_mapper expectations.
    """
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(poem_text)
    
    # Enhanced emotion detection with more nuanced categories
    compound = scores["compound"]
    positive = scores["pos"]
    negative = scores["neg"]
    
    # More sophisticated emotion mapping
    if compound >= 0.6:
        # Very positive - could be joy or love
        if "love" in poem_text.lower() or "heart" in poem_text.lower() or "dear" in poem_text.lower():
            return "love"
        else:
            return "joy"
    elif compound >= 0.2:
        # Mildly positive
        return "joy"
    elif compound <= -0.6:
        # Very negative - could be sadness, anger, or fear
        if "angry" in poem_text.lower() or "rage" in poem_text.lower() or "mad" in poem_text.lower():
            return "anger"
        elif "scared" in poem_text.lower() or "afraid" in poem_text.lower() or "fear" in poem_text.lower():
            return "fear"
        else:
            return "sadness"
    elif compound <= -0.2:
        # Mildly negative
        return "sadness"
    else:
        # Neutral
        return "neutral"

def get_emotion_intensity(poem_text):
    """
    Get the intensity of the detected emotion (0.0 to 1.0)
    Useful for adjusting visual effects
    """
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(poem_text)
    return abs(scores["compound"])

def analyze_poem_mood(poem_text):
    """
    Comprehensive poem analysis returning emotion, intensity, and keywords
    """
    # Create analyzer once for this function
    analyzer = SentimentIntensityAnalyzer()
    
    emotion = detect_emotion(poem_text)
    intensity = get_emotion_intensity(poem_text)
    
    # Additional mood indicators
    mood_keywords = {
        "joy": ["happy", "bright", "sun", "smile", "laugh", "dance", "celebration"],
        "love": ["love", "heart", "dear", "beloved", "kiss", "embrace", "romance"],
        "sadness": ["sad", "cry", "tear", "lonely", "dark", "rain", "sorrow"],
        "anger": ["angry", "rage", "mad", "fury", "storm", "fire", "hate"],
        "fear": ["fear", "scared", "afraid", "dark", "shadow", "nightmare", "worry"],
        "neutral": []
    }
    
    found_keywords = []
    poem_lower = poem_text.lower()
    for keyword in mood_keywords.get(emotion, []):
        if keyword in poem_lower:
            found_keywords.append(keyword)
    
    return {
        "emotion": emotion,
        "intensity": intensity,
        "mood_keywords": found_keywords,
        "raw_scores": analyzer.polarity_scores(poem_text)  # ✅ Now analyzer is defined!
    }

def get_recommended_background_type(emotion):
    """
    Get recommended background type based on detected emotion
    This integrates with the BackgroundManager system
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
    