# Changelog
All notable changes to this project will be documented in this file.
This changelog follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.1] – 2025-06-19

### Added
- **CHANGELOG.md** - Project changelog following Keep a Changelog format
- **Enhanced Color Palettes** - Expanded from 4 to 8 vibrant colors per emotion
- **New Emotion Support** - Added dedicated "love" emotion with pink/red palette
- **Additional Shape Types** - Added hexagon and star shapes for more visual variety
- **Accent Color System** - Secondary color palettes for each emotion to increase variety
- **Decorative Particles** - 30 small colorful accent dots scattered throughout artwork
- **Shape Enhancement Effects** - Inner glows, borders, and transparency effects for depth
- **Multi-Color Gradient Backgrounds** - 3-color gradients replace simple 2-color fades

### Changed
- **Eliminated Grey Neutral Palette** - Replaced grey colors with vibrant blues, oranges, and purples
- **Increased Color Saturation** - All color values boosted for more vivid, less muted appearance
- **Enhanced Background Colors** - More colorful base backgrounds instead of dark/grey tones
- **Improved Text Rendering** - Added text shadows and used vibrant colors for better readability
- **Reduced Fog Effect** - Decreased from 60 to 15 particles with lower opacity (5-15 vs 15-35)
- **Disabled Fog by Default** - Changed default fog setting to `False` to preserve color vibrancy
- **Increased Minimum Elements** - Now generates at least 8 visual elements for richer composition
- **Better Element Positioning** - Improved spacing to avoid text area overlap

### Fixed
- **Dull/Greyscale Image Output** - Resolved primary issue causing washed-out, grey-toned artwork
- **Color Washing from Fog** - Heavy fog effect no longer desaturates the overall image
- **Limited Visual Variety** - More shapes, colors, and effects create more diverse artwork
- **Poor Color Distribution** - Better balance between main palette and accent colors

---

## [0.1.0] – 2025-06-01

### Initial Release
- **Poem Analysis Engine** - NLP-based emotion detection using TextBlob/VADER
- **Keyword Extraction** - Automatic extraction of key themes and imagery words using NLTK
- **Visual Mapping System** - Maps emotions and keywords to colors, shapes, and visual elements
- **Pygame Art Generation** - Creates abstract artwork using geometric shapes and gradients
- **Emotion-Based Color Palettes** - Joy, sadness, anger, fear, and neutral emotion support
- **Shape Variety** - Circle, square, and triangle shape generation
- **Text Integration** - Keywords displayed as text overlay on generated artwork
- **Local Processing** - Completely offline operation with no external API dependencies
- **Sample Content** - Included sample poems and output examples for demonstration
