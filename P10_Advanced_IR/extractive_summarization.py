import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

# Required once if the NLTK resources are not already installed:
# python -m pip install nltk
# python -m nltk.downloader punkt_tab

text = """Artificial Intelligence is changing the world.
Machine learning is an important part of artificial intelligence.
AI is used in healthcare and education.
AI helps computers learn from data."""

sentences = sent_tokenize(text)

# Count all words
words = word_tokenize(text.lower())
freq = Counter(words)

# Score sentences
scores = {}

for sentence in sentences:
    sentence_words = word_tokenize(sentence.lower())
    scores[sentence] = sum(
        freq[word] for word in sentence_words
    )

# Select top 2 sentences
summary = sorted(
    sentences,
    key=lambda x: scores[x],
    reverse=True
)[:2]

print("Summary:")
print(" ".join(summary))
