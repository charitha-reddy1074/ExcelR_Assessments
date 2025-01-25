from collections import Counter
import re

def word_frequency(text):
    # Remove special characters and convert text to lowercase
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text).lower()
    
    # Tokenize the text into words
    words = text.split()
    
    # Calculate the frequency of each word
    word_counts = Counter(words)
    
    return word_counts

# Sample text for calculating word frequency
sample_text = "Hello world! Welcome to the world of Python. Python is great for text processing."

# Calculate word frequency
word_counts = word_frequency(sample_text)

# Print the words and their corresponding counts
for word, count in word_counts.items():
    print(f"'{word}': {count}")