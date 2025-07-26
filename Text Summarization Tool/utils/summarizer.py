import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from collections import defaultdict
import string

# Download required resources only once
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")


def summarize_text(text, max_sentences=2):
    """
    Summarize the input text by selecting top N scored sentences.

    Parameters:
    - text (str): Input article text.
    - max_sentences (int): Number of top sentences to include in summary.

    Returns:
    - summary (str): Extractive summary of the article.
    """
    sentences = sent_tokenize(text)
    if len(sentences) <= max_sentences:
        return text

    stop_words = set(stopwords.words("english"))
    word_freq = defaultdict(int)

    # Build word frequency table
    for sentence in sentences:
        for word in sentence.lower().split():
            word = word.strip(string.punctuation)
            if word and word not in stop_words:
                word_freq[word] += 1

    # Score each sentence
    sentence_scores = {}
    for sentence in sentences:
        score = 0
        word_count = 0
        for word in sentence.lower().split():
            word = word.strip(string.punctuation)
            if word in word_freq:
                score += word_freq[word]
                word_count += 1
        if word_count > 0:
            sentence_scores[sentence] = score / word_count  # Normalize score

    # Select top N sentences
    top_sentences = sorted(sentence_scores, key=sentence_scores.get, reverse=True)[:max_sentences]
    summary = " ".join(top_sentences)

    return summary
