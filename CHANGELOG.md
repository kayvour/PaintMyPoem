# 📖 Changelog
_All notable changes will be documented here following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and [Semantic Versioning](https://semver.org/spec/v2.0.0.html)._

---

## [0.2.0] – 2025-06-23

### Added
- **BackgroundManager** with caching, downloads, and fallback gradients
- **Unsplash API** for real nature backgrounds (sky, forest, ocean, etc.)
- **Background variants**: original, soft, vibrant, vintage
- **Post-processing**: smoothing and filters via PIL
- **Blending modes** to merge artwork with backgrounds
- **Social media optimization**: resizing & quality enhancement
- **Emotion detection**: improved with "love" category + intensity scoring
- **Theme-based visuals**: mood-based atmospheric adjustments
- **Demo mode**: quick generation from sample poems
- **Mood & theme analysis**: brightness, temperature, energy, keywords
- **Dynamic opacity** for backgrounds based on emotional depth

### Changed
- **Keyword extraction**: better stop word filtering & visual word focus
- **Text rendering**: semi-transparent backgrounds, improved readability
- **Backgrounds**: support both gradient & image-based
- **Art generation**: tighter background-foreground integration
- **Color logic**: more contrast-aware and theme-aware visuals

### Fixed
- **Download failures**: fallback handling for backgrounds
- **Text visibility**: shadows and overlays for better clarity
- **Memory & file management**: cleanup of temp/old files
- **Image pipeline**: robust post-processing error handling

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
- `CHANGELOG.md` using Keep a Changelog format
- **"Love" emotion support** with pink/red palettes
- **Expanded color palettes**: 8 colors per emotion
- **New shapes**: hexagon and star
- **Accent system**: secondary emotion colors
- **Decorative particles**: 30 color accent dots
- **Shape effects**: glows, borders, transparency
- **3-color gradient backgrounds**

### Changed
- **Neutral palette**: grey replaced with vibrant hues
- **Color saturation**: boosted vibrancy overall
- **Text rendering**: added shadows, vibrant font colors
- **Fog**: reduced count, opacity, and disabled by default
- **Visual richness**: minimum of 8 elements, better layout

### Fixed
- **Grey/dull outputs**: resolved primary washout issue
- **Fog desaturation**: no longer drains image color
- **Visual variety**: more diverse shapes/effects
- **Color balance**: improved main vs. accent distribution

---

## [0.1.0] – 2025-06-01

### Initial Release
- **Poem Analysis Engine** using TextBlob/VADER
- **Keyword Extraction** via NLTK
- **Visual Mapping** of emotions/keywords to visuals
- **Pygame Artwork Generator** with shapes & gradients
- **Emotion Color Palettes**: joy, sadness, anger, fear, neutral
- **Shape types**: circle, square, triangle
- **Text Overlay**: keywords shown on visuals
- **Offline Support**: no external dependencies
- **Sample Content**: poems + demo outputs
