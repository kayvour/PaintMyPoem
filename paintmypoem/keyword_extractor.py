import re
import string
from collections import Counter

def extract_keywords(text: str, max_keywords: int = 5) -> list[str]:
    """Extract meaningful keywords from poem text with improved filtering.
    Args:
        text (str): Input text.
        max_keywords (int): Maximum number of keywords to return.
    Returns:
        list[str]: List of extracted keywords.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Invalid text")
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    phrases = re.findall(r'\w+\s\w+', text.lower())
    all_words = words + [phrase.replace(' ', '_') for phrase in phrases]

    stop_words = set([
        "the", "is", "in", "and", "to", "a", "of", "it", "i", "you", "we", "he", "she", "they",
        "on", "for", "with", "as", "at", "by", "an", "this", "that", "but", "be", "was", "are",
        "his", "her", "him", "them", "their", "its", "our", "my", "your", "me", "us", "had",
        "have", "has", "will", "would", "could", "should", "may", "might", "can", "do", "did",
        "does", "been", "being", "were", "am", "or", "so", "if", "than", "then", "now", "here",
        "there", "where", "when", "why", "how", "what", "who", "which", "all", "any", "both",
        "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only",
        "own", "same", "so", "than", "too", "very", "just", "now"
    ])

    meaningful_words = [word for word in all_words if word not in stop_words and len(word) > 2]
    word_counts = Counter(meaningful_words)
    scored_words = [(word, count * (len(word.split('_')[0]) / 5.0)) for word, count in word_counts.items()]
    scored_words.sort(key=lambda x: x[1], reverse=True)
    keywords = [word for word, _ in scored_words[:max_keywords]]
    if len(keywords) < max_keywords:
        remaining_words = [word for word in meaningful_words if word not in keywords]
        keywords.extend(remaining_words[:max_keywords - len(keywords)])
    return keywords[:max_keywords]

def extract_visual_keywords(text: str, max_keywords: int = 5) -> list[str]:
    """Extract keywords that are particularly suited for visual representation.
    Args:
        text (str): Input text.
        max_keywords (int): Maximum number of keywords to return.
    Returns:
        list[str]: List of visual keywords.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Invalid text")
    visual_word_categories = {
        'colors': ['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink', 'black', 'white', 
                   'gold', 'silver', 'crimson', 'azure', 'emerald', 'violet', 'amber'],
        'nature': ['tree', 'flower', 'sun', 'moon', 'star', 'ocean', 'mountain', 'river', 'forest',
                   'sky', 'cloud', 'rain', 'snow', 'wind', 'fire', 'earth', 'water', 'light'],
        'emotions': ['love', 'joy', 'happiness', 'sadness', 'anger', 'fear', 'hope', 'dream',
                     'peace', 'harmony', 'chaos', 'passion', 'desire', 'longing'],
        'shapes': ['circle', 'square', 'triangle', 'curve', 'line', 'spiral', 'wave', 'arrow'],
        'textures': ['smooth', 'rough', 'soft', 'hard', 'flowing', 'sharp', 'gentle', 'strong']
    }
    text_lower = text.lower()
    visual_keywords = []
    for category, words in visual_word_categories.items():
        for word in words:
            if word in text_lower:
                visual_keywords.append(word)
    if visual_keywords:
        visual_keywords = list(dict.fromkeys(visual_keywords))
        regular_keywords = extract_keywords(text, max_keywords * 2)
        combined = visual_keywords + [k for k in regular_keywords if k not in visual_keywords]
        return combined[:max_keywords]
    return extract_keywords(text, max_keywords)

def analyze_poem_themes(text: str) -> dict:
    """Analyze the poem for major themes and imagery.
    Args:
        text (str): Input text.
    Returns:
        dict: Keys 'primary_theme', 'all_themes', 'theme_strength'.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Invalid text")
    themes = {
        'nature': ['tree', 'flower', 'sun', 'moon', 'star', 'ocean', 'mountain', 'river', 'forest',
                   'sky', 'cloud', 'rain', 'snow', 'wind', 'fire', 'earth', 'water', 'light', 'dark'],
        'love': ['love', 'heart', 'kiss', 'embrace', 'romance', 'passion', 'desire', 'beloved',
                 'dear', 'honey', 'sweet', 'tender', 'gentle'],
        'time': ['time', 'moment', 'forever', 'eternal', 'always', 'never', 'yesterday', 'tomorrow',
                 'today', 'past', 'future', 'memory', 'remember'],
        'journey': ['path', 'road', 'journey', 'travel', 'walk', 'run', 'fly', 'move', 'go',
                    'destination', 'home', 'away', 'distance'],
        'conflict': ['war', 'battle', 'fight', 'struggle', 'conflict', 'oppose', 'against',
                     'defeat', 'victory', 'loss', 'win']
    }
    text_lower = text.lower()
    found_themes = {}
    for theme, keywords in themes.items():
        count = sum(1 for keyword in keywords if keyword in text_lower)
        if count > 0:
            found_themes[theme] = count
    sorted_themes = sorted(found_themes.items(), key=lambda x: x[1], reverse=True)
    return {
        'primary_theme': sorted_themes[0][0] if sorted_themes else 'general',
        'all_themes': dict(sorted_themes),
        'theme_strength': sorted_themes[0][1] if sorted_themes else 0
    }

def get_mood_descriptors(text: str) -> list[str]:
    """Extract mood-related descriptive words.
    Args:
        text (str): Input text.
    Returns:
        list[str]: List of mood descriptors.
    """
    if not text or not isinstance(text, str):
        raise ValueError("Invalid text")
    mood_words = {
        'bright': ['bright', 'brilliant', 'radiant', 'glowing', 'shining', 'luminous'],
        'dark': ['dark', 'shadow', 'dim', 'gloomy', 'murky', 'obscure'],
        'warm': ['warm', 'hot', 'cozy', 'comfortable', 'heated', 'tropical'],
        'cool': ['cool', 'cold', 'icy', 'frozen', 'chilly', 'arctic'],
        'peaceful': ['peaceful', 'calm', 'serene', 'tranquil', 'quiet', 'still'],
        'energetic': ['energetic', 'vibrant', 'dynamic', 'active', 'lively', 'spirited']
    }
    text_lower = text.lower()
    found_moods = []
    for mood, descriptors in mood_words.items():
        if any(desc in text_lower for desc in descriptors):
            found_moods.append(mood)
    return found_moods
    