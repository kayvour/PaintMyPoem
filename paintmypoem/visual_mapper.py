import random

def get_palette(emotion: str) -> list[tuple[int, int, int]]:
    """Enhanced color palettes with vibrant, saturated colors.
    Args:
        emotion (str): Detected emotion.
    Returns:
        list[tuple[int, int, int]]: Color palette.
    """
    palettes = {
        "joy": [(255, 215, 0), (255, 165, 0), (255, 69, 0), (255, 20, 147), (255, 105, 180), (255, 255, 0), (255, 140, 0), (255, 192, 203)],
        "sadness": [(65, 105, 225), (30, 144, 255), (0, 191, 255), (135, 206, 250), (70, 130, 180), (100, 149, 237), (0, 206, 209), (72, 209, 204)],
        "anger": [(255, 0, 0), (220, 20, 60), (255, 69, 0), (255, 140, 0), (255, 165, 0), (178, 34, 34), (139, 0, 0), (255, 99, 71)],
        "fear": [(138, 43, 226), (147, 112, 219), (186, 85, 211), (221, 160, 221), (218, 112, 214), (199, 21, 133), (148, 0, 211), (139, 69, 19)],
        "love": [(255, 20, 147), (255, 105, 180), (255, 182, 193), (255, 69, 0), (255, 99, 71), (255, 160, 122), (255, 192, 203), (220, 20, 60)],
        "neutral": [(138, 43, 226), (30, 144, 255), (255, 165, 0), (50, 205, 50), (255, 215, 0), (255, 20, 147), (0, 255, 127), (255, 69, 0)]
    }
    return palettes.get(emotion, palettes["neutral"])

def get_vibrant_background(emotion: str) -> tuple[int, int, int]:
    """Enhanced backgrounds with more color and gradients.
    Args:
        emotion (str): Detected emotion.
    Returns:
        tuple[int, int, int]: Background color.
    """
    backgrounds = {
        "joy": (255, 248, 220),
        "sadness": (25, 25, 112),
        "anger": (139, 0, 0),
        "fear": (72, 61, 139),
        "love": (255, 240, 245),
        "neutral": (47, 79, 79)
    }
    return backgrounds.get(emotion, (47, 79, 79))

def get_accent_colors(emotion: str) -> list[tuple[int, int, int]]:
    """Additional accent colors for more variety.
    Args:
        emotion (str): Detected emotion.
    Returns:
        list[tuple[int, int, int]]: Accent colors.
    """
    accents = {
        "joy": [(255, 215, 0), (255, 140, 0), (255, 69, 0)],
        "sadness": [(0, 191, 255), (65, 105, 225), (30, 144, 255)],
        "anger": [(255, 0, 0), (255, 69, 0), (220, 20, 60)],
        "fear": [(138, 43, 226), (147, 112, 219), (186, 85, 211)],
        "love": [(255, 20, 147), (255, 105, 180), (220, 20, 60)],
        "neutral": [(138, 43, 226), (255, 165, 0), (50, 205, 50)]
    }
    return accents.get(emotion, accents["neutral"])

def map_to_visuals(emotion: str, keywords: list[str]) -> dict:
    """Map emotion and keywords to visual elements.
    Args:
        emotion (str): Detected emotion.
        keywords (list[str]): Extracted keywords.
    Returns:
        dict: Visual plan with elements, colors, and settings.
    """
    palette = get_palette(emotion)
    accent_colors = get_accent_colors(emotion)
    background_color = get_vibrant_background(emotion)
    shape_options = ["circle", "square", "triangle", "hexagon", "star"]
    visuals = []
    num_elements = max(len(keywords) * 2, 8)
    for i in range(num_elements):
        if i < len(keywords):
            word = keywords[i]
        else:
            word = f"element_{i}"
        shape = random.choice(shape_options)
        x = random.randint(80, 720)
        y = random.randint(80, 600)
        position = (x, y)
        size = random.randint(25, 120)
        if random.random() < 0.7:
            color = random.choice(palette)
        else:
            color = random.choice(accent_colors)
        visuals.append({"type": shape, "position": position, "size": size, "color": color, "label": word, "alpha": random.randint(200, 255)})
    return {"background_color": background_color, "elements": visuals, "palette": palette, "accent_colors": accent_colors, "text": keywords, "fog": False, "emotion": emotion}
    