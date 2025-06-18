from PIL import Image, ImageFilter

def soften_image(pygame_surface, output_path='poem_art_final.png'):
    pygame.image.save(pygame_surface, "temp.png")
    img = Image.open("temp.png")
    img = img.filter(ImageFilter.SMOOTH_MORE)
    img.save(output_path)
    print(f"🖼️ Final polished image saved as '{output_path}'")
