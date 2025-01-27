import re
from collections import Counter

def load_text_file(file_path):
    """Load the contents of a text file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None

def tokenize_text(text):
    """Tokenize text into words."""
    return re.findall(r'\b\w+\b', text.lower())

def calculate_term_frequency(tokens):
    """Calculate term frequency for each token."""
    total_tokens = len(tokens)
    if total_tokens == 0:
        return {}
    token_counts = Counter(tokens)
    return {token: count / total_tokens for token, count in token_counts.items()}

def display_top_tokens(tf_dict, top_n=5):
    """Display the top N tokens by term frequency."""
    sorted_tokens = sorted(tf_dict.items(), key=lambda x: x[1], reverse=True)
    print(f"Top {top_n} tokens:")
    for token, tf in sorted_tokens[:top_n]:
        print(f"{token}: {tf:.4f}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ")
    text = load_text_file(file_path)

    if text:
        tokens = tokenize_text(text)
        tf_dict = calculate_term_frequency(tokens)
        display_top_tokens(tf_dict, top_n=5)
