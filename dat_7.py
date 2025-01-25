import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure you have the necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Load NLTK stopwords
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Remove stopwords
    tokens = [token for token in tokens if token not in stop_words]
    
    return tokens

# Sample text for preprocessing
sample_text = "Hello, World! Welcome to NLP 101."

# Preprocess the sample text
preprocessed_text = preprocess_text(sample_text)
print(f"Preprocessed text: {preprocessed_text}")