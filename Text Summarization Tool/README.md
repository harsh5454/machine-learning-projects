# 🧠 Text Summarizer in Python

A simple Python-based project that summarizes long articles using basic NLP techniques like tokenization and frequency-based sentence scoring.

---

## 📁 Project Structure

Task1/
├── main.py # Entry point – reads article, generates summary, saves output
├── utils/
│ └── summarizer.py # Core logic for summarizing text
├── sample_article.txt # Sample input article for testing
└── summaries/
└── summary_output.txt # Output summary file (auto-generated)

yaml
Copy
Edit

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/text-summarizer.git
cd text-summarizer
2. Create and activate virtual environment (optional but recommended)
bash
Copy
Edit
python -m venv .venv
.venv\Scripts\activate     # Windows
# source .venv/bin/activate  # macOS/Linux
3. Install dependencies
bash
Copy
Edit
pip install nltk
4. Download NLTK data (happens automatically, but ensure internet is active)
python
Copy
Edit
import nltk
nltk.download('punkt')
nltk.download('stopwords')
🧪 How to Run
bash
Copy
Edit
python main.py
Reads sample_article.txt

Summarizes it using summarizer.py

Saves summary to summaries/summary_output.txt

Also prints summary to terminal

🧠 How It Works
Tokenize the article into sentences.

Score sentences based on word frequency (ignoring stopwords).

Select top N sentences as the summary.

🛠️ Future Improvements
Use advanced NLP techniques (e.g., spaCy or transformers)

Add command-line arguments (e.g., custom input/output paths)

Web or GUI interface

