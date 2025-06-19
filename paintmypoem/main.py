from emotion_detector import detect_emotion
from keyword_extractor import extract_keywords
from visual_mapper import map_to_visuals
from art_generator import draw_art

print("Enter your poem (end with an empty line):")

lines = []
while True:
    line = input()
    if line.strip() == "":
        break
    lines.append(line)

poem = "\n".join(lines)

emotion = detect_emotion(poem)
print(f"\nDetected Emotion: {emotion}")

keywords = extract_keywords(poem)
print(f"Extracted Keywords: {keywords}")

visual_plan = map_to_visuals(emotion, keywords)
print(f"Using palette: {visual_plan['palette']}")

# ✅ Final draw call
draw_art(visual_plan)

print("\n✅ Visual poem saved as 'poem_art.png'")
