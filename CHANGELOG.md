# 📖 Changelog
_All notable changes will be documented here following the [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) format and [Semantic Versioning](https://semver.org/spec/v2.0.0.html)._

---

## [0.4.0] – 2025-08-28

### Added
- **Logging System** - Added file-based logging in `main.py` to track execution details and errors.
- **Type Hints** - Implemented type annotations across all modules for better code clarity and IDE support.
- **Input Validation** - Added comprehensive checks for user inputs and function parameters in all files.
- **Resource Cleanup** - Introduced `tempfile.NamedTemporaryFile` for automatic cleanup of temporary files in `image_renderer.py`.
- **Retry Logic** - Added 3-attempt retry mechanism for background downloads in `background_manager.py`.
- **Pygame Context Manager** - Added `with` statement for Pygame initialization and cleanup in `art_generator.py` and `main.py`.

### Changed
- **Art Generation Pipeline** - Refactored Pygame initialization to a helper function `initialize_pygame` in `main.py`.
- **Background Management** - Enhanced `prepare_background_surface` with context manager for PIL image handling in `background_manager.py`.
- **Error Handling** - Improved exception handling with specific error messages and fallbacks across all modules.
- **Style Application** - Updated `apply_style_to_palette` in `styles.py` to include bounds checking for color values.
- **Input Workflow** - Enhanced `main.py` input validation for background selection with a retry loop.

### Fixed
- **Resource Leaks** - Resolved potential memory leaks from repeated Pygame initialization in `art_generator.py`.
- **Permission Issues** - Added handling for directory permission errors in `background_manager.py` cleanup.
- **Input Errors** - Fixed invalid input handling in `main.py` to ensure valid background choices.
- **Image Processing** - Ensured robust surface validation and fallback in `image_renderer.py`.

### Enhanced
- **Code Maintainability** - Expanded docstrings with detailed parameter and return descriptions in all files.
- **Robustness** - Improved stability with better error recovery and logging for debugging.
- **Flexibility** - Added configurable size parameter to `draw_art` in `art_generator.py`.

---

## [0.3.0] – 2025-08-03

### Added
- **🎨 Style Presets System** - Complete artistic style management with 5 predefined styles
- **Vibrant Style** - Bold colors, high contrast, energetic feel with increased element count
- **Minimalist Style** - Clean, simple shapes with limited color palette and reduced visual noise
- **Ethereal Style** - Soft, dreamy aesthetic with transparent layers and flowing particles
- **Bold Style** - High contrast geometric shapes with thick borders and strong visual impact
- **Organic Style** - Natural, flowing shapes with earth-inspired colors and atmospheric effects
- **Auto-Style Selection** - Intelligent style selection based on poem emotion and theme analysis
- **Style-Specific Visual Effects** - Customized particle counts, gradient complexity, and shape preferences per style
- **Dynamic Element Scaling** - Element count and sizing automatically adjusted based on selected style
- **Enhanced Shape Rendering** - Style-aware shape drawing with borders, glows, and transparency effects
- **Style Configuration System** - Extensible framework for adding new artistic styles
- **Interactive Style Menu** - User-friendly style selection with descriptions and auto-select option

### Changed
- **Main Interface** - Added comprehensive style selection workflow after poem analysis
- **Art Generation Pipeline** - Integrated style modifications throughout the visual creation process
- **Color Processing** - Style-specific saturation and intensity adjustments for palettes
- **Text Rendering** - Style-aware font sizing and contrast adjustments
- **Background Integration** - Style-specific gradient complexity and overlay effects
- **File Naming** - Output files now include style name for better organization
- **Demo Mode** - Auto-selects appropriate styles for sample poems

### Enhanced
- **Visual Variety** - Each style produces distinctly different artistic results from the same poem
- **User Control** - Immediate visual customization without complex parameter adjustment
- **Artistic Coherence** - Style presets ensure visually harmonious results
- **Extensibility** - Easy framework for adding custom styles and modifications

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
