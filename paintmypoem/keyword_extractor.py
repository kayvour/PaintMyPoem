import re
import string
from collections import Counter

def extract_keywords(text, max_keywords=5):
    """
    Extract meaningful keywords from poem text with improved filtering
    """
    # Lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    # Expanded stop words list
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

    # Filter out stop words and short words
    meaningful_words = [word for word in words if word not in stop_words and len(word) > 2]
    
    # Count word frequency
    word_counts = Counter(meaningful_words)
    
    # Get most common words, but prefer longer, more descriptive words
    scored_words = []
    for word, count in word_counts.items():
        # Score based on frequency and length
        score = count * (len(word) / 5.0)  # Favor longer words
        scored_words.append((word, score))
    
    # Sort by score and take top keywords
    scored_words.sort(key=lambda x: x[1], reverse=True)
    keywords = [word for word, score in scored_words[:max_keywords]]
    
    # If we don't have enough keywords, fill with any remaining words
    if len(keywords) < max_keywords:
        remaining_words = [word for word in meaningful_words if word not in keywords]
        keywords.extend(remaining_words[:max_keywords - len(keywords)])
    
    return keywords[:max_keywords]

def extract_visual_keywords(text, max_keywords=5):
    """
    Extract keywords that are particularly suited for visual representation
    """
    # Keywords that translate well to visual elements
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
    
    # Find visual words in the text
    for category, words in visual_word_categories.items():
        for word in words:
            if word in text_lower:
                visual_keywords.append(word)
    
    # If we have visual keywords, prioritize them
    if visual_keywords:
        # Remove duplicates while preserving order
        visual_keywords = list(dict.fromkeys(visual_keywords))
        
        # Fill remaining slots with regular keywords
        regular_keywords = extract_keywords(text, max_keywords * 2)
        combined = visual_keywords + [k for k in regular_keywords if k not in visual_keywords]
        
        return combined[:max_keywords]
    else:
        # Fall back to regular keyword extraction
        return extract_keywords(text, max_keywords)

def analyze_poem_themes(text):
    """
    Analyze the poem for major themes and imagery
    """
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
    
    # Sort themes by frequency
    sorted_themes = sorted(found_themes.items(), key=lambda x: x[1], reverse=True)
    
    return {
        'primary_theme': sorted_themes[0][0] if sorted_themes else 'general',
        'all_themes': dict(sorted_themes),
        'theme_strength': sorted_themes[0][1] if sorted_themes else 0
    }

def get_mood_descriptors(text):
    """
    Extract mood-related descriptive words
    """
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
    