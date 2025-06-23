import random
import pygame
import math
import os
from background_manager import BackgroundManager

def draw_art(visual_plan, background_type=None, background_opacity=0.4):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("PaintMyPoem")
    
    # Initialize background manager
    bg_manager = BackgroundManager()

    def draw_vibrant_gradient_background(screen, top_color, emotion):
        """Create more colorful gradient backgrounds"""
        # Create gradient variations based on emotion
        gradient_variants = {
            "joy": [(255, 248, 220), (255, 215, 0), (255, 165, 0)],
            "happy": [(255, 248, 220), (255, 215, 0), (255, 165, 0)],  # Same as joy
            "sadness": [(25, 25, 112), (65, 105, 225), (30, 144, 255)],
            "sad": [(25, 25, 112), (65, 105, 225), (30, 144, 255)],    # Same as sadness
            "anger": [(139, 0, 0), (255, 69, 0), (255, 140, 0)],
            "fear": [(72, 61, 139), (138, 43, 226), (147, 112, 219)],
            "love": [(255, 240, 245), (255, 20, 147), (255, 105, 180)],
            "neutral": [(47, 79, 79), (138, 43, 226), (30, 144, 255)]
        }
        
        colors = gradient_variants.get(emotion, gradient_variants["neutral"])
        
        for y in range(800):
            # Create a 3-color gradient
            if y < 400:
                # Top half: color1 to color2
                ratio = y / 400
                r = int(colors[0][0] + (colors[1][0] - colors[0][0]) * ratio)
                g = int(colors[0][1] + (colors[1][1] - colors[0][1]) * ratio)
                b = int(colors[0][2] + (colors[1][2] - colors[0][2]) * ratio)
            else:
                # Bottom half: color2 to color3
                ratio = (y - 400) / 400
                r = int(colors[1][0] + (colors[2][0] - colors[1][0]) * ratio)
                g = int(colors[1][1] + (colors[2][1] - colors[1][1]) * ratio)
                b = int(colors[1][2] + (colors[2][2] - colors[1][2]) * ratio)
            
            pygame.draw.line(screen, (r, g, b), (0, y), (800, y))

    def draw_enhanced_shape(screen, element):
        """Draw shapes with enhanced visual effects"""
        shape = element["type"]
        pos = element["position"]
        size = element["size"]
        color = element["color"]
        alpha = element.get("alpha", 255)
        
        # Create surface with alpha for transparency effects
        shape_surface = pygame.Surface((size * 2, size * 2), pygame.SRCALPHA)
        
        if shape == "circle":
            pygame.draw.circle(shape_surface, (*color, alpha), (size, size), size)
            # Add inner glow
            inner_size = max(size - 10, 5)
            brighter_color = tuple(min(255, c + 30) for c in color)
            pygame.draw.circle(shape_surface, (*brighter_color, alpha//2), (size, size), inner_size)
            
        elif shape == "square":
            rect = pygame.Rect(size//2, size//2, size, size)
            pygame.draw.rect(shape_surface, (*color, alpha), rect)
            # Add border
            pygame.draw.rect(shape_surface, (255, 255, 255, alpha//3), rect, 3)
            
        elif shape == "triangle":
            point1 = (size, size//2)
            point2 = (size//2, size + size//2)
            point3 = (size + size//2, size + size//2)
            pygame.draw.polygon(shape_surface, (*color, alpha), [point1, point2, point3])
            
        elif shape == "hexagon":
            # Draw hexagon
            points = []
            for i in range(6):
                angle = i * math.pi / 3
                x = size + size * 0.7 * math.cos(angle)
                y = size + size * 0.7 * math.sin(angle)
                points.append((x, y))
            pygame.draw.polygon(shape_surface, (*color, alpha), points)
            
        elif shape == "star":
            # Draw 5-pointed star
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
        
        # Blit the shape to the main screen
        screen.blit(shape_surface, (pos[0] - size, pos[1] - size))

    # Handle background rendering
    emotion = visual_plan.get("emotion", "neutral")
    
    if background_type:
        print(f"🌄 Adding {background_type} background with {background_opacity*100}% opacity...")
        
        # Get background image
        bg_path = bg_manager.get_background_image(background_type)
        if bg_path:
            # Create background surface
            bg_surface = bg_manager.prepare_background_surface(bg_path, background_opacity)
            screen.blit(bg_surface, (0, 0))
            
            # Add subtle gradient overlay to blend with poem art
            overlay = pygame.Surface((800, 800), pygame.SRCALPHA)
            bg_color = visual_plan.get("background_color", (47, 79, 79))
            # Create very subtle gradient overlay
            for y in range(800):
                alpha = int(30 * (1 - y/800))  # Fade from top to bottom
                color = (*bg_color, alpha)
                pygame.draw.line(overlay, color, (0, y), (800, y))
            screen.blit(overlay, (0, 0))
        else:
            print("⚠️ Background image failed, using gradient fallback")
            draw_vibrant_gradient_background(screen, visual_plan.get("background_color", (47, 79, 79)), emotion)
    else:
        # Draw vibrant gradient background (original behavior)
        bg_color = visual_plan.get("background_color", (47, 79, 79))
        draw_vibrant_gradient_background(screen, bg_color, emotion)

    # Get color palettes
    palette = visual_plan.get("palette", [(255, 255, 255)])
    accent_colors = visual_plan.get("accent_colors", palette)

    # Draw all elements with enhanced effects
    for element in visual_plan["elements"]:
        draw_enhanced_shape(screen, element)

    # Add decorative particles for extra vibrancy
    for _ in range(30):
        x = random.randint(0, 800)
        y = random.randint(0, 600)  # Avoid text area
        radius = random.randint(2, 8)
        color = random.choice(palette + accent_colors)
        alpha = random.randint(100, 200)
        
        particle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(particle_surface, (*color, alpha), (radius, radius), radius)
        screen.blit(particle_surface, (x - radius, y - radius))

    # Enhanced text rendering with better contrast for backgrounds
    font = pygame.font.SysFont("Georgia", 28, bold=True)
    shadow_font = pygame.font.SysFont("Georgia", 28, bold=True)
    
    # Create semi-transparent text background for better readability
    text_bg = pygame.Surface((800, 100), pygame.SRCALPHA)
    text_bg.fill((0, 0, 0, 100))  # Semi-transparent black
    screen.blit(text_bg, (0, 700))
    
    for i, word in enumerate(visual_plan.get("text", [])):
        # Use vibrant colors for text but ensure contrast
        text_color = random.choice(palette)
        
        # Make text brighter for better visibility on backgrounds
        enhanced_color = tuple(min(255, c + 50) for c in text_color)
        
        # Create text shadow for better readability
        shadow_text = shadow_font.render(word, True, (0, 0, 0))
        main_text = font.render(word, True, enhanced_color)
        
        x = 40 + (i % 4) * 180
        y = 720 + (i // 4) * 35
        
        # Draw shadow slightly offset
        screen.blit(shadow_text, (x + 2, y + 2))
        screen.blit(main_text, (x, y))

    # Optional: Light fog effect (much reduced)
    if visual_plan.get("fog", False):
        for _ in range(15):  # Reduced from 60
            x = random.randint(0, 800)
            y = random.randint(0, 800)
            radius = random.randint(15, 35)  # Smaller particles
            particle = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            alpha = random.randint(5, 15)  # Much more transparent
            white = (255, 255, 255, alpha)
            pygame.draw.circle(particle, white, (radius, radius), radius)
            screen.blit(particle, (x - radius, y - radius))

    pygame.display.flip()

    # Save the artwork
    try:
        pygame.image.save(screen, "poem_art.png")
        print("✅ Vibrant image saved successfully as 'poem_art.png'!")
    except Exception as e:
        print(f"❌ Failed to save image: {e}")

    # Clean up old backgrounds to save space
    bg_manager.cleanup_old_backgrounds()

    # Keep window open until user closes it
    running = True
    clock = pygame.time.Clock()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        clock.tick(60)  # Limit to 60 FPS

    pygame.quit()
    
    # Clean up temp files
    temp_files = ["temp.png"]
    for temp_file in temp_files:
        if os.path.exists(temp_file):
            os.remove(temp_file)
            