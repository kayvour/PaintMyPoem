from PIL import Image, ImageFilter, ImageEnhance
import pygame
import os
import tempfile

def soften_image(pygame_surface: pygame.Surface, output_path: str = 'poem_art_final.png') -> str:
    """Apply post-processing effects to the generated artwork.
    Args:
        pygame_surface (pygame.Surface): Surface to process.
        output_path (str): Path to save the final image.
    Returns:
        str: Path to the saved image.
    """
    if pygame_surface is None:
        raise ValueError("Invalid pygame_surface")
    try:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            pygame.image.save(pygame_surface, temp_file.name)
            with Image.open(temp_file.name) as img:
                img = img.filter(ImageFilter.SMOOTH_MORE)
                enhancer = ImageEnhance.Color(img)
                img = enhancer.enhance(1.1)
                img.save(output_path, quality=95)
                print(f"🖼️ Final polished image saved as '{output_path}'")
        os.remove(temp_file.name)
        return output_path
    except Exception as e:
        print(f"❌ Error in image post-processing: {e}")
        pygame.image.save(pygame_surface, output_path)
        print(f"🖼️ Image saved as '{output_path}' (without post-processing)")
        return output_path

def create_image_variants(pygame_surface: pygame.Surface, base_name: str = 'poem_art') -> list[tuple[str, str]]:
    """Create multiple versions of the artwork with different effects.
    Args:
        pygame_surface (pygame.Surface): Surface to process.
        base_name (str): Base name for variant files.
    Returns:
        list[tuple[str, str]]: List of (name, path) pairs for variants.
    """
    if pygame_surface is None:
        raise ValueError("Invalid pygame_surface")
    variants = []
    try:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_file:
            pygame.image.save(pygame_surface, temp_file.name)
            with Image.open(temp_file.name) as img:
                original_path = f"{base_name}_original.png"
                img.save(original_path)
                variants.append(("Original", original_path))
                
                soft_img = img.filter(ImageFilter.SMOOTH_MORE)
                soft_path = f"{base_name}_soft.png"
                soft_img.save(soft_path)
                variants.append(("Soft", soft_path))
                
                color_enhancer = ImageEnhance.Color(img)
                vibrant_img = color_enhancer.enhance(1.3)
                vibrant_path = f"{base_name}_vibrant.png"
                vibrant_img.save(vibrant_path)
                variants.append(("Vibrant", vibrant_path))
                
                vintage_img = img.convert('RGB')
                vintage_enhancer = ImageEnhance.Color(vintage_img)
                vintage_img = vintage_enhancer.enhance(0.8)
                contrast_enhancer = ImageEnhance.Contrast(vintage_img)
                vintage_img = contrast_enhancer.enhance(1.1)
                vintage_path = f"{base_name}_vintage.png"
                vintage_img.save(vintage_path)
                variants.append(("Vintage", vintage_path))
            print(f"✅ Created {len(variants)} image variants")
        os.remove(temp_file.name)
        return variants
    except Exception as e:
        print(f"❌ Error creating image variants: {e}")
        return [("Original", "poem_art.png")]

def apply_background_blend(pygame_surface: pygame.Surface, background_path: str, blend_mode: str = 'overlay', opacity: float = 0.3) -> str:
    """Blend the generated art with a background image using different blend modes.
    Args:
        pygame_surface (pygame.Surface): Surface to blend.
        background_path (str): Path to background image.
        blend_mode (str): Blend mode ('overlay' or 'multiply').
        opacity (float): Opacity level (0.0 to 1.0).
    Returns:
        str: Path to the blended image.
    """
    if pygame_surface is None:
        raise ValueError("Invalid pygame_surface")
    try:
        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as temp_art_file:
            pygame.image.save(pygame_surface, temp_art_file.name)
            with Image.open(temp_art_file.name).convert('RGBA') as art_img, Image.open(background_path).convert('RGBA') as bg_img:
                bg_img = bg_img.resize(art_img.size, Image.Resampling.LANCZOS)
                bg_alpha = Image.new('RGBA', bg_img.size, (255, 255, 255, int(255 * opacity)))
                bg_img = Image.alpha_composite(bg_img, bg_alpha)
                if blend_mode == 'overlay':
                    blended = Image.alpha_composite(bg_img, art_img)
                elif blend_mode == 'multiply':
                    blended = Image.blend(bg_img.convert('RGB'), art_img.convert('RGB'), 0.7)
                    blended = blended.convert('RGBA')
                else:
                    blended = Image.alpha_composite(bg_img, art_img)
                output_path = "poem_art_blended.png"
                blended.save(output_path)
                print(f"🎨 Blended artwork saved as '{output_path}'")
        os.remove(temp_art_file.name)
        return output_path
    except Exception as e:
        print(f"❌ Error in background blending: {e}")
        return None

def optimize_for_sharing(image_path: str, max_size: tuple[int, int] = (1080, 1080), quality: int = 85) -> str:
    """Optimize image for social media sharing.
    Args:
        image_path (str): Path to the image.
        max_size (tuple[int, int]): Maximum dimensions.
        quality (int): JPEG quality (0-100).
    Returns:
        str: Path to the optimized image.
    """
    try:
        with Image.open(image_path) as img:
            img.thumbnail(max_size, Image.Resampling.LANCZOS)
            if img.mode in ('RGBA', 'LA', 'P'):
                background = Image.new('RGB', img.size, (255, 255, 255))
                if img.mode == 'P':
                    img = img.convert('RGBA')
                background.paste(img, mask=img.split()[-1] if 'A' in img.mode else None)
                img = background
            optimized_path = image_path.replace('.png', '_optimized.jpg')
            img.save(optimized_path, 'JPEG', quality=quality, optimize=True)
            print(f"📱 Optimized for sharing: {optimized_path}")
            return optimized_path
    except Exception as e:
        print(f"❌ Error optimizing image: {e}")
        return image_path
        