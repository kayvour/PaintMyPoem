import random

def get_palette(emotion):
    """Enhanced color palettes with vibrant, saturated colors"""
    palettes = {
        "joy": [
            (255, 215, 0),      # Gold
            (255, 165, 0),      # Orange  
            (255, 69, 0),       # Red-Orange
            (255, 20, 147),     # Deep Pink
            (255, 105, 180),    # Hot Pink
            (255, 255, 0),      # Bright Yellow
            (255, 140, 0),      # Dark Orange
            (255, 192, 203)     # Pink
        ],
        "sadness": [
            (65, 105, 225),     # Royal Blue
            (30, 144, 255),     # Dodger Blue
            (0, 191, 255),      # Deep Sky Blue
            (135, 206, 250),    # Light Sky Blue
            (70, 130, 180),     # Steel Blue
            (100, 149, 237),    # Cornflower Blue
            (0, 206, 209),      # Dark Turquoise
            (72, 209, 204)      # Medium Turquoise
        ],
        "anger": [
            (255, 0, 0),        # Pure Red
            (220, 20, 60),      # Crimson
            (255, 69, 0),       # Red-Orange
            (255, 140, 0),      # Dark Orange
            (255, 165, 0),      # Orange
            (178, 34, 34),      # Fire Brick
            (139, 0, 0),        # Dark Red
            (255, 99, 71)       # Tomato
        ],
        "fear": [
            (138, 43, 226),     # Blue Violet
            (147, 112, 219),    # Medium Purple
            (186, 85, 211),     # Medium Orchid
            (221, 160, 221),    # Plum
            (218, 112, 214),    # Orchid
            (199, 21, 133),     # Medium Violet Red
            (148, 0, 211),      # Dark Violet
            (139, 69, 19)       # Saddle Brown
        ],
        "love": [
            (255, 20, 147),     # Deep Pink
            (255, 105, 180),    # Hot Pink
            (255, 182, 193),    # Light Pink
            (255, 69, 0),       # Red-Orange
            (255, 99, 71),      # Tomato
            (255, 160, 122),    # Light Salmon
            (255, 192, 203),    # Pink
            (220, 20, 60)       # Crimson
        ],
        "neutral": [
            (138, 43, 226),     # Blue Violet (instead of grey!)
            (30, 144, 255),     # Dodger Blue
            (255, 165, 0),      # Orange
            (50, 205, 50),      # Lime Green
            (255, 215, 0),      # Gold
            (255, 20, 147),     # Deep Pink
            (0, 255, 127),      # Spring Green
            (255, 69, 0)        # Red-Orange
        ]
    }
    return palettes.get(emotion, palettes["neutral"])

def get_vibrant_background(emotion):
    """Enhanced backgrounds with more color and gradients"""
    backgrounds = {
        "joy": (255, 248, 220),      # Cornsilk - warm cream
        "sadness": (25, 25, 112),    # Midnight Blue
        "anger": (139, 0, 0),        # Dark Red
        "fear": (72, 61, 139),       # Dark Slate Blue
        "love": (255, 240, 245),     # Lavender Blush
        "neutral": (47, 79, 79)      # Dark Slate Gray (not pure grey)
    }
    return backgrounds.get(emotion, (47, 79, 79))

def get_accent_colors(emotion):
    """Additional accent colors for more variety"""
    accents = {
        "joy": [(255, 215, 0), (255, 140, 0), (255, 69, 0)],
        "sadness": [(0, 191, 255), (65, 105, 225), (30, 144, 255)],
        "anger": [(255, 0, 0), (255, 69, 0), (220, 20, 60)],
        "fear": [(138, 43, 226), (147, 112, 219), (186, 85, 211)],
        "love": [(255, 20, 147), (255, 105, 180), (220, 20, 60)],
        "neutral": [(138, 43, 226), (255, 165, 0), (50, 205, 50)]
    }
    return accents.get(emotion, accents["neutral"])

def map_to_visuals(emotion, keywords):
    palette = get_palette(emotion)
    accent_colors = get_accent_colors(emotion)
    background_color = get_vibrant_background(emotion)

    # More varied shape options
    shape_options = ["circle", "square", "triangle", "hexagon", "star"]
    visuals = []

    # Create more elements for richer visuals
    num_elements = max(len(keywords) * 2, 8)  # At least 8 elements
    
    for i in range(num_elements):
        if i < len(keywords):
            word = keywords[i]
        else:
            word = f"element_{i}"
            
        shape = random.choice(shape_options)
        
        # Better positioning to avoid clustering
        x = random.randint(80, 720)
        y = random.randint(80, 600)  # Leave room for text at bottom
        position = (x, y)
        
        # More size variation
        size = random.randint(25, 120)
        
        # Use vibrant colors from palette and accents
        if random.random() < 0.7:  # 70% chance main palette
            color = random.choice(palette)
        else:  # 30% chance accent colors
            color = random.choice(accent_colors)

        visuals.append({
            "type": shape,
            "position": position,
            "size": size,
            "color": color,
            "label": word,
            "alpha": random.randint(200, 255)  # Add transparency variation
        })

    return {
        "background_color": background_color,
        "elements": visuals,
        "palette": palette,
        "accent_colors": accent_colors,
        "text": keywords,
        "fog": False,  # Disable fog by default for more vibrant images
        "emotion": emotion
    }
    