import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Required once if the NLTK resources are not already installed:
# python -m pip install nltk
# python -m nltk.downloader punkt_tab

text = """Python is a programming language.
Python was created by Guido van Rossum.
Python is widely used in Artificial Intelligence.
Python was first released in 1991."""

question = input("Enter question: ")

# Convert question into keywords
q_words = set(word_tokenize(question.lower()))

# Find the most relevant sentence
best_sentence = ""
best_score = -1

for sentence in sent_tokenize(text):
    words = set(word_tokenize(sentence.lower()))
    score = len(q_words & words)

    if score > best_score:
        best_score = score
        best_sentence = sentence

print("Answer:", best_sentence)
