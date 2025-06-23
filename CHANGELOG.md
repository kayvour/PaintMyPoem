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
