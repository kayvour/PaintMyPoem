import pygame
import os
import random
from PIL import Image, ImageEnhance
import requests
from io import BytesIO

class BackgroundManager:
    def __init__(self):
        self.background_types = {
            "sky": {
                "urls": [
                    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1419242902214-272b3f66ee7a?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1517685352821-92cf88aee5a5?w=800&h=800&fit=crop"
                ],
                "fallback_color": (135, 206, 235)  # Sky blue
            },
            "forest": {
                "urls": [
                    "https://images.unsplash.com/photo-1441974231531-c6227db76b6e?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1518837695005-2083093ee35b?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1574263867128-a3d5c1b1deaa?w=800&h=800&fit=crop"
                ],
                "fallback_color": (34, 139, 34)  # Forest green
            },
            "ocean": {
                "urls": [
                    "https://images.unsplash.com/photo-1439066615861-d1af74d74000?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1483683804023-6ccdb62f86ef?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1505142468610-359e7d316be0?w=800&h=800&fit=crop"
                ],
                "fallback_color": (0, 119, 190)  # Ocean blue
            },
            "mountains": {
                "urls": [
                    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1464822759844-d150ba4ba2b8?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1506197603052-3cc9c3a201bd?w=800&h=800&fit=crop"
                ],
                "fallback_color": (139, 137, 137)  # Mountain grey
            },
            "sunset": {
                "urls": [
                    "https://images.unsplash.com/photo-1495616811223-4d98c6e9c869?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1519904981063-b0cf448d479e?w=800&h=800&fit=crop",
                    "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800&h=800&fit=crop"
                ],
                "fallback_color": (255, 94, 77)  # Sunset orange
            }
        }
        
        # Create backgrounds directory if it doesn't exist
        os.makedirs("backgrounds", exist_ok=True)

    def download_background(self, bg_type):
        """Download a random background image of the specified type"""
        if bg_type not in self.background_types:
            return None
            
        bg_info = self.background_types[bg_type]
        url = random.choice(bg_info["urls"])
        
        try:
            print(f"🌅 Downloading {bg_type} background...")
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                filename = f"backgrounds/{bg_type}_{random.randint(1000, 9999)}.jpg"
                with open(filename, 'wb') as f:
                    f.write(response.content)
                print(f"✅ Background saved as {filename}")
                return filename
            else:
                print(f"❌ Failed to download background: HTTP {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Error downloading background: {e}")
            return None

    def create_fallback_background(self, bg_type, size=(800, 800)):
        """Create a simple gradient background if download fails"""
        if bg_type not in self.background_types:
            bg_type = "sky"
            
        base_color = self.background_types[bg_type]["fallback_color"]
        
        # Create PIL image with gradient
        img = Image.new('RGB', size, base_color)
        
        # Add some texture/gradient
        for y in range(size[1]):
            # Create subtle gradient effect
            ratio = y / size[1]
            new_color = tuple(max(0, min(255, int(c * (1 - ratio * 0.3)))) for c in base_color)
            for x in range(size[0]):
                img.putpixel((x, y), new_color)
        
        filename = f"backgrounds/fallback_{bg_type}.jpg"
        img.save(filename)
        print(f"🎨 Created fallback {bg_type} background")
        return filename

    def get_background_image(self, bg_type="sky", use_cache=True):
        """Get a background image, either from cache or download new one"""
        # Check if we have cached backgrounds
        if use_cache:
            cache_files = [f for f in os.listdir("backgrounds") if f.startswith(bg_type)]
            if cache_files:
                cached_file = f"backgrounds/{random.choice(cache_files)}"
                print(f"📁 Using cached {bg_type} background: {cached_file}")
                return cached_file
        
        # Try to download new background
        downloaded = self.download_background(bg_type)
        if downloaded:
            return downloaded
        
        # Fall back to generated background
        return self.create_fallback_background(bg_type)

    def prepare_background_surface(self, bg_path, opacity=0.6, size=(800, 800)):
        """Convert background image to pygame surface with opacity"""
        try:
            # Load and resize image
            pil_img = Image.open(bg_path)
            pil_img = pil_img.resize(size, Image.Resampling.LANCZOS)
            
            # Adjust opacity
            if pil_img.mode != 'RGBA':
                pil_img = pil_img.convert('RGBA')
            
            # Apply opacity
            enhancer = ImageEnhance.Brightness(pil_img)
            pil_img = enhancer.enhance(0.7)  # Darken slightly for better text readability
            
            # Convert to pygame surface
            img_string = pil_img.tobytes()
            pygame_surface = pygame.image.fromstring(img_string, size, 'RGBA')
            
            # Apply additional opacity
            opacity_surface = pygame.Surface(size, pygame.SRCALPHA)
            opacity_surface.fill((255, 255, 255, int(255 * opacity)))
            pygame_surface.blit(opacity_surface, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
            
            return pygame_surface
            
        except Exception as e:
            print(f"❌ Error preparing background surface: {e}")
            # Return a simple colored surface as fallback
            fallback_surface = pygame.Surface(size)
            fallback_surface.fill((100, 100, 150))  # Dark blue fallback
            return fallback_surface

    def get_recommended_background(self, emotion):
        """Suggest background type based on detected emotion"""
        emotion_backgrounds = {
            "joy": ["sunset", "sky", "mountains"],
            "happy": ["sunset", "sky", "mountains"],
            "sadness": ["ocean", "forest", "mountains"],
            "sad": ["ocean", "forest", "mountains"],
            "anger": ["mountains", "sunset", "forest"],
            "fear": ["forest", "mountains", "ocean"],
            "love": ["sunset", "sky", "ocean"],
            "neutral": ["sky", "forest", "ocean", "mountains"]
        }
        
        recommended = emotion_backgrounds.get(emotion, ["sky", "forest", "ocean"])
        return random.choice(recommended)

    def cleanup_old_backgrounds(self, keep_recent=5):
        """Clean up old background files to save space"""
        try:
            bg_files = []
            for f in os.listdir("backgrounds"):
                if f.endswith(('.jpg', '.png')):
                    filepath = os.path.join("backgrounds", f)
                    bg_files.append((filepath, os.path.getctime(filepath)))
            
            # Sort by creation time, newest first
            bg_files.sort(key=lambda x: x[1], reverse=True)
            
            # Delete old files beyond keep_recent count
            for filepath, _ in bg_files[keep_recent:]:
                os.remove(filepath)
                print(f"🗑️ Cleaned up old background: {os.path.basename(filepath)}")
                
        except Exception as e:
            print(f"⚠️ Error during cleanup: {e}")
            