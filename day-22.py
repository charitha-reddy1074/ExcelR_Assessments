import spacy

# Load the SpaCy model
nlp = spacy.load("en_core_web_sm")

# The sentence to be tagged
sentence = "NLP is amazing and fun to learn."

# Process the sentence
doc = nlp(sentence)

# Print the part-of-speech tags
for token in doc:
    print(f"{token.text}: {token.pos_}")