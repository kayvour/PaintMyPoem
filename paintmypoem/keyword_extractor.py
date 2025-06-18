import re
import string

def extract_keywords(text):
    # Lowercase and remove punctuation
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()

    stop_words = set([
        "the", "is", "in", "and", "to", "a", "of", "it", "i", "you", "we", "he", "she", "they",
        "on", "for", "with", "as", "at", "by", "an", "this", "that", "but", "be", "was", "are"
    ])

    keywords = [word for word in words if word not in stop_words]
    return keywords[:5]  # Return up to 5 keywords
