"""
Style Presets System for PaintMyPoem
Provides predefined visual styles that modify color palettes, shapes, and effects
"""

import random

class StylePresets:
    """Manages different visual styles for poem artwork generation"""
    
    def __init__(self):
        self.styles = {
            "vibrant": {
                "name": "Vibrant",
                "description": "Bold colors, high contrast, energetic feel",
                "color_intensity": 1.2,
                "saturation_boost": 50,
                "num_elements_multiplier": 1.5,
                "shape_preferences": ["circle", "star", "hexagon"],
                "size_range": (40, 140),
                "alpha_range": (220, 255),
                "particle_count": 40,
                "fog_enabled": False,
                "gradient_complexity": 3
            },
            "minimalist": {
                "name": "Minimalist", 
                "description": "Clean, simple shapes with limited color palette",
                "color_intensity": 0.8,
                "saturation_boost": -30,
                "num_elements_multiplier": 0.6,
                "shape_preferences": ["circle", "square"],
                "size_range": (60, 100),
                "alpha_range": (200, 240),
                "particle_count": 8,
                "fog_enabled": False,
                "gradient_complexity": 2
            },
            "ethereal": {
                "name": "Ethereal",
                "description": "Soft, dreamy with transparent layers and flowing shapes",
                "color_intensity": 0.9,
                "saturation_boost": 20,
                "num_elements_multiplier": 1.0,
                "shape_preferences": ["circle", "triangle"],
                "size_range": (30, 120),
                "alpha_range": (120, 200),
                "particle_count": 60,
                "fog_enabled": True,
                "gradient_complexity": 3
            },
            "bold": {
                "name": "Bold",
                "description": "High contrast, geometric shapes, strong visual impact",
                "color_intensity": 1.1,
                "saturation_boost": 40,
                "num_elements_multiplier": 1.2,
                "shape_preferences": ["square", "triangle", "hexagon"],
                "size_range": (50, 130),
                "alpha_range": (240, 255),
                "particle_count": 20,
                "fog_enabled": False,
                "gradient_complexity": 2
            },
            "organic": {
                "name": "Organic",
                "description": "Natural, flowing shapes with earth-inspired colors",
                "color_intensity": 0.95,
                "saturation_boost": 10,
                "num_elements_multiplier": 1.1,
                "shape_preferences": ["circle", "star"],
                "size_range": (35, 110),
                "alpha_range": (180, 230),
                "particle_count": 35,
                "fog_enabled": True,
                "gradient_complexity": 3
            }
        }
    
    def get_available_styles(self):
        """Return list of available style names and descriptions"""
        return [(name, info["name"], info["description"]) 
                for name, info in self.styles.items()]
    
    def apply_style_to_palette(self, base_palette, style_name, emotion):
        """Apply style modifications to the base color palette"""
        if style_name not in self.styles:
            return base_palette
            
        style = self.styles[style_name]
        modified_palette = []
        
        for color in base_palette:
            r, g, b = color
            
            # Apply intensity multiplier
            intensity = style["color_intensity"]
            r = min(255, int(r * intensity))
            g = min(255, int(g * intensity))
            b = min(255, int(b * intensity))
            
            # Apply saturation boost/reduction
            sat_boost = style["saturation_boost"]
            
            # Convert to HSV-like adjustment
            max_val = max(r, g, b)
            min_val = min(r, g, b)
            
            if max_val != min_val:
                # Calculate saturation adjustment
                if sat_boost > 0:
                    # Increase saturation
                    factor = 1 + (sat_boost / 100)
                    r = min(255, int(min_val + (r - min_val) * factor))
                    g = min(255, int(min_val + (g - min_val) * factor))
                    b = min(255, int(min_val + (b - min_val) * factor))
                else:
                    # Decrease saturation (move toward gray)
                    factor = 1 + (sat_boost / 100)  # This will be < 1
                    avg = (r + g + b) // 3
                    r = int(r * factor + avg * (1 - factor))
                    g = int(g * factor + avg * (1 - factor))
                    b = int(b * factor + avg * (1 - factor))
            
            modified_palette.append((r, g, b))
        
        return modified_palette
    
    def get_style_config(self, style_name):
        """Get the complete style configuration"""
        return self.styles.get(style_name, self.styles["vibrant"])
    
    def modify_visual_plan(self, visual_plan, style_name):
        """Apply style to a complete visual plan"""
        if style_name not in self.styles:
            return visual_plan
            
        style = self.styles[style_name]
        
        # Modify color palette
        visual_plan["palette"] = self.apply_style_to_palette(
            visual_plan["palette"], style_name, visual_plan.get("emotion", "neutral")
        )
        
        # Modify accent colors if they exist
        if "accent_colors" in visual_plan:
            visual_plan["accent_colors"] = self.apply_style_to_palette(
                visual_plan["accent_colors"], style_name, visual_plan.get("emotion", "neutral")
            )
        
        # Adjust number of elements
        current_count = len(visual_plan["elements"])
        new_count = int(current_count * style["num_elements_multiplier"])
        
        if new_count < current_count:
            # Remove elements (keep the first ones which are usually based on keywords)
            visual_plan["elements"] = visual_plan["elements"][:new_count]
        elif new_count > current_count:
            # Add more elements by duplicating and modifying existing ones
            additional_needed = new_count - current_count
            base_elements = visual_plan["elements"].copy()
            
            for i in range(additional_needed):
                if base_elements:
                    # Copy a random existing element and modify it
                    base_element = random.choice(base_elements).copy()
                    base_element["position"] = (
                        random.randint(80, 720),
                        random.randint(80, 600)
                    )
                    base_element["size"] = random.randint(*style["size_range"])
                    base_element["alpha"] = random.randint(*style["alpha_range"])
                    visual_plan["elements"].append(base_element)
        
        # Modify existing elements according to style
        for element in visual_plan["elements"]:
            # Update shape preferences
            if element["type"] not in style["shape_preferences"]:
                element["type"] = random.choice(style["shape_preferences"])
            
            # Update size and alpha ranges
            element["size"] = max(
                style["size_range"][0],
                min(style["size_range"][1], element.get("size", 60))
            )
            element["alpha"] = random.randint(*style["alpha_range"])
        
        # Apply style-specific effects
        visual_plan["fog"] = style["fog_enabled"]
        visual_plan["particle_count"] = style["particle_count"]
        visual_plan["gradient_complexity"] = style["gradient_complexity"]
        visual_plan["style_name"] = style_name
        
        return visual_plan

