import gensim
from gensim.parsing.preprocessing import remove_stopwords
from gensim.utils import simple_preprocess
from nltk.stem import SnowballStemmer
from nltk.corpus import wordnet
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
import nltk

# Ensure you have the necessary NLTK data files
nltk.download('punkt')
nltk.download('wordnet')

# Initialize stemmer and lemmatizer
stemmer = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    # Tokenization
    tokens = simple_preprocess(text)
    
    # Remove stopwords
    tokens = [remove_stopwords(token) for token in tokens]
    
    # Stemming
    stemmed_tokens = [stemmer.stem(token) for token in tokens]
    
    # Lemmatization
    lemmatized_tokens = [lemmatizer.lemmatize(token, pos=wordnet.VERB) for token in stemmed_tokens]
    
    return lemmatized_tokens

# Sample text for preprocessing
sample_text = "Natural Language Processing (NLP) is a fascinating field. It involves the interaction between computers and humans using natural language. NLP is amazing and fun to learn."

# Preprocess the sample text
preprocessed_text = preprocess_text(sample_text)
print(f"Preprocessed text: {preprocessed_text}")