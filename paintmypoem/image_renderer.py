from PIL import Image, ImageFilter, ImageEnhance
import pygame
import os

def soften_image(pygame_surface, output_path='poem_art_final.png'):
    """
    Apply post-processing effects to the generated artwork
    """
    try:
        # Save pygame surface to temp file
        temp_path = "temp_render.png"
        pygame.image.save(pygame_surface, temp_path)
        
        # Open with PIL for processing
        img = Image.open(temp_path)
        
        # Apply smoothing filter
        img = img.filter(ImageFilter.SMOOTH_MORE)
        
        # Optional: Enhance colors slightly
        enhancer = ImageEnhance.Color(img)
        img = enhancer.enhance(1.1)  # Slight color boost
        
        # Save final image
        img.save(output_path, quality=95)
        print(f"🖼️ Final polished image saved as '{output_path}'")
        
        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
        return output_path
        
    except Exception as e:
        print(f"❌ Error in image post-processing: {e}")
        # Fallback: just save the pygame surface directly
        pygame.image.save(pygame_surface, output_path)
        print(f"🖼️ Image saved as '{output_path}' (without post-processing)")
        return output_path

def create_image_variants(pygame_surface, base_name='poem_art'):
    """
    Create multiple versions of the artwork with different effects
    """
    variants = []
    
    try:
        # Save original pygame surface
        temp_path = "temp_variants.png"
        pygame.image.save(pygame_surface, temp_path)
        img = Image.open(temp_path)
        
        # Original version
        original_path = f"{base_name}_original.png"
        img.save(original_path)
        variants.append(("Original", original_path))
        
        # Soft version
        soft_img = img.filter(ImageFilter.SMOOTH_MORE)
        soft_path = f"{base_name}_soft.png"
        soft_img.save(soft_path)
        variants.append(("Soft", soft_path))
        
        # Enhanced colors version
        color_enhancer = ImageEnhance.Color(img)
        vibrant_img = color_enhancer.enhance(1.3)
        vibrant_path = f"{base_name}_vibrant.png"
        vibrant_img.save(vibrant_path)
        variants.append(("Vibrant", vibrant_path))
        
        # Vintage version
        vintage_img = img.convert('RGB')
        vintage_enhancer = ImageEnhance.Color(vintage_img)
        vintage_img = vintage_enhancer.enhance(0.8)
        contrast_enhancer = ImageEnhance.Contrast(vintage_img)
        vintage_img = contrast_enhancer.enhance(1.1)
        vintage_path = f"{base_name}_vintage.png"
        vintage_img.save(vintage_path)
        variants.append(("Vintage", vintage_path))
        
        print(f"✅ Created {len(variants)} image variants")
        
        # Clean up temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)
            
        return variants
        
    except Exception as e:
        print(f"❌ Error creating image variants: {e}")
        return [("Original", "poem_art.png")]

def apply_background_blend(pygame_surface, background_path, blend_mode='overlay', opacity=0.3):
    """
    Blend the generated art with a background image using different blend modes
    """
    try:
        # Save pygame surface to temp file
        temp_art_path = "temp_art_blend.png"
        pygame.image.save(pygame_surface, temp_art_path)
        
        # Open both images
        art_img = Image.open(temp_art_path).convert('RGBA')
        bg_img = Image.open(background_path).convert('RGBA')
        
        # Resize background to match art dimensions
        bg_img = bg_img.resize(art_img.size, Image.Resampling.LANCZOS)
        
        # Apply opacity to background
        bg_alpha = Image.new('RGBA', bg_img.size, (255, 255, 255, int(255 * opacity)))
        bg_img = Image.alpha_composite(bg_img, bg_alpha)
        
        # Blend the images
        if blend_mode == 'overlay':
            # Simple alpha composite
            blended = Image.alpha_composite(bg_img, art_img)
        elif blend_mode == 'multiply':
            # Darker blend
            blended = Image.blend(bg_img.convert('RGB'), art_img.convert('RGB'), 0.7)
            blended = blended.convert('RGBA')
        else:
            # Default to overlay
            blended = Image.alpha_composite(bg_img, art_img)
        
        # Save blended result
        output_path = "poem_art_blended.png"
        blended.save(output_path)
        print(f"🎨 Blended artwork saved as '{output_path}'")
        
        # Clean up temp file
        if os.path.exists(temp_art_path):
            os.remove(temp_art_path)
            
        return output_path
        
    except Exception as e:
        print(f"❌ Error in background blending: {e}")
        return None

def optimize_for_sharing(image_path, max_size=(1080, 1080), quality=85):
    """
    Optimize image for social media sharing
    """
    try:
        img = Image.open(image_path)
        
        # Resize if needed
        img.thumbnail(max_size, Image.Resampling.LANCZOS)
        
        # Convert to RGB if needed (for JPEG)
        if img.mode in ('RGBA', 'LA', 'P'):
            # Create white background
            background = Image.new('RGB', img.size, (255, 255, 255))
            if img.mode == 'P':
                img = img.convert('RGBA')
            background.paste(img, mask=img.split()[-1] if 'A' in img.mode else None)
            img = background
        
        # Save optimized version
        optimized_path = image_path.replace('.png', '_optimized.jpg')
        img.save(optimized_path, 'JPEG', quality=quality, optimize=True)
        
        print(f"📱 Optimized for sharing: {optimized_path}")
        return optimized_path
        
    except Exception as e:
        print(f"❌ Error optimizing image: {e}")
        return image_path
        