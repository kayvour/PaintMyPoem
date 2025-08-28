import random
import pygame
import math
import os
from background_manager import BackgroundManager

def draw_art(visual_plan: dict, background_type: str = None, background_opacity: float = 0.4, size: tuple[int, int] = (800, 800)) -> None:
    """Draw poem art based on visual plan with optional background.
    Args:
        visual_plan (dict): Dictionary containing art elements, colors, and style.
        background_type (str, optional): Type of background to use.
        background_opacity (float): Opacity level for background (0.0 to 1.0).
        size (tuple[int, int]): Dimensions of the drawing surface.
    """
    if not visual_plan or "elements" not in visual_plan:
        raise ValueError("Invalid visual_plan: must contain 'elements' key")

    screen = pygame.display.get_surface()  # Use the existing surface from main.py
    if screen is None:
        raise RuntimeError("No Pygame display surface available. Ensure Pygame is initialized.")

    # Initialize background manager
    bg_manager = BackgroundManager()

    def draw_vibrant_gradient_background(screen, top_color, emotion, complexity=3):
        """Create more colorful gradient backgrounds with variable complexity"""
        gradient_variants = {
            "joy": [(255, 248, 220), (255, 215, 0), (255, 165, 0)],
            "happy": [(255, 248, 220), (255, 215, 0), (255, 165, 0)],
            "sadness": [(25, 25, 112), (65, 105, 225), (30, 144, 255)],
            "sad": [(25, 25, 112), (65, 105, 225), (30, 144, 255)],
            "anger": [(139, 0, 0), (255, 69, 0), (255, 140, 0)],
            "fear": [(72, 61, 139), (138, 43, 226), (147, 112, 219)],
            "love": [(255, 240, 245), (255, 20, 147), (255, 105, 180)],
            "neutral": [(47, 79, 79), (138, 43, 226), (30, 144, 255)]
        }
        
        colors = gradient_variants.get(emotion, gradient_variants["neutral"])
        
        if complexity == 2:
            for y in range(size[1]):
                ratio = y / size[1]
                r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * ratio)
                g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * ratio)
                b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * ratio)
                pygame.draw.line(screen, (r, g, b), (0, y), (size[0], y))
        else:
            for y in range(size[1]):
                if y < size[1] // 2:
                    ratio = y / (size[1] // 2)
                    r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * ratio)
                    g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * ratio)
                    b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * ratio)
                else:
                    ratio = (y - size[1] // 2) / (size[1] // 2)
                    r = int(colors[1][0] + (colors[2][0] - colors[1][0]) * ratio)
                    g = int(colors[1][1] + (colors[2][1] - colors[1][1]) * ratio)
                    b = int(colors[1][2] + (colors[2][2] - colors[1][2]) * ratio)
                pygame.draw.line(screen, (r, g, b), (0, y), (size[0], y))

    def draw_enhanced_shape(screen, element, style_name="vibrant"):
        """Draw shapes with enhanced visual effects based on style"""
        shape = element["type"]
        pos = element["position"]
        size = element["size"]
        color = element["color"]
        alpha = element.get("alpha", 255)
        
        shape_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        
        if style_name == "minimalist":
            if shape == "circle":
                pygame.draw.circle(shape_surface, (*color, alpha), (size, size), size)
            elif shape == "square":
                rect = pygame.Rect(size//2, size//2, size, size)
                pygame.draw.rect(shape_surface, (*color, alpha), rect)
        elif style_name == "bold":
            if shape == "circle":
                pygame.draw.circle(shape_surface, (*color, alpha), (size, size), size)
                pygame.draw.circle(shape_surface, (255, 255, 255, alpha), (size, size), size, 5)
            elif shape == "square":
                rect = pygame.Rect(size//2, size//2, size, size)
                pygame.draw.rect(shape_surface, (*color, alpha), rect)
                pygame.draw.rect(shape_surface, (255, 255, 255, alpha), rect, 5)
            elif shape == "triangle":
                point1 = (size, size//2)
                point2 = (size//2, size + size//2)
                point3 = (size + size//2, size + size//2)
                pygame.draw.polygon(shape_surface, (*color, alpha), [point1, point2, point3])
                pygame.draw.polygon(shape_surface, (255, 255, 255, alpha), [point1, point2, point3], 4)
            elif shape == "hexagon":
                points = []
                for i in range(6):
                    angle = i * math.pi / 3
                    x = size + size * 0.7 * math.cos(angle)
                    y = size + size * 0.7 * math.sin(angle)
                    points.append((x, y))
                pygame.draw.polygon(shape_surface, (*color, alpha), points)
                pygame.draw.polygon(shape_surface, (255, 255, 255, alpha), points, 4)
        else:
            if shape == "circle":
                pygame.draw.circle(shape_surface, (*color, alpha), (size, size), size)
                inner_size = max(size - 10, 5)
                brighter_color = tuple(min(255, c + 30) for c in color)
                pygame.draw.circle(shape_surface, (*brighter_color, alpha//2), (size, size), inner_size)
            elif shape == "square":
                rect = pygame.Rect(size//2, size//2, size, size)
                pygame.draw.rect(shape_surface, (*color, alpha), rect)
                pygame.draw.rect(shape_surface, (255, 255, 255, alpha//3), rect, 3)
            elif shape == "triangle":
                point1 = (size, size//2)
                point2 = (size//2, size + size//2)
                point3 = (size + size//2, size + size//2)
                pygame.draw.polygon(shape_surface, (*color, alpha), [point1, point2, point3])
            elif shape == "hexagon":
                points = []
                for i in range(6):
                    angle = i * math.pi / 3
                    x = size + size * 0.7 * math.cos(angle)
                    y = size + size * 0.7 * math.sin(angle)
                    points.append((x, y))
                pygame.draw.polygon(shape_surface, (*color, alpha), points)
            elif shape == "star":
                points = []
                for i in range(10):
                    angle = i * math.pi / 5
                    if i % 2 == 0:
                        radius = size * 0.8
                    else:
                        radius = size * 0.4
                    x = size + radius * math.cos(angle - math.pi/2)
                    y = size + radius * math.sin(angle - math.pi/2)
                    points.append((x, y))
                pygame.draw.polygon(shape_surface, (*color, alpha), points)
        
        screen.blit(shape_surface, (pos[0] - size, pos[1] - size))

    emotion = visual_plan.get("emotion", "neutral")
    gradient_complexity = visual_plan.get("gradient_complexity", 3)
    
    if background_type:
        print(f"🌄 Adding {background_type} background with {background_opacity*100}% opacity...")
        bg_path = bg_manager.get_background_image(background_type)
        if bg_path:
            bg_surface = bg_manager.prepare_background_surface(bg_path, background_opacity, size)
            screen.blit(bg_surface, (0, 0))
            overlay = pygame.Surface(size, pygame.SRCALPHA)
            bg_color = visual_plan.get("background_color", (47, 79, 79))
            for y in range(size[1]):
                alpha = int(30 * (1 - y/size[1]))
                color = (*bg_color, alpha)
                pygame.draw.line(overlay, color, (0, y), (size[0], y))
            screen.blit(overlay, (0, 0))
        else:
            print("⚠️ Background image failed, using gradient fallback")
            draw_vibrant_gradient_background(screen, visual_plan.get("background_color", (47, 79, 79)), emotion, gradient_complexity)
    else:
        bg_color = visual_plan.get("background_color", (47, 79, 79))
        draw_vibrant_gradient_background(screen, bg_color, emotion, gradient_complexity)

    palette = visual_plan.get("palette", [(255, 255, 255)])
    accent_colors = visual_plan.get("accent_colors", palette)
    style_name = visual_plan.get("style_name", "vibrant")
    particle_count = visual_plan.get("particle_count", 30)

    for element in visual_plan["elements"]:
        draw_enhanced_shape(screen, element, style_name)

    if style_name != "minimalist":
        for _ in range(particle_count):
            x = random.randint(0, size[0])
            y = random.randint(0, size[1] - 200)
            radius = random.randint(2, 8)
            color = random.choice(palette + accent_colors)
            if style_name == "ethereal":
                alpha = random.randint(60, 120)
            elif style_name == "bold":
                alpha = random.randint(180, 255)
            else:
                alpha = random.randint(100, 200)
            particle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(particle_surface, (*color, alpha), (radius, radius), radius)
            screen.blit(particle_surface, (x - radius, y - radius))

    font_size = 28 if style_name != "minimalist" else 24
    font = pygame.font.SysFont("Georgia", font_size, bold=True)
    shadow_font = pygame.font.SysFont("Georgia", font_size, bold=True)
    
    text_bg = pygame.Surface((size[0], 100), pygame.SRCALPHA)
    bg_alpha = 100 if style_name != "minimalist" else 50
    text_bg.fill((0, 0, 0, bg_alpha))
    screen.blit(text_bg, (0, size[1] - 100))
    
    for i, word in enumerate(visual_plan.get("text", [])):
        if style_name == "minimalist":
            text_color = random.choice([(100, 100, 100), (150, 150, 150), (80, 80, 80)])
        elif style_name == "bold":
            text_color = random.choice([(255, 255, 255), (0, 0, 0)] + list(palette[:2]))
        else:
            text_color = random.choice(palette)
        
        if style_name != "minimalist":
            enhanced_color = tuple(min(255, c + 50) for c in text_color)
        else:
            enhanced_color = text_color
        
        if style_name != "minimalist":
            shadow_text = shadow_font.render(word, True, (0, 0, 0))
            main_text = font.render(word, True, enhanced_color)
            x = 40 + (i % 4) * 180
            y = size[1] - 80 + (i // 4) * 35
            screen.blit(shadow_text, (x + 2, y + 2))
            screen.blit(main_text, (x, y))
        else:
            main_text = font.render(word, True, enhanced_color)
            x = 40 + (i % 4) * 180
            y = size[1] - 80 + (i // 4) * 35
            screen.blit(main_text, (x, y))

    if visual_plan.get("fog", False) and style_name in ["ethereal", "organic"]:
        fog_intensity = 15 if style_name == "ethereal" else 8
        for _ in range(fog_intensity):
            x = random.randint(0, size[0])
            y = random.randint(0, size[1])
            radius = random.randint(15, 35)
            particle = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            alpha = random.randint(5, 15)
            white = (255, 255, 255, alpha)
            pygame.draw.circle(particle, white, (radius, radius), radius)
            screen.blit(particle, (x - radius, y - radius))

    pygame.display.flip()

    try:
        pygame.image.save(screen, "poem_art.png")
        print("✅ Stylized image saved successfully as 'poem_art.png'!")
    except Exception as e:
        print(f"❌ Failed to save image: {e}")

    bg_manager.cleanup_old_backgrounds()
    