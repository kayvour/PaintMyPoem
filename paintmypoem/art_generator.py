import random
import pygame

def draw_art(visual_plan):
    pygame.init()
    screen = pygame.display.set_mode((800, 800))
    pygame.display.set_caption("PaintMyPoem")

    # Draw gradient background
    def draw_gradient_background(screen, top_color, bottom_color):
        for y in range(800):
            r = top_color[0] + (bottom_color[0] - top_color[0]) * y // 800
            g = top_color[1] + (bottom_color[1] - top_color[1]) * y // 800
            b = top_color[2] + (bottom_color[2] - top_color[2]) * y // 800
            pygame.draw.line(screen, (r, g, b), (0, y), (800, y))

    bg_color = visual_plan.get("background_color", (30, 30, 30))
    draw_gradient_background(screen, bg_color, (20, 20, 20))  # soft bottom fade

    # Get palette once at top
    palette = visual_plan.get("palette", [(255, 255, 255)])

    # Draw shapes
    for element in visual_plan["elements"]:
        shape = element["type"]
        pos = element["position"]
        size = element["size"]
        color = random.choice(palette)

        if shape == "circle":
            pygame.draw.circle(screen, color, pos, size)
        elif shape == "square":
            rect = pygame.Rect(pos[0] - size // 2, pos[1] - size // 2, size, size)
            pygame.draw.rect(screen, color, rect)
        elif shape == "triangle":
            point1 = (pos[0], pos[1] - size)
            point2 = (pos[0] - size, pos[1] + size)
            point3 = (pos[0] + size, pos[1] + size)
            pygame.draw.polygon(screen, color, [point1, point2, point3])

    # Draw poem keywords as text at bottom
    font = pygame.font.SysFont("Georgia", 24, bold=True)
    for i, word in enumerate(visual_plan.get("text", [])):
        text = font.render(word, True, random.choice(palette))
        x = 30 + (i % 5) * 150  # 5 words per row
        y = 720 + (i // 5) * 30  # next line if overflow
        screen.blit(text, (x, y))

    # Particle/fog effect
    for _ in range(80):
        x = random.randint(0, 800)
        y = random.randint(0, 800)
        radius = random.randint(20, 60)
        particle = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        alpha = random.randint(20, 50)
        white = (255, 255, 255, alpha)
        pygame.draw.circle(particle, white, (radius, radius), radius)
        screen.blit(particle, (x - radius, y - radius))

    # Save and display
    pygame.display.flip()
    pygame.image.save(screen, "poem_art.png")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()
