#!/usr/bin/env python
# coding: utf-8

# In[1]:


#day 8
import nltk

# Ensure the necessary resources are downloaded
nltk.download('punkt')

from nltk.tokenize import word_tokenize, sent_tokenize

# Sample paragraph
paragraph = """
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence (AI). 
It involves the interaction between computers and humans using natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is valuable.
"""

# Tokenize the paragraph into sentences
sentences = sent_tokenize(paragraph)
print("Sentences:")
for sentence in sentences:
    print(sentence)

# Tokenize the paragraph into words
words = word_tokenize(paragraph)
print("\nWords:")
print(words)


# In[2]:


#day 7
get_ipython().system('pip install gensim nltk')


# In[3]:


import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import gensim
from gensim.utils import simple_preprocess
import string

# Ensure the necessary resources are downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Sample text to be written to a file
sample_text = """
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence (AI). 
It involves the interaction between computers and humans using natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is valuable.
"""

# Write sample text to a file
with open('sample_text.txt', 'w') as file:
    file.write(sample_text)

# Read the text file
with open('sample_text.txt', 'r') as file:
    text = file.read()

# Tokenization
tokens = word_tokenize(text)

# Remove punctuation
tokens = [word for word in tokens if word.isalnum()]

# Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word.lower() not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]

# Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

# Gensim preprocessing
gensim_tokens = simple_preprocess(text)

# Print results
print("Original Text:")
print(text)
print("\nTokens:")
print(tokens)
print("\nStemmed Tokens:")
print(stemmed_tokens)
print("\nLemmatized Tokens:")
print(lemmatized_tokens)
print("\nGensim Tokens:")
print(gensim_tokens)


# In[11]:


#day 6
get_ipython().system('pip install spacy')


# In[14]:


import nltk
import spacy
from nltk.corpus import stopwords

# Ensure the necessary resources are downloaded
nltk.download('stopwords')

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

# Sample text
text = """
Natural Language Processing (NLP) is a fascinating field of Artificial Intelligence (AI). 
It involves the interaction between computers and humans using natural language. 
The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is valuable.
"""

# Convert text to lowercase using SpaCy
doc = nlp(text.lower())

# Tokenize and remove stopwords using NLTK
stop_words = set(stopwords.words('english'))
filtered_tokens = [token.text for token in doc if token.text not in stop_words]

# Print results
print("Original Text:")
print(text)
print("\nLowercase Text:")
print(doc.text)
print("\nFiltered Tokens (without stopwords):")
print(filtered_tokens)


# In[ ]:




