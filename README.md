# PaintMyPoem 🖌️

A Python-based tool that transforms poems into abstract art using natural language processing and simple machine learning.

![poem_art](https://github.com/user-attachments/assets/60fdc8a4-0eb6-441e-894c-03a7712a3f51)
---

## 📝 What It Does
- Analyzes the **mood and tone** of the poem using NLP and sentiment analysis
- Extracts **keywords** and emotional themes
- Generates visual elements and color palettes to match the poem.
- Creates abstract artwork using `pygame`, saves it as a `.png` image.

---

## 🚀 Features
- Detects emotions using `TextBlob` or `VADER`
- Extracts key themes using `nltk`
- Matches emotion to color palettes
- Places visual elements (shapes, patterns, swirls) based on poem keywords
- Generates and saves art.
- Runs locally.

---

## ⚙️ Getting Started
1. Clone the repository:
git clone https://github.com/your-username/paintmypoem.git
cd paintmypoem

2. Install dependencies:
pip install -r requirements.txt

3. Run the script:
python main.py

4. Choose and paste a poem when prompted, or use one from the /sample poems folder.
 
 ---

## 🧠 How It Works
- Sentiment analysis determines the emotional tone (e.g., joy, sadness, anger).
- Keywords are extracted (e.g., stars, rain, fire).
- Visual plans are generated with shapes, positions, and colors based on the emotion and keywords.
- Artwork is created using pygame.

## 🧰 Built With
- 🐍 Python 3
- 🧠 Natural Language Toolkit (nltk)
- 💬 TextBlob / VADER Sentiment Analysis
- 🎮 pygame for art generation

## 📌 Notes
- Works best with short poems.
- Poetic imagery and emotion words improve output.
- Sample poems included in the /sample poems folder were generated using ChatGPT.

## 🔮 Future Improvements
- Add style presets.
- Optional background image overlays (e.g., sky, forest, ocean).
- More detailed shape variations.
- GUI version for drag-and-drop poem uploads.
- Create an executable release (.exe) so users can run without installing Python.
- Optimize and test for longer poems.

## 🤝 Contributing
Contributions are welcome! If you have suggestions, improvements, or bug fixes, please fork the repository and submit a pull request. For major changes, feel free to open an issue to discuss first.

## 📄 License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

