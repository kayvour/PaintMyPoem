# PaintMyPoem
<p align="center">
  <a href="https://github.com/kayvour/PaintMyPoem/releases"><img src="https://img.shields.io/github/v/release/kayvour/PaintMyPoem?include_prereleases&sort=semver&style=flat-square&label=pre-release"></a>
  <a href="https://github.com/kayvour/PaintMyPoem/commits"><img src="https://img.shields.io/github/last-commit/kayvour/PaintMyPoem?style=flat-square"></a>
  <a href="https://github.com/kayvour/PaintMyPoem/issues"><img src="https://img.shields.io/github/issues/kayvour/PaintMyPoem?style=flat-square"></a>
  <a href="https://github.com/kayvour/PaintMyPoem/blob/main/LICENSE"><img src="https://img.shields.io/github/license/kayvour/PaintMyPoem?style=flat-square"></a>
  <img src="https://img.shields.io/badge/python-3.10+-blue?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/status-pre--release-orange?style=flat-square">
  <img src="https://img.shields.io/badge/theme-poetry🪷-ff69b4?style=flat-square">
</p>

---
📄 Full changelog → [`CHANGELOG.md`](./CHANGELOG.md)

A Python-based tool that transforms poems into abstract art using natural language processing and simple machine learning. Choose from multiple artistic styles to match your poem's mood!

![poem_art](https://github.com/user-attachments/assets/60fdc8a4-0eb6-441e-894c-03a7712a3f51)

---

## 📝 What It Does
- Analyzes the **mood and tone** of the poem using NLP and sentiment analysis
- Extracts **keywords** and emotional themes
- **🎨 NEW: Choose from 5 artistic styles** - Vibrant, Minimalist, Ethereal, Bold, or Organic
- Generates visual elements and color palettes to match the poem and selected style
- Uses Unsplash API to add backgrounds (optional)
- Creates abstract artwork using `pygame`, saves it as a `.png` image

---

## 🚀 Features

### Core Analysis
- Detects emotions using `TextBlob` or `VADER`
- Extracts key themes using `nltk`
- Matches emotion to color palettes
- Places visual elements (shapes, patterns, swirls) based on poem keywords

### 🎨 Artistic Styles *(NEW)*
- **🌟 Vibrant**: Bold colors, high contrast, energetic feel
- **🎯 Minimalist**: Clean, simple shapes with limited color palette  
- **✨ Ethereal**: Soft, dreamy with transparent layers and flowing shapes
- **💪 Bold**: High contrast, geometric shapes, strong visual impact
- **🌿 Organic**: Natural, flowing shapes with earth-inspired colors
- **🤖 Auto-select**: Automatically picks the best style based on poem emotion

### Visual Generation
- Generates original, soft, vibrant, and vintage art variants
- Complete background image management with download and caching
- Integration with Unsplash API for nature backgrounds (sky, forest, ocean, mountains, sunset)
- Style-specific particle effects and visual elements
- Dynamic element count and sizing based on selected style
- Runs completely locally

---

## ⚙️ Getting Started

1. **Clone the repository:**
```bash
git clone https://github.com/kayvour/paintmypoem.git
cd paintmypoem
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the script:**
```bash
python main.py
```

4. **Choose your experience:**
   - Select interactive mode for full features
   - Use demo mode with sample poems
   - Choose from 5 artistic styles or let the AI auto-select
   - Add backgrounds or use gradient-only mode

![terminal](https://github.com/user-attachments/assets/eeeff672-d7dc-4f21-953c-89e6fad80f7c)

---

## 🧠 How It Works

1. **Poem Analysis**: Sentiment analysis determines emotional tone (joy, sadness, anger, etc.)
2. **Keyword Extraction**: Key themes and visual words are identified (stars, rain, fire, etc.)
3. **🎨 Style Selection**: Choose your preferred artistic style or let AI auto-select
4. **Visual Planning**: Shapes, positions, and colors are mapped based on emotion, keywords, and style
5. **Background Selection**: Optional nature backgrounds from Unsplash API
6. **Art Generation**: Final artwork created using pygame with style-specific effects

### Style Examples
- **Minimalist + Sad Poem** = Clean circles, muted blues, few elements
- **Vibrant + Joyful Poem** = Bold stars, bright yellows/oranges, many elements  
- **Ethereal + Love Poem** = Soft circles, transparent pinks, flowing particles
- **Bold + Angry Poem** = Sharp triangles, high contrast reds, thick borders
- **Organic + Nature Poem** = Flowing shapes, earth tones, atmospheric effects

---

## 🧰 Built With
- 🐍 Python 3
- 🧠 Natural Language Toolkit (nltk)
- 💬 TextBlob / VADER Sentiment Analysis
- 🎮 pygame for art generation
- 🖼️ Unsplash API for background images
- 🎨 Custom Style Presets System

---

## 📌 Notes
- Works best with short to medium poems (4-12 lines)
- Poetic imagery and emotion words improve output quality
- Each style produces distinctly different visual results
- Background images enhance the final artwork but are optional
- The sample poems in the `/sample poems` folder were generated using ChatGPT for demonstration

---

## 🔮 Future Improvements
- ~~Add style presets~~ ✅ **COMPLETED**
- More detailed shape variations (fractals, splines, organic forms)
- GUI version for drag-and-drop poem uploads
- Custom style creator for advanced users
- Integration with more background sources
- Create an executable release (.exe) so users can run without installing Python
- Optimize and test for longer poems with chunking/batching
- Advanced sentiment analysis with transformer models
- Animation mode for moving visualizations
- Social media sharing integration

---

## 🤝 Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

For major changes, please open an issue to discuss first.

### Ideas for Contributors
- New artistic styles in `styles.py`
- Additional shape types in `art_generator.py`
- Enhanced keyword extraction patterns
- New background sources or generation methods

---

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**PaintMyPoem** celebrates the union of poetry and code. Whether you're a writer exploring visual expression or a coder fascinated by creative applications, this project helps bring verse to life through generative art! 🎨✨
