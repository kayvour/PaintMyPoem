import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import logging
from emotion_detector import detect_emotion, get_recommended_background_type, analyze_poem_mood
from keyword_extractor import extract_keywords, extract_visual_keywords, analyze_poem_themes
from visual_mapper import map_to_visuals
from art_generator import draw_art
from image_renderer import soften_image, create_image_variants
from styles import get_style_menu, auto_select_style, StylePresets
import random
import pygame

logging.basicConfig(level=logging.INFO, filename='paintmypoem.log')

def initialize_pygame(size=(800, 800)):
    """Initialize Pygame with given size and return the display surface."""
    pygame.init()
    return pygame.display.set_mode(size)

def cleanup_pygame():
    """Clean up Pygame resources."""
    pygame.quit()

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

    mood_analysis = analyze_poem_mood(poem)
    emotion = mood_analysis["emotion"]
    intensity = mood_analysis["intensity"]
    
    print(f"🎭 Detected Emotion: {emotion.title()} (intensity: {intensity:.2f})")
    if mood_analysis["mood_keywords"]:
        print(f"🏷️  Mood Keywords: {', '.join(mood_analysis['mood_keywords'])}")

    visual_keywords = extract_visual_keywords(poem, 5)
    theme_analysis = analyze_poem_themes(poem)
    
    print(f"📝 Visual Keywords: {visual_keywords}")
    print(f"🎯 Primary Theme: {theme_analysis['primary_theme'].title()}")

    recommended_bg = get_recommended_background_type(emotion)
    print(f"🌄 Recommended Background: {recommended_bg.title()}")
    
    style_choice = get_style_menu()
    
    if style_choice == "auto":
        selected_style = auto_select_style(emotion, visual_keywords)
        print(f"🤖 Auto-selected style: {selected_style.title()}")
    else:
        selected_style = style_choice
    
    print("\n" + "="*50)
    print("🎨 CREATING YOUR ARTWORK...")
    print("="*50)

    valid_choices = {'y', 'n', 'custom'}
    use_background = input(f"\nWould you like to use a {recommended_bg} background? (y/n/custom): ").lower().strip()
    while use_background not in valid_choices:
        print("❌ Invalid choice. Please enter 'y', 'n', or 'custom'.")
        use_background = input(f"Would you like to use a {recommended_bg} background? (y/n/custom): ").lower().strip()

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

    if background_type:
        background_opacity = max(0.2, 0.6 - (intensity * 0.3))
        print(f"🔧 Background opacity: {background_opacity:.1f}")

    visual_plan = map_to_visuals(emotion, visual_keywords)
    style_manager = StylePresets()
    visual_plan = style_manager.modify_visual_plan(visual_plan, selected_style)
    print(f"✨ Applied {selected_style.title()}")
    
    if theme_analysis['primary_theme'] == 'nature':
        visual_plan['fog'] = True
    
    print(f"🎨 Using Color Palette: {len(visual_plan['palette'])} colors")
    print(f"🔷 Generating {len(visual_plan['elements'])} visual elements...")

    try:
        screen = initialize_pygame()
        draw_art(visual_plan, background_type, background_opacity, size=(800, 800))
        print("✅ Base artwork generated successfully!")
        
        create_variants = input("\nCreate multiple versions? (y/n): ").lower().strip() == 'y'
        
        if create_variants:
            variants = create_image_variants(screen, f'poem_art_{selected_style}')
            print(f"✅ Created {len(variants)} variants:")
            for name, path in variants:
                print(f"   📸 {name}: {path}")
        else:
            final_path = soften_image(screen, f'poem_art_{selected_style}_final.png')
            print(f"✅ Final artwork saved: {final_path}")
    except Exception as e:
        print(f"❌ Error generating artwork: {e}")
    finally:
        cleanup_pygame()

    print("\n" + "="*50)
    print("🎉 ARTWORK COMPLETE!")
    print("="*50)
    print(f"Your visual poem has been created in {selected_style.title()} style!")
    print("Files generated:")
    print(f"  📄 poem_art.png - Main artwork")
    print(f"  ✨ poem_art_{selected_style}_final.png - Polished version")
    if create_variants:
        print("  🎨 Multiple variants in different styles")
    print("\nThank you for using PaintMyPoem! 🎨✨")

def interactive_demo():
    sample_poems = [
        {"title": "Morning Joy", "text": "Golden sunlight dances through the trees,\nBirds sing melodies on the gentle breeze,\nFlowers bloom in colors bright and true,\nEvery morning brings a world anew."},
        {"title": "Ocean Sadness", "text": "Waves crash against the lonely shore,\nMy heart aches like never before,\nDark clouds gather in the sky,\nSilent tears I cannot cry."},
        {"title": "Forest Love", "text": "In the forest deep and green,\nYour beauty is the fairest seen,\nHearts entwined like ancient trees,\nLove that flows like summer breeze."}
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
        lines = selected_poem['text'].split('\n')
        poem = '\n'.join(lines)
        emotion = detect_emotion(poem)
        visual_keywords = extract_visual_keywords(poem)
        selected_style = auto_select_style(emotion, visual_keywords)
        print(f"🤖 Auto-selected style for demo: {selected_style.title()}")
        visual_plan = map_to_visuals(emotion, visual_keywords)
        style_manager = StylePresets()
        visual_plan = style_manager.modify_visual_plan(visual_plan, selected_style)
        screen = initialize_pygame()
        draw_art(visual_plan, get_recommended_background_type(emotion), 0.4, size=(800, 800))
        soften_image(screen, f"{selected_poem['title'].lower().replace(' ', '_')}_{selected_style}_art.png")
        cleanup_pygame()
        print(f"✅ Demo artwork created for '{selected_poem['title']}' in {selected_style.title()} style!")
    elif choice == '4':
        main()
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
        