# Changelog
All notable changes to this project will be documented in this file.
This changelog follows the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.2.0] – 2025-06-23

### Added
- **BackgroundManager System** - Complete background image management with download and caching
- **Real Background Images** - Integration with Unsplash API for nature backgrounds (sky, forest, ocean, mountains, sunset)
- **Background Caching** - Local storage of downloaded backgrounds to reduce API calls
- **Fallback Background Generation** - Automatic gradient backgrounds when downloads fail
- **Post-Processing Effects** - Image smoothing and enhancement filters using PIL
- **Multiple Image Variants** - Generate original, soft, vibrant, and vintage versions of artwork
- **Background Blending** - Advanced blend modes for combining artwork with background images
- **Social Media Optimization** - Automatic image resizing and optimization for sharing
- **Enhanced Emotion Detection** - More sophisticated emotion mapping with love category support
- **Emotion Intensity Analysis** - Intensity scoring to adjust visual effects dynamically
- **Theme-Based Enhancement** - Atmospheric effects based on detected poem themes
- **Interactive Demo Mode** - Sample poems with quick generation for demonstration
- **Comprehensive Mood Analysis** - Raw sentiment scores and mood keyword extraction
- **Background Opacity Control** - Dynamic opacity adjustment based on emotion intensity
- **Visual Keywords Extraction** - Specialized keyword extraction for visual representation
- **Theme Analysis System** - Detection of major themes (nature, love, time, journey, conflict)
- **Mood Descriptors** - Extraction of brightness, temperature, and energy descriptors

### Changed
- **Enhanced Keyword Extraction** - Improved filtering with expanded stop words and visual word prioritization
- **Background Integration** - Artwork now supports both gradient and photographic backgrounds
- **Improved Text Rendering** - Semi-transparent background for better text readability over backgrounds
- **Dynamic Background Selection** - Emotion-based background recommendations with user choice
- **Enhanced Art Generation** - Better integration between background and foreground elements
- **Expanded Visual Mapping** - Theme-aware visual element generation
- **Improved Color Handling** - Better contrast and brightness adjustment for background compatibility

### Fixed
- **Background Download Reliability** - Proper error handling and fallback systems
- **Memory Management** - Automatic cleanup of temporary and old background files
- **Image Processing Stability** - Robust error handling in post-processing pipeline
- **Text Visibility Issues** - Enhanced text rendering with shadows and background overlays
- **File Management** - Better temporary file cleanup and organization

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
