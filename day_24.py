import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

# Ensure the necessary NLTK data is downloaded
nltk.download('punkt')

def load_text_file(file_path):
    """Load the contents of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def tokenize_text(text):
    """Tokenize text using NLTK."""
    return word_tokenize(text)

def get_most_common_words(tokens, n=10):
    """Get the N most common words from the tokens."""
    word_counts = Counter(tokens)
    return word_counts.most_common(n)

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    text = load_text_file(file_path)

    if text:
        tokens = tokenize_text(text)
        common_words = get_most_common_words(tokens, n=10)
        print("10 Most Common Words:")
        for word, count in common_words:
            print(f"{word}: {count}")
