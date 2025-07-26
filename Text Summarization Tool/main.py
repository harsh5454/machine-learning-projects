from utils.summarizer import summarize_text
import os

# Ensure the summaries folder exists
os.makedirs("summaries", exist_ok=True)

# Read the article
with open("sample_article.txt", "r", encoding="utf-8") as file:
    article = file.read()

# Generate the summary
summary = summarize_text(article)

# Save the summary to a file
with open("summaries/summary_output.txt", "w", encoding="utf-8") as file:
    file.write(summary)

# Also print it to terminal
print("\n🔹 Summary:\n", summary)
