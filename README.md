# PaintMyPoem 🖌️

A Python-based creative tool that transforms poems into abstract generative art using natural language processing and simple machine learning.

🎨 *Turn verses into visuals, words into wonder.*

---

## 📝 What It Does

PaintMyPoem helps poets and creatives visualize their poetry by:

- Analyzing the **mood and tone** of the poem using NLP and sentiment analysis
- Extracting **keywords** and emotional themes
- Generating visual elements and color palettes to match the poem’s emotional weight
- Creating abstract artwork using `pygame`, saved as a `.png` image

---

## 🚀 Features

- Supports `.txt` poetry input
- Detects emotions using `TextBlob` or `VADER`
- Extracts key themes using `nltk`
- Matches emotion to color palettes
- Places visual elements (shapes, patterns, swirls) based on poem keywords
- Generates and saves high-resolution art as `poem_art.png`
- Runs completely locally — no internet or web app required

---

## 📁 Project Structure

```
paintmypoem/
├── __pycache__/                      # Compiled Python files (can be ignored)
│
├── art_generator.py                 # Generates visuals from visual plans using pygame
├── emotion_detector.py             # Detects sentiment/emotion from the poem
├── image_renderer.py               # (Optional) for advanced rendering or PIL usage
├── keyword_extractor.py            # Extracts key themes/words from the poem
├── visual_mapper.py                # Maps keywords and emotion to visual elements
├── main.py                         # Entry point — runs the pipeline
├── __init__.py                     # Makes it a Python package

├── sample output/                  # Saved example art images
│   ├── one.png
│   └── two.png

├── sample poems/                   # Collection of sample poems
│   ├── one.txt
│   ├── two.txt
│   ├── three.txt
│   ├── four.txt
│   └── five.txt

├── .gitignore                      # Files/folders Git should ignore
├── README.md                       # Project overview and documentation
├── requirements.txt                # Python dependencies

```


---

## ⚙️ Getting Started

1. Clone the repository:

git clone https://github.com/your-username/paintmypoem.git
cd paintmypoem

2. Install dependencies:
pip install -r requirements.txt

3. Run the script:
python main.py

4. Choose a poem file when prompted, or use one from the /sample poems folder.
 
 ---

## 🧠 How It Works
- The poem is read from a .txt file.
- Sentiment analysis determines the emotional tone (e.g., joy, sadness, anger).
- Keywords are extracted (e.g., stars, rain, fire).
- Visual plans are generated with shapes, positions, and colors based on the emotion and keywords.
- Artwork is created using pygame and saved as poem_art.png.

## ✍️ Sample Usage
> Enter the path to your poem file:
poems/rain_memory.txt

Generating art...
Done! Your poem has been visualized and saved as 'poem_art.png'.

## 📌 Notes
- Works best with short-to-medium length poems (4–12 lines).
- Poetic imagery and emotion words improve output.
- No internet required after initial dependency install.

## 🔮 Future Improvements
- Add style presets (e.g., minimal, vibrant, surreal) to change visual moods
- Optional background image overlays (e.g., sky, forest, ocean)
- More detailed shape variations (e.g., splines, fractals, or organic forms)
- GUI version for drag-and-drop poem uploads
- Integration with image captioning or generative feedback for enhanced creativity
- Create an executable release (.exe) so users can run without installing Python
- Optimize and test for longer poems — chunking, batching, or layered rendering for large inputs

## 🤝 Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please fork the repository and submit a pull request. For major changes, feel free to open an issue to discuss first.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions, feedback, or collaboration, open an issue or reach out via the repo.

PaintMyPoem was built to celebrate the union of poetry and code. Whether you’re a writer or a curious coder, this project helps bring verse to life through generative visuals.