import random

def get_palette(emotion):
    palettes = {
        'joy': [(255, 223, 186), (255, 159, 128), (255, 94, 98)],
        'sadness': [(40, 60, 90), (30, 40, 70), (80, 120, 150)],
        'anger': [(200, 50, 50), (150, 30, 30), (90, 10, 10)],
        'fear': [(70, 70, 100), (100, 80, 120), (50, 30, 80)],
        'neutral': [(180, 180, 180), (220, 220, 220), (140, 140, 140)]
    }
    return palettes.get(emotion, palettes['neutral'])

def map_to_visuals(emotion, keywords):
    color_map = {
        "joy": (255, 255, 200),      # pale yellow
        "sadness": (50, 50, 100),    # deep blue
        "anger": (150, 30, 30),      # dark red
        "fear": (80, 80, 120),       # muted violet
        "neutral": (200, 200, 200)   # grey
    }

    shape_options = ["circle", "square", "triangle"]
    visuals = []

    for word in keywords:
        shape = random.choice(shape_options)
        position = (random.randint(50, 750), random.randint(50, 750))
        size = random.randint(30, 100)
        color = tuple(random.randint(100, 255) for _ in range(3))
        
        visuals.append({
            "type": shape,
            "position": position,
            "size": size,
            "color": color,
            "label": word
        })

    return {
        "background_color": color_map.get(emotion, (200, 200, 200)),
        "elements": visuals,
        "palette": get_palette(emotion),
        "text": keywords
    }