def get_style_menu():
    """Display style selection menu and return chosen style"""
    preset_manager = StylePresets()
    styles = preset_manager.get_available_styles()
    
    print("\n" + "="*50)
    print("🎨 CHOOSE YOUR ARTISTIC STYLE")
    print("="*50)
    
    for i, (style_id, name, description) in enumerate(styles, 1):
        print(f"{i}. {name}")
        print(f"   {description}")
        print()
    
    print(f"{len(styles) + 1}. Auto-select based on poem emotion")
    print()
    
    while True:
        try:
            choice = input(f"Enter your choice (1-{len(styles) + 1}): ").strip()
            
            if choice == str(len(styles) + 1):
                return "auto"
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(styles):
                style_id = styles[choice_num - 1][0]
                style_name = styles[choice_num - 1][1]
                print(f"✨ Selected: {style_name}")
                return style_id
            else:
                print(f"❌ Please enter a number between 1 and {len(styles) + 1}")
                
        except ValueError:
            print("❌ Please enter a valid number")

def auto_select_style(emotion, keywords):
    """Automatically select the best style based on poem emotion and keywords"""
    # Style mappings based on emotion
    emotion_styles = {
        "joy": "vibrant",
        "happy": "vibrant", 
        "love": "ethereal",
        "sadness": "minimalist",
        "sad": "minimalist",
        "anger": "bold",
        "fear": "organic",
        "neutral": "organic"
    }
    
    # Check for nature keywords that might suggest organic style
    nature_keywords = ["tree", "flower", "forest", "ocean", "mountain", "river", "sky", "earth"]
    has_nature = any(keyword in " ".join(keywords).lower() for keyword in nature_keywords)
    
    if has_nature and emotion in ["neutral", "love", "sadness"]:
        return "organic"
    
    return emotion_styles.get(emotion, "organic")
    