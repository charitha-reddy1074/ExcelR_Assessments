import re
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Ensure you have the necessary NLTK data files
nltk.download('punkt')

def clean_text(text):
    # Remove special characters using regular expressions
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    # Convert the text to lowercase
    cleaned_text = cleaned_text.lower()
    return cleaned_text

# Test the function
input_text = 'Hello, World! Welcome to NLP 101.'
cleaned_text = clean_text(input_text)
print(f"Cleaned text: {cleaned_text}")

# Sample paragraph for tokenization
sample_paragraph = "Natural Language Processing (NLP) is a fascinating field. It involves the interaction between computers and humans using natural language. NLP is amazing and fun to learn."

# Tokenize into sentences
sentences = sent_tokenize(sample_paragraph)
print(f"Sentences: {sentences}")

# Tokenize into words
words = word_tokenize(sample_paragraph)
print(f"Words: {words}")