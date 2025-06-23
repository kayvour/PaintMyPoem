import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from emotion_detector import detect_emotion, get_recommended_background_type, analyze_poem_mood
from keyword_extractor import extract_keywords, extract_visual_keywords, analyze_poem_themes
from visual_mapper import map_to_visuals
from art_generator import draw_art
from image_renderer import soften_image, create_image_variants
import random

def main():
    print("🎨 Welcome to PaintMyPoem! 🎨")
    print("Enter your poem (end with an empty line):")
    print("-" * 40)

    lines = []
    while True:
        line = input()
        if line.strip() == "":
            break
        lines.append(line)

    if not lines:
        print("❌ No poem entered. Please try again.")
        return

    poem = "\n".join(lines)
    print("\n" + "="*50)
    print("🔍 ANALYZING YOUR POEM...")
    print("="*50)

    # Enhanced emotion analysis
    mood_analysis = analyze_poem_mood(poem)
    emotion = mood_analysis["emotion"]
    intensity = mood_analysis["intensity"]
    
    print(f"🎭 Detected Emotion: {emotion.title()} (intensity: {intensity:.2f})")
    
    if mood_analysis["mood_keywords"]:
        print(f"🏷️  Mood Keywords: {', '.join(mood_analysis['mood_keywords'])}")

    # Enhanced keyword extraction
    visual_keywords = extract_visual_keywords(poem, 5)
    theme_analysis = analyze_poem_themes(poem)
    
    print(f"📝 Visual Keywords: {visual_keywords}")
    print(f"🎯 Primary Theme: {theme_analysis['primary_theme'].title()}")

    # Background selection
    recommended_bg = get_recommended_background_type(emotion)
    print(f"🌄 Recommended Background: {recommended_bg.title()}")
    
    print("\n" + "="*50)
    print("🎨 CREATING YOUR ARTWORK...")
    print("="*50)

    # Ask user about background preference
    use_background = input(f"\nWould you like to use a {recommended_bg} background? (y/n/custom): ").lower().strip()
    
    background_type = None
    background_opacity = 0.4
    
    if use_background == 'y':
        background_type = recommended_bg
        print(f"🌅 Using {recommended_bg} background...")
    elif use_background == 'custom':
        print("Available backgrounds: sky, forest, ocean, mountains, sunset")
        custom_bg = input("Enter background type: ").lower().strip()
        if custom_bg in ['sky', 'forest', 'ocean', 'mountains', 'sunset']:
            background_type = custom_bg
            print(f"🌅 Using {custom_bg} background...")
        else:
            print("⚠️ Invalid background type, using gradient instead")
    else:
        print("🎨 Using gradient background...")

    # Adjust background opacity based on emotion intensity
    if background_type:
        # Higher intensity emotions get more transparent backgrounds to let art show through
        background_opacity = max(0.2, 0.6 - (intensity * 0.3))
        print(f"🔧 Background opacity: {background_opacity:.1f}")

    # Generate visual plan
    visual_plan = map_to_visuals(emotion, visual_keywords)
    
    # Add theme-based enhancements
    if theme_analysis['primary_theme'] == 'nature':
        visual_plan['fog'] = True  # Add atmospheric effect for nature themes
    
    print(f"🎨 Using Color Palette: {len(visual_plan['palette'])} colors")
    print(f"🔷 Generating {len(visual_plan['elements'])} visual elements...")

    # Generate the artwork
    try:
        pygame_surface = draw_art(visual_plan, background_type, background_opacity)
        print("✅ Base artwork generated successfully!")
        
        # Post-processing options
        create_variants = input("\nCreate multiple versions? (y/n): ").lower().strip() == 'y'
        
        if create_variants:
            variants = create_image_variants(pygame_surface, 'poem_art')
            print(f"✅ Created {len(variants)} variants:")
            for name, path in variants:
                print(f"   📸 {name}: {path}")
        else:
            # Just create the polished version
            final_path = soften_image(pygame_surface, 'poem_art_final.png')
            print(f"✅ Final artwork saved: {final_path}")
        
    except Exception as e:
        print(f"❌ Error generating artwork: {e}")
        return

    print("\n" + "="*50)
    print("🎉 ARTWORK COMPLETE!")
    print("="*50)
    print("Your visual poem has been created and saved!")
    print("Files generated:")
    print("  📄 poem_art.png - Main artwork")
    print("  ✨ poem_art_final.png - Polished version")
    
    if create_variants:
        print("  🎨 Multiple variants in different styles")
    
    print("\nThank you for using PaintMyPoem! 🎨✨")

def interactive_demo():
    """
    Run an interactive demo with sample poems
    """
    sample_poems = [
        {
            "title": "Morning Joy",
            "text": "Golden sunlight dances through the trees,\nBirds sing melodies on the gentle breeze,\nFlowers bloom in colors bright and true,\nEvery morning brings a world anew."
        },
        {
            "title": "Ocean Sadness", 
            "text": "Waves crash against the lonely shore,\nMy heart aches like never before,\nDark clouds gather in the sky,\nSilent tears I cannot cry."
        },
        {
            "title": "Forest Love",
            "text": "In the forest deep and green,\nYour beauty is the fairest seen,\nHearts entwined like ancient trees,\nLove that flows like summer breeze."
        }
    ]
    
    print("🎭 PaintMyPoem Interactive Demo")
    print("Choose a sample poem or enter your own:")
    print()
    
    for i, poem in enumerate(sample_poems, 1):
        print(f"{i}. {poem['title']}")
    print("4. Enter my own poem")
    
    choice = input("\nEnter your choice (1-4): ").strip()
    
    if choice in ['1', '2', '3']:
        selected_poem = sample_poems[int(choice) - 1]
        print(f"\n📝 Selected: {selected_poem['title']}")
        print("-" * 40)
        print(selected_poem['text'])
        print("-" * 40)
        
        # Process the selected poem
        lines = selected_poem['text'].split('\n')
        poem = '\n'.join(lines)
        
        # Continue with normal processing...
        emotion = detect_emotion(poem)
        visual_keywords = extract_visual_keywords(poem)
        visual_plan = map_to_visuals(emotion, visual_keywords)
        
        # Quick generation without user prompts for demo
        background_type = get_recommended_background_type(emotion)
        pygame_surface = draw_art(visual_plan, background_type, 0.4)
        soften_image(pygame_surface, f"{selected_poem['title'].lower().replace(' ', '_')}_art.png")
        
        print(f"✅ Demo artwork created for '{selected_poem['title']}'!")
        
    elif choice == '4':
        main()  # Run normal interactive mode
    else:
        print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    print("🎨 PaintMyPoem - Transform your poetry into visual art!")
    print()
    
    mode = input("Choose mode:\n1. Interactive (full features)\n2. Demo (sample poems)\nEnter choice (1-2): ").strip()
    
    if mode == '2':
        interactive_demo()
    else:
        main()
        